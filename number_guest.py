#Importation du module random pour la valeur aléatoire
import random
#Importation du module date
import datetime
#Variable stockant la valeur aléatoire
random_number = random.randint(1, 200)
#Variable stockant le nombre d'essai effectué par l'utilisateur
counter = 0
#Variable qui vérifie si le programme est démarré ou pas
is_running = True
#Consigne destiné à l'utilisateur pour savoir ce que le programme lui demande de faire
date = datetime.datetime.now()
date = date.strftime('%d-%m-%y %H:%M')
print('***************************************************')
print('------------------- Consignes ---------------------')
print('Trouvez le bon chiffre entre 1 et 200. Vous avez droit à 5 essais.')
print('')
print('------------------- Code source -------------------')
print('Github Repository : ')
print('')
print(date)
print('***************************************************')
print('')
print('')
#Condition qui verifie si le programme est demarré et le nombre d'essais effectué par l'utilisateur
while is_running:
    if counter < 5:
        try:
            user_input = int(input('Quel chiffre que le système a choisi aléatoirement? : '))
            counter += 1
            if user_input < random_number:
                print('Mauvaise réponse. Choisissez un chiffre plus grand')
                print('')
            elif user_input > random_number:
                print('Mauvaise réponse. Choisissez un chiffre plus petit')
                print('')
            else:
                print('Félicitations. Vous avez trouvé la bonne réponse')
                is_running = False
        except:
            print('Veuillez entrer un chiffre entier')
            print('')
    else:
        print('Partie terminée. Le nombre d\'essai est atteint.')
        print('Le bon chiffre est : ', random_number)
        is_running = False
    