# -*- coding: utf-8 -*-
"""
Created on Sun May 30 20:02:10 2021

@author: Luna
"""

#%% Setup paths
import os
from scipy import fftpack
os.chdir('/home/tian/Desktop/labo4/Grupo5/Practica5/Grupo5/RP')
script_dir = os.path.abspath('/home/tian/Desktop/labo4/Grupo5/RP')
project_dir =  os.path.dirname(os.path.abspath('/home/tian/Desktop/labo4/Grupo5/RP/'))
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

# NUMERO DE ITERACIONES QUE ESTIMAMSO QU E VAA SER EL TIEMPOD DE RRTA
it = 100

#frecuenciaas a setear
frecuencia  = rp.set_freq( 102 ) #PONER LA FRECUENCIAS MAS LINDA

#seteamos el filtro con frec de corte 29
rp.set_lpf(22,order=1 , line='ref' ) 

tau , orden = rp.get_lpf('ref')

# seteamos la amplitud temporal para serciorarnos de que la amplitud que fijemos sea distinta a la que estaba antes
Vmod_out1   = rp.set_modulation_amplitud(1639, ch='out1')
sleep(0.1)

X=[]
Y=[]
t=[]
t0=time()

for i in range(5):
    sleep(0.1)
    x, y = rp.get_XY(units='int') / 8192 #le sacamos el offeset
    t.append(time() - t0)
    X.append(x)
    Y.append(y)
# seteamos la amplitud
Vmod_out1   = rp.set_modulation_amplitud(8190, ch='out1')
#frecuencia  = rp.set_freq( 122 )
for i in range (it):
    sleep(0.1)
    x, y = rp.get_XY(units='int') / 8192 #le sacamos el offeset
    t.append(time() - t0)
    X.append(x)
    Y.append(y)
    
df = pd.DataFrame({'Tiempo': t, 'X': X, 'Y': Y })
df.to_csv(r'data\data_ej_5_a.csv')
#%%
plt.plot(t,X,'.',label='X')
plt.plot(t,Y,'.',label='Y')
#plt.plt
#%%

#AHORA HACEMOS LO MISMO CON EL ORDEN DEL FILTRO CAMBIADO

#seteamos el filtro con frec de corte 29
rp.set_lpf(22,order=2 , line='ref' ) 

tau , orden = rp.get_lpf('ref')

# seteamos la amplitud temporal para serciorarnos de que la amplitud que fijemos sea distinta a la que estaba antes
Vmod_out1   = rp.set_modulation_amplitud(1639, ch='out1')
sleep(0.1)

X=[]
Y=[]
t=[]
t0=time()

for i in range(20):
    x, y = rp.get_XY(units='int') / 8192 #le sacamos el offeset
    t.append(time() - t0)
    X.append(x)
    Y.append(y)
# seteamos la amplitud
Vmod_out1   = rp.set_modulation_amplitud(8190, ch='out1')

for i in range (it):
    x, y = rp.get_XY(units='int') / 8192 #le sacamos el offeset
    t.append(time() - t0)
    X.append(x)
    Y.append(y)
    
df = pd.DataFrame({'Tiempo': t, 'X': X, 'Y': Y })
df.to_csv(r'data\data_ej_5_b.csv')

plt.plot(t,X,'.',label='X')
plt.plot(t,Y,'.',label='Y')
#%%
#AHORA HACEMOS LO MISMO CON FREC CORTE 25
#seteamos el filtro con frec de corte 29
rp.set_lpf(20,order=2 , line='ref' ) 

tau , orden = rp.get_lpf('ref')

# seteamos la amplitud temporal para serciorarnos de que la amplitud que fijemos sea distinta a la que estaba antes
Vmod_out1   = rp.set_modulation_amplitud(1639, ch='out1')
sleep(0.1)

X=[]
Y=[]
t=[]
t0=time()

for i in range(5):
    x, y = rp.get_XY(units='int') / 8192 #le sacamos el offeset
    t.append(time() - t0)
    X.append(x)
    Y.append(y)
# seteamos la amplitud
Vmod_out1   = rp.set_modulation_amplitud(8190, ch='out1')

for i in range (it):
    x, y = rp.get_XY(units='int') / 8192 #le sacamos el offeset
    t.append(time() - t0)
    X.append(x)
    Y.append(y)
    
df = pd.DataFrame({'Tiempo': t, 'X': X, 'Y': Y })
df.to_csv(r'data\data_ej_5_c.csv')


plt.plot(t,X,'.',label='X')
plt.plot(t,Y,'.',label='Y')
#%%
#AHORA HACEMOS LO MISMO CON FREC CORTE 20
#seteamos el filtro con frec de corte 29
rp.set_lpf(26,order=2 , line='ref' ) 

tau , orden = rp.get_lpf('ref')

# seteamos la amplitud temporal para serciorarnos de que la amplitud que fijemos sea distinta a la que estaba antes
Vmod_out1   = rp.set_modulation_amplitud(1639, ch='out1')
sleep(0.1)

X=[]
Y=[]
t=[]
t0=time()

for i in range(5):
    x, y = rp.get_XY(units='int') / 8192 #le sacamos el offeset
    t.append(time() - t0)
    X.append(x)
    Y.append(y)
# seteamos la amplitud
Vmod_out1   = rp.set_modulation_amplitud(8190, ch='out1')

for i in range (it):
    x, y = rp.get_XY(units='int') / 8192 #le sacamos el offeset
    t.append(time() - t0)
    X.append(x)
    Y.append(y)
    
df = pd.DataFrame({'Tiempo': t, 'X': X, 'Y': Y })
df.to_csv(r'data\data_ej_5_d.csv')
