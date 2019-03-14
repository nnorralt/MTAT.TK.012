def teleri_diagonaal(asukohani):
    diagonaal = round(asukohani * 100 * 0.39 / 2.5)
    return diagonaal
asukohani = float(input("kui kaugel on diivanist televiisor?"))
print(str(teleri_diagonaal(asukohani)))