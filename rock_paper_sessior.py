import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp =='r':
        if you =='s':
            return False
        elif you =='p':
            return True
    elif comp =='p':
        if you =='r':
            return False
        elif you =='s':
            return True
    elif comp =='s':
        if you =='p':
            return False
        elif you =='r':
            return True



randno=random.randint(1,3)

if randno == 1:
    comp = 'r'
elif randno == 2:
    comp ='p'
elif randno == 3:
    comp ='s'



you=input("Your turn: Rock(r) Paper(p) Sissers(s)")
a=gamewin(comp,you)

print(f"comp turn {comp}")

print(f"you turn {you}")

if a == None:
    print("this game is tie!")
elif a:
    print("you win")
else :
    print("you loose")