from random import randint

taringuid = int(input("Mitu täringut visatakse?"))
i = 0
vise = 0
while taringuid != i:
    vise = randint(1,6)
    print(str(vise))
    taringuid = taringuid - 1

                   