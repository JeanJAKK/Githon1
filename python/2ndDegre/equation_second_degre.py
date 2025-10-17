from math import sqrt

print("\n=== RÉSOLVEUR D'ÉQUATION DU SECOND DEGRÉ ===\n")
print("Cette équation est de la forme ax^2 + bx + c\n")

a = 0
while a == 0:
    a = float(input(f"Entrer a (valeur non nulle) : "))
b = float(input("Entrer b : "))
c = float(input("Entrer c : "))

delta = b ** 2 - 4 * a * c

if delta < 0 :
    neg_delta = -delta
    print(f'''
Solution 1 : {-b / (2 * a) } - {sqrt(neg_delta) / (2 * a) }i
Solution 2 : {-b / (2 * a)} + {sqrt(neg_delta) / (2 * a) }i
''')
elif delta == 0:
    print(f"Solution double : {-b / 2 * a}")
elif delta > 0:
    print(f'''
Solution 1 : {(-b - sqrt(delta)) / (2 * a) }
Solution 2 : {(-b + sqrt(delta)) / (2 * a) }
''')