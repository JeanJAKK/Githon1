# saisi des notes
note1 = float(input("La première note: "))
note2 = float(input("La deuxième note: "))
note3 = float(input("La troisième note: "))

# Traitement
moyenne = (note1 + note2 + note3)/ 3

# Affichage
if moyenne >=16 :
    print(f"La moyenne est {moyenne:.2f}. Mention: Très Bien")
elif moyenne < 16 and moyenne >= 14 :
    print(f"La moyenne est {moyenne:.2f}. Mention: Bien")
elif moyenne < 14 and moyenne >= 12 :
    print(f"La moyenne est {moyenne:.2f}. Mention: Assez Bien")
elif moyenne < 12 and moyenne >= 10 :
    print(f"La moyenne est {moyenne:.2f}. Mention: Passable")
else :
    print(f"La moyenne est {moyenne:.2f}. Mention: Insuffissant")
