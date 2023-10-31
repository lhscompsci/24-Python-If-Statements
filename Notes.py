#Making Decisions in Python
import pygame
from pygame import K_UP, event

num = 87
if num >= 90:
    print("Hello")
    print("World")

seconds = 10
if seconds >= 60:
    print("over a minute")
else:  #otherwise
    print("under a minute")


num = 96
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

seconds = 10
if seconds < 60:
    print("under a minute")
elif seconds < 120:
    print("over a minute")
else:
    print("over two minutes")

num = 97
if not num % 2 == 0:
    print ("Odd")
else:
    print("Even")

x = 50
y = 700
if x < 10 or y < 50:
    print("Fun")
elif x < 400 or y < 300:
    print("Wow")

x = 50
y = 100
if x < 400 and y < 300:
    print("Upper right")
elif x < 400 and y > 300:
    print("upper left")

grade = 97
if grade >= 70:
    print("Passing")
    if grade >= 90:
        print("A")
else:
    print("Failing")


if pygame.event.key == pygame.K_UP :
    print ("Do something")