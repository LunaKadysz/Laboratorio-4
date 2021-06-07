#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 10:39:51 2021

@author: kenneths
"""

#%% Setup paths
import os
from scipy import fftpack
os.chdir(r'/home/publico/Desktop/Grupo 5/')
script_dir = os.path.abspath('/home/publico/Desktop/Grupo 5/')
data_dir = os.path.join(script_dir, 'data')


from scipy import signal
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from time import sleep,time
import control_finn
from control_finn import RedPitayaApp, reg_labels

rp = RedPitayaApp('http://rp-f061b6.local/lock_in+pid_harmonic_hf/?type=run', name='rp')
#%%

#frecuencia  = rp.set_freq( 10 )
Vmod_out1   = rp.set_modulation_amplitud(2048, ch='out1')
frecuencias =np.array( np.exp(np.linspace(np.log(1239),np.log(0.0001),20)),dtype='int')

#print(f"Configuramos la frecuencia de modulación en {frecuencia} Hz")
#print(f"A la salida out1 se le suma la modulación con {Vmod_out1} V de amplitud")

#rp.set_lpf(16 , order=1 , line='ref' ) 
#tau , orden = rp.get_lpf('ref')

#print(f"El pasabajos para la democulación de X e Y es de orden {orden} y tiempo característico {tau} seg ")
#print(f"La frecuencia de corte es fc={1/(tau*2*np.pi)} Hz ")


#X_en_ints  = rp.lock.X_28 con esto adquiris directo los datos mas rapido
#X, Y = rp.get_XY()
X=[]
Y=[]


for i in range(10):

    rp.set_lpf(20+i,order=2 , line='ref' ) 
    print(20+i)
    tau , orden = rp.get_lpf('ref')
    X.append([])
    Y.append([])
    for f in frecuencias:
        frec  = rp.set_freq( f )
        sleep(1) 
        x, y = rp.get_XY(units='int') / 8192
        X[i].append(x)
        Y[i].append(y)
    X[i]=np.array(X[i])
    Y[i]=np.array(Y[i])
#%%
for i in range(10):
    plt.semilogx(frecuencias,np.sqrt(X[i]**2+Y[i]**2),'-',label='{}'.format(20 + i))
    plt.xlabel('Frecuencias')
    plt.ylabel('X')
    plt.legend()
#%%

Vmod_out1   = rp.set_modulation_amplitud(4048, ch='out1')

frecuencias =np.array( np.exp(np.linspace(np.log(1239),np.log(0.0001),100)),dtype='int')
frecss=[]
for i,f in enumerate(frecuencias):
    if i<len(frecuencias)-1:
        if frecuencias[i+1] != frecuencias[i]:
            frecss.append(frecuencias[i])

frecuencias=np.array(frecss)

X=[]
Y=[]
for i in range(10):

    rp.set_lpf(20+i,order=2 , line='ref' ) 
    print(20+i)
    tau , orden = rp.get_lpf('ref')
    X.append([])
    Y.append([])
    for f in frecuencias:
        frec  = rp.set_freq( f )
        sleep(1) 
        x, y = rp.get_XY(units='int') / 8192
        X[i].append(x)
        Y[i].append(y)
    X[i]=np.array(X[i])
    Y[i]=np.array(Y[i])

#%%   
for i in range(10):
    plt.semilogx(frecuencias,X[i]**2+Y[i]**2,'-',label='{}'.format(20 + i))
    plt.xlabel('Frecuencias')
    plt.ylabel('X')
    plt.legend()
    
#%%
for i in range(10):
    df = pd.DataFrame({'frecs': frecuencias, 'X': X[i], 'Y': Y[i]})
    df.to_csv(r'data/FCandFRECS/{}.csv'.format(i))

#%%
Amps=np.linspace(0,8190,200)
rp.set_lpf(22,order=2 , line='ref' ) 
frec  = rp.set_freq( 38 )
tau , orden = rp.get_lpf('ref')
sleep(1) 
Xa=[]
Ya=[]
for a in Amps:
    Vmod_out1   = rp.set_modulation_amplitud(a, ch='out1')
    sleep(1)
    x, y = rp.get_XY(units='int') / 8192
    Xa.append(x)
    Ya.append(y)
Xa=np.array(Xa)
Ya=np.array(Ya)
#%%
plt.plot(Amps,Xa)
df = pd.DataFrame({'amp': Amps, 'X': Xa, 'Y': Ya})
df.to_csv(r'data/Amps.csv')
#%%
Vmod_out1   = rp.set_modulation_amplitud(8190, ch='out1')
sleep(30)

X=[]
Y=[]

rp.set_lpf(22,order=2 , line='ref' )
tau , orden = rp.get_lpf('ref')
for f in frecuencias:
    frec  = rp.set_freq( f )
    sleep(1) 
    x, y = rp.get_XY(units='int') / 8192
    X.append(x)
    Y.append(y)

X=np.array(X)
Y=np.array(Y)
#%%
Vmod_out1   = rp.set_modulation_amplitud(-1, ch='out1')
sleep(30)

X=[]
Y=[]
R=[]
ph=[]

rp.set_lpf(22,order=2 , line='ref' )
tau , orden = rp.get_lpf('ref')
for f in frecuencias:
    frec  = rp.set_freq( f )
    sleep(1) 
    Xs=[]
    Ys=[]
    for l in range(100):
        x, y = rp.get_XY(units='int') / 8192
        Xs.append(x)
        Ys.append(y)
    Xs=np.array(Xs)
    Ys=np.array(Ys)
    X.append(np.std(Xs))
    Y.append(np.std(Ys))
    R.append(np.std(np.sqrt(Xs**2+Ys**2)))
    ph.append(np.std(np.arctan(Ys/Xs)))

X=np.array(X)
Y=np.array(Y)
R=np.array(R)
ph=np.array(ph)