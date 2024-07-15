from picographics import PicoGraphics, DISPLAY_TUFTY_2040
from jpegdec import JPEG

display = PicoGraphics(display=DISPLAY_TUFTY_2040)
display.clear()

j = JPEG(display)

j.open_file("pico_profile.jpg")
j.decode()
display.update()

WHITE = display.create_pen(255, 255, 255)

display.set_pen(WHITE)
display.set_font('bitmap8')
display.text("My name is", 0, 0, 320, 4)
display.text("DaShaun.", 10, 100, 320, 5)
display.text("I like to party!", 35, 200, 320, 4)
display.update()
