""" Turtle in Pygame

We really miss the turtle module from Python's standard library. It was a great
way to introduce programming, so let's make something similar in PyGame, using
objects. 

"""
import math

import pygame

from turtle import Turtle

tom = Turtle()

tom.shape('turtle')
tom.speed(2)
tom.pencolor('blue')

def event_loop():
    """Wait until user closes the window"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

for i in range (4):
    tom.forward(90)
    tom.left(90)

tom.penup()
tom.goto(0,-100)
tom.pencolor('orange')
tom.pendown()
for i in range (5):
    tom.forward(70)
    tom.left(72)

tom.penup()
tom.goto(-40,30)
tom.pencolor('red')
tom.pendown()
for i in range (6):
    tom.forward(90)
    tom.left(60)


tom.penup()
tom.goto(-60,-90)
tom.pencolor('yellow')
tom.pendown()
for i in range (12):
    tom.forward(50)
    tom.left(30)

tom.penup()
tom.goto(-90,-130)
tom.pencolor('purple')
tom.pendown()
for i in range (10):
    tom.forward(20)
    tom.left(36)

tom.penup()
tom.goto(60,-90)
tom.pencolor('lightgreen')
tom.pendown()
for i in range (30):
    tom.forward(10)
    tom.left(12)



class Turtle:
    def __init__(tom, screen, x: int, y: int):
        tom.x = x
        tom.y = y
        tom.screen = screen
        tom.angle = 0  # Angle in degrees, starting facing right

    def forward(tom, distance):
        # Calculate new position based on current angle
        radian_angle = math.radians(tom.angle)

        start_x = tom.x  # Save the starting position
        start_y = tom.y

        # Calculate the new position displacement
        dx = math.cos(radian_angle) * distance
        dy = math.sin(radian_angle) * distance

        # Update the turtle's position
        tom.x += dx
        tom.y -= dy

        # Draw line to the new position
        pygame.draw.line(tom.screen, black, (start_x, start_y), (tom.x, tom.y), 2)

    def left(tom, angle):
        # Turn left by adjusting the angle counterclockwise
        tom.angle = (tom.angle + angle) % 360


# Main loop

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
width, height = 00, 10
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Turtle Style Drawing")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

screen.fill(white)
turtle = Turtle(screen, screen.get_width() // 2, screen.get_height() // 2)  # Start at the center of the screen

# Draw a square using turtle-style commands
for i in range(4):
    turtle.forward(90)  # Move forward by 100 pixels
    turtle.left(90)  # Turn left by 90 degrees

# Display the drawing
pygame.display.flip()

# Wait to quit
event_loop()

# Quit Pygame
pygame.quit()
