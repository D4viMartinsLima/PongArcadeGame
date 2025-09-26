from turtle import Turtle

#Aqui é utilizado herança
# A classe que está sendo criada(Paddle) herda todos os métodos e atributos da Classe Turtle
class Paddle(Turtle):
    #Nesse trecho a classe é inicializada
    def __init__(self, position):
        #esse super().__init__() mostra que esta é uma subclasse
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)