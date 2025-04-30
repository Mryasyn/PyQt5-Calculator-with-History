from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from pickle import load , dump


def pgcd(A,B):
    while A != B:
        if A > B:
            A = A-B
        else:
            B = B-A
    return A

def ppcm(A,B):
    C = A
    while A%B != 0:
        A = A+C
    return A

def puis(A,B):
    return int(A)**int(B)

def calculer():
    A = w.le1.text()
    B = w.le2.text()
    sl = w.cbx.currentText()
    Bin = w.r1.isChecked()
    Oct = w.r2.isChecked()
    Dec = w.r3.isChecked()
    Hex = w.r4.isChecked()
    if A == "" or not A.isdecimal():
        QMessageBox.critical(w,"Erreur","A doit etre non Vide et Numerique")
        return
    elif B == "" or not B.isdecimal():
        QMessageBox.critical(w,"Erreur","B doit etre non Vide et Numerique")
        return
    elif not(Bin or Oct or Dec or Hex):
        QMessageBox.critical(w,"Erreur","Selecter la Base")
        return 
    else:
        e = dict(A = int() , B = int() , Base = str , ResO = int())
        e["A"] = int(A)
        e["B"] = int(B)
        if Bin:
            e["Base"] = "Bin"
        elif Oct:
            e["Base"] = "Oct"
        elif Dec:
            e["Base"] = "Dec"
        else:
            e["Base"] = "Hex"
        
        if sl == "PGCD(A, B)":
            e["ResO"] = pgcd(e["A"],e["B"])
            f = open("pgcd.dat","ab")
            dump(e,f)
            f.close()
        elif sl == "PPCM(A, B)":
            e["ResO"] = ppcm(e["A"],e["B"])
            f1 = open("ppcm.dat","ab")
            dump(e,f1)
            f1.close()
        else:
            e["ResO"] = puis(e["A"],e["B"])
            f2 = open("puiss.dat","ab")
            dump(e,f2)
            f2.close()
     
def tpgcd():
    try:
        f = open("pgcd.dat","rb")
        i = 0
        eof = False
        while not eof:
            try:
                e = load(f)
                w.tw1.insertRow(i)
                w.tw1.setItem(i , 0 , QTableWidgetItem(str(e['A'])))
                w.tw1.setItem(i , 1 , QTableWidgetItem(str(e['B'])))
                w.tw1.setItem(i , 2 , QTableWidgetItem(str(e['Base'])))
                w.tw1.setItem(i , 3 , QTableWidgetItem(str(e['ResO'])))
                i += 1
            except:
                eof = True
        f.close()
    except:
        QMessageBox.critical(w,"ErrorFile","Fichier introuvable!")

def tppcm():
    try:
        f = open("ppcm.dat","rb")
        i = 0
        eof = False
        while not eof:
            try:
                e = load(f)
                w.tw2.insertRow(i)
                w.tw2.setItem(i , 0 , QTableWidgetItem(str(e['A'])))
                w.tw2.setItem(i , 1 , QTableWidgetItem(str(e['B'])))
                w.tw2.setItem(i , 2 , QTableWidgetItem(str(e['Base'])))
                w.tw2.setItem(i , 3 , QTableWidgetItem(str(e['ResO'])))
                i += 1
            except:
                eof = True
        f.close()
    except:
        QMessageBox.critical(w,"ErrorFile","Fichier introuvable!")
    
def tpuis():
    try:
        f = open("puiss.dat","rb")
        i = 0
        eof = False
        while not eof:
            try:
                e = load(f)
                w.tw3.insertRow(i)
                w.tw3.setItem(i , 0 , QTableWidgetItem(str(e['A'])))
                w.tw3.setItem(i , 1 , QTableWidgetItem(str(e['B'])))
                w.tw3.setItem(i , 2 , QTableWidgetItem(str(e['Base'])))
                w.tw3.setItem(i , 3 , QTableWidgetItem(str(e['ResO'])))
                i += 1
            except:
                eof = True
        f.close()
    except:
        QMessageBox.critical(w,"ErrorFile","Fichier introuvable!")

def stat():
    nbpg = 0
    nbpp = 0
    nbpu = 0
    
    try:
        f = open("pgcd.dat","rb")
        eof = False
        while not eof:
            try:
                e = load(f)
                nbpg +=1
            except:
                eof = True
        f.close()
                
        f1 = open("ppcm.dat","rb")
        eof = False
        while not eof:
            try:
                e = load(f1)
                nbpp +=1
            except:
                eof = True
        f1.close()

        f2 = open("puiss.dat","rb")    
        eof = False
        while not eof:
            try:
                e = load(f2)
                nbpu +=1
            except:
                eof = True
        f2.close()
    except:
        QMessageBox.critical(w,"ErrorFile","Fichier puiss.dat introuvable!")
    total = nbpg + nbpp + nbpu
    if total == 0:
        QMessageBox.information(w, "Information", "Aucune opération enregistrée.")
        
    else:
        w.tw4.setRowCount(3)
        
        w.tw4.setItem(0 , 0 , QTableWidgetItem(str("PGCD")))
        w.tw4.setItem(0 , 1 , QTableWidgetItem(str(nbpg)))
        w.tw4.setItem(0 , 2 , QTableWidgetItem(f"{(nbpg/total) * 100:.2f}%"))

        w.tw4.setItem(1 , 0 , QTableWidgetItem(str("PPCM")))
        w.tw4.setItem(1 , 1 , QTableWidgetItem(str(nbpp)))
        w.tw4.setItem(1 , 2 , QTableWidgetItem(f"{(nbpp/total) * 100:.2f}%"))

        w.tw4.setItem(2 , 0 , QTableWidgetItem(str("PUISSANCE")))
        w.tw4.setItem(2 , 1 , QTableWidgetItem(str(nbpu)))
        w.tw4.setItem(2 , 2 , QTableWidgetItem(f"{(nbpu/total) * 100:.2f}%"))
        

app = QApplication([])
w = loadUi("sujet7.ui")
w.show()
                      
w.b1.clicked.connect(calculer)
w.b2.clicked.connect(tpgcd)
w.b3.clicked.connect(tppcm)
w.b4.clicked.connect(tpuis)
w.b5.clicked.connect(stat)
                      
app.exec_()