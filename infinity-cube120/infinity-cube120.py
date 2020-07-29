import board
import neopixel
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.sequence import AnimationSequence

pixel_pin = board.A1
num_pixels = 35
SPARKLE_SPEED = 0.3
purple = (200, 0, 200)

strip_pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

animations = AnimationSequence(
    AnimationGroup(
        Sparkle(strip_pixels, SPARKLE_SPEED, purple)
    ),
)

while True:

    animations.animate()
