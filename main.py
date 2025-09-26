from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

#Criação da Tela
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0),

#Criação dos paddle
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#Criação da bola
ball = Ball()






#Event listener adicionado para movimentação de ambos Paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



gameIsOn = True

while gameIsOn:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Colisão com parede
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Colisão com o Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detectar se a bola passou direto na direita
    if ball.xcor() > 380:
        ball.reset_position()

    #Detectar e bola passou direto na esquerda

    if ball.xcor() < -380:
        ball.reset_position()




screen.exitonclick()