from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Chemin du fichier de sortie
pdf_output_path = "convention_nomage_branches_v2.pdf"

# Création du PDF
c = canvas.Canvas(pdf_output_path, pagesize=A4)
width, height = A4

# === Titre principal ===
c.setFont("Helvetica-Bold", 16)
c.setFillColor(colors.darkblue)
c.drawCentredString(width / 2, height - 60, "📘 Convention de nommage des branches GitHub")

# Position de départ
y_position = height - 100
line_height = 18

# === Contenu structuré ===
sections = [
    ("🎯 Objectif", [
        "Faciliter la gestion des branches en identifiant clairement :",
        "➤ La zone technique concernée (front, back, ou shared)",
        "   ▪ front : Travail sur le front-end",
        "   ▪ back : Travail sur le back-end",
        "   ▪ shared : Travail sur les deux",
        "➤ Le prénom de l’auteur"
    ]),
    ("📌 Règles", [
        "• Tout en minuscules",
        "• Format kebab-case : mots séparés par des tirets (-)",
        "• Zone : front, back, ou shared",
        "• Prénom : sans majuscule",
        "• Faire des commit concis."
    ])
]

# === Affichage du contenu ===
for title, content in sections:
    # Titre de section
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.black)
    c.drawString(50, y_position, title)
    y_position -= line_height * 1.5

    # Corps du texte
    c.setFont("Helvetica", 12)
    for line in content:
        c.drawString(70, y_position, line)
        y_position -= line_height

        # Saut de page automatique si besoin
        if y_position < 60:
            c.showPage()
            y_position = height - 60
            c.setFont("Helvetica", 12)

c.save()

print(f"✅ PDF généré avec succès : {pdf_output_path}")
