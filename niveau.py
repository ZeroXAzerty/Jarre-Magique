from random import randint
import time
from colorama import Fore, Back, Style


def niveau1():
    while True :
        jarre = randint(0,5)
        value = int(input("""||Choisis une jarre entre 1 et 5 !||
||Je souhaite la jarre """))

        if value == jarre:
            print(f"||{Fore.RED}La jarre étais piégé !!{Fore.WHITE}---------||")
            print("||--------------------------------||")
        else : 
            print(f"||{Fore.GREEN}La jarre n'étais pas piégé{Fore.WHITE}------||")
            print("||--------------------------------||")

def niveau2():
    jarre = randint(0,5)
    clé = 0
    run = True
    while run == True:
        if clé < 3 : 
            value = int(input("""||Choisis une jarre entre 1 et 5 !||
||Je souhaite la jarre """))

            if value == jarre:
                print(f"||{Fore.RED}La jarre étais piégé !!{Fore.WHITE}---------||")
                time.sleep(1.5)
                print(f"||{Fore.RED}Tu perd une clé !{Fore.WHITE}---------------||")
                clé = clé - 1
                time.sleep(1.5)
                print(f"||Tu es a {clé} clées------------------||")
                time.sleep(1.5)
                print("||--------------------------------||")
            elif value > 5 :
                print("En dessous de 5 !")
                time.sleep(1.5)
                print("||--------------------------------||")
            else : 
                print(f"||{Fore.GREEN}La jarre n'étais pas piégé{Fore.WHITE}------||")
                time.sleep(1.5)
                print("||Tu gagne une clé !--------------||")
                clé = clé + 1
                time.sleep(1.5)
                print(f"||Tu es a {clé} clées------------------||")
                time.sleep(1.5)
                print("||--------------------------------||")

        elif clé == 0 :
            print(f"{Fore.RED}||Tu as perdu !{Fore.WHITE}-------------------||")

        else :
            print("||Bravo tu a gagné !--------------||")
            time.sleep(1.5)
            print("||--------------------------------||")

        
