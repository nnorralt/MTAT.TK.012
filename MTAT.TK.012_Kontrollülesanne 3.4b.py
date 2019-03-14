from random import randint
max_vise = int(input("Mis on tõenäosus visketabavusel?"))
i = 0
vise = randint(1,100)
tabamusi = 0
while i <= 1000 :
    if randint(1,100) <= max_vise:
        print(str(i) + " vise tabas.")
        tabamusi = tabamusi + 1
    else:
        print(str(i) + " vise oli mööda.")
    i = i + 1
print("Tabas " + str(tabamusi) + " viset.")