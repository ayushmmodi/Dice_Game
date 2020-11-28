import random

ans="y"
while ans=="y":
    d1=random.randint(1,6)
    print(d1)
    ans=input("Do you want to continue ").lower()
    if ans == 'n'.lower():
        break