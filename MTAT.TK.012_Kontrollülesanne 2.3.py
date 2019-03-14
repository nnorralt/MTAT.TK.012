nimi = input("Sisestage Leedu perekonnanimi:")
if nimi[-2] == "n" and nimi[-1] == "e":
    print("Abielus")
elif nimi[-2] == "t" and nimi[-1] == "e":
    print("Vallaline")
elif nimi[-1] == "e" and nimi[-2] != "t" and nimi[-2] != "n":
    print("Määramata")
elif nimi[-1] != "e":
    print("Pole ilmselt leedulanna perekonnanimi")