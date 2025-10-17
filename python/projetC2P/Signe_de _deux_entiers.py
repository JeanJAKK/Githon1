# entré
pre = int(input("Le premier nombre: "))
second = int(input("Le second nombre: "))

# Traitement
if pre * second > 0 :
    print("Les deux nombres sont de même signe")
elif pre * second < 0 :
    print("Les deux nombres sont de signes contraires")
elif second == 0 and pre == 0 :
    print("Les deux nombres sont nul")
else :
    print("L'un des deux nombres est nul")