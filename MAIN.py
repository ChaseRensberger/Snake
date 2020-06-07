import time
import random

class Snake:

    def __init__(self):
        self.X = 740 / 2
        self.Y = 740 / 2
        self.speedX = -10
        self.speedY = 0

        self.numApples = 5

        self.tailPositions = []

    def drawSnake(self):

        fill(255)

        rect(self.X, self.Y, 10, 10)

        self.X += self.speedX
        self.Y += self.speedY

        if (self.X, self.Y) in self.tailPositions:
            self.kill()
        else:
            self.tailPositions.append((self.X, self.Y))

        for i in self.tailPositions:
            rect(i[0], i[1], 10, 10)

        if len(self.tailPositions) > self.numApples:
            self.tailPositions.pop(0)

        if self.X > 750 or self.X < 0 or self.Y > 750 or self.Y < 0:
            self.kill()


    def kill(self):
        exit()



class Apple:

    def __init__(self):
        self.X = random.choice([i for i in range(0, 750, 10)])
        self.Y = random.choice([i for i in range(0, 750, 10)])

    def drawApple(self):
        fill(255, 0, 0)
        rect(self.X, self.Y, 10, 10)

    def changeLocation(self):
        self.X = random.choice([i for i in range(0, 750, 10)])
        self.Y = random.choice([i for i in range(0, 750, 10)])





Player = Snake()
App = Apple()


def checkCollision():
    if Player.X == App.X and Player.Y == App.Y:
        Player.numApples += 1
        App.changeLocation()

def keyPressed():

    if keyCode == UP and Player.speedY <= 0:
        Player.speedY = -10
        Player.speedX = 0
    if keyCode == DOWN and Player.speedY >= 0:
        Player.speedY = 10
        Player.speedX = 0
    if keyCode == LEFT and Player.speedX <= 0:
        Player.speedX = -10
        Player.speedY = 0
    if keyCode == RIGHT and Player.speedX >= 0:
        Player.speedX = 10
        Player.speedY = 0
        

def drawBoard():
    background(0)
    stroke(0)
    for i in range(0, width, 10):
        line(i, 0, i, height)
    for i in range(0, height, 10):
        line(0, i, width, i)


def setup():
    size(750, 750)
    

def draw():

    drawBoard()
    Player.drawSnake()
    App.drawApple()
    checkCollision()
    time.sleep(0.05)


        
