#adds user input for circle radius and speed

speed1 = input("Circle 1 Forward Speed: ")
rotation1 = input("Circle 1 Rotation Speed: ")
speed2 = input("Circle 2 Forward Speed: ")
rotation2 = input("Circle 2 Rotation Speed: ")
speed3 = input("Circle 3 Forward Speed: ")
rotation3 = input("Circle 3 Rotation Speed: ")

from turtle import Turtle, Screen

circ1 = Turtle()
circ1.shape("circle")
circ1.color("#8A3E3E")

circ2 = Turtle()
circ2.shape("circle")
circ2.color("#E6D262")

circ3 = Turtle()
circ3.shape("circle")
circ3.color("#2F52A3")

i = 0

while i == 0:
        circ1.forward(int(speed1))
        circ1.right(int(rotation1))
        circ2.forward(int(speed2))
        circ2.right(int(rotation2))
        circ3.forward(int(speed3))
        circ3.right(int(rotation3))

newscreen = Screen()
print(newscreen.canvheight)
newscreen.exitonclick
