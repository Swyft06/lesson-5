from tkinter import *
import tkinter.font as font

root=Tk()
root.geometry("600x300")
root.title("Celsius to Fahrenheit Converter")

def Converter():
    celsius = temperature_entry.get()
    if celsius.replace('.','').isnumeric():
        error_label.grid_forget()

        fahrenheit = (float(celsius)*9/5)+32
        output_label.config(text=str(fahrenheit))





title_label = Label(root, text="Celsius -> Fahrenheit",font=font.Font(size=20),fg="grey")
title_label.pack()

entry_label = Label(root,text="Enter Temperature in Celsius: ",font=font.Font(size=12))
entry_label.place(x=100,y=80)

temperature_entry = Entry(root,width=30)
temperature_entry.place(x=320,y=83)

temperature_label = Label(root,text="Temperature in Fahrenheit:",font=font.Font(size=15))
temperature_label.place(x=150,y=150)

convert_button = Button(root,text="Convert",bg="light green",width=50,height=2,command=Converter)
convert_button.place(x=120,y=200)

output_label = Label(root,font=font.Font(size=15))
output_label.place(x=400,y=150)

error_label = Label(root,text="Please enter valid input...",fg="red")


root.mainloop()
