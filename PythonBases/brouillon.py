#Message de bienvenue
print("\n=== AFRIKART GENERATOR ===")
print("Bienvenue dans votre générateur d'art africain !\n")

#Récolte des infos personnelles
nom = input("Quel est votre nom ? : ")
pays = input("Dans quel pays vivez-vous ? : ")
ville = input("Dans quelle ville ? : ")
age = input("Quel est votre âge ? : ")
langue = input("Quelle langue parlez-vous le mieux ? : ")
plat = input("Quel est votre plat africain préféré ? : ")

print(f"Ah ! Vous venez du {pays}\nBonjour Koffi de {ville} !")

#affichage des infos récapitulatives
print("Nom : ")
print("Pays : ")
print("Ville : ")
print("Âge : ")
print("Langue : ")
print("Plat préféré :")
print("")

#Drapeau du pays
print("")

#Création des motifs si la personne le souhaite
print(f"{nom}, voulez-vous créer des motifs artistiques ?")
continuer = input("Tapez 'oui' pour continuer : ")

if continuer in ('oui', 'Oui', 'OUI'):
    print("")

    print("=== GÉNÉRATEUR DE MOTIFS ===")
    print("Choisissez votre forme : ")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Pyramide")
    print("4. Pyramide inversée")
    print("")
    choix = int(input("Votre choix (1-4) : "))
    #construction du motif selon le choix
if choix == 1:
    hauteur = int(input(f"Hauteur du triangle (3 - 10) : "))
    caractere = input("Caractère à utiliser (*, #, @, etc.) : ")
    for i in range(hauteur + 1):
        print(i * caractere)
elif choix == 2:
        while 1:
            longueur = int(input(f"Longueur du rectangle (3 - 10) : "))
            largeur = int(input("Largeur du rectangle (3 - 10): "))
            if longueur < largeur:
                print("La longueur doit être supérieure à la largeur.")
            else:
                break
        caractere = input("Caractère à utiliser (*, #, @, etc.) : ")
        print(caractere * longueur)

