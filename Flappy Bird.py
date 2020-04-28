import turtle
import time
import random

# Building a screen:
wn=turtle.Screen()
wn.title("Flappy Bird By Samip")
wn.bgcolor("#51C0C9")
wn.bgpic("background.gif")
wn.setup(500,700)
wn.tracer(0)

wn.register_shape("pipe.gif")
wn.register_shape("ground.gif")
wn.register_shape("bird1.gif")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0,250)
pen.write("0",move=False,align="center",font=("Arial",32,"bold"))

# Making a player:
player = turtle.Turtle()
player.speed(0)
player.shape("bird1.gif")
player.color("red")
player.shapesize(stretch_len=3,stretch_wid=3)
player.penup()
player.goto(-200,0)
player.dy= 1

# Lets make some pipes:
pipe1_top = turtle.Turtle()
pipe1_top.shape("pipe.gif")
pipe1_top.speed(0)
pipe1_top.color("#4e8711")
pipe1_top.shapesize(stretch_wid=29,stretch_len=3)
pipe1_top.penup()
rnum1 = random.randint(260,580)
pipe1_top.goto(300,rnum1)
pipe1_top.dx=-2
pipe1_top.value = 1

pipe1_bottom = turtle.Turtle()
pipe1_bottom.shape("pipe.gif")
pipe1_bottom.speed(0)
pipe1_bottom.color("#4e8711")
pipe1_bottom.shapesize(stretch_wid=29,stretch_len=3)
pipe1_bottom.penup()
pipe1_bottom.goto(300,rnum1-720)
pipe1_bottom.dx=-2

pipe2_top = turtle.Turtle()
pipe2_top.shape("pipe.gif")
pipe2_top.speed(0)
pipe2_top.color("#4e8711")
pipe2_top.shapesize(stretch_wid=29,stretch_len=3)
pipe2_top.penup()
rnum2 = random.randint(260,580)
pipe2_top.goto(600,rnum2)
pipe2_top.dx=-2
pipe2_top.value = 1

pipe2_bottom = turtle.Turtle()
pipe2_bottom.shape("pipe.gif")
pipe2_bottom.speed(0)
pipe2_bottom.color("#4e8711")
pipe2_bottom.shapesize(stretch_wid=29,stretch_len=3)
pipe2_bottom.penup()
pipe2_bottom.goto(600,rnum2-720)
pipe2_bottom.dx=-2

ground = turtle.Turtle()
ground.shape("ground.gif")
ground.speed(0)
ground.color("#DED895")
ground.shapesize(stretch_wid=5,stretch_len=28)
ground.penup()
ground.goto(0,-300)



gravity = -2

def jump():
    player.dy=16
    if player.dy>16:
        player.dy=16


wn.listen()
wn.onkeypress(jump,'Up')
wn.onkeypress(jump,'space')


# Initialize game variables
player.score = 0


pipes = [(pipe1_top,pipe1_bottom),(pipe2_top,pipe2_bottom)]

while True:
    time.sleep(0.02)
    wn.update()

    # Move the player
    player.dy+=gravity
    player.sety(player.ycor()+player.dy)

    # Bottom Border:
    if player.ycor()<-230:
        player.dy=0
        player.sety(-230)
        pen.clear()
        pen.write("Game Over!",move=False,align="center",font=("Arial",32,"bold"))
        wn.update()
        time.sleep(1)
        # Reset Score
        player.score = 0
        # Move pipes back
        pipe_top.setx(300)
        pipe_bottom.setx(300)
        pipe_top.setx(600)
        pipe_bottom.setx(600)
        # Move player back 
        player.goto(-200,0)
        player.dy = 0
        pen.clear()

    
    # Iterate through each pipes:
    for pipe_pair in pipes:
        pipe_top = pipe_pair[0]
        pipe_bottom = pipe_pair[1]

            # Move the pipes:
        pipe_top.setx(pipe_top.xcor()+pipe_top.dx)
        pipe_bottom.setx(pipe_bottom.xcor() + pipe_bottom.dx)

    

        # Returning the pipes
        if pipe_top.xcor()<-280:
            rnumf1 = random.randint(260, 580)
            pipe_top.goto(300,rnumf1)
            pipe_bottom.goto(300,rnumf1-720)
    

        # Check for Collision:
        if (player.xcor()+25>pipe_top.xcor()-30) and (player.xcor()-25<pipe_top.xcor()+30):
            if(player.ycor()+25>pipe_top.ycor()-290)or(player.ycor()-25<pipe_bottom.ycor()+290):
                pen.clear()
                pen.write("Game Over!",move=False,align="center",font=("Arial",32,"bold"))
                wn.update()
                time.sleep(1)
                # Reset Score
                player.score = 0
                # Move pipes back
                pipe_top.setx(300)
                pipe_bottom.setx(300)
                # Move player back 
                player.goto(-200,0)
                player.dy = 0
                pen.clear()
        
        # Checking the score
        if pipe_top.xcor()+30<player.xcor()-25:
            player.score += pipe_top.value
            pipe_top.value = 0
            pen.clear()
            pen.write(player.score,move=False,align="center",font=("Arial",32,"bold"))

    

wn.mainloop()