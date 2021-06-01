# -*- coding: utf-8 -*-
"""
Created on Fri May 28 07:51:46 2021

"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 28 07:41:49 2021

"""

#%% Setup paths
import os
from scipy import fftpack
os.chdir('/home/tian/Desktop/labo4/Grupo5/Practica5/Grupo5/RP')
#%%
import pandas as pd
from scipy import signal
import numpy as np
from matplotlib import pyplot as plt
from time import sleep,time
import control_finn
from control_finn import RedPitayaApp, reg_labels

rp = RedPitayaApp('http://10.200.1.240/lock_in+pid_harmonic/?type=run', name='rp')


#%%
#frecuenciaas a setear
frecuencias = np.linspace(1235,990,15,dtype=int)

# seteamos la amplitud
Vmod_out1   = rp.set_modulation_amplitud( 8190, ch='out1')

print(f"Configuramos la frecuencia de modulación entre {frecuencias[0]} Hz y {frecuencias[-1]}")
print(f"A la salida out1 se le suma la modulación con {Vmod_out1} V de amplitud")

#seteamos el filtro con frec de corte 29
rp.set_lpf(20,order=2 , line='ref' ) 

tau , orden = rp.get_lpf('ref')

print(f"El pasabajos para la democulación de X e Y es de orden {orden} y tiempo característico {tau} seg ")
print(f"La frecuencia de corte es fc={1/(tau*2*np.pi)} Hz ")

t0=time()
tiempos = np.linspace(0,5,50)

Fs = 1/tiempos[1]  
        
def MakeSpectral(y, Fs):
    
    yfft = fftpack.fft(y)
    N = len(y)
    xf = np.linspace(0, Fs/2, int(N/2))
    yf = 2.0/N * np.abs(yfft[:N//2])
    #print(PosicionPicos)
    #print(IntensidadPicos)
#    VectorFrecuenciaPicos = [xf[i] for i in PosicionPicos]
    return xf, yf

X={f: [] for f in frecuencias}
Y={f: [] for f in frecuencias}
FFT = {f: {'frec': [], 'fft': []} for f in frecuencias}

for f in frecuencias:
    frec  = rp.set_freq( f )
    for t in tiempos:
        sleep(0.10204082) 
        x, y = rp.get_XY(units='int') / 8192
        X[f].append(x)
        Y[f].append(y)
    frec,fft = MakeSpectral(X[f], Fs)
    FFT[f]['frec'].append(frec)
    FFT[f]['fft'].append(fft)
    
    
    
plt.figure()
for f in frecuencias:
    x = np.transpose(FFT[f]['frec'])
    y = np.transpose(FFT[f]['fft'])
    plt.plot(x,y,label=f'Frecuencia {f}')
plt.xlim([0,5])   
plt.legend()

#%%
for f in frecuencias:
    df = pd.DataFrame(data={'Tiempo': tiempos, 'X': X[f], 'Y': Y[f]})
    df.to_csv(r'data/data20/data_ej_3_frec_corte_20_{}.csv'.format(f))
    
        
    



    


