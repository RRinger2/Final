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


#Adding Icon
icon=PhotoImage(file='logo.png')
root.iconphoto(False,icon)

#Heading in window
Label(root,text='Please Enter Customer Data',font='times 13 bold',bg='#e9967a',fg='black').place(x=20,y=20)

Label(root,text='Name',font='times',bg='#e9967a',fg='black').place(x=50,y=100)
Label(root,text='Name',font='times',bg='#e9967a',fg='black').place(x=50,y=150)
Label(root,text='Name',font='times',bg='#e9967a',fg='black').place(x=50,y=200)
Label(root,text='Name',font='times',bg='#e9967a',fg='black').place(x=50,y=250)
Label(root,text='Name',font='times',bg='#e9967a',fg='black').place(x=50,y=300)

root.mainloop()