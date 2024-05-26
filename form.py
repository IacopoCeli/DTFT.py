import DTFT
from tkinter import *
import numpy as np;
from tkinter import filedialog
import matplotlib.pyplot as plt

window = Tk()
window.geometry("600x720")
window.title("Discrate Time Fourier Transform")
window.resizable(False, False)

#INPUT DATA
row = 0
title = Label(window, text="Input data", font="Arial 20").grid(row=row,column=2)

#frequencies label
row += 1
fMinLabel = Label(window, text="minimum frequency [Hz]").grid(row=1,column=1)
fResolutionLabel = Label(window, text="resolution [Hz]").grid(row=1, column=2)
fMaxLabel = Label(window, text="maximum frequency [Hz]").grid(row=row,column=3)

#frequencies Entry
row += 1
fMin = Entry(window, font="Arial 12", justify="center")
fMin.grid(row=2, column=1, padx=8)
fMin.insert(index=0, string="0")
fResolution = Entry(window, font="Arial 12", justify="center")
fResolution.grid(row=2, column=2, padx=8)
fResolution.insert(index=0, string="0.25")
fMax = Entry(window, font="Arial 12", justify="center")
fMax.grid(row=2, column=3, padx=8)
fMax.insert(index=0, string="50")

#file selection

def OpenFile():
    fileTypes = (
        ('text files', '*.txt'),
        ('all files', '*.*')
    )
    fileName = filedialog.askopenfilename(title="Open file", initialdir="./", filetypes=fileTypes)
    selectFileLabel.configure(text=fileName, font="Arial 7")

row += 1
selectFileButton = Button(window, text="...", command=OpenFile).grid(row=row, column=1, pady = 10, padx=8, sticky="W")
selectFileLabel = Label(window)
selectFileLabel.grid(row=row, column=1, columnspan=3)

#feature selection
row += 1
features = {"pk-pk" : 4, "0-pk" : 2, "pk-0" : -2, "RMS" : np.power(2,0.5), "N": 1}

_feature = StringVar()
w_H = StringVar()
w_B = StringVar()
w_R = StringVar()
avg = StringVar()

pkpk = Radiobutton(window, text="pk-pk", variable=_feature, value="pk-pk")
pkpk.grid(row=row, column=1, padx=8, sticky="W")

averaging = Checkbutton(window, text="Zero average signal", variable=avg)
averaging.grid(row=row, column=2, padx=8, sticky="W")

row += 1
pk = Radiobutton(window, text="0-pk", variable=_feature, value="0-pk")
pk.grid(row=row, column=1, padx=8, sticky="W")

row += 1
_pk = Radiobutton(window, text="pk-0", variable=_feature, value="pk-0")
_pk.grid(row=row, column=1, padx=8, sticky="W")

rect = Checkbutton(window, text="Rectangular Windowing", variable=w_R)
rect.grid(row=row, column=2, padx=8, sticky="W")

row += 1
RMS = Radiobutton(window, text="RMS", variable=_feature, value="RMS")
RMS.grid(row=row, column=1, padx=8, sticky="W")

hanning = Checkbutton(window, text="Hanning Windowing", variable=w_H)
hanning.grid(row=row, column=2, padx=8, sticky="W")

row += 1
N = Radiobutton(window, text="None", variable=_feature, value="N")
N.grid(row=row, column=1, padx=8, sticky="W")

bartlett = Checkbutton(window, text="Bartlett Windowing", variable=w_B)
bartlett.grid(row=row, column=2, padx=8, sticky="W")

#start process
def execute():

    try:

        #pulisco la textbox
        clear()

        #Scarico tutti i dati dal file selezionato
        signal = [] #lista contenente il segnale campionato
        time = [] #lista contenente gli steps temporali

        filePath = selectFileLabel.cget("text")

        f = open(filePath, "r")
        count = 0

        while(True):
            line = f.readline()
            if(line):
                c = np.longdouble(line[:-1])
                signal.append(c)
                time.append(count)
                count += 1
            else:
                break

        f.close

        if(int(avg.get())):
            signal = DTFT.NoAvreageSeries(signal)

        if(int(w_H.get())):
            signal = DTFT.HanningWindowing(signal)

        if(int(w_B.get())):
            signal = DTFT.BartlettWindowing(signal)

        if(int(w_R.get())):
            signal = DTFT.RectangularWindowing(signal)

        fMinValue = np.longdouble(fMin.get()) #frequenza minima su cui calcolare la DTFT
        fMaxValue = np.longdouble(fMax.get()) #frequenza massima su cui calcolare la DTFT

        step = np.longdouble(fResolution.get()) #risoluzione dello spettro
        if(step <= 0):
            step = 1

        freq = [] #lista contenente le frequenze dei vettori complessi
        mod = [] #lista contenente i moduli dei vettori complessi

        count = np.longdouble(fMinValue) #variabile ausiliaria per il ciclo while
        while(count<=fMaxValue+step): #scorro tutte le frequenza discretizzate per il valore di step
            freq.append(count) #aggiungo alla lista freq la frequenza analizzata alla presente iterazione
            mod.append(DTFT.DiscrateFourierTransform(signal,count)*np.longdouble(features[_feature.get()])) #aggiungo alla lista mod i moduli dei vettori complessi alla frequenza analizzata in questa iterazione
            write(str(np.round(freq[-1],5)) + "\t" + str(mod[-1]), np.longdouble(((count/step)-fMinValue+1))) #stampo a video il risultato
            count += step #incremento la variabile count per l'iterazione successiva

        #stampo i grafici tempo/frequenza del segnale
        fig, (sgn, dft) = plt.subplots(nrows=2, ncols=1)

        f = _feature.get()

        if(f == "N"):
            f = ""

        fig.text(0.0, 0.0, 
                "Maximum peack: " + str(round(max(mod),5)) + " [Amp " + f + "] @ " + str(round(freq[mod.index(max(mod))],5)) + " [Hz] " + "(spectrum resolution " + str(step) + " [Hz])",
                )

        subtitle = ""

        if(int(avg.get())):
            subtitle += "No-AVG"

        if(int(w_H.get())):
            if(subtitle != ""):
                subtitle += ", "
            subtitle += "Hanning windowed"

        if(int(w_B.get())):
            if(subtitle != ""):
                subtitle += ", "
            subtitle += "Bartlett windowed"

        if(int(w_R.get())):
            if(subtitle != ""):
                subtitle += ", "
            subtitle += "Rectangular windowed"

        if(subtitle != ""):
            subtitle = " ( " + subtitle + " )"

        sgn.plot(time, signal, color = "red")
        sgn.set_title("Signal " + subtitle)
        sgn.set_xlabel("time")
        sgn.set_ylabel("Amp")
        sgn.grid(True,"both","both")

        dft.plot(freq, mod, color = "blue")
        dft.set_xlabel("frequency")
        dft.set_ylabel("Amp")
        dft.grid(True,"both","both")

        plt.show()

    except:
        write("Invalid input parameters!", 0.0)

def write(text:str, index:float):
    results.insert(chars=text + "\n", index=np.round(index,1))

def clear():
    results.delete(index1=0.0, index2=END)

row += 1
startButton = Button(window, text="Start process", command=execute).grid(row=row,column=1,pady=10,padx=8,columnspan=4, sticky="W", ipadx=250)

#results
row += 1
title2 = Label(window, text="Results", font="Arial 20").grid(pady = 3, row=row, column=2)

row += 1
results = Text(window, font="Arial 9")
results.grid(row=row, column=1, pady=5, columnspan=4, rowspan=2)

if __name__ == "__main__":
    window.mainloop()