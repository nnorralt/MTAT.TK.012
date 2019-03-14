suurus = float(input("Suurus mb?"))
pealkiri = input("kirja pealkiri?")
fail_olemas = input("Fail manusena kaasas, jah või ei?")

if (not pealkiri) or (fail_olemas in ("jah") and suurus > 1): #if not on soovituslik viis stackoverflow
    #järgi mille järgi ideaalis kirjutada et sisu ehk pealkiri peaks eksisteerima. ta checkib kas
    #sellele muutujale on üldse mingi väärtus ka antud ehk kas pealkiri üldse midagi tähendab
    print("Kiri on spämm")

else:
    print("Kiri ei ole spämm")