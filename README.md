# DIY RPI PICO MACROPAD
 

A project in CircuitPython to get the RPI Pico working as a USB HID.

## Installation
Note: these instructions are written from a Windows perspective. You may have to modify them slightly if using other operating systems.

1. Flash your Pico with CircuitPython.
    - You can download the latest release [here](https://circuitpython.org/board/raspberry_pi_pico/).
    - The code has been tested with versions 7.1.1
1. Download the [AdaFruit circuit python bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20210604/adafruit-circuitpython-bundle-py-20210604.zip).
1. Create a `lib` folder on the Pico and copy over the following files and folders into the lib folder:
    - adafruit_hid (folder)
    - adafruit_matrixkeypad.py (file)
1. Copy the contents of the `src` folder to the root of the Pico.

## Description of necessary files
   - *code.py* - Main Code
   - *macros.py* - Macros
   - *config.txt* - For Configuration of Timing of Macropad
   - *debug.txt* - For Debugging
   - *keys.txt* - Supported keys
   - *MACROS.png* - Defaults Macros Shown By A Diagram