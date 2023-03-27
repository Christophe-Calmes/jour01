#Jobbbb 19
# Définir la largeur et la hauteur du rectangle
debug = True
array = []
message = ["Hauteur de votre rectangle ?", "Largeur de votre rectangle ?"]

#Déclaration des fonctions

def draw_rectangle (array):
    
    withd = array[1]
    heigth = array[0]
# Définir les chaînes de caractères pour les bords et l'intérieur du rectangle
    bord_horizontal = '--' * withd
    bord_vertical = '|'
    interieur =  '  ' * heigth

    # Afficher le rectangle
    print(bord_vertical + bord_horizontal + bord_vertical)
    for i in range(heigth - 4):
        print(bord_vertical + interieur + bord_vertical)

    print(bord_vertical + bord_horizontal + bord_vertical)    



def integration(array, message, i):
        a = input(message[i])
        
        if (a.isdigit()):
            a = int(a)
            array.append(a)
        else:
            print("Vous n'avez pas taper un integer ou mi un chiffre négatif.")
            a = input("Entrer un integer ?")

        return array

for i in range(2):
    integration(array, message, i)


if len(array) == 2:
    if debug:
        print(array)
    draw_rectangle(array)

   

    if debug:
        withd = 5
        heigth = 5
        #Définir les chaînes de caractères pour les bords et l'intérieur du rectangle
        bord_horizontal = '--' * withd
        bord_vertical = '|'
        interieur =  '  ' * heigth
    # Afficher le rectangle
        print("###########Exemple##########")
        print(bord_vertical + bord_horizontal + bord_vertical)
        for i in range(heigth - 4):
            print(bord_vertical + interieur + bord_vertical)
            print(bord_vertical + bord_horizontal + bord_vertical)