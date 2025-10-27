
from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry("600x300")
root.title("Kg to pounds converter")

def Converter():
    kg = kg_entry.get()
    if kg.replace('.','').isnumeric():
        error_label.grid_forget()

        pounds = float(kg)*2.2
        output_label.config(text=str(pounds))

title_label = Label(root,text="Kg to Pounds Converter",font=font.Font(size=20))
title_label.pack()

kg_label = Label(root,text="Enter weight in kilograms:",font=font.Font(size=12))
kg_label.place(x=100,y=80)

kg_entry = Entry(root,width = 20)
kg_entry.place(x=350,y=83)

pounds_label = Label(root,text="Weight in Pounds:",font=font.Font(size=15))
pounds_label.place(x=170,y=130)

convert_button = Button(root,text="Convert", bg="light green",width = 50,height = 2,command=Converter)
convert_button.place(x=120,y=200)

output_label = Label(root,font=font.Font(size=15))
output_label.place(x=350,y=130)

error_label = Label(root,text="Please enter valid input...",fg="red")





root.mainloop()
