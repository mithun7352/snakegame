import turtle
import random
import time

delay = 0.1
score = 0
highest_score = 0

# Create a body of a snake
bodies = []

# Create a screen
s = turtle.Screen()
s.title("Snake new game")
s.bgcolor("light blue")
s.setup(width=600, height=600)  # Size of the screen

# Create a snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.fillcolor("pink")
head.penup()  # For not moving the object
head.goto(0, 0)  # For placing at the center
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.fillcolor("green")
food.penup()
food.ht()  # For hiding a turtle
food.goto(150, 200)  # Where to show food
food.st()  # Show turtle

# Score board
sb = turtle.Turtle()
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, 250)
sb.write("Score:0 | Highest Score:0")

# Function definitions
def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event handling - key mappings
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

# Main loop
while True:
    s.update()  # To update screen

    # Check collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, 0)

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)  # Move food to a random position
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the length of snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("red")
        bodies.append(body)

        score += 100
        delay -= 0.001  # Increase the speed
        if score > highest_score:
            highest_score = score
        sb.clear()
        sb.write("Score:{} | Highest Score:{}".format(score, highest_score))

    # Move snake bodies
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)
    
    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide body
            for b in bodies:
                b.hideturtle()
            bodies.clear()
            score = 0
            delay = 0.1
            sb.clear()
            sb.write("Score:{} | Highest Score:{}".format(score, highest_score))

    time.sleep(delay)

s.mainloop()
