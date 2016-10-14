# -*-coding:Latin-1

import os.path
import time
from datetime import datetime


#Premier test du futur programme Python
#Variables:
y = ("oui")
n = ("non")
v = 0
d = 0
nb_cnx = 0
nb_question = 2

t = datetime.now()

print(t)
print('Bonjour ! ')

print('Veille a mettre un espace avant chacunes de tes reponses !')

name = raw_input('Quel est ton nom ? ')

#enregistrement du nombre de connexion
cnxFilename = name + 'co.txt'
if os.path.exists(cnxFilename):
    nb_cnx = int(open(cnxFilename, "r").read())
    print('Tu as fait:' + str(nb_cnx) + 'parties')
nb_cnx = nb_cnx + 1
connexion = open(cnxFilename, "w")
connexion.write(str(nb_cnx))
connexion.close()

ask = raw_input('Tu te nommes bien ' + name + ' ? ')

if ask >= y:
   print(' Super ' + name + '!')
else:
   print(' Dommage, relance le programme et recommence ! ')

game = raw_input('Veux-tu jouer a un jeu ?')

if ask >= y:
   print('Bien, nous allons commencer!')
else:
   print('Tu peux fermer le programme. Bonne journee!')


##time.sleep(3)

source = open("source.txt", "r")

resultFilename = name + ".result.txt"
resultFile = open(resultFilename, "a")
answers = ""
for line in source:
  if not line:
     break
  else:
     tableau_question = line.strip().split(';')
     print(tableau_question[0])
     print(tableau_question[1])
     print(tableau_question[2])
     expectedAnswer = tableau_question[3]
     answer = input('Ta reponse:')
     answers = answers + ";Q" + str(tableau_question[0]) + ":" + str(answer)
     print(answer)
     print(expectedAnswer)
     if str(answer) != str(expectedAnswer):
       print("non!")
       d = d + 1
     else:
        print ("bien joue!")
        v = v + 1
answers = answers + ";" + str(v) + ";" + str(d)
resultFile.write(str(t) + answers)
resultFile.close()
source.close()

print("Merci d'avoir joue, je vais calculer tes reponses, afin de t'indiquer ton score. Tu peux egalement retrouver toutes tes reponses, dans un fichier stoker dans le dossier du jeu...")


if v > d:
     print("Tu remportes la victoire!""")

else:
     print("Perdu, relance le programme, et retente ta chance!")


cota_de_victoire = v*100/2





#time.sleep(2)

print('Resume de ' + name)

print('Tu as joue ' + str(nb_cnx) + ' parties')
print('Ton pourcentage de reussite pour cette partie est de ' + str(cota_de_victoire) + '%')


import time
#time.sleep(15)
