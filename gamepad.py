"""
This module allows generating every possible inputs
"""
import vgamepad as vg
import time

gamepad = vg.VDS4Gamepad()

gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
gamepad.update()
time.sleep(0.5)
gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
gamepad.update()
time.sleep(0.5)

def reset():
    """
    This function resets the gamepad state 
    (releases button and sticks to 0)
    """
    gamepad.reset()
    gamepad.update()

#-------------------------------------------------
# ---------------------BUTTONS--------------------
#-------------------------------------------------

def smash():
    gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
    gamepad.update()


def attack():
    gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
    gamepad.update()


def special():
    gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
    gamepad.update()


def jump():
    gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
    gamepad.update()

#-------------------------------------------------
# ----------------------STICKS--------------------
#-------------------------------------------------

def light_left():
    gamepad.left_joystick_float(x_value_float=-0.5, y_value_float=0)
    gamepad.update()

def full_left():
    gamepad.left_joystick_float(x_value_float=-1, y_value_float=0)
    gamepad.update()

def light_right():
    gamepad.left_joystick_float(x_value_float=0.5, y_value_float=0)
    gamepad.update()

def full_right():
    gamepad.left_joystick_float(x_value_float=1, y_value_float=0)
    gamepad.update()

def light_up():
    gamepad.left_joystick_float(x_value_float=0, y_value_float=0.5)
    gamepad.update()

def full_up():
    gamepad.left_joystick_float(x_value_float=0, y_value_float=1)
    gamepad.update()

def light_down():
    gamepad.left_joystick_float(x_value_float=0, y_value_float=-0.5)
    gamepad.update()

def full_down():
    gamepad.left_joystick_float(x_value_float=0, y_value_float=-1)
    gamepad.update() 

def precise(x: float, y: float):
    """
    This function inputs a precise value on the left stick
    @params Must be in a range of -1 and 1
    """
    gamepad.left_joystick_float(x_value_float=x, y_value_float=y)
    gamepad.update()


#-------------------------------------------------
# --------------------TRIGGERS--------------------
#-------------------------------------------------

def r_trigger(value: float=1):
    """
    @params Must be in a range of 0 and 1
    """
    gamepad.right_trigger_float(value_float=1)
    gamepad.update()

def l_trigger(value: float=1):
    """
    @params Must be in a range of 0 and 1
    """
    gamepad.left_trigger_float(value_float=value)
    gamepad.update()

