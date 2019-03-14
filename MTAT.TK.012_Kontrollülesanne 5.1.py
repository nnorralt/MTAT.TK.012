
fail = open("mopeedid.txt", encoding="UTF-8")
 
mopeedid = []
for rida in fail:
 
   mopeedid.append(int(rida))   
 
fail.close()
valik = int(input("Palun sisesta mitmes kuu numbriga:"))
print(str(valik) + ". kuul registreeriti " + str(mopeedid[valik - 1]))