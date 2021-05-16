#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Demostración del funcionamiento de un lock-in.

Created on Thu Sep 10 16:17:07 2020

@author: labo4_2020
"""

#- Qué se puede hacer con un lock in?
#- ver la fase de la respuesta
#- encontar señal enterrada en ruido.
#- ver la derivada de una señal.




import numpy as np
import matplotlib.pyplot as plt
from scipy import signal



# Abrimos los datos.
medicion = np.loadtxt('data/v1/ej11_medicion.txt', delimiter=' ', skiprows=3)


#%%

### Defino variables temporales de la medición.
Fs = 100000;           #[Hz] Frecuencia de muestreo                    
FRef =1400.3;          #[Hz] Frecuencia de la referencia
L = len(medicion);     #[muestras] Longitud de la señal
# Calculamos variables asociadas 
T = 1/Fs;              #[s] Periodo de muestreo
MaxT = L/Fs;           #[s] Tiempo maximo
t = np.linspace(0,L-1,L)*T;         #[s] Time vector
OmegaRef = FRef*2*np.pi;     #[rad/s] frecuencia angular de referencia

# Elección de tiempo caracteríscito y orden del filtro
fc=15           #[Hz] Frecuencia de corte
orden = 6; # Orden del filtro.


#Genero las señales de referencia del lock-in.
Referencia_x=np.array(np.sin(OmegaRef*t));
Referencia_y=np.array(np.cos(OmegaRef*t)); #referencia desfasada en 90º





#%% Demodulación lock-in.

# Generamos una figura
plt.figure(1)
plt.clf()
fig, ax = plt.subplots(4,1,num=1, sharex=True)
ax[3].set_xlabel('Tiempo [s]')



# 1 Muestro la referencia.
ax[0].plot(t, Referencia_x, label='Referencia')
#ax[0].plot(t, Referencia_y, label='Referencia')
ax[0].set_ylabel('Referencia [V]')
ax[0].grid(True)

# 2 Muestro la señal
ax[1].plot(t, medicion, label='Señal')
ax[1].set_ylabel('Señal [V]'), ax[1].grid(True)

# 3 Detección de fase. Multiplicación por referencia
PSDx = 2 * medicion * Referencia_x;
PSDy = 2 * medicion * Referencia_y; #PSD del segundo canal
# Graficamos señal multiplicada
ax[2].plot(t, PSDx, label='Señal')
# ax[2].plot(t, PSDy, label='Señal')
ax[2].set_ylabel('PSD [V]'), ax[2].grid(True)


# Filtrado de señal 
sos = signal.bessel(orden, 2*np.pi*fc, 'low', fs=Fs,output='sos') # Generación de parametros del filrado
PSDxFiltrada= signal.sosfilt(sos,PSDx) # Filtrado
PSDyFiltrada= signal.sosfilt(sos,PSDy) # Filtrado


## Para graficar R y theta
ax[3].plot(t,np.arctan2(PSDyFiltrada,PSDxFiltrada,), label=r'$\theta$')
ax[3].plot(t,PSDxFiltrada**2+PSDyFiltrada**2,label='R')
## Para graficar X e Y
#ax[3].plot(t,PSDxFiltrada,label='X')
#ax[3].plot(t,PSDyFiltrada,label='Y')
plt.legend(loc='lower right')
ax[3].set_ylabel('Salida'), ax[3].grid(True)


# Ordenamos y salvamos la figura.
plt.tight_layout()  
plt.savefig(f'seniales.png')




#%% Análisis de Fourier de cada etapa.

# Armamos una figura conjunta
plt.figure(2)
plt.clf()
fig, ax = plt.subplots(4,1,num=2,sharex=True)
# Determinamos los ejes para todos lo gráficos.
ax[3].set_xlabel('Frecuencia [Hz]')
ax[3].set_xlim([1,2.5*FRef])
ax[3].set_xscale('linear')


# Armamos el vector de frecuencias.
freqs=np.fft.fftfreq(L,1/Fs)

# 1 Grafica la FFT de la referencia
fftReferencia= np.abs(np.fft.fft(Referencia_x));
ax[0].semilogy(freqs[0:L//2],fftReferencia[0:L//2],'o-') 
ax[0].set_ylabel('Referencia'),ax[0].grid(True)


# 2 Grafica la FFT de la señal
fftSenial= np.abs(np.fft.fft(medicion));
ax[1].semilogy(freqs[0:L//2],fftSenial[0:L//2],'o-') 
ax[1].set_ylabel('Señal'),ax[1].grid(True)

# 3 Grafica la FFT de la señal multiplicada
fftPSDx= np.abs(np.fft.fft(PSDx));
fftPSDy= np.abs(np.fft.fft(PSDy));
ax[2].semilogy(freqs[0:L//2],fftPSDx[0:L//2],'o-') 
ax[2].set_ylabel('PSD'),ax[2].grid(True)


# 4 Grafica la FFT de la señal demodulada
fftPSDxFiltrada= np.abs(np.fft.fft(PSDxFiltrada));
fftPSDyFiltrada= np.abs(np.fft.fft(PSDyFiltrada));
ax[3].semilogy(freqs[0:L//2],fftPSDxFiltrada[0:L//2],'o-') 
ax[3].set_ylabel('Salida'),ax[3].grid(True)


plt.tight_layout()  
plt.savefig(f'fourier.png')


