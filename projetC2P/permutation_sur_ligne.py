# entré
pre = int(input("Le premier nombre: "))
second = int(input("Le second nombre: "))

# Traitement
if pre * second > 0 :
    pre,second = second,pre
    print(f"pre ={pre} et second ={second}")
elif pre * second < 0 :
    pre, second = pre + second , pre * second 
    print(f"pre ={pre} et second ={second}")
elif second == 0 and pre == 0 :
    print("Les deux nombres sont nul")
else :
    print("L'un des deux nombres est nul")