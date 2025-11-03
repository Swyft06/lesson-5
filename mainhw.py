from tkinter import *
import tkinter.font as font


root = Tk()
root.geometry("600x300")
root.title("Usd to Yen converter")

def Converter():
    usd = usd_entry.get()
    if usd.replace('.','').isnumeric():
        error_label.grid_forget()

        yen = float(usd) *153.95
        output_label.config(text=str(yen))


title_label = Label(root,text="Usd to Yen converter",font=font.Font(size=20))
title_label.pack()

usd_label = Label(root,text="Enter amount in usd:",font=font.Font(size=12))
usd_label.place(x=100,y=80)

usd_entry = Entry(root,width = 20)
usd_entry.place(x=350,y=83)

yen_label = Label(root,text="Amount in Yen:",font=font.Font(size=15))
yen_label.place(x=170,y=130)

convert_button = Button(root,text="Convert", bg="light green",width = 50,height = 2,command=Converter)
convert_button.place(x=120,y=200)

output_label = Label(root,font=font.Font(size=15))
output_label.place(x=350,y=130)

error_label = Label(root,text="Please enter valid input...",fg="red")




root.mainloop()
