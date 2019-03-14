from datetime import *

failinimi = input("Sisesta failinimi:")
fail = open(failinimi, encoding="UTF-8")
jrk = 1
mitmes = 0
for each in fail:
    print(str(jrk) + ". " + str(each))
    jrk = jrk + 1
valik = int(input("vali milline sihtkoht broneerida:"))
if valik = 1:
    for each in fail:
        print(
