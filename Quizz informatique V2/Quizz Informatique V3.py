# -*-coding:Latin-1

#Premier test du futur programme Python
#Variables:
y = ("Oui")
n = ("Non")
v = 0
d = 0
#Les variables "v" et "d" sont là pour une futur version du quizz, ou le pgrogramme pourra calcuer les réponses de l'utilisateurs,
#et déduire sa victoire ou sa défaite, en fonction de son nombres de bonnes/mauvaises réponses.

print('Bonjour ! ')

print('Veuille a mettre un espace avant chacunes de tes reponses !')

name = raw_input('Quel est ton nom ? ')

fichier = open('result'+ name + 'result.txt', "a")


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

print """ Question 1: Sais-tu d'ou vient le nom du langage de programmation Python ? \n
  1. Du serpent
  2. D'un groupe de musique
  3. D'une ville
  4. D'une serie televisee\n"""

answer1=input('Votre reponse:')

if answer1<=3:
  print("non!")
  d = d + 1
  fichier = open('result'+ name + 'result.txt', "a")
  fichier.write("Q1: Mauvaise réponse;")
  50
  fichier.close()

else:
   print ("bien joue!")
   v = v + 1
   fichier = open('result'+ name + 'result.txt', "a")
   fichier.write("Q1: Bonne reponse;")
   50
   fichier.close()

import time
time.sleep(3)

print """ Question 2: Quelle formule est courrament utilisee lors de la creation de son premier programme? \n
  1. Bonjour à tous.
  2. Hello World?
  3. Hello Word!
 \n"""

answer2=input('Votre reponse:')

if answer2<=2:
   print("non!")
   d = d + 1
   fichier = open('result'+ name + 'result.txt', "a")
   fichier.write(" Q2: Mauvaise réponse;")
   50
   fichier.close()

else:
   print("bien joue!")
   v = v + 1
   fichier = open('result'+ name + 'result.txt', "a")
   fichier.write(" Q2: Bonne réponse;")
   50
   fichier.close()

#   import time
time.sleep(2)

print("Merci d'avoir joue, je vais calculer tes réponses, afin de t'indiquer ton score. Tu peux également retrouver toutes tes reponses, dans un fichier stoker dans le dssier du jeu...")

time.sleep(5)


if v > d:
     print("Tu remportes la victoire !")
else:
     print("Perdu, relance le programme, et retente ta chance!")