kliendiarv = int(input("mitu klienti tuleb?"))
algklient = 1
lilledearv = 0
while algklient <= kliendiarv:
    if algklient % 2 != 0:
        lilledearv = lilledearv + algklient
    algklient = algklient + 1
print(str(lilledearv))
    