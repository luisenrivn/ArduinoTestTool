This is a prototype of the Arduino Automated Test Tool.

This tool can be used to test software applications on micro-controllers, it allows to create python scripts
which interact with Arduino via serial communication and simulates the inputs for the micro-controller and 
gets the its outputs.

Right now only the functions to test applications that uses GPIO as digital input/output are ready to use.

Functions to test drivers for communication protocols such SPI, I2C, UART, etc, and other testing capabilities
are considered to be developed in the future.

The folder where the script are stored is "scripts", there is already an scripts example to test an application
that runs on a STM32 micro-controller.

MCU settings considerations.

For STM32 micro-controllers:

For the test example, the outputs of Arduino are configured with the internal pull_up resistors enabled.
That means if we have the GPIO pin Arduino connected to nothing(floating) reads it as High and when we put the pin to
ground it is read as Low. This configuration allows to connect the Arduino inputs directly to the SMT32 outputs, therefore
the STM32 outputs must have the open-drain configuration (High - floating, Low - ground).

