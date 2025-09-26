from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()

#Criação da Tela
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0)

#Criação dos paddle
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))







#Event listener adicionado para movimentação de ambos Paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



gameIsOn = True

while gameIsOn:
    screen.update()




screen.exitonclick()