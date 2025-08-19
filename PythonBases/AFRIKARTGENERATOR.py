# importation de la biblio de code pays
import pycountry

# Message d'acceuil

print("🌍=== AFRIKART GENERATOR ===")
print(" Bienvenue dans votre générateur d\'art africain ! ")
print()

# Questionnaire sur info personnelles
nom = str(input("Quel est votre nom ? " ))
pays = str(input(" Dans quel pays vivez-vous ? "))
ville = str(input("Dans quelle ville ?" ))
age = int(input("Quel est votre âge ? "))
langueParlée = input(str(" Quelles langue parlez-vous le mieux ? "))
platPréféré = input(str("Quel est votre plat préféré ?" ))

# Recherche du pays dans la base ISO 3166-1
nomPays = pays
pays = pycountry.countries.get(name = pays)
if pays:
    codePays = pays.alpha_2
else:
    codePays = "xx"

# Sortie 
print(f" {codePays} Ah ! Vous venez du {nomPays} !")
print(f"Bonjour {nom} de {ville} !")

# Récapitulatif
print("=== INFORMATION RÉCAPITULATIVES ===")
print(f"👤 Nom : {nom}")
print(f"🌍 Pays : {nomPays}")
print(f"🏙 Ville : {ville}")
print(f"🎂 Âge : {age}")
print(f"🗣️ Langue : {langueParlée}")
print(f"🍽️ Plat préférée : {platPréféré}")
print()

# Affichage de dessin du drapeau du pays 
print(f"{codePays} DRAPEAU DU PAYS {codePays}")
if nomPays in ("Togo", "togo", "TOGO"): 
    # Au fait je me demand esi c'est possible de creer une biblio qui va 
    # contenir les drapeaux de tout les pays qu'in aura a dessiner nous même
    # pour le moment on a que pour le togo 
    print("🟦"*5 + "🟨"*10 )
    print("🟦" + "⭐" +"🟦"*3 + "🟩"*10 )
    print("🟦"*5 + "🟨"*10 )
    print("🟦"*5 +  "🟩"*10 )
    print("🟨"*15 )

else:
    print("Oups")


#Création des motifs si la personne le souhaite
print()
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
    # choix 1
if choix == 1:
    hauteur = int(input(f"Hauteur du triangle (3 - 10) : "))
    caractere = input("Caractère à utiliser (*, #, @, etc.) : ")
    for i in range(hauteur + 1):
        print(i * caractere)

     #choix 2 
elif choix == 2:
        while 1:
            longueur = int(input(f"Longueur du rectangle (3 - 10) : "))
            largeur = int(input("Largeur du rectangle (3 - 10): "))
            if longueur < largeur:
                print("La longueur doit être supérieure à la largeur.")
            else:
                 break
        caractere = input("Caractère à utiliser (*, #, @, etc.) : ")
        for i in range(largeur):
                      print(f"{caractere}" *longueur)

    #choix 3