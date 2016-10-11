# Reste à faire sur le projet Quizz Informatique

- [] : Ecrire les résultats de chaque partie dans un fichier nommé <nom_joueur>.res.txt (1)
- [] : Lire les question depuis un fichier source (2)
- [] : Afficher un résumé des résultats du joueur en fin de partie (3)

# Spécifications

## (1): Ecrire les résultats de chaque partie dans un fichier nommé "[nom_joueur].res.txt"
  Le format de sortie de ces résultats doit respecter les règles suivantes :
  - 1 ligne par partie
  - Le format d'une ligne est le suivant : [date_aaaammjj];Q1:reponse1;Q2:response2...;nb_reponse_vrai;nb_response_fausse

## (2): Lire les questions depuis un fichier source
  pour que la liste des questions puisse être dynamique, il faut pouvoir les lire depuis un fichier source.
  - Chaque ligne du fichier représente une question
  - Le format d'un ligne est le suivant : numero_de_la_question;intitulé_de_la_question;propositions;reponse_attendue

## (3): En fin de partie le quizz doit afficher un résumé des résultats du joueur.
Ce résumé affichera le nombre de partie joué ainsi que le pourcentage de victoire.
