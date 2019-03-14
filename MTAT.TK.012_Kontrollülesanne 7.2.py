from datetime import datetime

x = 0
paevik = open("paevik.txt", "a", encoding="UTF-8")
kanne = input("Mida sooviksid kirjutada oma päevikkuse?")
while x == 0:
    x = x + 1
    kuupäev_kellaeg = datetime.today()
    paevik.write(str(kuupäev_kellaeg))
    paevik.write(kanne)
paevik.close()