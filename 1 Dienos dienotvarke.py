import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

langas=Tk()
langas.title('Dienos dienotvarke')
langas.geometry('230x420')
langas.resizable(False,False)

def baigti():
    messagebox.showinfo('Pranešimas', 'Programa uždaroma')
    langas.quit()
def issaugoti():
    f = open('Data.txt', 'w')  # sukuriamas, arba atidaromas sukurtas txt failas
    f.write(viens and '\t' and pirm_laik and '\t' and pirm_veikl and '\n' and \
            du  and '\t' and antr_laik and '\t' and antr_veikl and '\n' and \
            trys  and '\t' and trc_laik  and '\t' and trc_veikl and '\n' and \
            ketr  and '\t' and ketvr_laik  and '\t' and ketvr_veikl and '\n' and \
            penk  and '\t' and penkt_laik  and '\t' and penkt_veikl) #nzn ar teisingai ciaaa
    f.close()  # failas uždaromas po įrašymo

def my_popup(e):
    my_menu.tk_popup(e.x_root, e.y_root)

Diena_L=Label(langas,text='Pirmadienis', anchor='c',fg='red',font='16').place(x=80,y=10)
Laikas_L=Label(langas,text='Laikas:').place(x=20,y=30)
Veikla_L=Label(langas,text='Uzsiemimas:').place(x=70,y=30)
viens=Label(langas,text='1)').place(x=5,y=48)
pirm_laik=Entry(langas,width=8,justify='l').place(x=20, y=50)
pirm_veikl=Entry(langas,width=20,justify='l').place(x=70, y=50)
du=Label(langas,text='2)').place(x=5,y=78)
antr_laik=Entry(langas,width=8,justify='l').place(x=20, y=80)
antr_veikl=Entry(langas,width=20,justify='l').place(x=70, y=80)
trys=Label(langas,text='3)').place(x=5,y=108)
trc_laik=Entry(langas,width=8,justify='l').place(x=20, y=110)
trc_veikl=Entry(langas,width=20,justify='l').place(x=70, y=110)
ketr=Label(langas,text='4)').place(x=5,y=138)
ketvr_laik=Entry(langas,width=8,justify='l').place(x=20, y=140)
ketvr_veikl=Entry(langas,width=20,justify='l').place(x=70, y=140)
penk=Label(langas,text='5)').place(x=5,y=168)
penkt_laik=Entry(langas,width=8,justify='l').place(x=20, y=170)
penkt_veikl=Entry(langas,width=20,justify='l').place(x=70, y=170)
Naujs=Button(langas,text='Naujas',command=issaugoti,height=2, width=11,activebackground='pink',bd='5',).place(x=20,y=220)
perras=Button(langas,text='Issaugoti',command=issaugoti,height=2, width=11,activebackground='pink',bd='5',).place(x=110,y=220)
trintii=Button(langas,text='Trinti',command=issaugoti,height=2, width=11,activebackground='pink',bd='5',).place(x=20,y=270)
atgall=Button(langas,text='Grizti',command=issaugoti,height=2, width=11,activebackground='pink',bd='5',).place(x=110,y=270)
baigtiii=Button(langas,text='Baigti',command=baigti,height=2, width=11,activebackground='pink',bd='5',).place(x=65,y=320)

my_menu=Menu(langas) # priskirti Menu klasei
langas.config(menu=my_menu) # lango konfiguravimas
file_menu=Menu(my_menu) # Šakninis meniu, kuris turi būti Menu klasėje
my_menu.add_cascade(label="Veiksmai", menu=file_menu) # Kuriamas kaskadinis meniu, t.y. einantis žemyn
file_menu.add_command(label='Naujas',)
file_menu.add_command(label='Issaugoti')
file_menu.add_command(label='Trinti',)
file_menu.add_command(label='Grizti')
file_menu.add_command(label='Baigti',command=baigti)

my_menu=Menu(langas, tearoff=0)
my_menu.add_command(label='Naujas',)
my_menu.add_command(label='Issaugoti', )
my_menu.add_command(label='Trinti',)
my_menu.add_command(label='Grizti')
my_menu.add_command(label='Baigti', command=baigti)
langas.bind("<Button-3>", my_popup)


langas.mainloop()

#21 skaidre yra
#cia toks labai scuffed vienos dienos dienotvarkes tvarkytuve (i guess)
#prototipas krc xd
#labai neina man su tom def tai nieko realiai nepadariau, reikia apsirasyt ir butu ok
