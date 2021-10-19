from random import randint
import time

def niveau1():
    jarre = randint(0,5)
    value = int(input("""||Choisis une jarre entre 1 et 5 !||
||Je souhaite la jarre """))

    if value == jarre:
        print("||La jarre étais piégé !!---------||")
        print("||--------------------------------||")
    else : 
        print("||La jarre n'étais pas piégé------||")
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
                print("||La jarre étais piégé !!---------||")
                time.sleep(1.5)
                print("||Tu perd une clé !---------------||")
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
                print("||La jarre n'étais pas piégé------||")
                time.sleep(1.5)
                print("||Tu gagne une clé !--------------||")
                clé = clé + 1
                time.sleep(1.5)
                print(f"||Tu es a {clé} clées------------------||")
                time.sleep(1.5)
                print("||--------------------------------||")
        else :
            print("||Bravo tu a gagné !--------------||")
            time.sleep(1.5)
            print("||--------------------------------||")