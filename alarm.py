from microbit import *
import music

sun = Image("00900:"
            "09990:"
            "99999:"
            "09990:"
            "00900")
temp = temperature()
light = display.read_light_level()
notsun = Image("90009:"
               "99099:"
               "90909:"
               "99099:"
               "90009")

while not button_a.is_pressed():
    if not button_a.is_pressed():
        if light > 75:
            if not button_a.is_pressed():
                music.play(music.PRELUDE)
                if not button_a.is_pressed():
                    display.show(sun)
                    if not button_a.is_pressed():
                        sleep(2000)
                        if not button_a.is_pressed():
                            display.show(temp)
                            if not button_a.is_pressed():
                                sleep(2000)
                                if not button_a.is_pressed():
                                    display.scroll("Guten Morgen!")
display.show(notsun)
music.play(music.DADADADUM)
sleep(1000)
display.show(temp)
sleep(2000)
display.scroll("Off")


