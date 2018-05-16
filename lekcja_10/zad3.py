import Tkinter as tk
import tkFont as tkF
import tkMessageBox as tkMB
from Tkinter import *


root = tk.Tk()

v = tk.IntVar()

def_fnt = tkF.nametofont("TkDefaultFont")
def_fnt.configure(size = 20)
root.option_add("*Font", def_fnt)

def changeColor(bt,rb):
	bt.configure(bg=rb.gettext())

def liczby():
	text.configure(Button.get())


def update_Entry(inputValue):
    #Updates the entry when a button is pressed.
    currentText = num1.get();
    update = num1.set(currentText + inputValue);

num1 = StringVar();
txtDisplay = Entry(root, textvariable = num1 );
txtDisplay.focus();

txtDisplay.grid(row=0)
print(txtDisplay.get())


#rb1 = tk.Radiobutton(root,text="red",value = 1,variable = v,command = lambda:changeColor(bt1,"red"))
#rb1.grid(row=0,column=0)

#rb2 = tk.Radiobutton(root,text="blue",value = 2,variable = v,command=lambda:changeColor(bt1,rb2))
#rb2.grid(row=0,column=1)

#rb3 = tk.Radiobutton(root,text="green",value = 3,variable = v,command= lambda:changeColor(bt1,rb3))
#rb3.grid(row=0,column=2)

button_0 = tk.Button(root, text=0, command = lambda:update_Entry('0'))
button_0.grid(row=5, column=1)

button_1 = tk.Button(root, text=1, command = lambda:update_Entry('1'))
button_1.grid(row=4, column=0)

button_2 = tk.Button(root, text=2, command = lambda:update_Entry('2'))
button_2.grid(row=4, column=1)

button_3 = tk.Button(root, text=3, command = lambda:update_Entry('3'))
button_3.grid(row=4, column=2)

button_4 = tk.Button(root, text=4, command = lambda:update_Entry('4'))
button_4.grid(row=3, column=0)

button_5 = tk.Button(root, text=5, command = lambda:update_Entry('5'))
button_5.grid(row=3, column=1)

button_6 = tk.Button(root, text=6, command = lambda:update_Entry('6'))
button_6.grid(row=3, column=2)

button_7 = tk.Button(root, text=7, command = lambda:update_Entry('7'))
button_7.grid(row=2, column=0)

button_8 = tk.Button(root, text=8, command = lambda:update_Entry('8'))
button_8.grid(row=2, column=1)

button_9 = tk.Button(root, text=9, command = lambda:update_Entry('9'))
button_9.grid(row=2, column=2)

button_przecinek = tk.Button(root, text=",", command = lambda:update_Entry(','))
button_przecinek.grid(row=5, column=0)

button_dodaj = tk.Button(root, text="+", command = lambda:update_Entry('+'))
button_dodaj.grid(row=2, column=3)

button_minus = tk.Button(root, text="-", command = lambda:update_Entry('-'))
button_minus.grid(row=3, column=3)

button_podziel = tk.Button(root, text="/", command = lambda:update_Entry('/'))
button_podziel.grid(row=4, column=3)

button_mnoz = tk.Button(root, text="*", command = lambda:update_Entry('*'))
button_mnoz.grid(row=5, column=3)

button_wynik = tk.Button(root, text="=", command = lambda:update_Entry('='))
button_wynik.grid(row = 5, column = 2)





root.mainloop()