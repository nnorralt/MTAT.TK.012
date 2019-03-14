def banner (lause):
    return lause.upper()
    
mitu = int(input("mitu korda tahad kuvada lauset?"))
lause = input("mis on lause?")

while mitu != 0:
    mitu = mitu - 1
    print(banner(lause))
    