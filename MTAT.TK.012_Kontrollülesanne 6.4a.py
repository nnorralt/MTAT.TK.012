def tervitus (jrk):
    print('Võõrustaja: "Tere!" \n    Täna ' + str(jrk) + '. kord tervitada, mõtiskleb võõrustaja. \n    Külaline: "Tere, suur tänu kutse eest!"')
kylalisi = int(input("mitu külalist on?"))
kylalisi = kylalisi + 1
jrk = 1
while jrk != kylalisi:
    tervitus(jrk)
    jrk = jrk + 1