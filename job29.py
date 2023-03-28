#note = 83
#print(note % 5)

# Création d'une fonction 
array = []
arrayNote = []
debug = True
#Fonction d'ajout de donnée dans le tableau
print("Luke, entre 5 notes comprise entre 0 et 100.")
def integration(array):
        a = input("Entrer une note Luke ?")
        
        if (a.startswith('-') and a[1:].isdigit()) or (a.isdigit()):
            a = int(a)
           
            if a <= 100:
                array.append(a)
            else:
                 print("La note est trop haute.")
        else:
            print("Vous n'avez pas taper un integer ou mi un chiffre négatif.")
            a = input("Entrer un integer ?")

        return array

def transforce(note):
     if (note % 5 == 0):
            return note
     if  ((note + 2) % 5 == 0):
          return note + 2
     if  ((note + 1) % 5 == 0):
          return note + 1
     if note % 5 != 0:
          return note



def force (array, arrayNote):
    i = 0
    while i < len(array):
        if array[i] < 40:
            arrayNote.append(0)
            print("note < 40")
        else:
             #Transformation
                arrayNote.append(transforce(array[i]))
            
        i += 1
    return arrayNote

               

for i in range(5):
    integration(array)
if debug:
     print(array)
    
force(array, arrayNote)
print(arrayNote)
