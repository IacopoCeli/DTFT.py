import numpy as np

def function(t:np.longdouble):
    return np.longdouble(10 * np.cos(5.10*2*np.pi*t))

samplingRate:int = 1200
step:np.longdouble = 1/samplingRate
count:np.longdouble = 0
sgn:str = ""

freq = 10.1723
w = 2 * np.pi * freq
x = []
for i in range(0,samplingRate):
    x.append(np.longdouble(w*i*step))

#freq = 14.597
#w = 2 * np.pi * freq
#y=[]
#for i in range(0,samplingRate):
#    y.append(np.longdouble(w*i*step))

sgn = np.cos(x) #+ 20 * np.sin(y)

s = ""
for i in sgn:
    s += str(i) + "\n"

s = s[0:-1]

f = open("sgn.txt", "w")
f.write(s)
f.close