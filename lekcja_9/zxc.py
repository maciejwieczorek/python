import Tkinter as tk
import tkFont as tkF
import tkMessageBox as tkMB

root = tk.Tk()

v = tk.IntVar()

def_fnt = tkF.nametofont("TkDefaultFont")
def_fnt.configure(size = 20)
root.option_add("*Font", def_fnt)

def changeColor(bt,rb):
	bt.configure(bg=rb.gettext())


bt1 = tk.Button(root,text="START")
bt1.grid(row=1,column=1)

rb1 = tk.Radiobutton(root,text="red",value = 1,variable = v,command = lambda:changeColor(bt1,"red"))
rb1.grid(row=0,column=0)

rb2 = tk.Radiobutton(root,text="blue",value = 2,variable = v,command=lambda:changeColor(bt1,rb2))
rb2.grid(row=0,column=1)

rb3 = tk.Radiobutton(root,text="green",value = 3,variable = v,command= lambda:changeColor(bt1,rb3))
rb3.grid(row=0,column=2)



root.mainloop()