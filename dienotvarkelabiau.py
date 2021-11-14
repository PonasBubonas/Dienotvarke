from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import json

program_data = {}
DATA = "Duomenys/darbai.txt"
redaguojama_diena = "1";

savaitės_dienos = {
    "1": "Pirmadienis",
    "2": "Antradienis",
    "3": "Trečiadienis",
    "4": "Ketvirtadienis",
    "5": "Penktadienis",
    "6": "Šeštadienis",
    "7": "Sekmadienis"
}

def atidaryti_dienos_redagavimas(diena_skaičius):
    global redaguojama_diena
    redaguojama_diena = diena_skaičius

    dienos_redagavimas_langas.title(savaitės_dienos[redaguojama_diena])
    dienos_redagavimas_listbox.delete(0, END)

    if redaguojama_diena in program_data:
        užduočių_sąrašas = program_data[redaguojama_diena]
    else:
        užduočių_sąrašas = list()

    for užduotis in užduočių_sąrašas:
        dienos_redagavimas_listbox.insert(END, užduotis)

    dienos_redagavimas_langas.deiconify()

def disable_event():
    pass

def sukurti_langą():
    return Tk()

def diena_pridėti_darbas():
    užduotis = dienos_redagavimas_entry_laikas.get() + " " + dienos_redagavimas_entry_užduotis.get()
    if dienos_redagavimas_entry_užduotis.get() == "":
        messagebox.showwarning("Klaida!", "Įrašykitę užduotį!")
    elif dienos_redagavimas_entry_laikas.get() == "":
        messagebox.showwarning("Klaida!", "Įrašykitę laiką!")
    else:
        dienos_redagavimas_listbox.insert(END, užduotis)
        dienos_redagavimas_entry_užduotis.delete(0, "end")
        dienos_redagavimas_entry_laikas.delete(0,"end")

def diena_ištrinti_darbas():
    dienos_redagavimas_listbox.delete(ANCHOR)

def data_išsaugoti_savaitė():
    with open(DATA, "w") as file:
        file.write(json.dumps(program_data))
    messagebox.showinfo('Pranešimas', 'Programa uždaroma')
    savaitės_langas.quit()

def data_išsaugoti_diena(diena_skaičius):
    global redaguojama_diena
    redaguojama_diena = diena_skaičius
    program_data[redaguojama_diena] = dienos_redagavimas_listbox.get(0, "end")
    with open(DATA, "w") as file:
        file.write(json.dumps(program_data))

def window_withdraw_day_edit():
    dienos_redagavimas_langas.withdraw()


savaitės_langas = sukurti_langą()
savaitės_langas.title('Savaites vaizdas')
savaitės_langas.geometry('1050x350')
savaitės_langas.config(bg='#223441')
savaitės_langas.resizable(False, False)

# <editor-fold desc="Redagavimo Langas">
dienos_redagavimas_langas = Tk()
dienos_redagavimas_langas.geometry('500x600')
dienos_redagavimas_langas.title(savaitės_dienos[redaguojama_diena])
dienos_redagavimas_langas.config(bg='#223441')
dienos_redagavimas_langas.resizable(width=False, height=False)
dienos_redagavimas_langas.withdraw()
dienos_redagavimas_langas.protocol("WM_DELETE_WINDOW", disable_event)

dienos_redagavimas_frame = Frame(dienos_redagavimas_langas)
dienos_redagavimas_frame.pack(pady=10)

dienos_redagavimas_listbox = Listbox(
    dienos_redagavimas_frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",

)
dienos_redagavimas_listbox.pack(side=LEFT, fill=BOTH)


dienos_redagavimas_scrollbar = Scrollbar(dienos_redagavimas_frame)
dienos_redagavimas_scrollbar.pack(side=RIGHT, fill=BOTH)

dienos_redagavimas_listbox.config(yscrollcommand=dienos_redagavimas_scrollbar.set)
dienos_redagavimas_scrollbar.config(command=dienos_redagavimas_listbox.yview)

dienos_redagavimas_pav_laikas = Label(
    dienos_redagavimas_langas,
    text="Laikas:",
    font=('times', 24))
dienos_redagavimas_entry_laikas = Entry(
    dienos_redagavimas_langas,
    font=('times', 24)
)

dienos_redagavimas_pav_laikas.pack(pady=1)
dienos_redagavimas_entry_laikas.pack(pady=3)
dienos_redagavimas_pav = Label(
    dienos_redagavimas_langas,
    text="Veikla:",
    font=('times', 24))
dienos_redagavimas_entry_užduotis = Entry(
    dienos_redagavimas_langas,
    font=('times', 24)
)
dienos_redagavimas_pav.pack(pady=1)
dienos_redagavimas_entry_užduotis.pack(pady=3)





dienos_redagavimas_mygtukai_frame = Frame(dienos_redagavimas_langas, width = 10)
dienos_redagavimas_mygtukai_frame.pack(pady=20)

dienos_redagavimas_mygtukas_pridėti = Button(
    dienos_redagavimas_mygtukai_frame,
    text='Pridėti',
    font=('times 14'),
    bg='#c5f776',
    activebackground='pink',
    padx=20,
    pady=10,
    command=diena_pridėti_darbas
)
dienos_redagavimas_mygtukas_pridėti.pack(fill=BOTH, expand=True, side=LEFT)

dienos_redagavimas_mygtukas_trinti = Button(
    dienos_redagavimas_mygtukai_frame,
    text='Trinti',
    font=('times 14'),
    bg='#ff8b61',
    activebackground='pink',
    padx=20,
    pady=10,
    command=diena_ištrinti_darbas
)
dienos_redagavimas_mygtukas_trinti.pack(fill=BOTH, expand=True, side=LEFT)

dienos_redagavimas_mygtukas_saugoti = Button(
    dienos_redagavimas_mygtukai_frame,
    text='Išsaugoti',
    font=('times 14'),
    bg='#ff8b61',
    activebackground='pink',
    padx=20,
    pady=10,
    command=lambda: data_išsaugoti_diena(redaguojama_diena)
)
dienos_redagavimas_mygtukas_saugoti.pack(fill=BOTH, expand=True, side=TOP
                                         )

dienos_redagavimas_mygtukas_išeiti = Button(
    dienos_redagavimas_mygtukai_frame,
    text='Išeiti',
    font=('times 14'),
    bg='#ff8b61',
    activebackground='pink',
    padx=20,
    pady=10,
    command=window_withdraw_day_edit
)
dienos_redagavimas_mygtukas_išeiti.pack(fill=BOTH, expand=True, side=TOP)

savaitės_pavadinimas = Label(savaitės_langas, text='Lapkričio 1 savaite', anchor='c', height=2, width=25, font='27').place(x=410, y=10)
# </editor-fold>

# <editor-fold desc="Savaitės Langas">



pirmadienis=Label(savaitės_langas, text='Pirmadienis', height=2, width=13).place(x=10, y=75)
redagavimas1=Button(savaitės_langas, text=u"\u270E", height=0, width=0, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("1")).place(x=100, y=75)
tekstas1=Text(savaitės_langas, width=15, height=10).place(x=10, y=110)

antradienis=Label(savaitės_langas, text='Antradienis',height=2, width=13).place(x=160, y=75)
redagavimas2=Button(savaitės_langas, text=u"\u270E", height=0, width=0, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("2")).place(x=250, y=75)
tekstas2=Text(savaitės_langas, width=15, height=10).place(x=160, y=110)

treciadienis=Label(savaitės_langas, text='Treciadienis',height=2, width=13).place(x=310, y=75)
redagavimas3=Button(savaitės_langas, text=u"\u270E", height=0, width=0, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("3")).place(x=400, y=75)
tekstas3=Text(savaitės_langas, width=15, height=10).place(x=310, y=110)

ketvirtadienis=Label(savaitės_langas, text='Ketvirtadienis',height=2, width=13).place(x=460, y=75)
redagavimas4=Button(savaitės_langas, text=u"\u270E", height=0, width=0, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("4")).place(x=550, y=75)
tekstas4=Text(savaitės_langas, width=15, height=10).place(x=460, y=110)

penktadienis=Label(savaitės_langas, text='Penktadienis',height=2, width=13).place(x=610, y=75)
redagavimas5=Button(savaitės_langas, text=u"\u270E", height=0, width=0, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("5")).place(x=700, y=75)
tekstas5=Text(savaitės_langas, width=15, height=10).place(x=610, y=110)

sestadienis=Label(savaitės_langas, text='Šeštadienis',height=2, width=13).place(x=760, y=75)
redagavimas6=Button(savaitės_langas, text=u"\u270E", height=0, width=0, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("6")).place(x=850, y=75)
tekstas6=Text(savaitės_langas, width=15, height=10).place(x=760, y=110)

sekmadienis=Label(savaitės_langas, text='Sekmadienis',height=2, width=13).place(x=910, y=75)
redagavimas7=Button(savaitės_langas, text=u"\u270E", height=0, width=0, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("7")).place(x=1000, y=75)
tekstas7=Text(savaitės_langas, width=15, height=10).place(x=910, y=110)

trinti=Button(savaitės_langas, text='trinti', height=2, width=10, activebackground='pink', bd='2', bg='#ff8b61').place(x=520, y=290)
saugoti=Button(savaitės_langas, text='issaugoti', height=2, width=10, activebackground='pink', bd='2',bg='#c5f776').place(x=360, y=290)
naujas=Button(savaitės_langas, text='naujas', height=2, width=10, activebackground='pink', bd='2', bg='#c5f776').place(x=440, y=290)
baigti=Button(savaitės_langas, text='baigti', height=2, width=10, activebackground='pink', bd='2',bg='#ff8b61', command=lambda: data_išsaugoti_savaitė()).place(x=600, y=290)

my_menu=Menu(savaitės_langas) # priskirti Menu klasei
savaitės_langas.config(menu=my_menu) # lango konfiguravimas
file_menu=Menu(my_menu) # Šakninis meniu, kuris turi būti Menu klasėje
my_menu.add_cascade(label="Veiksmai", menu=file_menu) # Kuriamas kaskadinis meniu, t.y. einantis žemyn
file_menu.add_command(label='Naujas',)
file_menu.add_command(label='Issaugoti')
file_menu.add_command(label='Trinti',)
file_menu.add_command(label='Baigti', command=lambda: data_išsaugoti_savaitė())
# </editor-fold>

try:
    with open(DATA, "r") as file:
        program_data = json.loads(file.read())
except:
    program_data = {}

savaitės_langas.mainloop()