import numpy as np;
import cmath;

#-----------------------------------------------------------------------------------------------
#
#       Author:         Iacopo Celi
#       Creation date:  2023-03-31
#       Parameters:     Nothing
#       Description:    Funzione che restituisce la versione della libreria.
#
#-----------------------------------------------------------------------------------------------
def SayHello():
    print("Hi! I'm DTFT version 1.0.0")

#-----------------------------------------------------------------------------------------------
#
#       Author:         Iacopo Celi
#       Creation date:  2023-03-31
#       Parameters:     (1) series:List -> Serie numerica
#       Description:    Funzione che data in input una serie restituisce la stessa serie a media nulla.
#
#-----------------------------------------------------------------------------------------------
def NoAvreageSeries(series:list):
    try:
        average = (sum(series) / len(series))

        for index in range(0, len(series)):
            series[index] -= average

        return series

    except:
        return None

#-----------------------------------------------------------------------------------------------
#
#       Author:         Iacopo Celi
#       Creation date:  2023-04-09
#       Parameters:     (1) series:List -> Serie numerica
#       Description:    Funzione che data in input una serie restituisce la stessa serie finestrata con Hanning.
#
#-----------------------------------------------------------------------------------------------
def HanningWindowing(series:list):
    try:
        series *= np.hanning(len(series))
        return series
    except:
        return None
    
#-----------------------------------------------------------------------------------------------
#
#       Author:         Iacopo Celi
#       Creation date:  2023-04-09
#       Parameters:     (1) series:List -> Serie numerica
#       Description:    Funzione che data in input una serie restituisce la stessa serie finestrata con Blackman.
#
#-----------------------------------------------------------------------------------------------
def BartlettWindowing(series:list):
    try:
        series *= np.bartlett(len(series))
        return series
    except:
        return None
    
#-----------------------------------------------------------------------------------------------
#
#       Author:         Iacopo Celi
#       Creation date:  2023-04-09
#       Parameters:     (1) series:List -> Serie numerica
#       Description:    Funzione che data in input una serie restituisce la stessa serie finestrata con Blackman.
#
#-----------------------------------------------------------------------------------------------
def RectangularWindowing(series:list):
    try:
        series[0] = 0
        series[-1] = 0
        return series
    except:
        return None

#-----------------------------------------------------------------------------------------------
#
#       Author:         Iacopo Celi
#       Creation date:  2023-03-31
#       Parameters:     (1) series:List -> Serie numerica
#                       (2) frequency:float -> frequenza dell'armonica di cui siamo interessati
#       Description:    Funzione che dato in input una serie numerica e una frequenza restituisce il modulo del vettore
#                       complesso rappresentante l'armonica alla frequenza specificata.
#
#-----------------------------------------------------------------------------------------------
def DiscrateFourierTransform(series:list, frequency:float):

    w = 2 * np.pi * np.abs(frequency)
    x = series
    T = (1/len(x))

    DTFT = 0
    for n in range(0,len(series)):
        DTFT += x[n] * np.exp(complex(0,(-1 * w * n * T))) * T

    return cmath.polar(DTFT)[0]
