def triangle(h):        
    if (h.isdigit()):
        h = int(h)
    else:
        print("Vous n'avez pas taper un integer ou mi un chiffre négatif.")
        h = input("Entrer un integer ?")

    # Boucle pour dessiner les lignes du triangle


    for i in range(1, h):
    
        if i == 1:
            print(" " * ((h-1) - i) + "/\\" + " " * (5 - i))

        elif i == (h-1):
            print("/" + "_"  * ((i *2) - 2) + "\\")
        else:
            print(" " * ((h-1) - i) + "/" + " " * ((i - 1) * 2) + "\\" + " " * ((h-1) - i))

h = input("Hauteur du triangle ?")
triangle(h)