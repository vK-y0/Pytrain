print("Hello world!")

x = float(input("la valeur de x : "))
y = float(input("la valeur de y : "))

print("x :", x)
print("y :", y)

test = ( x + y ) / 2

print("Résultat :", test)

# Exercice 1 :

a = str(input(" 1ere string svp :"))
b = str(input(" 2ere string svp :"))

a.count(a[2])
c = a + b
print(c)
print(a.upper())
print(b.upper())
print(a.lower())
print(b.lower())
print(a.replace(a[2], "a", 1))
print(len(a))
print(len(b))

# # Exercice 2 :

d = int(input("Entrez un INTEGER ( Chiffre entier )"))
e = float(input("Entrez un FLOAT ( Chiffre decimal )"))
print( d + e )
print ( d * e )
print (( d + e ) / 2 )
print (d*d)
print (e*e)
print ( "x est plus grand" if d > e else "Les deux valeurs sont egales" if d == e else "y est plus grand")

# # Exercice 3 :

f = (input("Votre phrase"))
for i , item in enumerate(f):
    print(item)

# Exercice 4 :

#saisir taille du tableau
# creer un tableau en consequence
import random

array = [0]*(int(input("Veuillez entrez un nombre de case pour votre tableau")))

for i in range(len(array)):
    array[i] = random.randint(0,100)



# # afficher tableau case par case
for i in range(len(array)):
    print(array[i])
# comparer et trier T[i] et t[i+1]

for i in range(len(array)):
    if i+1 < len(array) and array[i] > array[i+1]:
        temp = array[i]
        array[i] = array[i+1]
        array[i+1] = temp

print(array)


# # generer un tableau a deux dimension avec 4 lignes et 6 colonnes le tout rempli de 0

nbligne = 4
nbcolonnes = 6
arr = [0]*nbligne
for i in range(0,nbligne):
    arr[i] = [0]*nbcolonnes
print(arr)

# Exercice 1 : « Premiers pas en Python »
# Ecrire un programme qui permet de :
# 1. Affectez les variables temps et distance par les valeurs 6.892 et 19.7.
temps = 6.892
distance = 19.7
# Calculez et affichez la valeur de la vitesse. Améliorez l’affichage en imposant un chiffre après le
# point décimal.
vitesse = distance/temps
print(round(vitesse,1))
# 2. Saisir un nom et un âge en utilisant l’instruction input(). Les afficher.
name = str(input("Saisissez votre nom"))
age = int(input("Saisissez votre age"))

print(name, age)
# Refaire la saisie du nom, mais avec l’instruction raw_input(). L’afficher.
# Enfin, utilisez la « bonne pratique » : recommencez l’exercice en transtypant les saisies
# effectuées avec l’instruction raw_input().
# Ecrire un programme qui demande à l’utilisateur de saisir un nom et un âge en utilisant
# l’instruction input(). Puis, les afficher.
# Exercice 2 :
# Ecrire un programme qui permet de saisir un flottant. Vérifier s’il est positif ou nul, affichez sa
# racine, sinon affichez un message d’erreur.
import math

floatToCheck = float(input("Saisissez un chiffre a virgule : "))
if floatToCheck > 0:
    print(floatToCheck,"est positif")
    print("Racine carré du chiffre que vous avez entré :", math.sqrt(floatToCheck))
# Exercice 3:
# Un entier est dit distinct s’il est composé de chiffres distincts (différents). Ecrire un programme
# python qui permet de saisir un entier n(n>0), puis de vérifier et d’afficher si cet entier est distinct
# ou non
# Exemple
# • N=1273 est dit distinct car il est formé par les chiffres 1,2, 7 et 3 qui sont tous distincts,
# donc, le programme affichera : cet entier est distinct
# • N=1565 est dit non distinct car il est formé par les chiffres 1,5, 6, 5 qui ne sont pas tous
# distincts (le chiffre 5 se répète deux fois, doncle programme affichera : cet entier est non
# distinct
distinct = str(input("Entrez un chiffre entier :"))
counter = 0
if int(distinct) > 0:
    for i in distinct:
        if distinct.count(i) > 1:
            print(i + " trouvé en double !!")
            print("Ce chiffre n'est pas distinct!")
            break
        else:
            counter += 1
            print("Chiffre " + i + " non trouvé en double")
            continue
    if counter == len(distinct):
        print("Le chiffre est distinct !!")

# Exercice 4 :
# Ecrire un programme qui permet de saisir deux mots, comparez-les en terme de longueur pour
# trouver le « plus petit » et affichez le résultat.
# Année Universitaire 2022-2023
# Marwa BEN M’BAREK 2

word1 = str(input("Entrez un premier mot : "))
word2 = str(input("Entrez un deuxieme mot : "))
print("le premier mot est plus petit" if len(word1) < len(word2) else "Les deux mots font la meme taille" if len(word1) == len(word2) else "le deuxieme mot est plus petit!")
# Exercice 5 :
# Ecrire un programme en Python qui demande à l’utilisateur de saisir le rayon d'un cercle et de lui
# renvoyer la surface et le périmètre.

rayon = int(input("Entrez un rayon de cercle : "))
pi = 3.14
print("Ceci est la surface du cercle :" , pi * rayon * rayon )
print("Son perimetre est : ", (rayon * 2) * pi)
# Exercice 6 :
# Écrire 2 fonctions :

def Even(number):
    return number%2 == 0

def Odd(number):
    return number%2 == 1

numberToTest = int(input("Veuillez entrer un chiffre pour voir si il est pair ou impair"))
print(Even(numberToTest))
print(Odd(numberToTest))

# — pair (nbre), qui renvoie True, si le nombre est Pair
# — impair (nbre), qui renvoie True, si le nombre est Impair
# Le nombres sera demandé à l’utilisateur.
# Exercice 7 :
# Écrire 2 fonctions :
# — mini (a,b) qui renvoie le minimum entre a et b
# — maxi (a,b) qui renvoie le maximum entre a et b
# Les 2 nombres a et b seront demandés à l’utilisateur.

def mini(a,b):
    return a if a < b else b

def maxi(a,b):
    return a if a > b else b

numberTwoToTest = int(input("Veuillez entrer un chiffre : "))
numberThreeToTest = int(input("Veuillez entrer un deuxieme chiffre : "))

print("le minimum est : ",mini(numberTwoToTest, numberThreeToTest))
print("le maximum est : ",maxi(numberTwoToTest, numberThreeToTest))
