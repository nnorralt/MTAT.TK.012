def eelarve (kylalised):
    kogusumma = kylalised * 10 + 55
    return kogusumma

kylalised = int(input("Mitu inimest on kutsutud?"))
tulijad = int(input("Kes kindlalt tuleb?"))
print("maximaalne " + str(eelarve(kylalised)))
print("minimaalne " + str(eelarve(kylalised) - (kylalised - tulijad)*10))