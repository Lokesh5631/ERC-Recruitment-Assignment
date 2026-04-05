This is a very basic game which tests the reaction timing of the player.
## Rules
* You will be shown a digit from 0 to 9 on 7-segment display at the beginning of the game, for three times.
* After that, your countdown starts.
* You are supposed to hit the button once the target number gets displayed, wait till it comes and don't miss it !
* If u have pressed the button at the wrong time, the game will restart again.
* If u get the number correct, you go to the next round.
* It looks easy at the beginning, but the game gets faster and faster in subsequent rounds.
* There are a total of 8 maximum rounds. If you clear all of them, then u're the winner !

## Circuit Building

* Arduino Nano is the main brain of this game. It controls the 7-segment display how to show numbers and keeps track of the button being pressed.
* 7-segment display is an inner combination of LEDs which are lined up in a sequence.
* 7 digital pins of the Nano are connected to the seven segments of the the display. nano controls when to light up each segment.
* A 220Ω resistor is required to be connected tso that the current does not rise too much to blow up the display.
* The push button and buzzer are also connected to digital pins.
* The display used is a common-cathode display, the common cathode is connected to ground. This ensures that if there is no signal passes through a connection it does not remain open, but is connected to the ground.

### Power
While the arduino is connected to laptop, the power is also used from the laptop.
While the USB is removed, the 9V battery supplies power.

## Code
* The code for making the system work is given.
* A very simple to-do task for the participants is to identify what should be state of each segment for lighting a particular number, provided:
  a - Top
  b - Top-right
  c - Bottom-right
  d - Bottom
  e - Bottom-left
  f - Top-left
  g - Middle
* A map is created for each digit to the correspoding sequence of binary values for each segment.
* The push_button is set in INPUT_PULLUP state so that it remains HIGH when not pressed, through its connection to nano's 5V rail using a pullup resistor. Oce pressed it is connected to ground and becomes 0.
* A random target is chosen and displayed three times.
* Then the countdown starts. For every number the buzzer produces a beep sound.
* Whenever each number is shown, there is timer measuring the time taken by the player to hit the button. If this is less thsn the gamespeed the player loses his chance.
* If the button was pressed correctly u get a high frequency sound 3 times.
* If wring, then u get a dull low frequency sound.
  
