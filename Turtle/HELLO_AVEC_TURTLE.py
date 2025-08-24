nom=str(input("Votre nom s\'il vous plait : "))
print(f"\n Monsieur, Madame {nom} veuillez  s\'il vous plait passer en mode plein écran pour l'exécution du programme.\n")

# Draw "HELLO" with turtle graphics
import turtle

# Configuration
t=turtle.Turtle()
turtle.bgcolor("black")
t.pensize(5)
t.speed(1)


# Draw H
t.pencolor("red")
t.penup()
t.goto(-400 ,90)
t.pendown()
t.right(90)
t.forward(180)
t.penup()
t.goto(-300 , 90)
t.pendown()
t.forward(180)
t.penup()
t.goto( -400 , 0)
t.pendown()
t.left(90)
t.forward(100)

# Draw E
t.pencolor("yellow")
t.penup()
t.goto(-140 , -90)
t.pendown()
t.left(180)
t.forward(80)
t.right(90)
t.forward(180)
t.right(90)
t.forward(80)
t.penup()
t.goto(-220 , 0)
t.pendown()
t.forward(70)

# Draw L
t.pencolor("green")
t.penup()
t.goto(30 , -90)
t.pendown()
t.right(180)
t.forward(80)
t.right(90)
t.forward(180)

# Draw second L
t.pencolor("violet")
t.penup()
t.goto(110 , 90)
t.pendown()
t.left(180)
t.forward(180)
t.left(90)
t.forward(80)

# Draw O
t.pencolor("blue")
t.penup()
t.goto(310 , -90)
t.pendown()
t.circle(90 , 360)

turtle.bgcolor("white")

turtle.done()