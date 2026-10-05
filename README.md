# Raspberry Pi Pico Parking Sensor

A car parking assistant built with a Raspberry Pi Pico and MicroPython.
An ultrasonic sensor measures distance, LEDs show the zone (green, yellow,
red), and a buzzer beeps faster the closer the obstacle gets.

**Live simulation:** https://wokwi.com/projects/477028391037196289

## Features
- Three distance zones with colour-coded LEDs
- Buzzer beep rate increases as the obstacle gets closer
- Pure MicroPython, no external libraries

## Distance zones
| Distance | LED | Buzzer |
|---|---|---|
| Over 150 cm | Green | Silent |
| 60 to 150 cm | Yellow | Slow beeps |
| Under 60 cm | Red | Fast beeps |

## Components
| Part | Qty |
|---|---|
| Raspberry Pi Pico | 1 |
| HC-SR04 ultrasonic sensor | 1 |
| LEDs (green, yellow, red) | 3 |
| 220Ω resistors | 3 |
| Buzzer | 1 |

## Wiring
| Component | Pico pin |
|---|---|
| HC-SR04 TRIG | GP3 |
| HC-SR04 ECHO | GP2 |
| HC-SR04 VCC / GND | VBUS / GND |
| Green LED (via resistor) | GP10 |
| Yellow LED (via resistor) | GP11 |
| Red LED (via resistor) | GP12 |
| Buzzer | GP15 |

> **Real hardware note:** the HC-SR04 ECHO pin outputs 5V. Use a voltage
> divider before connecting it to a Pico pin (the Pico is 3.3V logic).

## How to run
1. Open the Wokwi link (MicroPython Pico template) and press ▶.
2. Click the HC-SR04 and drag the distance slider.
3. Watch the LEDs change and the beeping speed up as the distance drops.

## How it works
A 10 µs pulse is sent to TRIG, and `time_pulse_us()` measures how long ECHO
stays high. Distance in cm is `time × 0.0343 / 2`. The distance then decides
which LED turns on and how long the delay between beeps is.

## Future improvements
- Show distance on an OLED display
- Add a second sensor for rear corners
- Smooth readings with a moving average

## License
MIT
