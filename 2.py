import tkinter
import random
import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
from PIL import ImageTk, Image
filename_=""
def name():
    if vardas_tekst.get().isalpha() == False:
        messagebox.showinfo(title='Error', message='Vardas turi buti sudarytas is raidziu.')
        vardas_tekst.delete(0, 'end')
def surname():
    if pavarde_tekst.get().isalpha() == False:
        messagebox.showinfo(title='Error', message='Pavarde turi buti sudaryta is raidziu.')
        pavarde_tekst.delete(0, 'end')
def skaiciai():
    if len(str(asmn_tekst.get())) != 11:
            messagebox.showinfo(title='Error', message='Asmens kodas turi buti 11 skaitmenu.')
            asmn_tekst.delete(0, 'end')
def ilgis():
    if asmn_tekst.get().isdigit() == False:
        messagebox.showinfo(title='Error', message='Asmens kodas turi buti sudarytas is skaiciu.')
        asmn_tekst.delete(0, 'end')
def photo():
    global filename_
    filename_ = askopenfilename()
    print(filename_)
    newWindow = Toplevel(langas)
    img = ImageTk.PhotoImage(Image.open(filename_))
    panel = tk.Label(newWindow, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    newWindow.mainloop()
def deleteFile():
    file=open("file.txt", "w").close()
def tikrinti():
    if len(str(asmn_tekst.get())) == 0 or len(str(vardas_tekst.get())) == 0 or len(str(pavarde_tekst.get())) == 0:
        messagebox.showinfo(title='Error', message='Ne viskas buvo uzpildyta')
def openFile():
    subprocess.call(['notepad.exe', 'file.txt'])
def valyti():
    vardas_tekst.delete(0,'end')
    pavarde_tekst.delete(0, 'end')
    asmn_tekst.delete(0, 'end')
def v_autocapitalize(*arg):
    vardas.set(vardas.get().capitalize())
def p_autocapitalize(*arg):
        pavarde.set(pavarde.get().capitalize())
def save_info():
    global filename_
    vardas_tekst = vardas.get()
    pavarde_tekst = pavarde.get()
    asmn_tekst = kodas.get()
    photo=filename_
    print(vardas_tekst,pavarde_tekst,asmn_tekst,filename_)
    file=open("file.txt","a")
    file.write("\n")
    file.write("Vardas: "+ vardas_tekst)
    file.write("\n")
    file.write("Pavarde: " + pavarde_tekst)
    file.write("\n")
    file.write("Asmens kodas: " + str(asmn_tekst))
    file.write("\n")
    file.write("Nuotraukos directory: " + str(photo))
    file.write("\n")
    file.write("----------------------------------")
    file.write("\n")
    file.close()
langas=Tk()
langas.title('Vartotojo duomenys')
langas.geometry('470x145')
menubar=Menu(langas)
langas.config(menu=menubar)
fileMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Duomenys',menu=fileMenu)
fileMenu.add_command(label='Naujas',command=deleteFile)
fileMenu.add_command(label='Atidaryti',command=openFile)
fileMenu.add_command(label='Saugoti')
fileMenu.add_command(label='Iseiti',command=quit)
vardas=StringVar()
pavarde=StringVar()
kodas=StringVar()
filename=StringVar()
vardas_label=Label(langas,text='Vardas').place(x=20,y=20)
vardas_tekst=tk.Entry(langas,textvariable=vardas,justify = 'c',width=34)
vardas_tekst.place(x=130, y=20)
vardas.trace("w", v_autocapitalize)
pavarde_label=Label(langas,text='Pavarde').place(x=20,y=50)
pavarde_tekst=tk.Entry(langas,textvariable=pavarde,justify = 'c',width=34)
pavarde_tekst.place(x=130, y=50)
pavarde.trace("w", p_autocapitalize)
asmn_label=Label(langas,text='Asmens kodas').place(x=20, y=80)
asmn_tekst=tk.Entry(langas,textvariable=kodas,width=34, show='*',justify = 'c')
asmn_tekst.place(x=130, y=80)
Pateikti=Button(langas,text='Pateikti', width=8,command=lambda:[save_info(),skaiciai(),tikrinti(),name(),surname(),ilgis()])
Pateikti.place(x=130, y=110)
Valyti=Button(langas,text='Trinti',width=8,command=valyti).place(x=200, y=110)
Nuotrauka=Button(langas,text='Nuotrauka',width=8,command=photo).place(x=270, y=110)
Baigti=Button(langas,text='Baigti',width=8, command=langas.quit).place(x=340, y=110)

langas.mainloop()