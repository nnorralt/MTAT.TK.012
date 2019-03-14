vanus = int(input("Sisesta oma vanus täisarvuna:"))
sugu = input("Sisesta oma sugu (m - mees, n - naine):")
treening = int(input("Sisesta oma treening (1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening)"))
naine = ["n","N"]
mees = ["m", "M"]
meespulss1min = round(0.5*(220-vanus))
meespulss1max = round(0.7*(220-vanus))
meespulss2min = round(0.7*(220-vanus))
meespulss2max = round(0.8*(220-vanus))
meespulss3min = round(0.8*(220-vanus))
meespulss3max = round(0.87*(220-vanus))
nainepulss1min = round(0.5*(206-(0.88*vanus)))
nainepulss1max = round(0.7*(206-(0.88*vanus)))
nainepulss2min = round(0.7*(206-(0.88*vanus)))
nainepulss2max = round(0.8*(206-(0.88*vanus)))
nainepulss3min = round(0.8*(206-(0.88*vanus)))
nainepulss3max = round(0.87*(206-(0.88*vanus)))

if sugu in mees and treening == 1:
    print("Pulsisagedus peaks olema vahemikus " + str(meespulss1min) + " kuni " + str(meespulss1max))
elif sugu in mees and treening == 2:
    print("Pulsisagedus peaks olema vahemikus " + str(meespulss2min) + " kuni " + str(meespulss2max))
elif sugu in mees and treening == 3:
    print("Pulsisagedus peaks olema vahemikus " + str(meespulss3min) + " kuni " + str(meespulss3max))
if sugu in naine and treening == 1:
    print("Pulsisagedus peaks olema vahemikus " + str(nainepulss1min) + " kuni " + str(nainepulss1max))
if sugu in naine and treening == 2:
    print("Pulsisagedus peaks olema vahemikus " + str(nainepulss2min) + " kuni " + str(nainepulss2max))
if sugu in naine and treening == 3:
    print("Pulsisagedus peaks olema vahemikus " + str(nainepulss3min) + " kuni " + str(nainepulss3max))