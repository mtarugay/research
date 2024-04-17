#turtle text
from turtle import Turtle, Screen

tom = Turtle()
tom.shape("circle")
tom.color("#FCB501")

tam = Turtle()
tam.shape("circle")
tam.color("#FF960D")

tim = Turtle()
tim.shape("circle")
tim.color("#CE4100")

tum = Turtle()
tum.shape("circle")
tum.color("#963131")

i = 0

# 8 loop
while i == 0:
    tom.forward(6)
    tom.right(6)
    tim.backward(6)
    tim.right(6)
    tum.forward(8)
    tum.right(8)
    tam.backward(8)
    tam.right(8)

# orbit loop
# while i == 0:
#         tom.forward(10)
#         tom.right(7)
#         tam.forward(9)
#         tam.right(8)
#         tim.forward(8)
#         tim.right(9)
#         tum.forward(7)
#         tum.right(10)

newscreen = Screen()
print(newscreen.canvheight)
newscreen.exitonclick
