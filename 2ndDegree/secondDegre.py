from math import sqrt
# Message d'acceuil
print("=== 2nd DEGREE EQUATION SOLVER ===\n")
print("Ce programme vous permet de résoudre les équations du second degré !")

# Saisie des données
while 1:
    a = 0
    while a == 0 :
        a = float(input("\nEntrer le coefficient de degré 2 (non nul) : "))
    b = float(input("Entrer le coefficient de degré 1 : "))
    c = float(input("Entrer le coefficient de degré nul : "))

    # Confirmation des données
      # déterminer le signe des coefficients
    signe_b = "+" if b > 0 else ""
    signe_c = "+" if c > 0 else ""
    print(f"\nVotre équation est {a}x\u00B2{signe_b}{b}x{signe_c}{c}  ")   # code Unicode x\u00B2 pour écrire x²
    # Traitements
    delta = b**2 - 4*a*c
    if delta < 0 :
        racdelta = sqrt(-delta)   # Ici racdelta est en réalité la racine carrée de l'opposé de delta 

                # Considérons le signe de a pour mieux gérer l'affichage
        if a > 0 :
            print(f"Les solutions sont: {-b / (2*a)} + {racdelta / (2*a)}i et {-b / (2*a)} - {racdelta / (2*a)}i")
        if a < 0 :
                print(f"Les solutions sont: {-b / (2*a)} {racdelta / (2*a)}i et {-b / (2*a)} {racdelta / (2*a)}i")

    elif delta > 0 :
            racdelta = sqrt(delta)   # Ici racdelta est en réalité la racine carrée de l'opposé de delta 
            print(f"Les solutions sont: {(-b + racdelta )/ (2*a)} et {(-b - racdelta )/ (2*a)} ")

    else :
        print(f"La solution est : {-b / (2*a)}")

    poursuivre = input("Avez-vous une autre équation (oui/non) : ")
    if poursuivre.lower() == 'non':
        break
