import time

from digitalio import DigitalInOut, Direction
import board

import adafruit_matrixkeypad

import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode as CCC

COLS = [DigitalInOut(x) for x in (board.GP3, board.GP2, board.GP1, board.GP0)]
ROWS = [DigitalInOut(x) for x in (board.GP4, board.GP5, board.GP6, board.GP7)]
KEYS = ((1, 2, 3, 4),(5, 6, 7, 8),(9, 10, 11, 12),(13, 14, 15, 16))

KEYPAD = adafruit_matrixkeypad.Matrix_Keypad(ROWS, COLS, KEYS)

CONFIG = {}
MACROS_LST = []

KEYBOARD = Keyboard(usb_hid.devices)
CC = ConsumerControl(usb_hid.devices)

LED = DigitalInOut(board.LED)
LED.direction = Direction.OUTPUT

def get_config():
	with open("config.txt", "r") as f:
		RAW_CONFIGS = f.readlines()
		for RAW_CONFIG in RAW_CONFIGS:
			if "MACROS_DELAY" == RAW_CONFIG.split('=')[0]:
				MACROS_DELAY = float(RAW_CONFIG.split('=')[1])
			elif "MULTIPLE_MACROS_DELAY" == RAW_CONFIG.split('=')[0]:
				MULTIPLE_MACROS_DELAY = float(RAW_CONFIG.split('=')[1])
			elif "MACRO_RELEASE_DELAY" == RAW_CONFIG.split('=')[0]:
				MACRO_RELEASE_DELAY = float(RAW_CONFIG.split('=')[1])
			elif "MACRO_KEYSTROKE_DELAY" == RAW_CONFIG.split('=')[0]:
				MACRO_KEYSTROKE_DELAY = float(RAW_CONFIG.split('=')[1])

	global CONFIG
	CONFIG = {'MACROS_DELAY':MACROS_DELAY, 'MULTIPLE_MACROS_DELAY':MULTIPLE_MACROS_DELAY, 'MACRO_RELEASE_DELAY':MACRO_RELEASE_DELAY, 'MACRO_KEYSTROKE_DELAY':MACRO_KEYSTROKE_DELAY}

def get_macros_lst():
	with open("macros.txt", "r") as f:
		global MACROS_LST
		MACROS_LST = f.readlines()
		print(MACROS_LST)

def get_macro(KEY):
	return MACROS_LST[KEY[0]-1]

def run_macro(MACRO_KEYSTROKES):
	CURRENT_MACRO_KEYS_STR = MACRO_KEYSTROKES.split(' , ')
	CURRENT_MACRO_KEYS_STR[-1] = ''.join(CURRENT_MACRO_KEYS_STR[-1].splitlines())
	MACRO_KEYS_LIST = {'A':Keycode.A, 'B':Keycode.B, 'C':Keycode.C, 'D':Keycode.D, 'E':Keycode.E, 'F':Keycode.F, 'G':Keycode.G, 'H':Keycode.H, 'I':Keycode.I, 'J':Keycode.J, 'K':Keycode.K, 'L':Keycode.L, 'M':Keycode.M, 'N':Keycode.N, 'O':Keycode.O, 'P':Keycode.P, 'Q':Keycode.Q, 'R':Keycode.R, 'S':Keycode.S, 'T':Keycode.T, 'V':Keycode.V, 'W':Keycode.W, 'X':Keycode.X, 'Y':Keycode.Y, 'Z':Keycode.Z, '1':Keycode.ONE, '2':Keycode.TWO, '3':Keycode.THREE, '4':Keycode.FOUR, '5':Keycode.FIVE, '6':Keycode.SIX, '7':Keycode.SEVEN, '8':Keycode.EIGHT, '9':Keycode.NINE, '0':Keycode.ZERO, 'ENTER':Keycode.ENTER, 'RETURN':Keycode.RETURN, 'ESCAPE':Keycode.ESCAPE, 'BACKSPACE':Keycode.BACKSPACE, 'TAB':Keycode.TAB, 'SPACE':Keycode.SPACEBAR, 'MINUS':Keycode.MINUS, 'EQUAL':Keycode.EQUALS, 'F20':Keycode.F20, 'F21':Keycode.F21, 'F22':Keycode.F22, 'F23':Keycode.F23, 'F24':Keycode.F24, 'LEFT_BRACKET':Keycode.LEFT_BRACKET, 'RIGHT_BRACKET':Keycode.RIGHT_BRACKET, 'BACKSLASH':Keycode.BACKSLASH, 'POUND':Keycode.POUND, 'SEMICOLON':Keycode.SEMICOLON, 'QUOTE':Keycode.QUOTE, 'GRAVE_ACCENT':Keycode.GRAVE_ACCENT, 'COMMA':Keycode.COMMA, 'PERIOD':Keycode.PERIOD, 'FORWARD_SLASH':Keycode.FORWARD_SLASH, 'CAPS_LOCK':Keycode.CAPS_LOCK, 'F1':Keycode.F1, 'F2':Keycode.F2, 'F3':Keycode.F3, 'F4':Keycode.F4, 'F5':Keycode.F5, 'F6':Keycode.F6, 'F7':Keycode.F7, 'F8':Keycode.F8, 'F9':Keycode.F9, 'F10':Keycode.F10, 'F11':Keycode.F11, 'F12':Keycode.F12, 'PRINT_SCREEN':Keycode.PRINT_SCREEN, 'SCROLL_LOCK':Keycode.SCROLL_LOCK, 'PAUSE':Keycode.PAUSE, 'INSERT':Keycode.INSERT, 'HOME':Keycode.HOME, 'PAGE_UP':Keycode.PAGE_UP, 'DELETE':Keycode.DELETE, 'END':Keycode.END, 'PAGE_DOWN':Keycode.PAGE_DOWN, 'RIGHT_ARROW':Keycode.RIGHT_ARROW, 'LEFT_ARROW':Keycode.LEFT_ARROW, 'DOWN_ARROW':Keycode.DOWN_ARROW, 'UP_ARROW':Keycode.UP_ARROW, 'KEYPAD_NUMLOCK':Keycode.KEYPAD_NUMLOCK, 'KEYPAD_FORWARD_SLASH':Keycode.KEYPAD_FORWARD_SLASH, 'KEYPAD_ASTERISK':Keycode.KEYPAD_ASTERISK, 'KEYPAD_MINUS':Keycode.KEYPAD_MINUS, 'KEYPAD_PLUS':Keycode.KEYPAD_PLUS, 'KEYPAD_ENTER':Keycode.KEYPAD_ENTER, 'KEYPAD_ONE':Keycode.KEYPAD_ONE, 'KEYPAD_TWO':Keycode.KEYPAD_TWO, 'KEYPAD_THREE':Keycode.KEYPAD_THREE, 'KEYPAD_FOUR':Keycode.KEYPAD_FOUR, 'KEYPAD_FIVE':Keycode.KEYPAD_FIVE, 'KEYPAD_SIX':Keycode.KEYPAD_SIX, 'KEYPAD_SEVEN':Keycode.KEYPAD_SEVEN, 'KEYPAD_EIGHT':Keycode.KEYPAD_EIGHT, 'KEYPAD_NINE':Keycode.KEYPAD_NINE, 'KEYPAD_ZERO':Keycode.KEYPAD_ZERO, 'KEYPAD_PERIOD':Keycode.KEYPAD_PERIOD, 'KEYPAD_BACKSLASH':Keycode.KEYPAD_BACKSLASH, 'APPLICATION':Keycode.APPLICATION, 'LEFT_CONTROL':Keycode.LEFT_CONTROL, 'LEFT_SHIFT':Keycode.LEFT_SHIFT, 'LEFT_ALT':Keycode.LEFT_ALT, 'LEFT_GUI':Keycode.LEFT_GUI, 'RIGHT_CONTROL':Keycode.RIGHT_CONTROL, 'RIGHT_SHIFT':Keycode.RIGHT_SHIFT, 'RIGHT_ALT':Keycode.RIGHT_ALT, 'RIGHT_GUI':Keycode.RIGHT_GUI, 'CCC_BRIGHTNESS_DECREMENT':CCC.BRIGHTNESS_DECREMENT, 'CCC_BRIGHTNESS_INCREMENT':CCC.BRIGHTNESS_INCREMENT, 'CCC_EJECT':CCC.EJECT, 'CCC_MUTE':CCC.MUTE, 'CCC_PLAY_PAUSE':CCC.PLAY_PAUSE, 'CCC_VOLUME_DECREMENT':CCC.VOLUME_DECREMENT, 'CCC_VOLUME_INCREMENT':CCC.VOLUME_INCREMENT}
	CURRENT_MACRO_KEYS_LIST = []
	for CURRENT_MACRO_KEY in CURRENT_MACRO_KEYS_STR:
		if CURRENT_MACRO_KEY=='EXIT':exit()
		elif 'CCC_' in CURRENT_MACRO_KEY:
			CC.send(MACRO_KEYS_LIST.get(CURRENT_MACRO_KEY))
			return None
		elif CURRENT_MACRO_KEY!=None:CURRENT_MACRO_KEYS_LIST.append(MACRO_KEYS_LIST.get(CURRENT_MACRO_KEY))
		else:return None

	for KEY_TO_PRESS in CURRENT_MACRO_KEYS_LIST:
		KEYBOARD.press(KEY_TO_PRESS)
		time.sleep(CONFIG['MACRO_KEYSTROKE_DELAY'])

	CURRENT_MACRO_KEYS_LIST.reverse()
	time.sleep(CONFIG['MACRO_RELEASE_DELAY'])

	for KEY_TO_RELEASE in CURRENT_MACRO_KEYS_LIST:
		KEYBOARD.release(KEY_TO_RELEASE)
		time.sleep(CONFIG['MACRO_KEYSTROKE_DELAY'])

def run_macros(MACROS):
	MACROS_LST = MACROS.split(' + ')
	MACROS_LST[-1] = ''.join(MACROS_LST[-1].splitlines())
	for MACRO_KEYSTROKES in MACROS_LST:
		run_macro(MACRO_KEYSTROKES)
		time.sleep(CONFIG['MULTIPLE_MACROS_DELAY'])

while True:
	get_config()
	get_macros_lst()
	KEY = KEYPAD.pressed_keys
	if KEY:
		MACROS = get_macro(KEY)
		print(MACROS)
		if MACROS!=None:
			LED.value = True
			run_macros(MACROS)
			LED.value = False
			time.sleep(CONFIG['MACROS_DELAY'])