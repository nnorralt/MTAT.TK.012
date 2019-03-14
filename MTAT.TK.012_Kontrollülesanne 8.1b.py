#KIRJELDUS:
#Dungeons & Dragons duelli simulaator. Programm on loodud original content reeglistikule ja 'maailmale'
#et tuvastada, kelle tegelased tõenäoliselt võidaksid kahevõitluse. Pärast kahe võitleja andmete sisestamist jooksutab
#programm läbi palutud arvu võitlusi ning väljastab andmed: tõenäolise võitja ja palju muud statistikat. Programm on loodud spetsiaalselt, et
#tuvastada võimalused tasakaalust väljas tegelaskujude loomiseks ning tulevikus reeglistikku korrigeerida.

from random import randint
from easygui import * #easygui.py folderist

kaitsminevariandid = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
eludvariandid = [0,6,12,18,24,30,36,42,48,54,60]
pihtavariandid = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
kaitsevariandid = [0,1,2,3,4,5,6,7,8,9,10]
hitsvariandid = [1,2,3,4]
boonusdmgvariandid = [0,1,2,3,4,5,6,7,8,9,10]
relvvariandid = [4,6,8,10,12,20]




#siin on global muutujad välja toodud

hero1voit = 0 #esimese võitleja võitude arv
hero2voit = 0 #teise võitleja võitude arv
x = 0 #duelli number
y = 0 #roundide nr võitluses
z = 0 #kõikide roundide hulga nr
herovise1 = 0 #d20 vise pihta löömisel esimesel võitlejal
herovise2 = 0 #d20 vise pihta löömisel teisel võitlejal
critS1 = 0 #d100 critical range kui crit hit
critF1 = 0 #d100 crit range kui crit fail
critS2 = 0 #d100 critical range kui crit hits
critF2 = 0 #d100 crit range kui crit fail
stunround1 = 0 #vahele jäävate roundide arv 1. võitlejale (alg muutuja)
stunround2 = 0 #vahele jäävate roundide arv 2. võitlejale (alg muutuja)

hero_1 = 0
hero_2 = 0
elud_1 = 0
elud_2 = 0
relv_1 = 0
relv_2 = 0
herovise_1 = 0
herovise_2 = 0
hits_1 = 0
hits_2 = 0
kaitsmine_1 = 0
kaitsmine_2 = 0
stunround_1 = 0
stunround_2 = 0

#loome akna easyGUI-ga ja sisestame duellide simuleerimise arvu
simulatsiooniarv = int(enterbox("Sisesta mitu korda duelli simuleeritakse:"))

# 1. võitleja statid easyGUI-ga
hero1 = enterbox("Sisesta esimese võitleja nimi: ")
elud1 = int(choicebox("Sisesta esimese võitleja elud:", choices = eludvariandid))
kaitsmine1 = int(choicebox("Sisesta esimese võitleja kaitsmine:", choices = kaitsminevariandid))
kaitse1 = int(choicebox("Sisesta esimese võitleja kaitse:", choices = kaitsevariandid))
pihta1 = int(choicebox("Sisesta esimese võitleja pihta:", choices = pihtavariandid))
haiget1 = int(choicebox("Sisesta esimese võitleja haiget tegemise boonus:", choices = boonusdmgvariandid))
hits1 = int(choicebox("Sisesta mitu korda esimene võitleja lööb käigu jooksul:", choices = hitsvariandid))
relv1 = int(choicebox("Sisesta esimese võitleja relva täringu number( nt 8 kui on relv d8):", choices = relvvariandid))
# 2. võitleja statid
hero2 = enterbox("Sisesta teise võitleja nimi: ")
elud2 = int(choicebox("Sisesta teise võitleja elud:", choices = eludvariandid))
kaitsmine2 = int(choicebox("Sisesta teise võitleja kaitsmine:", choices = kaitsminevariandid))
kaitse2 = int(choicebox("Sisesta teise võitleja kaitse:", choices = kaitsevariandid))
pihta2 = int(choicebox("Sisesta teise võitleja pihta:", choices = pihtavariandid))
haiget2 = int(choicebox("Sisesta teise võitleja haiget tegemise boonus:", choices = boonusdmgvariandid))
hits2 = int(choicebox("Sisesta mitu korda teise võitleja lööb käigu jooksul:", choices = hitsvariandid))
relv2 = int(choicebox("Sisesta teise võitleja relva täringu number( nt 8 kui on relv d8):", choices = relvvariandid))

#alljärgnevalt nimekirjad statistika ja keskmiste arvutamiseks.
hero1list = [] #list millesse lisatakse iga duelli lõpus esimese võitleja elud
hero2list = [] #list millesse lisatakse iga duelli lõpus teise võitleja elud
hero1hitlist = [] #list millesse lisatakse esimese võitleja haiget teinud löögid
hero2hitlist = [] #list millesse lisatakse teise võitleja haiget teinud löögid
vehkimisi1list = [] #list millesse lisatakse  esimese võitleja pihta läinud löögid
vehkimisi2list = [] #list millesse lisatakse teise võitleja pihta läinud löögid

#algavad crit funktsioonide defineerimine hero 1 jaoks

#crit hit funktsioonid 1. võitleja jaoks

def crit1hit1 ():
    global hero1
    global hero2
    global relv_1
    global haiget1
    global elud_2
    global kaitse2
    global hero1hitlist
    dam1 = (randint(1,relv_1) + haiget1 - kaitse2)
    if dam1 > 0:
        elud_2 = elud_2 - dam1
        print(hero1 + " lõi " + hero2 + " CRITICALIGA ja " + hero2 + " on nüüd " + str(elud_2) + " elusid")
        hero1hitlist.append(1)
    
def crit1hit2 ():
    global relv_1
    global haiget1
    global kaitse2
    global elud_2
    global hero2
    global hero1
    global hero1hitlist
    dam1 = ((randint(1,relv_1) + haiget1) * 2 - kaitse2)
    if dam1 > 0:
        elud_2 = elud_2 - dam1
        print(hero1 + " lõi " + hero2 + " CRITICALIGA ja " + hero2 + " on nüüd " + str(elud_2) + " elusid")
        hero1hitlist.append(1)

def crit1hit3 ():
    global relv_1
    global haiget1
    global kaitse2
    global elud_2
    global hero2
    global hero1
    global hero1hitlist
    global hits_1
    hits_1 = hits_1 + 1
    dam1 = (randint(1,relv_1) + haiget1 - kaitse2)
    print(hero1 + " ründab eriti hoogsalt ja saab lisarünnaku!")
    if dam1 > 0:
        elud_2 = elud_2 - dam1
        print(hero1 + " lõi " + hero2 + " CRITICALIGA ja " + hero2 + " on nüüd " + str(elud_2) + " elusid")
        hero1hitlist.append(1)

def crit1hit4 ():
    global relv_1
    global haiget1
    global kaitse2
    global elud_2
    global hero2
    global hero1
    global hero1hitlist
    dam1 = relv_1 + haiget1 - kaitse2
    if dam1 > 0:
        elud_2 = elud_2 - dam1
        print(hero1 + " lõi " + hero2 + " CRITICALIGA ja " + hero2 + " on nüüd " + str(elud_2) + " elusid")
        hero1hitlist.append(1)
        
def crit1hit5 ():
    global relv_1
    global haiget1
    global kaitse2
    global elud_2
    global hero2
    global hero1
    global hero1hitlist
    dam1 = ((randint(1,relv_1) + haiget1) * 3 - kaitse2)
    if dam1 > 0:
        elud_2 = elud_2 - dam1
        print(hero1 + " lõi " + hero2 + " CRITICALIGA ja " + hero2 + " on nüüd " + str(elud_2) + " elusid")
        hero1hitlist.append(1)
        
def crit1hit6 ():
    global relv_1
    global haiget1
    global kaitse2
    global elud_2
    global hero2
    global hero1
    global hero1hitlist
    global hits_2
    hits_2 = 0
    dam1 = (randint(1,relv_1) + haiget1 - kaitse2)
    if dam1 > 0:
        elud_2 = elud_2 - dam1
        print(hero1 + " lõi " + hero2 + " CRITICALIGA ja " + hero2 + " on nüüd " + str(elud_2) + " elusid")
        hero1hitlist.append(1)
        
def crit1hit7 ():
    global relv_1
    global haiget1
    global kaitse2
    global elud_2
    global hero2
    global hero1
    global hero1hitlist
    global hits_2
    global kaitsmine_2
    hits_2 = 0
    kaitsmine_2 = kaitsmine_2 - 4
    dam1 = (randint(1,relv_1) + haiget1 - kaitse2)
    if dam1 > 0:
        elud_2 = elud_2 - dam1
        print(hero1 + " lõi " + hero2 + " CRITICALIGA ja " + hero2 + " on nüüd " + str(elud_2) + " elusid")
        hero1hitlist.append(1)
        
def crit1hit8 (): #stun round crit
    global relv_1
    global haiget1
    global kaitse2
    global elud_2
    global hero2
    global hero1
    global hero1hitlist
    global hits_2
    global kaitsmine_2
    global stunround_2
    dam1 = (randint(1,relv_1) + haiget1 - kaitse2)
    if dam1 > 0:
        elud_2 = elud_2 - dam1
        print(hero1 + " lõi " + hero2 + " CRITICALIGA ja " + hero2 + " on nüüd " + str(elud_2) + " elusid")
        hero1hitlist.append(1)
    if (randint(1,20) + elud2/6) <= randint(1,20):
        stunround_2 = randint(1,4)
        print(hero1 + " suutis peksta " + hero2 + " uimaseks " + str(stunround_2) + " käiguks.")

def crit1hit9 ():
    global relv_1
    global haiget1
    global kaitse2
    global elud_2
    global hero2
    global hero1
    global hero1hitlist
    global hits_2
    global kaitsmine_2
    hits_2 = 0
    dam1 = (randint(1,relv_1) + haiget1 - kaitse2)
    if dam1 > 0:
        elud_2 = elud_2 - dam1
        print(hero1 + " lõi " + hero2 + " CRITICALIGA ja " + hero2 + " on nüüd " + str(elud_2) + " elusid")
        hero1hitlist.append(1)

def crit1hit10 ():
    global elud_2
    global vehkimisi1list
    global hero1hitlistlist
    print(hero1 + " lõi " + hero2 + " CRITICALIGA sandiks " + hero2 + " on kaotanud.")
    elud_2 = 0
    vehkimisi1list.append(1)
    hero1hitlist.append(1)

def crit1hit11 ():
    global elud_2
    global vehkimisi1list
    global hero1hitlistlist
    print(hero1 + " lõi " + hero2 + " CRITICALIGA käe otsast ja " + hero2 + " on kaotanud.")
    elud_2 = 0
    vehkimisi1list.append(1)
    hero1hitlist.append(1)

def crit1hit12 ():
    global elud_2
    global vehkimisi1list
    global hero1hitlistlist
    print(hero1 + " raius " + hero2 + " CRITICALIGA " + hero2 + "pea maha.")
    elud_2 = 0
    vehkimisi1list.append(1)
    hero1hitlist.append(1)

#crit miss funktsioonid 1. võitleja jaoks

def crit1miss1 ():
    print("Esimene võitleja vehkis väga mööda.")
def crit1miss2 ():
    global kaitsmine_1
    kaitsmine_1 = kaitsmine_1 - 4
    print(hero1 + " komistas veidike ja kaotas tasakaalu.")
def crit1miss3 ():
    global hits_1
    hits_1 = 0
    print(hero1 + " kaotas löögivõimaluse tänu ebaõnnestunud löögile.")
def crit1miss4 ():
    global hits_1
    global kaitsmine_1
    hits_1 = 0
    kaitsmine_1 = kaitsmine_1 - 4
    print(hero1 + " kaotas löögivõimaluse tänu ebaõnnestunud löögile ja kaotas valvsuse.")
def crit1miss5 ():
    print(hero1 + " lõi väga mööda")
def crit1miss6 ():
    global elud_1
    global relv_1
    elud_1 = elud_1 - randint(1,relv_1)
    print(hero1 + " tegi endale viga.")
def crit1miss7 ():
    global elud_1
    global relv_1
    elud_1 = elud_1 - randint(1, relv_1)*2
    print(hero1 + " tegi raskelt viga.")
def crit1miss8 ():
    global hits_1
    hits_1 = 0
    print(hero1 + " kaotas relva ja koperdas ringi, et seda üles korjata.")
def crit1miss9 ():
    global relv_1
    global hits_1
    if randint(1,20) >= randint(1,20):
        relv_1 = relv_1 - 2
        hits_1 = 0
        print(hero1 + " relv purunes ja ta pidi haarama varurelva.")
    else:
        print("Esimene võitleja vehkis väga mööda.")
def crit1miss10 ():
    global elud_1
    print("Esimene võitleja lõi nii mööda, et kukkus ja surmati...")
    elud_1 = 0


### algavad crit funktsioonide (def)  defineerimine hero 2 jaoks

### crit hit funktsioonid 2. võitleja jaoks

def crit2hit1():
    global relv_2
    global haiget2
    global kaitse1
    global elud_1
    global hero1
    global hero2
    global hero2hitlist
    dam2 = (randint(1, relv_2) + haiget2 - kaitse1)
    if dam2 > 0:
        elud_1 = elud_1 - dam2
        print(hero2 + " lõi " + hero1 + " CRITICALIGA ja " + hero1 + " on nüüd " + str(elud_1) + " elusid")
        hero2hitlist.append(1)


def crit2hit2():
    global relv_2
    global haiget2
    global kaitse1
    global elud_1
    global hero1
    global hero2
    global hero2hitlist
    dam2 = ((randint(1, relv_2) + haiget2) * 2 - kaitse1)
    if dam2 > 0:
        elud_1 = elud_1 - dam2
        print(hero2 + " lõi " + hero1 + " CRITICALIGA ja " + hero1 + " on nüüd " + str(elud_1) + " elusid")
        hero2hitlist.append(1)

def crit2hit3():
    global relv_2
    global haiget2
    global kaitse1
    global elud_1
    global hero1
    global hero2
    global hits_2
    global hero2hitlist
    hits_2 = hits_2 + 1
    dam2 = (randint(1, relv_2) + haiget2 - kaitse1)
    print(hero2 + " ründab eriti hoogsalt ja saab lisarünnaku!")
    if dam2 > 0:
        elud_1 = elud_1 - dam2
        print(hero2 + " lõi " + hero1 + " CRITICALIGA ja " + hero1 + " on nüüd " + str(elud_1) + " elusid")
        hero1hitlist.append(1)

def crit2hit4():
    global relv_2
    global haiget2
    global kaitse1
    global elud_1
    global hero1
    global hero2
    global hits_2
    global hero2hitlist
    dam2 = relv_2 + haiget2 - kaitse1
    if dam2 > 0:
        elud_1 = elud_1 - dam2
        print(hero2 + " lõi " + hero1 + " CRITICALIGA ja " + hero1 + " on nüüd " + str(elud_1) + " elusid")
        hero2hitlist.append(1)

def crit2hit5():
    global relv_2
    global haiget2
    global kaitse1
    global elud_1
    global hero1
    global hero2
    global hits_2
    global hero2hitlist
    dam2 = ((randint(1, relv_2) + haiget2) * 3 - kaitse1)
    if dam2 > 0:
        elud_1 = elud_1 - dam2
        print(hero2 + " lõi " + hero1 + " CRITICALIGA ja " + hero1 + " on nüüd " + str(elud_1) + " elusid")
        hero2hitlist.append(1)

def crit2hit6():
    global relv_2
    global haiget2
    global kaitse1
    global elud_1
    global hero1
    global hero2
    global hits_1
    global hero2hitlist
    hits_1 = 0
    dam2 = (randint(1, relv_2) + haiget2 - kaitse1)
    print(hero2 + " ründab " + hero1 + " nii edukalt, et see ei suuda vastu rünnata teda!")
    if dam2 > 0:
        elud_1 = elud_1 - dam2
        print(hero2 + " lõi " + hero1 + " CRITICALIGA ja " + hero1 + " on nüüd " + str(elud_1) + " elusid")
        hero2hitlist.append(1)

def crit2hit7():
    global relv_2
    global haiget2
    global kaitse1
    global elud_1
    global hero1
    global hero2
    global hits_1
    global kaitsmine_1
    global hero2hitlist
    hits_1 = 0
    kaitsmine_1 = kaitsmine_1 - 4
    dam2 = (randint(1, relv_2) + haiget2 - kaitse1)
    print(hero2 + " ründab nii edukalt " + hero1 + ", et ta ei suuda end edukalt kaitsta mõnda aega, ega ka vastu rünnata!")
    if dam2 > 0:
        elud_1 = elud_1 - dam2
        print(hero2 + " lõi " + hero1 + " CRITICALIGA ja " + hero1 + " on nüüd " + str(elud_1) + " elusid")
        hero2hitlist.append(1)


def crit2hit8():  #stun round crit
    global relv_2
    global haiget2
    global kaitse1
    global elud_1
    global elud1
    global hero1
    global hero2
    global hits_1
    global kaitsmine_1
    global hero2hitlist
    dam2 = (randint(1, relv_2) + haiget2 - kaitse1)
    if dam2 > 0:
        elud_1 = elud_1 - dam2
        print(hero2 + " lõi " + hero1 + " CRITICALIGA ja " + hero1 + " on nüüd " + str(elud_1) + " elusid")
        hero2hitlist.append(1)
    if (randint(1, 20) + elud1 / 6) <= randint(1, 20):
        stunround_1 = randint(1, 4)
        print(hero1 + " suutis peksta " + hero1 + " uimaseks " + str(stunround_1) + " käiguks.")

def crit2hit9():
    global relv_2
    global haiget2
    global kaitse1
    global elud_1
    global hero1
    global hero2
    global hits_1
    global kaitsmine_1
    global hero2hitlist
    hits_1 = 0
    dam2 = (randint(1, relv_2) + haiget2 - kaitse1)
    if dam2 > 0:
        elud_1 = elud_1 - dam2
        print(hero2 + " lõi " + hero1 + " criticaliga ja " + hero1 + " on nüüd " + str(elud_1) + " elusid")
        hero2hitlist.append(1)

def crit2hit10():
    global elud_1
    global hero2hitlist
    global vehkimisi2list
    print(hero2 + " lõi " + hero1 + " CRITICALIGA sandiks, " + hero1 + " on kaotanud.")
    elud_1 = 0
    vehkimisi2list.append(1)
    hero2hitlist.append(1)

def crit2hit11():
    global elud_1
    global hero2hitlist
    global vehkimisi2list
    print(hero2 + " lõi " + hero1 + " CRITICALIGA käe otsast ja " + hero1 + " on kaotanud.")
    elud_1 = 0
    vehkimisi2list.append(1)
    hero2hitlist.append(1)

def crit2hit12():
    global elud_1
    global hero2hitlist
    global vehkimisi2list
    print(hero2 + " raius " + hero1 + " CRITICALIGA " + hero1 + "pea maha.")
    elud_1 = 0
    vehkimisi2list.append(1)
    hero2hitlist.append(1)

#crit miss funktsioonid 2. võitleja jaoks

def crit2miss1 ():
    print("Teine võitleja vehkis väga mööda.")
def crit2miss2 ():
    global kaitsmine_2
    kaitsmine_2 = kaitsmine_2 - 4
    print(hero2 + " lõi nii mööda, et kaotas valvsuse.")
def crit2miss3 ():
    global hits_2
    hits_2 = 0
    print(hero2 + " lõi tugeva löögi mööda ja koperdas peaaegu pikali.")
def crit2miss4 ():
    global hits_2
    global kaitsmine_2
    hits_2 = 0
    kaitsmine_2 = kaitsmine_2 - 4
    print(hero2 + " ründas ebaõnnestunult ja komistas, kaotades peaaegu oma relva.")
def crit2miss5 ():
    print("Teine võitleja vehkis väga mööda.")
def crit2miss6 ():
    global elud_2
    global relv_2
    elud_2 = elud_2 - randint(1,relv_2)
    print(hero2 + " tegi endale ise haiget")
def crit2miss7 ():
    global elud_2
    global relv_2
    elud_2 = elud_2 - randint(1, relv_2)*2
    print(hero2 + " põhjustas endale raske haava")
def crit2miss8 ():
    global hits_2
    hits_2 = 0
    print(hero2 + " pillas mõõga ebaõnnestunud rünnaku käigus.")
def crit2miss9 ():
    global relv_2
    global hits_2
    if randint(1,20) >= randint(1,20):
        relv_2 = relv_2 - 2
        hits_2 = 0
        print(hero2 + " peksis hooletu rünnaku käigus oma relva puruks ja taganes, et haarata varurelv")
    else:
        print("Teine võitleja vehkis väga mööda.")
def crit2miss10 ():
    global elud_2
    print(hero2 +" lõi nii mööda, et lasi end vasturünnakuga tappa ning lebab nüüd veriselt tolmus.")
    elud_2 = 0

def duel():
    #järgmised global käsud määravad ära et def kasutab globaalseid muutujaid
    global hero1voit
    global hero2voit
    global x
    global y
    global z
    global hero1list
    global hero2list
    global hero1hitlist
    global hero2hitlist
    global vehkimisi1list
    global vehkimisi2list
    global herovise1
    global herovise2
    global critS1
    global critS2
    global critF1
    global critF2
    global hits1
    global hits2
    global kaitsmine1
    global kaitsmine2
    global stunround1
    global stunround2
    global relv1
    global relv2
    global hero_1
    global hero_2
    global elud_1
    global elud_2
    global relv_1
    global relv_2
    global herovise_1
    global herovise_2
    global hits_1
    global hits_2
    global kaitsmine_1
    global kaitsmine_2
    global stunround_1
    global stunround_2
    
    for x in range(simulatsiooniarv):
        hero_1 = hero1 #siin on asi tegelikult lihtne. iga korraga while loop lisab väärtustele juurde, aga kui iga loopi lõpus muutuvad local väärtused nagu elud_1 tagasi globaalväärtusteks nagu elud1, siis saab
                        #järgmine while-loopi osa alustada täpselt samade väärtustega
        hero_2 = hero2 
        elud_1 = elud1
        elud_2 = elud2
        relv_1 = relv1
        relv_2 = relv2
        yy = y
        herovise_1 = herovise1
        herovise_2 = herovise2
        hits_1 = hits1 #hits_1 on alternatiivne hits1 versioon selleks, et criticalide puhul oleks võimalik lisada lisalööke ning revertida tagasi algse väärtuse juurde järgmiseks käiguks
        hits_2 = hits2 #hits_2 on alternatiivne hits2 versioon selleks, et criticalide puhul oleks võimalik lisada lisalööke ning revertida tagasi algse väärtuse juurde järgmiseks käiguks
        kaitsmine_1 = kaitsmine1 #kaitsmine_1 ja kaitsmine_2 on muutujad, et criticalidel kaitsmise miinuseid luua ning neid resettida
        kaitsmine_2 = kaitsmine2
        stunround_1 = stunround1
        stunround_2 = stunround2


        while elud_1 > 0 and elud_2 > 0:
#algab 1. võitleja käik
#tuleb 1. võitleja esimene löök
            herovise_1 = randint(1,20) #enne iga löögi tegemist esimese võitleja jaoks tehakse vise d20 ja see saab muutuja väärtuseks herovise_1'le, et iga kord oleks uus random number
            if herovise_1 == 20 and hits_1 >= 1 and stunround_1 == 0 and elud_1 > 0: #kontrollib kas on critical hit
                critS1 = randint(1,100) #kui on crit 20 siis viskab 1-100 täringut et leida mis critical hit tuleb
                vehkimisi1list.append(1)
                if 1 <= critS1 <= 30:
                    crit1hit1 () #iga critical hiti kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. need on defineeritud alguses.
                elif 31 <= critS1 <= 45:
                    crit1hit2 ()
                elif 46 <= critS1 <= 55:
                    crit1hit3 ()
                elif 56 <= critS1 <= 60:
                    crit1hit4 ()
                elif 61 <= critS1 <= 65:
                    crit1hit5 ()
                elif 66 <= critS1 <= 70:
                    crit1hit6 ()
                elif 71 <= critS1 <= 75:
                    crit1hit7 ()
                elif 76 <= critS1 <= 80:
                    crit1hit8 ()
                elif 81 <= critS1 <= 85:
                    crit1hit9 ()
                elif 86 <= critS1 <= 90:
                    crit1hit10 ()
                elif 91 <= critS1 <= 94:
                    crit1hit11 ()
                elif 95 <= critS1 <= 100:
                    crit1hit12 ()
                    
            if herovise_1 == 0 and hits_1 >= 1 and stunround_1 == 0 and elud_1 > 0: #kontrollib kas on critical miss
                critF1 = randint(1,100) #kui on crit 0 siis viskab 1-100 täringut et leida mis critical miss tuleb
                if 1 <= critF1 <= 30:
                    crit1miss1 () #iga critical missi kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. Need on defineeritud alguses.
                elif 31 <= critF1 <= 45:
                    crit1miss2 ()
                elif 46 <= critF1 <= 55:
                    crit1miss3 ()
                elif 56 <= critF1 <= 65:
                    crit1miss4 ()
                elif 66 <= critF1 <= 75:
                    crit1miss5 ()
                elif 76 <= critF1 <= 80:
                    crit1miss6 ()
                elif 81 <= critF1 <= 85:
                    crit1miss7 ()
                elif 86 <= critF1 <= 90:
                    crit1miss8 ()
                elif 91 <= critF1 <= 95:
                    crit1miss9 ()
                elif 96 <= critF1 <= 100:
                    crit1miss10 ()
            elif (pihta1 + herovise_1) >= kaitsmine_2 and hits_1 >= 1 and stunround_1 == 0 and elud_1 > 0:
        #see on parem critical viske elif tingimuse all!!!!!! siis ta seda läbi ei võta kui critical tuli!!! NICE
                dam1 = (randint(1,relv_1) + haiget1 - kaitse2)
                vehkimisi1list.append(1)
                if dam1 > 0:
                    elud_2 = elud_2 - dam1
                    print(hero_1 + " lõi " + hero2 + " ja " + hero_2 + " on nüüd " + str(elud_2) + " elusid")
                    hero1hitlist.append(1) #see annab teada et toimus reaalselt haiget tegev löök ja see on vaja panna sisse ka critical hittide funktsiooni.
                    
#tuleb 1. võitleja teine löök
            herovise_1 = randint(1,20) #järgmise löögi jaoks uus väärtus löögiviske muutujale
            if herovise_1 == 20 and hits_1 >= 2 and stunround_1 == 0 and elud_1 > 0: #kontrollib kas on critical hit
                critS1 = randint(1,100) #kui on siis viskab 1-100 täringut et leida mis critical hit tuleb
                if 1 <= critS1 <= 30:
                    crit1hit1 () #iga critical hiti kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. need on defineeritud alguses.
                elif 31 <= critS1 <= 45:
                    crit1hit2 ()
                elif 46 <= critS1 <= 55:
                    crit1hit3 ()
                elif 56 <= critS1 <= 60:
                    crit1hit4 ()
                elif 61 <= critS1 <= 65:
                    crit1hit5 ()
                elif 66 <= critS1 <= 70:
                    crit1hit6 ()
                elif 71 <= critS1 <= 75:
                    crit1hit7 ()
                elif 76 <= critS1 <= 80:
                    crit1hit8 ()
                elif 81 <= critS1 <= 85:
                    crit1hit9 ()
                elif 86 <= critS1 <= 90:
                    crit1hit10 ()
                elif 91 <= critS1 <= 94:
                    crit1hit11 ()
                elif 95 <= critS1 <= 100:
                    crit1hit12 ()
                    
            if herovise_1 == 0 and hits_1 >= 2  and stunround_1 == 0 and elud_1 > 0: #kontrollib kas on critical miss
                critF1 = randint(1,100) #kui on siis viskab 1-100 täringut et leida mis critical miss tuleb
                if 1 <= critF1 <= 30:
                    crit1miss1 () #iga critical missi kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. Need on defineeritud alguses.
                elif 31 <= critF1 <= 45:
                    crit1miss2 ()
                elif 46 <= critF1 <= 55:
                    crit1miss3 ()
                elif 56 <= critF1 <= 65:
                    crit1miss4 ()
                elif 66 <= critF1 <= 75:
                    crit1miss5 ()
                elif 76 <= critF1 <= 80:
                    crit1miss6 ()
                elif 81 <= critF1 <= 85:
                    crit1miss7 ()
                elif 86 <= critF1 <= 90:
                    crit1miss8 ()
                elif 91 <= critF1 <= 95:
                    crit1miss9 ()
                elif 96 <= critF1 <= 100:
                    crit1miss10 ()
            elif (pihta1 + herovise_1) >= kaitsmine_2 and hits_1 >= 2  and stunround_1 == 0 and elud_1 > 0:
                dam1 = (randint(1,relv_1) + haiget1 - kaitse2)
                vehkimisi1list.append(1)
                if dam1 > 0:
                    elud_2 = elud_2 - dam1
                    print(hero_1 + " lõi " + hero2 + " ja " + hero_2 + " on nüüd " + str(elud_2) + " elusid")
                    hero1hitlist.append(1)
                    
#tuleb 1. võitleja kolmas löök
            herovise_1 = randint(1,20)
            if herovise_1 == 20 and hits_1 >= 3 and stunround_1 == 0 and elud_1 > 0: #kontrollib kas on critical hit
                critS1 = randint(1,100) #kui on siis viskab 1-100 täringut et leida mis critical hit tuleb
                if 1 <= critS1 <= 30:
                    crit1hit1 () #iga critical hiti kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. need on defineeritud alguses.
                elif 31 <= critS1 <= 45:
                    crit1hit2 ()
                elif 46 <= critS1 <= 55:
                    crit1hit3 ()
                elif 56 <= critS1 <= 60:
                    crit1hit4 ()
                elif 61 <= critS1 <= 65:
                    crit1hit5 ()
                elif 66 <= critS1 <= 70:
                    crit1hit6 ()
                elif 71 <= critS1 <= 75:
                    crit1hit7 ()
                elif 76 <= critS1 <= 80:
                    crit1hit8 ()
                elif 81 <= critS1 <= 85:
                    crit1hit9 ()
                elif 86 <= critS1 <= 90:
                    crit1hit10 ()
                elif 91 <= critS1 <= 94:
                    crit1hit11 ()
                elif 95 <= critS1 <= 100:
                    crit1hit12 ()
            if herovise_1 == 0 and hits_1 >= 3 and stunround_1 == 0 and elud_1 > 0: #kontrollib kas on critical miss
                critF1 = randint(1,100) #kui on siis viskab 1-100 täringut et leida mis critical miss tuleb
                if 1 <= critF1 <= 30:
                    crit1miss1 () #iga critical missi kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. Need on defineeritud alguses.
                elif 31 <= critF1 <= 45:
                    crit1miss2 ()
                elif 46 <= critF1 <= 55:
                    crit1miss3 ()
                elif 56 <= critF1 <= 65:
                    crit1miss4 ()
                elif 66 <= critF1 <= 75:
                    crit1miss5 ()
                elif 76 <= critF1 <= 80:
                    crit1miss6 ()
                elif 81 <= critF1 <= 85:
                    crit1miss7 ()
                elif 86 <= critF1 <= 90:
                    crit1miss8 ()
                elif 91 <= critF1 <= 95:
                    crit1miss9 ()
                elif 96 <= critF1 <= 100:
                    crit1miss10 ()
            elif (pihta1 + herovise_1) >= kaitsmine_2 and hits_1 >= 3 and stunround_1 == 0 and elud_1 > 0:
                dam1 = (randint(1,relv_1) + haiget1 - kaitse2)
                vehkimisi1list.append(1)
                if dam1 > 0:
                    elud_2 = elud_2 - dam1
                    print(hero_1 + " lõi " + hero2 + " ja " + hero_2 + " on nüüd " + str(elud_2) + " elusid")
                    hero1hitlist.append(1)

#tuleb 1. võitleja neljas löök
            herovise_1 = randint(1,20)
            if herovise_1 == 20 and hits_1 >= 4 and stunround_1 == 0 and elud_1 > 0: #kontrollib kas on critical hit
                critS1 = randint(1,100) #kui on crit 20 siis viskab 1-100 täringut et leida mis critical hit tuleb
                vehkimisi1list.append(1)
                if 1 <= critS1 <= 30:
                    crit1hit1 () #iga critical hiti kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. need on defineeritud alguses.
                elif 31 <= critS1 <= 45:
                    crit1hit2 ()
                elif 46 <= critS1 <= 55:
                    crit1hit3 ()
                elif 56 <= critS1 <= 60:
                    crit1hit4 ()
                elif 61 <= critS1 <= 65:
                    crit1hit5 ()
                elif 66 <= critS1 <= 70:
                    crit1hit6 ()
                elif 71 <= critS1 <= 75:
                    crit1hit7 ()
                elif 76 <= critS1 <= 80:
                    crit1hit8 ()
                elif 81 <= critS1 <= 85:
                    crit1hit9 ()
                elif 86 <= critS1 <= 90:
                    crit1hit10 ()
                elif 91 <= critS1 <= 94:
                    crit1hit11 ()
                elif 95 <= critS1 <= 100:
                    crit1hit12 ()
            if herovise_1 == 0 and hits_1 >= 4 and stunround_1 == 0 and elud_1 > 0: #kontrollib kas on critical miss
                critF1 = randint(1,100) #kui on crit 0 siis viskab 1-100 täringut et leida mis critical miss tuleb
                if 1 <= critF1 <= 30:
                    crit1miss1 () #iga critical missi kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. Need on defineeritud alguses.
                elif 31 <= critF1 <= 45:
                    crit1miss2 ()
                elif 46 <= critF1 <= 55:
                    crit1miss3 ()
                elif 56 <= critF1 <= 65:
                    crit1miss4 ()
                elif 66 <= critF1 <= 75:
                    crit1miss5 ()
                elif 76 <= critF1 <= 80:
                    crit1miss6 ()
                elif 81 <= critF1 <= 85:
                    crit1miss7 ()
                elif 86 <= critF1 <= 90:
                    crit1miss8 ()
                elif 91 <= critF1 <= 95:
                    crit1miss9 ()
                elif 96 <= critF1 <= 100:
                    crit1miss10 ()
            elif (pihta1 + herovise_1) >= kaitsmine_2 and hits_1 >= 4 and stunround_1 == 0 and elud_1 > 0:
                dam1 = (randint(1,relv_1) + haiget1 - kaitse2)
                vehkimisi1list.append(1)
                if dam1 > 0:
                    elud_2 = elud_2 - dam1
                    print(hero_1 + " lõi " + hero2 + " ja " + hero_2 + " on nüüd " + str(elud_2) + " elusid")
                    hero1hitlist.append(1)
            kaitsmine_2 = kaitsmine2
            
#algab 2. võitleja käik
#tuleb 2. võitleja esimene löök
            hits_1 = hits1
            herovise_2 = randint(1,20)
            if herovise_2 == 20 and hits_2 >= 1 and stunround_2 == 0 and elud_2 > 0: #kontrollib kas on critical hit
                critS2 = randint(1,100) #kui on crit 20 siis viskab 1-100 täringut et leida mis critical hit tuleb
                vehkimisi2list.append(1)
                if 1 <= critS2 <= 30:
                    crit2hit1 () #iga critical hiti kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. need on defineeritud alguses.
                elif 31 <= critS2 <= 45:
                    crit2hit2 ()
                elif 46 <= critS2 <= 55:
                    crit2hit3 ()
                elif 56 <= critS2 <= 60:
                    crit2hit4 ()
                elif 61 <= critS2 <= 65:
                    crit2hit5 ()
                elif 66 <= critS2 <= 70:
                    crit2hit6 ()
                elif 71 <= critS2 <= 75:
                    crit2hit7 ()
                elif 76 <= critS2 <= 80:
                    crit2hit8 ()
                elif 81 <= critS2 <= 85:
                    crit2hit9 ()
                elif 86 <= critS2 <= 90:
                    crit2hit10 ()
                elif 91 <= critS2 <= 94:
                    crit2hit11 ()
                elif 95 <= critS2 <= 100:
                    crit2hit12 ()
            if herovise_2 == 0 and hits_2 >= 1and stunround_2 == 0 and elud_2 > 0: #kontrollib kas on critical miss
                critF2 = randint(1,100) #kui on crit 0 siis viskab 1-100 täringut et leida mis critical miss tuleb
                if 1 <= critF2 <= 30:
                    crit2miss1 () #iga critical missi kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. Need on defineeritud alguses.
                elif 31 <= critF2 <= 45:
                    crit2miss2 ()
                elif 46 <= critF2 <= 55:
                    crit2miss3 ()
                elif 56 <= critF2 <= 65:
                    crit2miss4 ()
                elif 66 <= critF2 <= 75:
                    crit2miss5 ()
                elif 76 <= critF2 <= 80:
                    crit2miss6 ()
                elif 81 <= critF2 <= 85:
                    crit2miss7 ()
                elif 86 <= critF2 <= 90:
                    crit2miss8 ()
                elif 91 <= critF2 <= 95:
                    crit2miss9 ()
                elif 96 <= critF <= 100:
                    crit2miss10 ()
            elif elud_2 > 0 and (pihta2 + herovise_2) >= kaitsmine_1 and hits_2 >= 1 and stunround_2 == 0:
                dam2 = (randint(1,relv_2) + haiget2 - kaitse1)
                vehkimisi2list.append(1)
                if dam2 > 0:
                    elud_1 = elud_1 - dam2
                    print(hero_2 + " lõi " + hero_1 + " ja " + hero_1 + " on nüüd " + str(elud_1) + " elusid")
                    hero2hitlist.append(1)
                    
#tuleb 2. võitleja teine löök                   
            herovise_2 = randint(1,20)
            if herovise_2 == 20 and hits_2 >= 2 and stunround_2 == 0  and elud_2 > 0: #kontrollib kas on critical hit
                critS2 = randint(1,100) #kui on crit 20 siis viskab 1-100 täringut et leida mis critical hit tuleb
                vehkimisi2list.append(1)
                if 1 <= critS2 <= 30:
                    crit2hit1 () #iga critical hiti kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. need on defineeritud alguses.
                elif 31 <= critS2 <= 45:
                    crit2hit2 ()
                elif 46 <= critS2 <= 55:
                    crit2hit3 ()
                elif 56 <= critS2 <= 60:
                    crit2hit4 ()
                elif 61 <= critS2 <= 65:
                    crit2hit5 ()
                elif 66 <= critS2 <= 70:
                    crit2hit6 ()
                elif 71 <= critS2 <= 75:
                    crit2hit7 ()
                elif 76 <= critS2 <= 80:
                    crit2hit8 ()
                elif 81 <= critS2 <= 85:
                    crit2hit9 ()
                elif 86 <= critS2 <= 90:
                    crit2hit10 ()
                elif 91 <= critS2 <= 94:
                    crit2hit11 ()
                elif 95 <= critS2 <= 100:
                    crit2hit12 ()
            if herovise_2 == 0 and hits_2 >= 2 and stunround_2 == 0  and elud_2 > 0: #kontrollib kas on critical miss
                critF2 = randint(1,100) #kui on crit 0 siis viskab 1-100 täringut et leida mis critical miss tuleb
                if 1 <= critF2 <= 30:
                    crit2miss1 () #iga critical missi kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. Need on defineeritud alguses.
                elif 31 <= critF2 <= 45:
                    crit2miss2 ()
                elif 46 <= critF2 <= 55:
                    crit2miss3 ()
                elif 56 <= critF2 <= 65:
                    crit2miss4 ()
                elif 66 <= critF2 <= 75:
                    crit2miss5 ()
                elif 76 <= critF2 <= 80:
                    crit2miss6 ()
                elif 81 <= critF2 <= 85:
                    crit2miss7 ()
                elif 86 <= critF2 <= 90:
                    crit2miss8 ()
                elif 91 <= critF2 <= 95:
                    crit2miss9 ()
                elif 96 <= critF2 <= 100:
                    crit2miss10 ()
            elif elud_2 > 0 and (pihta2 + herovise_2) >= kaitsmine_1 and hits_2 >= 2 and stunround_2 == 0:
                dam2 = (randint(1,relv_2) + haiget2 - kaitse1)
                vehkimisi2list.append(1)
                if dam2 > 0:
                    elud_1 = elud_1 - dam2
                    print(hero_2 + " lõi " + hero_1 + " ja " + hero_1 + " on nüüd " + str(elud_1) + " elusid")
                    hero2hitlist.append(1)
                    
#tuleb 2. võitleja kolmas löök 
            herovise_2 = randint(1,20)
            if herovise_2 == 20 and hits_2 >= 3 and stunround_2 == 0  and elud_2 > 0: #kontrollib kas on critical hit
                critS2 = randint(1,100) #kui on crit 20 siis viskab 1-100 täringut et leida mis critical hit tuleb
                vehkimisi1list.append(1)
                if 1 <= critS2 <= 30:
                    crit2hit1 () #iga critical hiti kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. need on defineeritud alguses.
                elif 31 <= critS2 <= 45:
                    crit2hit2 ()
                elif 46 <= critS2 <= 55:
                    crit2hit3 ()
                elif 56 <= critS2 <= 60:
                    crit2hit4 ()
                elif 61 <= critS2 <= 65:
                    crit2hit5 ()
                elif 66 <= critS2 <= 70:
                    crit2hit6 ()
                elif 71 <= critS2 <= 75:
                    crit2hit7 ()
                elif 76 <= critS2 <= 80:
                    crit2hit8 ()
                elif 81 <= critS2 <= 85:
                    crit2hit9 ()
                elif 86 <= critS2 <= 90:
                    crit2hit10 ()
                elif 91 <= critS2 <= 94:
                    crit2hit11 ()
                elif 95 <= critS2 <= 100:
                    crit2hit12 ()
            if herovise_2 == 0 and hits_2 >= 3 and stunround_2 == 0  and elud_2 > 0: #kontrollib kas on critical miss
                critF2 = randint(1,100) #kui on crit 0 siis viskab 1-100 täringut et leida mis critical miss tuleb
                if 1 <= critF2 <= 30:
                    crit2miss1 () #iga critical missi kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. Need on defineeritud alguses.
                elif 31 <= critF2 <= 45:
                    crit2miss2 ()
                elif 46 <= critF2 <= 55:
                    crit2miss3 ()
                elif 56 <= critF2 <= 65:
                    crit2miss4 ()
                elif 66 <= critF2 <= 75:
                    crit2miss5 ()
                elif 76 <= critF2 <= 80:
                    crit2miss6 ()
                elif 81 <= critF2 <= 85:
                    crit2miss7 ()
                elif 86 <= critF2 <= 90:
                    crit2miss8 ()
                elif 91 <= critF2 <= 95:
                    crit2miss9 ()
                elif 96 <= critF2 <= 100:
                    crit2miss10 ()
            elif elud_2 > 0 and (pihta2 + herovise_2) >= kaitsmine_1 and hits_2 >= 3 and stunround_2 == 0 :
                dam2 = (randint(1,relv_2) + haiget2 - kaitse1)
                vehkimisi2list.append(1)
                if dam2 > 0:
                    elud_1 = elud_1 - dam2
                    print(hero_2 + " lõi " + hero_1 + " ja " + hero_1 + " on nüüd " + str(elud_1) + " elusid")
                    hero2hitlist.append(1)
        
#tuleb 2. võitleja neljas löök
            herovise_2 = randint(1,20)
            if herovise_2 == 20 and hits_2 >= 4 and stunround_2 == 0  and elud_2 > 0: #kontrollib kas on critical hit
                critS2 = randint(1,100) #kui on crit 20 siis viskab 1-100 täringut et leida mis critical hit tuleb
                vehkimisi2list.append(1)
                if 1 <= critS2 <= 30:
                    crit2hit1 () #iga critical hiti kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. need on defineeritud alguses.
                elif 31 <= critS2 <= 45:
                    crit2hit2 ()
                elif 46 <= critS2 <= 55:
                    crit2hit3 ()
                elif 56 <= critS2 <= 60:
                    crit2hit4 ()
                elif 61 <= critS2 <= 65:
                    crit2hit5 ()
                elif 66 <= critS2 <= 70:
                    crit2hit6 ()
                elif 71 <= critS2 <= 75:
                    crit2hit7 ()
                elif 76 <= critS2 <= 80:
                    crit2hit8 ()
                elif 81 <= critS2 <= 85:
                    crit2hit9 ()
                elif 86 <= critS2 <= 90:
                    crit2hit10 ()
                elif 91 <= critS2 <= 94:
                    crit2hit11 ()
                elif 95 <= critS2 <= 100:
                    crit2hit12 ()
            if herovise_2 == 0 and hits_2 >= 4 and stunround_2 == 0  and elud_2 > 0: #kontrollib kas on critical miss
                critF2 = randint(1,100) #kui on crit 0 siis viskab 1-100 täringut et leida mis critical miss tuleb
                if 1 <= critF2 <= 30:
                    crit2miss1 () #iga critical missi kohta on oma funktsioon mida kindel välja kutsutud randomint täringuvise välja kutsub. Need on defineeritud alguses.
                elif 31 <= critF2 <= 45:
                    crit2miss2 ()
                elif 46 <= critF2 <= 55:
                    crit2miss3 ()
                elif 56 <= critF2 <= 65:
                    crit2miss4 ()
                elif 66 <= critF2 <= 75:
                    crit2miss5 ()
                elif 76 <= critF2 <= 80:
                    crit2miss6 ()
                elif 81 <= critF2 <= 85:
                    crit2miss7 ()
                elif 86 <= critF2 <= 90:
                    crit2miss8 ()
                elif 91 <= critF2 <= 95:
                    crit2miss9 ()
                elif 96 <= critF2 <= 100:
                    crit2miss10 ()
            elif elud_2 > 0 and (pihta2 + herovise_2) >= kaitsmine_1 and hits_2 >= 4 and stunround_2 == 0:
                dam2 = (randint(1,relv_2) + haiget2 - kaitse1)
                vehkimisi2list.append(1)
                if dam2 > 0:
                    elud_1 = elud_1 - dam2
                    print(hero_2 + " lõi " + hero_1 + " ja " + hero_1 + " on nüüd " + str(elud_1) + " elusid")
                    hero2hitlist.append(1)
            hits_2 = hits2
            kaitsmine_1 = kaitsmine1        
            yy = yy + 1
            z = z + 1
            if stunround_1 > 0:
                stunround_1 = stunround_1 - 1
            if stunround_2 > 0:
                stunround_2 = stunround_2 - 1
            if elud_1 <= 0:
                print(hero_2 + " on võitnud!")
                hero2voit = hero2voit + 1
                hero1list.append(elud_1)
                hero2list.append(elud_2)
                break
            if elud_2 <= 0:
                print(hero_1 + " on võitnud!")
                hero1voit = hero1voit + 1
                hero1list.append(elud_1)
                hero2list.append(elud_2)
                break
        x = x + 1
        print("See oli " + str(x) + " duell. " + str(hero_1) + " on võitnud " + str(hero1voit) + " korda ja " + str(hero_2) + " on võitnud " + str(hero2voit) + " korda.")
        print("Keskmised elud alles " +  str(hero_1) + " " + str(sum(hero1list)/float(len(hero1list))) + ".")
        print("Keskmised elud alles " +  str(hero_2) + " " + str(sum(hero2list)/float(len(hero2list))) + ".")
        if sum(hero1hitlist) > 0:
            print("Keskmiselt lõi duellis haiget tegevaid lööke " +  str(hero_1) + " " + str(sum(hero1hitlist)/x) + ".")
        if sum(hero2hitlist) > 0:
            print("Keskmiselt lõi duellis haiget tegevaid lööke " +  str(hero_2) + " " + str(sum(hero2hitlist)/x) + ".")
        print("Keskmiselt duellis üldse tegi pihta lööke " +  str(hero_1) + " " + str(len(vehkimisi1list)/x) + ".")
        print("Keskmiselt duellis üldse tegi pihta lööke " +  str(hero_2) + " " + str(len(vehkimisi2list)/x) + ".")
        print("Round kestis " + str(yy*4) + " sekundit.")
        print("Keskmiselt kestavad roundid " + str(z*4/x) + " sekundit.")
        print("---------------------------------------------------------------------------------------------------")
        if simulatsiooniarv == x:
            msgbox("Duelle toimus " + str(x) + ". \n" + str(hero_1) + " on võitnud " + str(hero1voit) + " korda ja " + str(hero_2) + " on võitnud " + str(hero2voit) + " korda.\n"
                  "Keskmiselt jäi elusid alles " +  str(hero_1) + "'l " + str(sum(hero1list)/float(len(hero1list))) + ".\n"
                    "Keskmiselt jäi elusid alles " +  str(hero_2) + "'l " + str(sum(hero2list)/float(len(hero2list))) + ".\n"
                   "Keskmiselt lõi duellis haiget tegevaid lööke " +  str(hero_1) + " " + str(sum(hero1hitlist)/x) + ".\n"
                   "Keskmiselt lõi duellis haiget tegevaid lööke " +  str(hero_2) + " " + str(sum(hero2hitlist)/x) + ".\n"
                   "Keskmiselt tegi pihta lööke " +  str(hero_1) + " " + str(len(vehkimisi1list)/x) + ".\n"
                   "Keskmiselt tegi pihta lööke " +  str(hero_2) + " " + str(len(vehkimisi2list)/x) + ".\n"
                   "Keskmiselt kestsid duellid" + str(z*4/x) + " sekundit.\n")
duel()

#kaitsmine - 4 <<< ei ole praegu restarditud pärast iga roundi criticalile järgnevat roundi vaid pärast criticali teinud vastase korra lõppu
