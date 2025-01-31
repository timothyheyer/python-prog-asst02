# Second programming assignment in Python

This is a required graded programming assignment in MicroPython for the micro:bit.

## Requirements

1. MicroPython.
   For the assignment you should implement a non-trivial project in MicroPython for the micro:bit. Look at the [MicroPython Tutorials assignment](https://github.com/ivogeorg/micropython-tutorials) for detailed guidance.
   
2. Topic.
   You are free to pick any topic or project idea. Look at the [micro:bit awesome list](https://github.com/carlosperate/awesome-microbit) for inspiration. The following are *strict* requirements:
   - Non-triviality: The micro:bit is targeted at kids but is powerful enough for non-trivial projects. Please, take that in mind.
   - Originality: You can borrow a significant amount of code from an existing project, but you have to: (i) acknowledge it, and (ii) extend it with some original code.
   - Functionality: Your project should have clear input and output, and it should be either interactive (e.g. in the case of a game), or autonomous (e.g. in the case of an environmental monitor). Feel free to add external components and connect them to the micro:bit as part of your design.
   
2. Github.
   You should fork this assignment repository and clone it. You should commit all your code to your local clone and push them to the remote repository on Github, before the deadline. There is no need for any further submission.
   
3. README.
   You need to describe in detail your project in the README in the provided section below.
   
## Project description

This program uses micropython to turn the micro:bit (and attached speaker) into a light-sensing alarm clock. When the micro:bit is exposed to sufficient levels of light, the microbit displays the image of a sun, starts playing continuous music, and scrolls the current temperature and a good morning message. The alarm can be disabled by pressing and holding the A button, which will initialize a "shutdown theme song" displaying the current temperature, and scrolling the word "Off" on the display. 
The concept for this program was loosely inspired by the "microbit day and night sensor tutorial" on the MicroMonsters YouTube channel: https://www.youtube.com/watch?v=j5sRLGtN8lY. 