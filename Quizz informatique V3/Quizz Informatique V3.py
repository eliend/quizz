# -*-coding:Latin-1

#Premier test du futur programme Python
#Variables:
y = ("oui")
n = ("non")
v = 0
d = 0
nb_cnx = 0
nb_question = 2


import os.path

from datetime import datetime
t = datetime.now()


#Les variables "v" et "d" sont là pour une futur version du quizz, ou le programme pourra calcuer les réponses de l'utilisateurs,
#et déduire sa victoire ou sa défaite, en fonction de son nombres de bonnes/mauvaises réponses.

print(t)
print('Bonjour ! ')

print('Veuille a mettre un espace avant chacunes de tes reponses !')

name = raw_input('Quel est ton nom ? ')

filename = name + 'co.txt'
if os.path.exists(filename):
    nb_cnx = int(open(filename, "r").read())
    print('Tu as fait:' + str(nb_cnx) + 'parties')

nb_cnx = nb_cnx + 1
connexion = open(filename, "w")
connexion.write(str(nb_cnx))
connexion.close()

fichier = open(name + ".result.txt", "a")

ask = raw_input('Tu te nommes bien ' + name + ' ? ')

if ask >= y:
   print(' Super ' + name + '!')
else:
   print(' Dommage, relance le programme et recommence ! ')

game = raw_input('Veux-tu jouer a un jeu ?')

if ask >= y:
   print('Bien, nous allons commencer!')

else:
   print('Tu peux fermer le programme. Bonne journée!')

import time
time.sleep(3)

source = open("source.txt", "r")

for line in source:
  if not line:
     break
  else:
     tableau_question = line.split(';')
     print(tableau_question[0])
     print(tableau_question[1])
     print(tableau_question[2])


source.close()

answer1 = input('Ta reponse:')

if answer1<=3:
  print("non!")
  d = d + 1
  fichier = open(".result.txt", "a")
  fichier.write(str(t) + 'Q1: Mauvaise réponse; ')
  50
  fichier.close()

else:
   print ("bien joue!")
   v = v + 1
   fichier = open(name + ".result.txt", "a")
   fichier.write(str(t) + ' Q1: Bonne reponse;')
   50
   fichier.close()

import time
time.sleep(3)

answer2=input('Ta reponse:')

if answer2<=2<3:
   print("non!")
   d = d + 1
   fichier = open(name + ".result.txt", "a")
   fichier.write(" Q2: Mauvaise réponse;")
   50
   fichier.close()

else:
   print("bien joue!")
   v = v + 1
   fichier = open(name + ".result.txt", "a")
   fichier.write(" Q2: Bonne réponse;")
   50
   fichier.close()
time.sleep(2)

print("Merci d'avoir joue, je vais calculer tes réponses, afin de t'indiquer ton score. Tu peux egalement retrouver toutes tes reponses, dans un fichier stoker dans le dossier du jeu...")

time.sleep(5)

if v > d:
     print("Tu remportes la victoire!""")
else:
     print("Perdu, relance le programme, et retente ta chance!")



time.sleep(2)

print('Resume de ' + name)

print('Tu as joue ' + str(nb_cnx) + ' parties')

cota_de_victoire = v*100/2

print('Ton pourcentage de reussite est de ' + str(cota_de_victoire) + '%')



import time
time.sleep(15)
