# rpi-python-adc
DIY ramp-compare ADC for the Raspberry Pi

Warning, this is an unfinished piece of software

This is an implementation of a ramp-compare ADC for the Raspberry Pi. You must use two MOSFETs, one N-Channel and one P-channel. The P-Channel is used for charging the capacitor, with a series resistor. The N-Channel is for discharging, and you must still use a series resistor, although with a lower resistance. You should connect them to some circuit that can drive the FETs from 0-12V with the RPi output (I used a comparator with pull-ups). The detect pin must be connected to a comparator output that compares the capacitor voltage (non-inverting) with the one you want to measure (inverting).

The program just discharges the capacitor, saves the start time, adds an rising edge event detect and starts charging the capacitor. When the capacitor voltage exceeds the voltage you're measuring, the program saves the time. At the end, it calculates the time difference, and uses that to calculate the measured voltage using the exponential RC circuit equation.

To do:

Dynamic measurement time based on the RC constant

Dynamic measurement time based on the maximum voltage detected

Automatic averaging of several samples

Voltage divider inclusion (to measure higher voltages)

Graphing

GUI

Network control & reporting
