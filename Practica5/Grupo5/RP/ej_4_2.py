# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:37:13 2021

@author: Luna
"""

#%% Setup paths
import os
from scipy import fftpack
os.chdir(r'/home/tian/Desktop/labo4/Grupo5/Practica5/Grupo5/RP')
script_dir = os.path.abspath('/home/tian/Desktop/labo4/Grupo5/RP')
project_dir =  os.path.dirname(os.path.abspath('/home/tian/Desktop/labo4/Grupo5/RP'))
data_dir = os.path.join(project_dir, 'data')
#%%

from scipy import signal
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from time import sleep,time
import control_finn
from control_finn import RedPitayaApp, reg_labels

rp = RedPitayaApp('http://10.200.1.240/lock_in+pid_harmonic/?type=run', name='rp')


#%%
#frecuenciaas a setear
frecuencias =np.array( np.exp(np.linspace(np.log(1239),np.log(0.0001),500)),dtype='int')

# seteamos la amplitud
Vmod_out1   = rp.set_modulation_amplitud(8190, ch='out1')
sleep(1)
#seteamos el filtro con frec de corte 29
#%%
for i in range(10):

    rp.set_lpf(20+i,order=2 , line='ref' ) 
    print(20+i)
    tau , orden = rp.get_lpf('ref')
    X=[]
    Y = []

    for f in frecuencias:
        frec  = rp.set_freq( f )
        sleep(1) 
        x, y = rp.get_XY(units='int') / 8192
        X.append(x)
        Y.append(y)
    X=np.array(X)
    Y=np.array(Y)

    df=pd.DataFrame({'frec': frecuencias, 'X': X, 'Y': Y})
    df.to_csv(r'data/data4frecs/{}.csv'.format(20+i))

    plt.semilogx(frecuencias,X,'-',label='{}'.format(20 + i))
    plt.xlabel('Frecuencias')
    plt.ylabel('X')
    plt.legend()
#%%
#frecuenciaas a setear
frecuencias =np.array( np.exp(np.linspace(np.log(1239),np.log(0.0001),15)),dtype='int')

# seteamos la amplitud
Vmod_out1   = rp.set_modulation_amplitud(8190, ch='out1')
sleep(1)
#seteamos el filtro con frec de corte 29

%matplotlib qt
col=['m','r','g','b']

for i in range(4):

    rp.set_lpf(20+i*3,order=2 , line='ref' ) 
    print(20+i*3)
    tau , orden = rp.get_lpf('ref')
    X=[]
    Y = []

    for f in frecuencias:
        frec  = rp.set_freq( f )
        sleep(1) 
        x, y = rp.get_XY(units='int') / 8192
        X.append(x)
        Y.append(y)
    X=np.array(X)
    Y=np.array(Y)

    #f = pd.DataFrame({'frec': frecuencias, 'X': X, 'Y': Y})
    #df.to_csv(r'data/data_ej_4_a.csv')

    plt.semilogx(frecuencias,X,'{}-'.format(col[i]),label='señal {}'.format(i*3))
    plt.legend()
    
Vmod_out1   = rp.set_modulation_amplitud(-1, ch='out1')
sleep(1)
for i in range(4):    
    
    rp.set_lpf(20+i*3,order=2 , line='ref' ) 
    print(20+i*3)
    tau , orden = rp.get_lpf('ref')
    
    X1=[]
    Y1 = []

    for f in frecuencias:
        frec  = rp.set_freq( f )
        sleep(1) 
        x, y = rp.get_XY(units='int') / 8192
        X1.append(x)
        Y1.append(y)
    X1=np.array(X1)
    Y1=np.array(Y1)

    #f = pd.DataFrame({'frec': frecuencias, 'X': X, 'Y': Y})
    #df.to_csv(r'data/data_ej_4_a.csv')

    plt.semilogx(frecuencias,X1,'{}.'.format(col[i]),label='ruido{}'.format(i*3))
    plt.legend()
#%%
Vmod_out1   = rp.set_modulation_amplitud(-1, ch='out1')
rp.set_lpf(20+5,order=2 , line='ref' )
print(21+5)
tau , orden = rp.get_lpf('ref')


X=[]
Y = []

for f in frecuencias:
    frec  = rp.set_freq( f )
    sleep(1) 
    x, y = rp.get_XY(units='int') / 8192
    X.append(x)
    Y.append(y)
X=np.array(X)
Y=np.array(Y)
#f = pd.DataFrame({'frec': frecuencias, 'X': X, 'Y': Y})
#df.to_csv(r'data/data_ej_4_a.csv')
plt.semilogx(frecuencias,X,'-',label='ruido {}'.format(5))
plt.legend()

Vmod_out1   = rp.set_modulation_amplitud(8190, ch='out1')
rp.set_lpf(20+5,order=2 , line='ref' )
print(21+5)
tau , orden = rp.get_lpf('ref')


X=[]
Y = []

for f in frecuencias:
    frec  = rp.set_freq( f )
    sleep(1) 
    x, y = rp.get_XY(units='int') / 8192
    X.append(x)
    Y.append(y)
X=np.array(X)
Y=np.array(Y)


plt.semilogx(frecuencias,X,'-',label='señal {}'.format(5))
plt.legend()




#%%
#en el grafico elegimos la frecuencia optima
#con esa frecuencia la fijamos y agarramos la amplitud

frecuencia = rp.set_freq( 102 ) #NVENTO ACA PONEMOS LA FRECUENCIA IDEAL. HACERLO EN EL EJ 5 TAMBIEN

rp.set_lpf(25,order=2 , line='ref' ) 

tau , orden = rp.get_lpf('ref')

amplitudes = np.linspace(691,8190,1000,dtype='int')

X=[]
Y = []

for a in amplitudes:
    amp = rp.set_modulation_amplitud(a, ch='out1')
    sleep(1) 
    x, y = rp.get_XY(units='int') / 8192
    X.append(x)
    Y.append(y)
    
X=np.array(X)
Y=np.array(Y)

#df = pd.DataFrame({'amp': amplitudes, 'X': X, 'Y': Y})
#df.to_csv(r'data/data_ej_4_b.csv')
#%%
#plt.plot(amplitudes,np.sqrt(X**2+y**2)/amplitudes,'.',label='X')
#%%
#df = pd.DataFrame({'amp': amplitudes, 'X': X, 'Y': Y})
#df.to_csv(r'data/data4TRANSF.csv')
#%%

#frecuenciaas a setear
frecuencias =np.array( np.exp(np.linspace(np.log(1239),np.log(0.0001),500)),dtype='int')
frecss=[]
for i,f in enumerate(frecuencias):
    if i<len(frecuencias)-1:
        if frecuencias[i+1] != frecuencias[i]:
            frecss.append(frecuencias[i])

frecss=np.array(frecss)
#%%
# seteamos la amplitud
Vmod_out1   = rp.set_modulation_amplitud(8190, ch='out1')
#seteamos el filtro con frec de corte 29
rp.set_lpf(25,order=2 , line='ref' ) 
tau , orden = rp.get_lpf('ref')
sleep(1)


X=[]
Y = []
R = []

for f in frecss:
    print(f)
    frec  = rp.set_freq( f )
    sleep(1)
    Xs=[]
    Ys=[]
    for i in range(100):
        x, y = rp.get_XY(units='int') / 8192
        Xs.append(x)
        Ys.append(y)
    Xs=np.array(Xs)
    Ys=np.array(Ys)
    
    X.append(np.std(Xs))
    Y.append(np.std(Ys))
    R.append(np.std(np.sqrt(Xs**2+Ys**2)))

X=np.array(X)
Y=np.array(Y)
R=np.array(R)
#f = pd.DataFrame({'frec': frecuencias, 'X': X, 'Y': Y})
#df.to_csv(r'data/data_ej_4_a.csv')
#%%
plt.semilogx(frecss,X,'.',label='señal')
plt.legend()
#%%
#df = pd.DataFrame({'frec': frecss, 'X': X, 'Y': Y, 'R': R})
#df.to_csv(r'data/data4RuidoFrecs.csv')
#%%

X=[]
Y = []
R = []

frecuencia = rp.set_freq( 102 ) #NVENTO ACA PONEMOS LA FRECUENCIA IDEAL. HACERLO EN EL EJ 5 TAMBIEN

rp.set_lpf(25,order=2 , line='ref' ) 

tau , orden = rp.get_lpf('ref')

amplitudes = np.linspace(691,8190,100,dtype='int')

for a in amplitudes:
    amp = rp.set_modulation_amplitud(a, ch='out1')
    print(a)
    sleep(1)
    Xs=[]
    Ys=[]
    for i in range(100):
        x, y = rp.get_XY(units='int') / 8192
        Xs.append(x)
        Ys.append(y)
    Xs=np.array(Xs)
    Ys=np.array(Ys)
    
    X.append(np.std(Xs))
    Y.append(np.std(Ys))
    R.append(np.std(np.sqrt(Xs**2+Ys**2)))

X=np.array(X)
Y=np.array(Y)
R=np.array(R)
#df = pd.DataFrame({'amp': amplitudes, 'X': X, 'Y': Y})
#df.to_csv(r'data/data_ej_4_b.csv')
#%%
plt.plot(amplitudes,X/amplitudes,'.',label='X')
#%%
df = pd.DataFrame({'amp': amplitudes, 'X': X, 'Y': Y, 'R': R})
df.to_csv(r'data/data4RuidoAmps.csv')