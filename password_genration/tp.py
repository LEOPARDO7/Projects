import random

s=random.randint(0, 4)
v=int(input("Enter your number between 1-3\n"))

if (s==v):
    print(s)
    print("correct guess")
else:
    print(s)
    print("wrong guess")