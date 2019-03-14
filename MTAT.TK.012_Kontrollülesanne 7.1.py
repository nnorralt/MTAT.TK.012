failinput = input("sisesta faili nimi .txt lõpuga")
f = open(failinput,encoding="UTF-8")
loetud = f.read()
telegramm = ""
for rida in loetud: # ridade kaupa
    for sümbol in rida: # sümbolite kaupa
        if sümbol == "":
            break
        elif sümbol == "Ä":
            print("AE", end = "")
        elif sümbol == "ä":
            print("AE", end = "")
            
        elif sümbol == "Õ":
            print("OE", end = "")
        elif sümbol == "õ":
            print("OE", end = "")
        elif sümbol == "Ö":
            print("OE", end = "")
        elif sümbol == "ö":
            print("OE", end = "")
        elif sümbol == "Ü":
            print("UE", end = "")
        elif sümbol == "ü":
            print("UE", end = "")
        else:
            print(sümbol.upper(), end = "")
 
f.close() # faili ei lähe enam vaja        
