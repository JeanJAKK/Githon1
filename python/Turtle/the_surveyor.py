from turtle import *

z = int(-200)  # coordonnées initiales (-200, -200)
def ordonnee():  # Met à jour les coordonnées
    global z
    z += 7
    return z

def carre():   # Dessine un  carre
    for j in range(4):
       forward(70)
       left(90)

def triangle():     # Dessine un triangle
    for j in range(3):
       forward(70)
       left(120)

def draw_c():       # Dessine carre puis triangle et change de coorconnées
    penup()
    new_z = ordonnee()
    goto(new_z, new_z)
    pendown()
    for j in range(2):
       carre()  if j % 2 == 0 else triangle()

for i in range(50):      # Appel en boucle draw_c()
   draw_c()

done()