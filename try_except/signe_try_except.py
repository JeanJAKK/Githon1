# Saisi des valeurs de A et B

def saisi(position ="premier"):
    while True :
        try:
           nombre = int(input(f"Entrer un {position} nombre  : "))
           return nombre
        except ValueError:
           print("Un nombre svp")

A = saisi()
B = saisi("second")

# Définition de la fonction signe
def signe(A , B):
    if (A * B > 0):
        print(f"{A} et {B} sont de même signe.")
    elif ( A * B == 0):
        if (A == 0) :
           print(f"{A} est nul")
        elif (B == 0) :
            print(f"{B}  est nul")
        else :
            print(f"{A} et {B} sont nuls.")
    else :
        print(f"{A} et {B} sont de signe contraire.")

# Appel
signe(A, B)