# Importation de la fonction de traitement des images
from PIL import Image

# Ouvrir une image
image = Image.open("pillowTestImg.jpg")

# Redimensionner
icone = image.resize((64, 64))

# save as icone
icone.save("myicone.ico")
print("Icone crée avec succès !")