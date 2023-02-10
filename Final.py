from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import openpyxl ,xlrd
from openpyxl import Workbook
import pathlib

#Root Window
root=Tk()
root.title("Customer Data Entry")
root.geometry('700x400+300+200')
root.resizable(False,False)
root.configure(bg='#e9967a')






def submit():
    pass



def clear():
    name_value.set('')
    phone_value.set('')
    birth_value.set('')
    address_entry.delete('1.0',END)
    email_value.set('')
    


#Adding Icon
icon=PhotoImage(file='logo.png')
root.iconphoto(False,icon)

#Heading in window
Label(root,text='Please Enter Customer Data',font='times 13 bold',bg='#e9967a',fg='black').place(x=20,y=20)

Label(root,text='Name',font='23',bg='#e9967a',fg='black').place(x=50,y=100)
Label(root,text='Phone No.',font='23',bg='#e9967a',fg='black').place(x=50,y=150)
Label(root,text='Date of Birth',font='23',bg='#e9967a',fg='black').place(x=50,y=200)
Label(root,text='Email',font='23',bg='#e9967a',fg='black').place(x=375,y=200)
Label(root,text='Address',font='23',bg='#e9967a',fg='black').place(x=50,y=250)
Label(root,text='Gender',font='23',bg='#e9967a',fg='black').place(x=375,y=250)

#Entry Values
name_value = StringVar()
phone_value = StringVar()
birth_value = StringVar()
email_value = StringVar()

name_entry = Entry(root, textvariable=name_value,width=40,bd=2,font=20)
phone_entry = Entry(root, textvariable=phone_value,width=40,bd=2,font=20)
birth_entry = Entry(root, textvariable=birth_value,width=15,bd=2,font=20)
email_entry = Entry(root,textvariable=email_value,width=15,bd=2,font=20)

#Gender Combobox
gender_combobox = Combobox(root,values=['Male','Female','Other'],font='arial 14', state='r',width=14)
gender_combobox.place(x=450,y=250)

address_entry = Text(root,bd=2,width=20,height=2)


name_entry.place(x=200,y=100)
phone_entry.place(x=200,y=150)
birth_entry.place(x=200,y=200)
address_entry.place(x=200,y=250)
email_entry.place(x=450,y=200)

Button(root,text='Submit',bg='#e9967a',fg='white',width=15,height=2,command=submit).place(x=200,y=350)
Button(root,text='Clear',bg='#e9967a',fg='white',width=15,height=2,command=clear).place(x=340,y=350)
Button(root,text='Exit',bg='#e9967a',fg='white',width=15,height=2,command=lambda:root.destroy()).place(x=480,y=350)


root.mainloop()