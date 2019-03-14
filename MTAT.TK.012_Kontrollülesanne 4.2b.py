
from tkinter import *

raam = Tk()
raam.title("Liiklusmärk")
tahvel = Canvas(raam, width=1000,height=1600,background="white")

tahvel.create_rectangle(100-50,100-50,100+50,100+50, fill="red", outline="white")
tahvel.pack()
raam.mainloop()