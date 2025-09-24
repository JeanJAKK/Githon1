# Accueil et entrée des données par l'user

print("Calculateur de Notes - Système Educatif Togolais 🇹🇬")
print("=" * 60)

#Saisi informations personnelles
print("INFORMATIONS ETUDIANT")
nom_prenom = input("Nom et prénom de l'élève : ")
classe = input("Classe (ex: 3ème, 1ère, Tle) : ")
etablissement = input("Etablissement : ")

#Saisi des notes
print("SAISI DES NOTES DU TRIMESTRE ( sur 20 )")
note_math = float(input("Mathématiques : "))
note_francais = float(input("Feançais: "))
note_anglais = float(input("Anglais : "))
note_physique = float(input("Sciences Physiques : "))
note_svt = float(input("SVT : "))
note_histoGeo = float(input("Histoire-Géo : "))

# Affichage bulletin
print("=" * 60)
print(f"BULLETIN SCOLAIRE - {nom_prenom}")
print(f"{etablissement} - {classe}")
print("=" * 60)
print("\nNOTES DU TRIMESTRE :")
print(f"Mathématiques        : {note_math} (écart : +{note_math - 10}")
print(f"Français      : {note_francais} (écart : +{note_francais - 10}")
print(f"Anglais      : {note_anglais} (écart : +{note_anglais - 10}")
print(f"Sciences Physiques      : {note_physique} (écart : +{note_physique - 10}")
print(f"SVT     : {note_svt} (écart : +{note_svt - 10}")
print(f"Histoire - Géo      : {note_histoGeo} (écart : +{note_histoGeo - 10}")

print(f"\nRESULTATS GENERAUX : ")
# Calcul de points total et  moyenne generale
pts_total = note_svt + note_anglais + note_math + note_physique +note_histoGeo + note_francais
moyenne_gen = pts_total/6
print(f"Moyenne gnérales : {moyenne_gen:.2f}/20")
print(f"Total des points : {note_svt + note_anglais + note_math + note_physique +note_histoGeo +note_francais}/120")

# Validation
print("VALIDATION DES MATIERES (≥ 10/20) :")
print(f"Mathématiques  :{note_math >= 10}")
print(f"Français  :{note_francais >= 10}")
print(f"Anglais  :{note_anglais >= 10}")
print(f"Sciences Physiques  :{note_physique >= 10}")
print(f"SVT  :{note_svt >= 10}")
print(f"Histoire-Géo  :{note_histoGeo >= 10}")

# Analyses pédagogiques
print("\nANALYSES PEDAGOGIQUES :")
print(f"Matières fondamentales validées (Math ET Français) : {(note_math >= 10) and (note_francais >=10)}")
print(f"Toutes matières validées : {(note_math >= 10) and (note_francais >=10) and (note_anglais >= 10) and (note_svt >=10) and (note_physique >= 10) and (note_histoGeo >=10)}")
print(f"Profil scientifique : {note_math >= 14 and note_physique >= 14}")
print(f"Profil littéraire : {note_francais >= 14 and note_histoGeo >= 14}")
print(f"Profil équilibré : {note_math >= 14 and note_physique >= 14 and note_francais >= 14 and note_histoGeo}")

# Mention et décisions
print("\nMENTONS ET DECISIONS :")
print(f"Mention TRES BIEN (>= 16) : {moyenne_gen >= 16}")
print(f"Mention BIEN (>= 14) : {moyenne_gen >= 14}")
print(f"Mention ASSEZ BIEN (>= 12) : {moyenne_gen >= 12}")
print(f"Admis en classe supérieure (>= 10) : {moyenne_gen >= 10 and note_math >= 8 and note_francais >= 8}")
print(f"ECHEC (< 10) : {moyenne_gen < 10}")

# Matiere dominante
print("\nMATIERE DOMINANTE :")
print(f"Mathématiques en tête : {(note_math > note_physique) and (note_math > note_francais) and (note_math > 
                            note_anglais) and (note_math > note_svt) and (note_math > note_histoGeo)}")
print(f"Français en tête : {(note_francais > note_physique) and (note_francais > note_math) and (note_francais > note_anglais) and (note_francais > note_svt) and (note_francais > note_histoGeo)}")
print(f"Anglais en tête : {(note_anglais > note_physique) and (note_anglais > note_francais) and (note_anglais > note_math) and (note_anglais > note_svt) and (note_anglais > note_histoGeo)}")
print(f"Scinces Physiques en tête : {(note_physique > note_math) and (note_physique > note_francais) and (note_physique > note_anglais) and (note_physique > note_svt) and (note_physique > note_histoGeo)}")
print(f"Histoire-Géo en tête : {(note_histoGeo > note_physique) and (note_histoGeo > note_francais) and (note_histoGeo > note_anglais) and (note_histoGeo > note_svt) and (note_histoGeo > note_math)}")
print(f"SVT en tête : {(note_svt > note_physique) and (note_svt > note_francais) and (note_svt > note_anglais) and (note_svt > note_math) and (note_svt > note_histoGeo)}")

#Analyses approfondies
print("\nANALYSES APPROFONDIES")
print(f"Etudiant prometteur : {moyenne_gen >= 12 and not (note_math < 8 or note_francais < 8)}")
print(f"Orientation scientifique recommandée : {note_physique >= 12 and note_svt >= 12}")
print(f"Orientation littéraire recommandée : {note_histoGeo >=12}")
# une note ou plus inférieure à huit implique un besoin d'aide scolaire
print(f"Besoin de soutien scolaire : {note_svt < 8 or note_francais < 8 or note_math < 8 or note_histoGeo < 8 or note_anglais < 8 or note_physique < 8}")
print(f"Candidat à l'excellence : {note_math >= 18 or note_francais >= 18 or note_anglais >= 18}")

# Objectifs
print("\nOBJECTIFS A ATTEINDRE :")
print(f"Points pour la moyenne (10/20): {10 - moyenne_gen}")
print(f"Points pour Assez Bien (12/20): {12 - moyenne_gen}")
print(f"Points pour Bien (14/20): {14 - moyenne_gen}")
print(f"Points pour très Bien (16/20) : {16 - moyenne_gen}")

#potentiel
print("\nPOTENTIEL D'AMELIORATION :")
print(f"Maths : {20 - note_math} points sont possibles")
print(f"Français : {20 - note_francais} points sont possibles")
print(f"Anglais : {20 - note_anglais} points sont possibles")
print(f"Sciences : {20 - note_physique} points sont possibles")
print(f"SVT : {20 - note_svt} points sont possibles")
print(f"Géographie : {20 - note_histoGeo} points sont possibles")

# Messsage
print("🇹🇬 Bulletin établi selon le système éducatif togolais")
print("🎓 Bon courage  pour la suite de tes études !")
print(f"💪 Travaille dur {nom_prenom} pour réussir ton parcours scolaire !")