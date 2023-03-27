#Job 13
array = []
debug = False
#Fonction d'ajout de donnée dans le tableau
def integration(array):
        a = input("Entrer un integer ?")
        
        if (a.startswith('-') and a[1:].isdigit()) or (a.isdigit()):
            a = int(a)
            array.append(a)
        else:
            print("Vous n'avez pas taper un integer")
            a = input("Entrer un integer ?")

        return array

#Boucle while pour répéter 5 fois la solution

while len(array) < 5:
    integration(array)

# Affichage
if debug:
    print(array)

array.sort()

print("Affichage du tableau trié :")
print(array)