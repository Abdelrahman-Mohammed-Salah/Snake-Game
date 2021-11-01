
import turtle
from random import randint
from time import sleep

#create screen
scr = turtle.Screen()
scr.bgcolor('black')
scr.title("My Snake Game")
scr.setup(width=700,height=600)
scr.listen()
scr.tracer(0)

#create snake turtle
snake = turtle.Turtle()
snake.shape('square')
snake.color('green')
#user defined property
snake.direction = "stop"
snake.speed(0)
snake.up()

#create fruit turtle
fruit = turtle.Turtle()
fruit.shape('circle')
fruit.color('red')
fruit.up()
fruit.goto(randint(-300,300),randint(-200,200))
fruit.speed(0)

#create body parts
body_parts = []

#create writer turtle
writer = turtle.Turtle()
writer.color('white')
writer.speed(0)
writer.hideturtle()
writer.up()
writer.score = 0
writer.highscore = 0



def write_score():
    writer.goto(-150,235)
    writer.write(f'Score : {writer.score}',align="right",font="Arial")
    writer.goto(220,235)
    writer.write(f'High-Score : {writer.highscore}',align="right",font="Arial")


def move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)
    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)
    if snake.direction == "right":
        snake.setx(snake.xcor() + 20)




def move_right():
    if snake.direction != "left":
        snake.direction = "right"
def move_left():
    if snake.direction != "right":
        snake.direction = "left"
def move_up():
    if snake.direction != "down":
        snake.direction = "up"
def move_down():
    if snake.direction != "up":
        snake.direction = "down"



#declaration or definition
def control_score():
    if snake.distance(fruit) < 16:
        fruit.goto(randint(-300,300),randint(-200,200))
        writer.clear()
        writer.score += 10
        if writer.score > writer.highscore:
            writer.highscore = writer.score

        #adding new parts of snake's body
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.color("red")
        new_part.shape("square")
        new_part.up()
        body_parts.append(new_part)

        write_score()



def reset_snake():
    last_index = len(body_parts) - 1
    for i in body_parts:
        i.hideturtle()

    body_parts.clear()


def border_collision():
    if (
        snake.xcor() > 340
        or snake.xcor() < -340
        or snake.ycor() > 300
        or snake.ycor() < -300
    ):
        snake.direction = "stop"
        snake.goto(0,0)
        fruit.goto(randint(-300,300),randint(-200,200))
        sleep(0.4)
        writer.clear()
        writer.score = 0
        write_score()
        reset_snake()


#snake body controll
def snake_body():
   last_index = len(body_parts) - 1
   for i in range(last_index, 0, - 1):
        x = body_parts[i - 1].xcor()

        y = body_parts[i - 1].ycor()

        body_parts[i].goto(x,y)

   if len(body_parts) > 0:
        body_parts[0].goto(snake.xcor(),snake.ycor())



def body_collision():
    for i in body_parts:
        if snake.distance(i) < 20 :
            snake.direction = "stop"
            sleep(0.4)
            snake.goto(0,0)
            fruit.goto(randint(-300,300),randint(-200,200))
            writer.clear()
            writer.score = 0
            write_score()
            reset_snake()



scr.onkey(move_up,"Up")
scr.onkey(move_down,"Down")
scr.onkey(move_left,"Left")
scr.onkey(move_right,"Right")


game_mode = True
while game_mode:
    scr.update()
    sleep(0.1)
    control_score()
    snake_body()
    move()
    border_collision()
    write_score()
    body_collision()







