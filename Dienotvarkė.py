from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
import json


hash_dienos = {}
hash_metai = {}
DATA = "Duomenys/darbai.txt"
redaguojama_diena = "1"
redaguojama_savaitės_diena = "1"
savaitės_skaičius= "1"
metų_skaičius = "2021"
dienų_sulyginimas = 3

savaitės_dienos_metų_dienos = ["0","0","0","0","0","0","0"]

savaitės_dienos = {
    "1": "Pirmadienis",
    "2": "Antradienis",
    "3": "Trečiadienis",
    "4": "Ketvirtadienis",
    "5": "Penktadienis",
    "6": "Šeštadienis",
    "7": "Sekmadienis"
}

def diena_į_datą(dienos_skaičius, metų_skaičius):
    dienos_skaičius.rjust(3 + len(dienos_skaičius), '0')
    res = datetime.strptime(metų_skaičius + "-" + dienos_skaičius, "%Y-%j").strftime("%Y-%m-%d")
    return(str(res))
    print("Resolved date : " + str(res))

def dienų_sulyginimas_pirmyn():
    global dienų_sulyginimas
    if abs((int(metų_skaičius)-2020) % 4 == 0) or int(metų_skaičius) - 2020 == 0:
        dienų_sulyginimas = dienų_sulyginimas - 2
    else:
        dienų_sulyginimas = dienų_sulyginimas - 1

    if dienų_sulyginimas <= 0:
        dienų_sulyginimas = dienų_sulyginimas + 7

    print("dienų sulyginimas: "+ str(dienų_sulyginimas) + "\n")

def dienų_sulyginimas_atgal():
    global dienų_sulyginimas
    if abs((int(metų_skaičius)-2021) % 4 == 0) or int(metų_skaičius) - 2021 == 0:
        dienų_sulyginimas = dienų_sulyginimas + 2
    else:
        dienų_sulyginimas = dienų_sulyginimas + 1

    if dienų_sulyginimas >= 7:
        dienų_sulyginimas = dienų_sulyginimas - 7

    print("dienų sulyginimas: " + str(dienų_sulyginimas) + "\n")

def atnaujinti_tekstai_datos():
    global savaitės_dienos_metų_dienos

    pirmadienis_metų_dienos_skaičius = str((int(savaitės_skaičius) - 1) * 7 + 1 + dienų_sulyginimas)
    antradienis_metų_dienos_skaičius = str((int(savaitės_skaičius) - 1) * 7 + 2 + dienų_sulyginimas)
    trečiadienis_metų_dienos_skaičius = str((int(savaitės_skaičius) - 1) * 7 + 3 + dienų_sulyginimas)
    ketvirtadienis_metų_dienos_skaičius = str((int(savaitės_skaičius) - 1) * 7 + 4 + dienų_sulyginimas)
    penktadienis_metų_dienos_skaičius = str((int(savaitės_skaičius) - 1) * 7 + 5 + dienų_sulyginimas)
    šeštadienis_metų_dienos_skaičius = str((int(savaitės_skaičius) - 1) * 7 + 6 + dienų_sulyginimas)
    sekmadienis_metų_dienos_skaičius = str((int(savaitės_skaičius) - 1) * 7 + 7 + dienų_sulyginimas)
    savaitės_dienos_metų_dienos = []
    savaitės_dienos_metų_dienos = [pirmadienis_metų_dienos_skaičius, antradienis_metų_dienos_skaičius,
                                       trečiadienis_metų_dienos_skaičius, ketvirtadienis_metų_dienos_skaičius,
                                       penktadienis_metų_dienos_skaičius, šeštadienis_metų_dienos_skaičius,
                                       sekmadienis_metų_dienos_skaičius]
    print(savaitės_dienos_metų_dienos)

    try:
        pirmadienis.configure(text='Pirmadienis' + " " + diena_į_datą((pirmadienis_metų_dienos_skaičius), metų_skaičius))
    except:
        pirmadienis.configure(text='-----------')
    try:
        antradienis.configure(text='Antradienis' + " " + diena_į_datą((antradienis_metų_dienos_skaičius), metų_skaičius))
    except:
        antradienis.configure(text='-----------')
    try:
        treciadienis.configure(text='Trečiadienis' + " " + diena_į_datą((trečiadienis_metų_dienos_skaičius), metų_skaičius))
    except:
        treciadienis.configure(text='-----------')
    try:
        ketvirtadienis.configure(text='Ketvirtadienis' + " " + diena_į_datą((ketvirtadienis_metų_dienos_skaičius), metų_skaičius))
    except:
        ketvirtadienis.configure(text='-----------')
    try:
        penktadienis.configure(text='Penktadienis' + " " + diena_į_datą((penktadienis_metų_dienos_skaičius), metų_skaičius))
    except:
        penktadienis.configure(text='-----------')
    try:
        sestadienis.configure(text='Šeštadienis' + " " + diena_į_datą((šeštadienis_metų_dienos_skaičius), metų_skaičius))
    except:
        sestadienis.configure(text='-----------')
    try:
        sekmadienis.configure(text='Sekmadienis' + " " + diena_į_datą((sekmadienis_metų_dienos_skaičius), metų_skaičius))
    except:
        sekmadienis.configure(text='-----------')

def pirmyn_savaitė():
    global savaitės_skaičius
    savaitės_skaičius = int(savaitės_skaičius)
    savaitės_skaičius = savaitės_skaičius + 1
    savaitės_skaičius = str(savaitės_skaičius)
    atnaujinti_tekstai_datos()
    savaitės_pavadinimas.configure(text = savaitės_skaičius + " savaitė")

def atgal_savaitė():
    global savaitės_skaičius
    savaitės_skaičius = int(savaitės_skaičius)
    savaitės_skaičius = savaitės_skaičius - 1
    savaitės_skaičius = str(savaitės_skaičius)
    atnaujinti_tekstai_datos()
    savaitės_pavadinimas.configure(text= savaitės_skaičius + " savaitė")

def pirmyn_metai():
    global metų_skaičius
    metų_skaičius = int(metų_skaičius)
    metų_skaičius = metų_skaičius+1
    metų_skaičius = str(metų_skaičius)
    print(metų_skaičius)
    atnaujinti_tekstai_datos()

def atgal_metai():
    global metų_skaičius
    metų_skaičius = int(metų_skaičius)
    metų_skaičius = metų_skaičius - 1
    metų_skaičius = str(metų_skaičius)
    print(metų_skaičius)
    atnaujinti_tekstai_datos()

def atidaryti_dienos_redagavimas(diena_skaičius):
    global redaguojama_diena
    global redaguojama_savaitės_diena

    redaguojama_savaitės_diena = diena_skaičius
    redaguojama_diena = savaitės_dienos_metų_dienos[int(diena_skaičius)-1]

    dienos_redagavimas_langas.title(savaitės_dienos[diena_skaičius])
    dienos_redagavimas_listbox.delete(0, END)

    if (metų_skaičius+redaguojama_diena) in hash_dienos:
        užduočių_sąrašas = hash_dienos[metų_skaičius+redaguojama_diena]
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
        file.write(json.dumps(hash_dienos))
    messagebox.showinfo('Pranešimas', 'Programa uždaroma')
    savaitės_langas.quit()

def data_išsaugoti_diena(diena_skaičius):
    global redaguojama_diena
    global redaguojama_savaitės_diena


    redaguojama_savaitės_diena = diena_skaičius
    redaguojama_diena = savaitės_dienos_metų_dienos[int(diena_skaičius)-1]

    hash_dienos[metų_skaičius+(redaguojama_diena)] = dienos_redagavimas_listbox.get(0, "end")
    with open(DATA, "w") as file:
        file.write(json.dumps(hash_dienos))

def window_withdraw_day_edit():
    dienos_redagavimas_langas.withdraw()

def trinti_1():
    hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[0]]= ""
def trinti_2():
    hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[1]]= ""
def trinti_3():
    hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[2]]= ""
def trinti_4():
    hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[3]]= ""
def trinti_5():
    hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[4]]= ""
def trinti_6():
    hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[5]]= ""
def trinti_7():
    hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[6]]= ""
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
    command=lambda: data_išsaugoti_diena(redaguojama_savaitės_diena)
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


# </editor-fold>
pirmadienis_savaitės_skaičius= str((int(savaitės_skaičius)-1)*7+1)
antradienis_savaitės_skaičius= str((int(savaitės_skaičius)-1)*7+2)
trečiadienis_savaitės_skaičius= str((int(savaitės_skaičius)-1)*7+3)
ketvirtadienis_savaitės_skaičius= str((int(savaitės_skaičius)-1)*7+4)
penktadienis_savaitės_skaičius= str((int(savaitės_skaičius)-1)*7+5)
šeštadienis_savaitės_skaičius= str((int(savaitės_skaičius)-1)*7+6)
sekmadienis_savaitės_skaičius= str((int(savaitės_skaičius)-1)*7+7)


# <editor-fold desc="Savaitės Langas">
savaitės_pavadinimas = Label(savaitės_langas, text = savaitės_skaičius + " savaitė", anchor='c', height=1, width=25, font='27')
savaitės_pavadinimas.place(x=410, y=10)

pirmadienis=Label(savaitės_langas, text ='Pirmadienis'+ " " + diena_į_datą((pirmadienis_savaitės_skaičius),metų_skaičius))
pirmadienis.place(x=30, y=40)
redagavimas1=Button(savaitės_langas, text=u"\u270E", height=1, width=11, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("1")).place(x=12, y=230)
tekstas1=Listbox(savaitės_langas, width=20, height=10)
tekstas1.place(x=10, y=70)

antradienis=Label(savaitės_langas, text='Antradienis'+ " " + diena_į_datą((antradienis_savaitės_skaičius),metų_skaičius))
antradienis.place(x=170, y=40)
redagavimas2=Button(savaitės_langas, text=u"\u270E", height=1, width=11, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("2")).place(x=152, y=230)
tekstas2=Listbox(savaitės_langas, width=20, height=10)
tekstas2.place(x=150, y=70)

treciadienis=Label(savaitės_langas, text='Treciadienis'+ " " + diena_į_datą((trečiadienis_savaitės_skaičius),metų_skaičius))
treciadienis.place(x=310, y=40)
redagavimas3=Button(savaitės_langas, text=u"\u270E", height=1, width=11, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("3")).place(x=292, y=230)
tekstas3=Listbox(savaitės_langas, width=20, height=10)
tekstas3.place(x=290, y=70)

ketvirtadienis=Label(savaitės_langas, text='Ketvirtadienis'+ " " + diena_į_datą((ketvirtadienis_savaitės_skaičius),metų_skaičius))
ketvirtadienis.place(x=450, y=40)

redagavimas4=Button(savaitės_langas, text=u"\u270E", height=1, width=11, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("4")).place(x=442, y=230)
tekstas4=Listbox(savaitės_langas, width=20, height=10)
tekstas4.place(x=430, y=70)

penktadienis=Label(savaitės_langas, text='Penktadienis'+ " " + diena_į_datą((penktadienis_savaitės_skaičius),metų_skaičius))
penktadienis.place(x=590, y=40)
redagavimas5=Button(savaitės_langas, text=u"\u270E", height=1, width=11, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("5")).place(x=582, y=230)
tekstas5=Listbox(savaitės_langas, width=20, height=10)
tekstas5.place(x=570, y=70)

sestadienis=Label(savaitės_langas, text='Šeštadienis'+ " " + diena_į_datą((šeštadienis_savaitės_skaičius),metų_skaičius))
sestadienis.place(x=730, y=40)
redagavimas6=Button(savaitės_langas, text=u"\u270E", height=1, width=11, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("6")).place(x=707, y=230)
tekstas6=Listbox(savaitės_langas, width=20, height=10)
tekstas6.place(x=710, y=70)

sekmadienis=Label(savaitės_langas, text='Sekmadienis'+ " " + diena_į_datą((sekmadienis_savaitės_skaičius),metų_skaičius))
sekmadienis.place(x=870, y=40)
redagavimas7=Button(savaitės_langas, text=u"\u270E", height=1, width=11, activebackground='pink', bd='2', font=("Times", 14), command = lambda: atidaryti_dienos_redagavimas("7")).place(x=862, y=230)
tekstas7=Listbox(savaitės_langas, width=20, height=10)
tekstas7.place(x=850, y=70)

pirmyn_savaitė_mygtukas=Button(savaitės_langas, text='>SAV>', height=2, width=2, activebackground='pink', bd='2', bg='#ff8b61', command=pirmyn_savaitė).place(x=40, y=340)
atgal_savaitė_mygtukas=Button(savaitės_langas, text='<SAV<', height=2, width=2, activebackground='pink', bd='2', bg='#ff8b61', command=atgal_savaitė).place(x=10, y=340)
pirmyn_metai_mygtukas=Button(savaitės_langas, text='>MET>', height=2, width=2, activebackground='pink', bd='2', bg='#ff8b61', command=lambda:[dienų_sulyginimas_pirmyn(), pirmyn_metai()])
pirmyn_metai_mygtukas.place(x=40, y=400)
atgal_metai_mygtukas=Button(savaitės_langas, text='<MET<', height=2, width=2, activebackground='pink', bd='2', bg='#ff8b61', command=lambda:[dienų_sulyginimas_atgal(), atgal_metai()])
atgal_metai_mygtukas.place(x=10, y=400)
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
        hash_dienos = json.loads(file.read())
except:
    hash_dienos = {}

def atnaujinti():
    savaitės_langas.after(100, atnaujinti)

    try:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[0]]
    except:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[0]] = {}
    duomenys = hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[0]]
    tekstas1.delete(0, END)
    for eilutė in duomenys:
        tekstas1.insert(END, eilutė)


    try:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[1]]
    except:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[1]] = {}
    duomenys = hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[1]]
    tekstas2.delete(0, END)
    for eilutė in duomenys:
        tekstas2.insert(END, eilutė)


    try:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[2]]
    except:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[2]] = {}
    duomenys = hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[2]]
    tekstas3.delete(0, END)
    for eilutė in duomenys:
        tekstas3.insert(END, eilutė)


    try:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[3]]
    except:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[3]] = {}
    duomenys = hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[3]]
    tekstas4.delete(0, END)
    for eilutė in duomenys:
        tekstas4.insert(END, eilutė)


    try:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[4]]
    except:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[4]] = {}
    duomenys = hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[4]]
    tekstas5.delete(0, END)
    for eilutė in duomenys:
        tekstas5.insert(END, eilutė)


    try:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[5]]
    except:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[5]] = {}
    duomenys = hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[5]]
    tekstas6.delete(0, END)
    for eilutė in duomenys:
        tekstas6.insert(END, eilutė)


    try:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[6]]
    except:
        hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[6]] = {}
    duomenys = hash_dienos[metų_skaičius+savaitės_dienos_metų_dienos[6]]
    tekstas7.delete(0, END)
    for eilutė in duomenys:
        tekstas7.insert(END, eilutė)


savaitės_langas.after(0, atnaujinti)
savaitės_langas.mainloop()