# -*- coding: utf-8 -*-
"""
Created on Fri May 28 07:41:49 2021

"""

#%% Setup paths
import os
script_dir = os.path.abspath('/home/tian/Desktop/labo4/Grupo5/RP')
project_dir =  os.path.dirname(os.path.abspath('/home/tian/Desktop/labo4/Grupo5/RP/'))
data_dir = os.path.join(project_dir, 'data')
#%%

import numpy as np
from matplotlib import pyplot as plt
from time import sleep,time
import control_finn
from control_finn import RedPitayaApp, reg_labels

rp = RedPitayaApp('http://10.200.1.240/lock_in+pid_harmonic/?type=run', name='rp')


#%%
#frecuenciaas a setear
frecuencias = np.linspace(290,310,100)

# seteamos la amplitud
Vmod_out1   = rp.set_modulation_amplitud( 1639, ch='out1')

print(f"Configuramos la frecuencia de modulación en {frecuencia} Hz")
print(f"A la salida out1 se le suma la modulación con {Vmod_out1} V de amplitud")

#seteamos el filtro con frec de corte 29
rp.set_lpf(29,order=2 , line='ref' ) 

tau , orden = rp.get_lpf('ref')

print(f"El pasabajos para la democulación de X e Y es de orden {orden} y tiempo característico {tau} seg ")
print(f"La frecuencia de corte es fc={1/(tau*2*np.pi)} Hz ")



X=[]
Y=[]
'

for f in frecuencias:
    frec  = rp.set_freq( f )
    sleep(0.01) 
    x, y = rp.get_XY(units='int') / 8192
    X.append(x)
    Y.append(y)
    
X=np.array(X)
Y=np.array(Y)

df = pd.dataframe({'frec': frecuencias, 'X': X, 'Y': Y})
df.to_csv(r'data/data_ej_2.csv')

plt.plot(frecuencias,X,label='X')
plt.plot(frecuencias,Y,label='Y')