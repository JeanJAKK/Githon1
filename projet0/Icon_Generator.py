# biblio pillow
from PIL import Image

# Ouvrir une image
image = Image.open("Citation_Einstein.jpg")

# Redimensionner
icone = image.resize((164, 164))

# save as icone
icone.save("myIcone.ico")
print("Icone crée avec succès !")
