import turtle
import math
gamewindow = turtle.Screen()
gamewindow.bgpic('FroggerBG.gif')
gamewindow.title('Frogger')

#frogger
gamewindow.register_shape('Frog.gif')
frogShape = 'Frog.gif'
gamewindow.addshape(frogShape)
frog = turtle.Turtle()
frog.shape(frogShape)
frog.penup()
frog.speed(0)
frog.setposition(0, -289)
frogspeed = 18

#lives
froglives = 3
lives_pen = turtle.Turtle()
lives_pen.speed(0)
lives_pen.penup()
lives_pen.setposition(-290, 280)
livesstring = 'Lives: %s' %froglives
lives_pen.write(livesstring, False, align = 'Left', font=('Arial, 12'))
lives_pen.hideturtle()

#Score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.penup()
score_pen.setposition(-290, 265)
scorestring = 'Score: %s' %score
score_pen.write(scorestring, False, align = 'Left', font=('Arial, 12'))
score_pen.hideturtle()

carShape = 'firstCar.gif'
logShape = 'log.gif'
quickCarShape = 'fastCar.gif'
originalCarShape = 'thirdCar.gif'
gamewindow.addshape(originalCarShape)
gamewindow.addshape(quickCarShape)
gamewindow.addshape(logShape)
gamewindow.addshape(carShape)


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('Black')
border_pen.penup()
border_pen.setposition(320,480)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(80)
    border_pen.lt(120)
border_pen.hideturtle()


#first car starting position will be around (a x variable you need to calcualate and - 187.
#the car needs to return to that position everytime it moves off the screen
def move_left():
    x = frog.xcor()
    x -= frogspeed
    if x < -320:
        x = -320
    frog.setx(x)
def move_right():
    x = frog.xcor()
    x += frogspeed
    if x > 320:
        x = 320
    frog.setx(x)
def move_up():
    y = frog.ycor()
    y += frogspeed
    if y > 480:
        y = 480
    frog.sety(y)
def move_down():
    y = frog.ycor()
    y -= frogspeed
    if y < -480:
        y = -480
    frog.sety(y)



turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")

class firstCar(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(carShape)
        self.penup()
        self.speed(0)
        self.speed = -7
        self.setposition(190,-232)
    def move(self):
        self.forward(self.speed)
car = firstCar()

class originalCar(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(originalCarShape)
        self.penup()
        self.speed(0)
        self.speed = 10
        self.setposition(-175, -135)
    def move(self):
        self.forward(self.speed)
ogCar = originalCar()

class movinglog(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(logShape)
        self.penup()
        self.speed(0)
        self.speed = 1
        self.setposition(-150, -10)

    def move(self):
        self.forward(self.speed)
log = movinglog()


class quickCar(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(quickCarShape)
        self.penup()
        self.speed(0)
        self.speed = -20
        self.setposition(180,-35)

    def move(self):
        self.forward(self.speed)
fastCar = quickCar()

while True:
    car.move()
    fastCar.move()
    log.move()
    ogCar.move()
    #sets frog back to start
    if frog.ycor() > 198:
        frog.setposition(0,-289)
        score = score + 10
        scorestring = 'Score: %s' % score
        score_pen.clear()
        score_pen.write(scorestring, False, align='left', font="Arial, 12")
    #sets frog boundaries
    if frog.xcor() > 180:
        frog.setx(179)
    if frog.xcor() < -180:
        frog.setx(-179)
    if frog.ycor() > 198:
        frog.sety(197)
    if frog.ycor() < -290:
        frog.sety(-289)
    #look into the values needed for side boundaries
    #if frog.xcor() <= -179 and frog.ycor() >= 198:
    #    frog.setx(-178)
    #    frog.sety(197)
    #resets vehicles positions
    if car.xcor() < -165:
        car.setx(190)
        car.sety(-232)
    if fastCar.xcor() < -165:
        fastCar.setx(180)
        fastCar.sety(-35)
    if ogCar.xcor() > 165:
        ogCar.setx(-175)
        ogCar.sety(-135)
    #resets logs position
    if log.xcor() > 210:
        log.setx(-150)
        log.sety(-10)
    #collision checking
    distance = math.sqrt(math.pow(frog.xcor()-car.xcor(),2) + math.pow(frog.ycor()-car.ycor(),2))
    if distance < 30:
        frog.setposition(0,-289)
        froglives -= 1
        livesstring = 'Lives: %s' %froglives
        lives_pen.clear()
        lives_pen.write(livesstring, False, align='left', font="Arial, 12")
    distance = math.sqrt(math.pow(frog.xcor() - fastCar.xcor(), 2) + math.pow(frog.ycor() - fastCar.ycor(), 2))
    if distance < 30:
        frog.setposition(0, -289)
        froglives -= 1
        livesstring = 'Lives: %s' % froglives
        lives_pen.clear()
        lives_pen.write(livesstring, False, align='left', font="Arial, 12")
    distance = math.sqrt(math.pow(frog.xcor() - ogCar.xcor(), 2) + math.pow(frog.ycor() - ogCar.ycor(), 2))
    if distance < 20:
        frog.setposition(0, -289)
        froglives -= 1
        livesstring = 'Lives: %s' % froglives
        lives_pen.clear()
        lives_pen.write(livesstring, False, align='left', font="Arial, 12")
    #Closes the window when you run out of lives
    if froglives == 0:
        print('Game over!')
        gamewindow.bye()
    



gamewindow.mainloop()