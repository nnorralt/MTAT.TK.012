failinput = input("sisesta faili nimi .txt lõpuga")

f = open(failinput,encoding="UTF-8")
loetud = f.read()
kylalised = 0
tulijad = 0
for rida in loetud: # ridade kaupa
        if rida == "":
            break
        elif rida[0] == "?":
            kylalised += 1
        elif rida[0] == "+":
            kylalised += 1
            tulijad += 1
f.close() # faili ei lähe enam vaja        


def eelarve (kylalised):
    kogusumma = kylalised * 10 + 55
    return kogusumma

print("kutsutud on " + str(kylalised))
print("tulijad on " + str(tulijad))
print("maximaalne " + str(eelarve(kylalised)))
print("minimaalne " + str(eelarve(kylalised) - (kylalised - tulijad)*10))