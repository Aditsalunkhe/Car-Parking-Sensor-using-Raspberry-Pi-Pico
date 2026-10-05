from machine import Pin, PWM, time_pulse_us
import time

trig = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
leds = [Pin(p, Pin.OUT) for p in (10, 11, 12)]   # green, yellow, red
bz = PWM(Pin(15))

def dist():
    trig.low(); time.sleep_us(2)
    trig.high(); time.sleep_us(10); trig.low()
    t = time_pulse_us(echo, 1, 30000)
    return t * 0.0343 / 2 if t > 0 else None

def beep(ms=40):
    bz.freq(1500); bz.duty_u16(20000)
    time.sleep_ms(ms)
    bz.duty_u16(0)

while True:
    d = dist()
    for l in leds:
        l.off()
    if d is None or d > 150:
        leds[0].on(); time.sleep_ms(150)
    elif d > 60:
        leds[1].on(); beep(); time.sleep_ms(int(d * 6))
    else:
        leds[2].on(); beep(); time.sleep_ms(int(d * 3) + 20)