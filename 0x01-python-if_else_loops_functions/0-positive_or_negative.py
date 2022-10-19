#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
<<<<<<< HEAD
elif number == 0:
=======
elif:
    number == 0:
>>>>>>> deb8eb1c3c51de71649ced0519e3d3f2d595ce88
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
