
fail = open("konto.txt", encoding="UTF-8")
 
raha = []
for each in fail:
   raha.append(each)   
fail.close()
for each in raha:
    if float(each) >= 0:
        print(each)
    