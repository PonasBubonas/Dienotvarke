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

def trinti_1():
    program_data["1"]=""
def trinti_2():
    program_data["2"]=""
def trinti_3():
    program_data["3"]=""
def trinti_4():
    program_data["4"]=""
def trinti_5():
    program_data["5"]=""
def trinti_6():
    program_data["6"]=""
def trinti_7():
    program_data["7"]=""
def trinti_langas():
    trinti_langas=Toplevel()
    trinti_langas.title("Dienotvarkes redagavimas")
    trinti_langas.geometry('500x500')
    Myg1= Button(trinti_langas, text="Pirmadienis", bg='#223441', command=trinti_1).pack(side=TOP, expand=TRUE, fill=BOTH)
    Myg2=Button(trinti_langas, text="Antradienis", bg='#464646', command=trinti_2).pack(side=TOP, expand=TRUE, fill=BOTH)
    Myg3=Button(trinti_langas, text="Trečiadienis", bg='#223441', command=trinti_3).pack(side=TOP, expand=TRUE, fill=BOTH)
    Myg4=Button(trinti_langas, text="Ketvirtadienis", bg='#464646', command=trinti_4).pack(side=TOP, expand=TRUE, fill=BOTH)
    Myg5=Button(trinti_langas, text="Penktadienis", bg='#223441', command=trinti_5).pack(side=TOP, expand=TRUE, fill=BOTH)
    Myg6=Button(trinti_langas, text="Šeštadienis", bg='#464646', command=trinti_6).pack(side=TOP, expand=TRUE, fill=BOTH)
    Myg7=Button(trinti_langas, text="Sekmadienis", bg='#223441', command=trinti_7).pack(side=TOP, expand=TRUE, fill=BOTH)

savaitės_langas = sukurti_langą()
savaitės_langas.title('Savaites vaizdas')
savaitės_langas.geometry('1050x450')
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
pirmadienis=Label(savaitės_langas, text='Pirmadienis').place(x=30, y=40)
redagavimas1=Button(savaitės_langas, text=u"\u270E", height=1, width=1, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("1")).place(x=100, y=40)
tekstas1=Listbox(savaitės_langas, width=20, height=10)
tekstas1.place(x=10, y=70)

antradienis=Label(savaitės_langas, text='Antradienis').place(x=170, y=40)
redagavimas2=Button(savaitės_langas, text=u"\u270E", height=1, width=2, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("2")).place(x=240, y=40)
tekstas2=Listbox(savaitės_langas, width=20, height=10)
tekstas2.place(x=150, y=70)

treciadienis=Label(savaitės_langas, text='Treciadienis').place(x=310, y=40)
redagavimas3=Button(savaitės_langas, text=u"\u270E", height=1, width=1, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("3")).place(x=380, y=40)
tekstas3=Listbox(savaitės_langas, width=20, height=10)
tekstas3.place(x=290, y=70)

ketvirtadienis=Label(savaitės_langas, text='Ketvirtadienis').place(x=450, y=40)
redagavimas4=Button(savaitės_langas, text=u"\u270E", height=1, width=1, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("4")).place(x=530, y=40)
tekstas4=Listbox(savaitės_langas, width=20, height=10)
tekstas4.place(x=430, y=70)

penktadienis=Label(savaitės_langas, text='Penktadienis').place(x=590, y=40)
redagavimas5=Button(savaitės_langas, text=u"\u270E", height=1, width=1, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("5")).place(x=670, y=40)
tekstas5=Listbox(savaitės_langas, width=20, height=10)
tekstas5.place(x=570, y=70)

sestadienis=Label(savaitės_langas, text='Šeštadienis').place(x=730, y=40)
redagavimas6=Button(savaitės_langas, text=u"\u270E", height=1, width=1, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("6")).place(x=795, y=40)
tekstas6=Listbox(savaitės_langas, width=20, height=10)
tekstas6.place(x=710, y=70)

sekmadienis=Label(savaitės_langas, text='Sekmadienis').place(x=870, y=40)
redagavimas7=Button(savaitės_langas, text=u"\u270E", height=1, width=1, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("7")).place(x=950, y=40)
tekstas7=Listbox(savaitės_langas, width=20, height=10)
tekstas7.place(x=850, y=70)

trinti=Button(savaitės_langas, text='trinti', height=2, width=10, activebackground='pink', bd='2', bg='#ff8b61', command=trinti_langas).place(x=520, y=290)
saugoti=Button(savaitės_langas, text='issaugoti', height=2, width=10, activebackground='pink', bd='2',bg='#c5f776').place(x=360, y=290)
naujas=Button(savaitės_langas, text='naujas', height=2, width=10, activebackground='pink', bd='2', bg='#c5f776').place(x=440, y=290)
baigti=Button(savaitės_langas, text='baigti', height=2, width=10, activebackground='pink', bd='2',bg='#ff8b61', command=lambda: data_išsaugoti_savaitė()).place(x=600, y=290)

my_menu=Menu(savaitės_langas) # priskirti Menu klasei
savaitės_langas.config(menu=my_menu) # lango konfiguravimas
file_menu=Menu(my_menu) # Šakninis meniu, kuris turi būti Menu klasėje
my_menu.add_cascade(label="Veiksmai", menu=file_menu) # Kuriamas kaskadinis meniu, t.y. einantis žemyn
file_menu.add_command(label='Naujas',)
file_menu.add_command(label='Issaugoti')
file_menu.add_command(label='Trinti', command=lambda: trinti_langas)
file_menu.add_command(label='Baigti', command=lambda: data_išsaugoti_savaitė())
# </editor-fold>

try:
    with open(DATA, "r") as file:
        program_data = json.loads(file.read())
except:
    program_data = {}

def atnaujinti():
    savaitės_langas.after(100, atnaujinti)
    duomenys = program_data["1"]
    tekstas1.delete(0, END)
    for eilutė in duomenys:
        tekstas1.insert(END, eilutė)

    duomenys = program_data["2"]
    tekstas2.delete(0, END)
    for eilutė in duomenys:
        tekstas2.insert(END, eilutė)

    duomenys = program_data["3"]
    tekstas3.delete(0, END)
    for eilutė in duomenys:
        tekstas3.insert(END, eilutė)

    duomenys = program_data["4"]

    tekstas4.delete(0, END)
    for eilutė in duomenys:
        tekstas4.insert(END, eilutė)

    duomenys = program_data["5"]
    tekstas5.delete(0, END)
    for eilutė in duomenys:
        tekstas5.insert(END, eilutė)

    duomenys = program_data["6"]
    tekstas6.delete(0, END)
    for eilutė in duomenys:
        tekstas6.insert(END, eilutė)

    duomenys = program_data["7"]
    tekstas7.delete(0, END)
    for eilutė in duomenys:
        tekstas7.insert(END, eilutė)

savaitės_langas.after(0, atnaujinti)
savaitės_langas.mainloop()