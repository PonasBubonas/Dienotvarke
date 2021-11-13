import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

langas=Tk()
langas.title('Savaites vaizdas')
langas.geometry('1000x300')
langas.resizable(False,False)

def baigti():
    messagebox.showinfo('Pranešimas', 'Programa uždaroma')
    langas.quit()

Sav_pav=Label(langas,text='Laipkricio 1 savaite', anchor='c',font='16').place(x=450,y=10)
pirmadienis=Label(langas,text='Pirmadienis').place(x=30,y=40)
redagavimas1=Button(langas,'',height=1, width=1,activebackground='pink',bd='2',).place(x=100,y=40)\
    #neleidzia jokio simbolio tik raides, tai kazka del to reiktu
#viens=Label(langas,text='1)').place(x=5,y=68) #su situ nzn, kaip
tekstas1=Text(langas,width=15, height=10).place(x=10,y=70)
antradienis=Label(langas,text='Antradienis').place(x=170,y=40)
redagavimas2=Button(langas,'',height=1, width=1,activebackground='pink',bd='2',).place(x=240,y=40)
tekstas2=Text(langas,width=15, height=10).place(x=150,y=70)
treciadienis=Label(langas,text='Treciadienis').place(x=310,y=40)
redagavimas3=Button(langas,'',height=1, width=1,activebackground='pink',bd='2',).place(x=380,y=40)
tekstas3=Text(langas,width=15, height=10).place(x=290,y=70)
ketvirtadienis=Label(langas,text='Ketvirtadienis').place(x=450,y=40)
redagavimas4=Button(langas,'',height=1, width=1,activebackground='pink',bd='2',).place(x=530,y=40)
tekstas4=Text(langas,width=15, height=10).place(x=430,y=70)
penktadienis=Label(langas,text='Penktadienis').place(x=590,y=40)
redagavimas5=Button(langas,'',height=1, width=1,activebackground='pink',bd='2',).place(x=670,y=40)
tekstas5=Text(langas,width=15, height=10).place(x=570,y=70)
sestadienis=Label(langas,text='Sestadienis').place(x=730,y=40)
redagavimas6=Button(langas,'',height=1, width=1,activebackground='pink',bd='2',).place(x=795,y=40)
tekstas6=Text(langas,width=15, height=10).place(x=710,y=70)
sekmadienis=Label(langas,text='Sekmadienis').place(x=870,y=40)
redagavimas7=Button(langas,'',height=1, width=1,activebackground='pink',bd='2',).place(x=950,y=40)
tekstas7=Text(langas,width=15, height=10).place(x=850,y=70)
trinti=Button(langas,text='trinti',height=2, width=10,activebackground='pink',bd='2',).place(x=300,y=250)
saugoti=Button(langas,text='issaugoti',height=2, width=10,activebackground='pink',bd='2',).place(x=390,y=250)
naujas=Button(langas,text='naujas',height=2, width=10,activebackground='pink',bd='2',).place(x=480,y=250)
baigt=Button(langas,text='baigti',height=2, width=10,activebackground='pink',bd='2',command=baigti).place(x=570,y=250)

my_menu=Menu(langas) # priskirti Menu klasei
langas.config(menu=my_menu) # lango konfiguravimas
file_menu=Menu(my_menu) # Šakninis meniu, kuris turi būti Menu klasėje
my_menu.add_cascade(label="Veiksmai", menu=file_menu) # Kuriamas kaskadinis meniu, t.y. einantis žemyn
file_menu.add_command(label='Naujas',)
file_menu.add_command(label='Issaugoti')
file_menu.add_command(label='Trinti',)
file_menu.add_command(label='Baigti',command=baigti)

langas.mainloop()