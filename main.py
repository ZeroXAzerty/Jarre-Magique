from random import randint
from niveau import niveau1
from niveau import niveau2
print("||--------------------------------||")
niveau = int(input("""||Quel niveau veux tu faire-------||
||Je souhaite faire le niveau """))
if niveau == 1:
    niveau1()
if niveau == 2:
    niveau2()
