import os
import tkinter as tk
from pathlib import Path
from tkinter import ttk
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
import shutil
import re
from tkinter import filedialog
import plotGraph
import os
import subprocess
def buildMatrixPathsList(directory):
    matrici = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            matrici.append(f)
    return matrici

window = tk.Tk()
window.geometry("1900x1000")
window.title("Benvenuto nella GUI di pyLibraryMetodi")
window.configure(background="black")
#colonne con matrici
list=buildMatrixPathsList("dati")
count=0
buttons=[]
buttonsTol=[]
buttonsTests=[]
contMatrix=0
#canvas=Canvas(window, width=500, height=300)
#ig1.createLine(canvas)

def buildTestList():
    list = []
    directory = os.getcwd() + "/tests"
    for file in os.listdir(directory):
        if (str(file) != "__init__.py") & (str(file) != "__pycache__"):
            list.append(file)
    return list

def returnWindow():
    return window

list = buildTestList()
countRow=2
countCol=1
label = tk.Text(width=20, height=1, background="black", foreground="#fff", borderwidth=0, font=('Sans Serif', 13, 'italic bold'))
label.insert("1.0", " Unit Tests selection:")
label.grid(row=1, column=1)
label2 = tk.Text(height=1, background="black", foreground="red", borderwidth=0, font=('Sans Serif', 8, 'italic bold'))
label2.insert("0.0", " (Execution could take several seconds)")
label2.grid(row=2, column=6)
for subd in list:
    stringPath ="python -m  unittest tests."+subd
    countCol=countCol+1
    countRow=2
    buttonsLocal = []
    contMatrix=0
    for file in os.listdir(os.getcwd() + "/tests/" + subd):
        if (str(file) != "__init__.py") & (str(file) != "__pycache__"):
            testName=str(stringPath+"."+file[:-3]+" -v")
            buttonsLocal.append(tk.Button(text=str(file)[:-3], width=20, bg='#5DADE2', command=(lambda testName=testName, file=file: unitTest(testName,file))))
            buttonsLocal[contMatrix].grid(row=countRow, column=countCol)
            countRow = countRow + 1
            contMatrix = contMatrix + 1

def unitTest(nome,file):
    result = subprocess.getoutput(nome)
    print("result::: ", result)

    newWindow = tk.Toplevel(window)
    newWindow.title(str(file)[:-3])

    # sets the geometry of toplevel
    newWindow.geometry("600x400")

    # A Label widget to show in toplevel
    label= Label(newWindow,text=result)
    label.grid(row=1,column=1)



def stampaMatrice(matrice,tol):
    print("TOLLERANZA2")
    print(tol)
    print(type(tol))
    plotGraph.plot(matrice,tol).grid(row=100, column=100)

def choseTol(matrice,riga):
    contTol = 0
    count = 2
    listTol=[10 ** -4, 10 ** -6, 10 ** -8, 10 ** -10]
    for tol in listTol:
        print(tol)
        buttonsTol.append(tk.Button(text=str(tol), width=20, bg='#CCCCFF', command=(lambda tol=tol,matrice=matrice: stampaMatrice(matrice,tol))))
        buttonsTol[contTol].grid(row=riga, column=count)
        count = count + 1
        contTol = contTol + 1

def UploadAction(riga):
    contMatrix = 0
    riga=riga+2
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    shutil.copy(str(filename), str(os.getcwd()) + "/dati")
    for el in buildMatrixPathsList("dati"):
        buttons.append(tk.Button(text=str(el), width=20, bg='#CCCCFF', command= (lambda el=el, rigaTol=rigaTol: choseTol(str(el),8)) ))
        buttons[contMatrix].grid(row=riga+1, column=1)
        riga = riga + 1
        contMatrix = contMatrix + 1

contMatrix=0
label = tk.Text(width=20, height=1, background="black", foreground="#FFFFFF", borderwidth=0, font=('Sans Serif', 9, 'italic bold'))
label.insert("0.0", "Select tolerance")
label.grid(row=countRow+1, column=2)
button1 = tk.Button(window, text='Open', width=20, bg='#000080', fg='#FFFFFF', font=('Sans Serif', 9, 'italic bold'), command=(lambda countRow=countRow: UploadAction(countRow)))
button1.grid(row=(countRow+2),column=1)
countRow=countRow+2
rigaTol=countRow


for el in buildMatrixPathsList("dati"):
    buttons.append(tk.Button(text=str(el), width=20, bg='#CCCCFF', command= (lambda el=el, rigaTol=rigaTol: choseTol(str(el),rigaTol)) ))
    buttons[contMatrix].grid(row=countRow+1, column=1)
    countRow=countRow+1
    contMatrix=contMatrix+1
time.sleep(15)


for bottone in buttons:
    print(bottone['text'])

window.mainloop()