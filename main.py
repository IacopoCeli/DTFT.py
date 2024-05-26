import DTFT
import numpy as np;
import matplotlib.pyplot as plt

DTFT.SayHello()

features = {"pk-pk" : 4, "0-pk" : 2, "pk-0" : -2, "RMS" : np.power(2,0.5), "None": 1}
selectedFeature = "0-pk"

signal = [] #lista contenente il segnale campionato
time = [] #lista contenente gli steps temporali

fMin = 0 #frequenza minima su cui calcolare la DTFT
fMax = 50 #frequenza massima su cui calcolare la DTFT
step = 0.5 #risoluzione dello spettro

freq = [] #lista contenente le frequenze dei vettori complessi
mod = [] #lista contenente i moduli dei vettori complessi

#-----------------------------------------------------------------------------------------------
#                                   SIGNALS EXAMPLE
#
#   - SIN_1_10.txt          ->      funzione seno di ampiezza 1 frequenza 1Hz campionata a 10Hz
#   - SIN_1_1000.txt        ->      funzione seno di ampiezza 1 frequenza 1Hz campionata a 1kHz
#   - SGN1_1_2000.txt       ->      funzione campionata a 2kHz composta dalla somma dei seguenti segnali ([w/f] = 2 * pi):
#                                   - 10 SIN([w/f] * t)
#                                   - 8 SIN(4 * [w/f] * t)
#                                   - 6 SIN(8 * [w/f] * t)
#                                   - 4 SIN(16 * [w/f] * t)
#                                   - 2 SIN(32 * [w/f] * t)
#   - SGN2(N)_100_20000.txt ->      funzione campionata a 20kHz composta dalla somma dei seguenti segnali ([w/f] = 2 * pi)
#                                   - 2 SIN(100 * [w/f] * t)
#                                   - 4 COS(200 * [w/f] * t)
#                                   - 6 COS(300 * [w/f] * t)
#                                   - 8 SIN(400 * [w/f] * t)
#                                   - random noise        
#   - STP_1_1000.txt        ->      funzione step di ampiezza 1 frequenza 1Hz campionata a 1kHz
#   - SGN_1_1000.txt        ->      funzione segno di ampiezza 1 frequenza 1Hz capionata a 1kHz
#   - SAW_2_1000.txt        ->      funzione dente di sega di ampiezza 10 freqenza 2Hz campionata a 1kHz
#   - COS_10_10000.txt      ->      funzione coseno di ampiezza 1 frequenza 10Hz campionata a 10kHz
#   - COS(N)_10_10000.txt   ->      funzione coseno (con disturbi) di ampiezza 1 frequenza 10Hz campionata a 10kHz
#
#-----------------------------------------------------------------------------------------------
filePath = "2991898 - TK complete waveform 18-00-29.txt"

f = open(filePath, "r")
count = 0

while(True):
    line = f.readline()
    if(line):
        signal.append(float(line))
        time.append(count)
        count += 1
    else:
        break

f.close

count = fMin #variabile ausiliaria per il ciclo while
while(count<=fMax): #scorro tutte le frequenza discretizzate per il valore di step
    freq.append(count*(1)) #aggiungo alla lista freq la frequenza analizzata alla presente iterazione
    mod.append(DTFT.DiscrateFourierTransform(signal,count)*features[selectedFeature]) #aggiungo alla lista mod i moduli dei vettori complessi alla frequenza analizzata in questa iterazione
    print(str(count) + ") " + str(mod[-1])) #stampo a video il risultato
    count += step #incremento la variabile count per l'iterazione successiva

#Stampo le principali informazioni di interesse
print("Picco massimo di ampiezza: " + str(round(max(mod),3)) + " Amp alla frequenza di: " + str(round(freq[mod.index(max(mod))],3)) + " Hz")

#stampo i grafici tempo/frequenza del segnale
fig, (sgn, dft) = plt.subplots(nrows=2, ncols=1)

sgn.plot(time, signal, color = "red")
sgn.set_title("Signal")
sgn.set_xlabel("time")
sgn.set_ylabel("Amp")
sgn.grid(True,"both","both")

dft.plot(freq, mod, color = "blue")
#dft.set_title("DTFT")
dft.set_xlabel("frequency")
dft.set_ylabel("Amp")
dft.grid(True,"both","both")

plt.show()