mot = input("Veuillez entrer un mot sans espace ni caractère spécial : ")

# Vérifier si le mot ne contient que des lettres de l'alphabet
if not mot.isalpha():
    print("Le mot doit contenir uniquement des lettres de l'alphabet.")
    exit()

# Convertir le mot en une liste de caractères pour pouvoir le modifier facilement
lettres = list(mot)

# Parcourir la liste de caractères et trouver les deux lettres qui doivent être échangées
for i in range(len(lettres)-1, 0, -1):
    if lettres[i] > lettres[i-1]:
        # Trouver la lettre la plus petite qui est plus grande que la lettre précédente
        min_suivant = i
        for j in range(i, len(lettres)):
            if lettres[j] > lettres[i-1] and lettres[j] < lettres[min_suivant]:
                min_suivant = j
        # Échanger les deux lettres
        lettres[i-1], lettres[min_suivant] = lettres[min_suivant], lettres[i-1]
        # Trier les lettres suivantes pour qu'elles soient dans l'ordre croissant
        lettres[i:] = sorted(lettres[i:])
        # Sortir de la boucle
        break

# Reconstruire le mot à partir de la liste de caractères modifiée
nouveau_mot = ''.join(lettres)

# Afficher le résultat
print("Le nouveau mot est :", nouveau_mot)
