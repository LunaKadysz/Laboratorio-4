# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:37:13 2021

@author: Luna
"""

#%% Setup paths
import os
from scipy import fftpack
script_dir = os.path.abspath('/home/tian/Desktop/labo4/Grupo5/RP')
project_dir =  os.path.dirname(os.path.abspath('/home/tian/Desktop/labo4/Grupo5/RP/'))
data_dir = os.path.join(project_dir, 'data')
#%%

from scipy import signal
import numpy as np
from matplotlib import pyplot as plt
from time import sleep,time
import control_finn
from control_finn import RedPitayaApp, reg_labels

rp = RedPitayaApp('http://10.200.1.240/lock_in+pid_harmonic/?type=run', name='rp')


#%%
#frecuenciaas a setear
frecuencias = np.linspace(np.e**2000,np.e**0,15)

# seteamos la amplitud
Vmod_out1   = rp.set_modulation_amplitud(8190, ch='out1')

#seteamos el filtro con frec de corte 29
rp.set_lpf(29,order=2 , line='ref' ) 

tau , orden = rp.get_lpf('ref')


X=[]
Y = []

for f in frecuencias:
    frec  = rp.set_freq( f )
    sleep(0.01) 
    x, y = rp.get_XY(units='int') / 8192
    X.append(x)
    Y.append(y)
    
X=np.array(X)
Y=np.array(Y)

df = pd.dataframe({'frec': frecuencias, 'X': X, 'Y': Y})
df.to_csv(r'data/data_ej_4_a.csv')

plt.plot(frecuencias,X/Vmod_out1,label='X')


#en el grafico elegimos la frecuencia optima
#con esa frecuencia la fijamos y agarramos la amplitud

frecuencia = rp.set_freq( 619 ) #NVENTO ACA PONEMOS LA FRECUENCIA IDEAL. HACERLO EN EL EJ 5 TAMBIEN

amplitudes = np.linspace(1639,8190,100)

X=[]
Y = []

for a in amplitudes:
    amp = rp.set_modulation_amplitud(a, ch='out1')
    sleep(0.01) 
    x, y = rp.get_XY(units='int') / 8192
    X.append(x)
    Y.append(y)
    
X=np.array(X)
Y=np.array(Y)

df = pd.dataframe({'amp': amplitudes, 'X': X, 'Y': Y})
df.to_csv(r'data/data_ej_4_b.csv')

plt.plot(amplitudes,X/amplitudes,label='X')



