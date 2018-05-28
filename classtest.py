import turtle

wn =turtle.Screen()
wn.bgcolor('black')
wn.title('Movement Test')
carShape = 'firstCar.gif'
wn.addshape(carShape)

class firstCar(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(carShape)
        self.penup()
        self.speed(0)
        self.speed = -1

    def move(self):
        self.forward(self.speed)

player = firstCar()

while True:
    player.move()

