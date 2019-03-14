from easygui import * #easygui.py peab olema samas folderis, muidu ei tööta.

arv1 = integerbox("1. arv", lowerbound = 1, upperbound = 10)
arv2 = integerbox("2. arv", lowerbound = 1, upperbound = 10)
choices=("+", "-", "*")
bbox = buttonbox(msg='teheMSG', title='tehexTITLE', choices=choices)
if bbox == "+":
    msgbox(str(arv1 + arv2))
elif bbox == "-":
    msgbox(str(arv1 - arv2))
elif bbox1 == "*":
    msgbox(str(arv1 * arv2))