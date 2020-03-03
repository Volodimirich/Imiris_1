from tkinter import *

F = Frame(borderwidth=2,relief="ridge")
F.master.columnconfigure(0,weight=1);
F.master.rowconfigure(0,weight=1)
F.grid(sticky="NEWS")

F.columnconfigure(0,weight=1);
F.columnconfigure(1,weight=2)

B1 = Button(master=F,text="Button1")
B2 = Button(master=F,text="Button2")

B1.grid(sticky="NEWS")
B2.grid(sticky="NEWS",column=1,row=0)
