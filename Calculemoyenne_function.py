import tkinter as tk

def calculeMoyenne(Algo, Python, Php, Javascript):
    """_summary_

    Args:
        Algo (_int_): _Note de l'étudiant en Algoritme_
        Python (_int_): _Note de l'étudiant en Python_
        Php (_int_): _Note de l'étudiant en PHP_
        Javascript (_int_): _Note de l'étudiant en Java_

    Returns:
        _type_: _description_
    """
    Moyenne = (Python + Algo + Php + Javascript) / 4
    return Moyenne  

def Boutton_click():
    Py = float(txtpy.get("1.0", "end-1c"))
    Al = float(txtAl.get("1.0", "end-1c"))
    Ph = float(txtPh.get("1.0", "end-1c"))
    Java = float(txtJava.get("1.0", "end-1c"))

    moy = calculeMoyenne(Al, Py, Ph, Java)
    moyenne_label.config(text="La moyenne de l'étudiant est : {:.2f}".format(moy))
    if moy<10 : 
        mention_label.config(text="Mention= Recalé")
    elif moy>10 and moy<=12 :
        mention_label.config(text="Mention= Passable")
    elif moy>12 and moy<=14 :
        mention_label.config(text="Mention= Assez-Bien")
    elif moy>14 and moy<=16 :
        mention_label.config(text="Mention= Bien")
    elif moy>16:
        mention_label.config(text="Mention= Très-bien")  
         
Menu1 = tk.Tk()
Menu1.maxsize
Titre = tk.Label(Menu1, text="LOGICIEL DE CALCULE DE MOYENNE")
Titre.pack()
Titre.config(bg="blue", fg="white", font=("Arial", 24))

Myframe = tk.Frame(Menu1)
Myframe.pack()

labpy = tk.Label(Myframe, text="SAISIR LA NOTE DE PYTHON :")
labpy.pack()
txtpy = tk.Text(Myframe, width=20, height=1.5)
txtpy.pack()

labAl = tk.Label(Myframe, text="SAISIR LA NOTE D'ALGO :")
labAl.pack()
txtAl = tk.Text(Myframe, width=20, height=1.5)
txtAl.pack()

labPh = tk.Label(Myframe, text="SAISIR LA NOTE DE PHP :")
labPh.pack()
txtPh = tk.Text(Myframe, width=20, height=1.5)
txtPh.pack()

labJava = tk.Label(Myframe, text="SAISIR LA NOTE DE JAVA :")
labJava.pack()
txtJava = tk.Text(Myframe, width=20, height=1.5)
txtJava.pack()

BoutonAccepte = tk.Button(Myframe, text="Calculer la moyenne", command=Boutton_click)
BoutonAccepte.pack()

moyenne_label = tk.Label(Menu1, text="")
moyenne_label.pack()
mention_label = tk.Label(Menu1, text="")
mention_label.pack()

Menu1.mainloop()


