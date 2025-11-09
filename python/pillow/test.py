# Importation de la fonction de traitement des images
from PIL import Image

# Ouvrir une image
try:
    chemin = input("Le chemin d'accès e l'image : ")
    image = Image.open(chemin)

    # Redimensionner
    icone = image.resize((64, 64))

    # save as icone
    icone.save("myicone.ico")
    print("Icone crée avec succès !")
except FileNotFoundError:
   print("Chemin ivalide ")