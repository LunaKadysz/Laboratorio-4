#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:55:43 2020

@author: nico
"""
import numpy as np
import matplotlib.pyplot as plt
   


#%% Generamos una función de prueba.

# El tiempo está en segundos y la frecuencia en Hertz    
N=10000 # cantidad de pasos
tmax=10 #tiempo máximo
t = np.linspace(0, 10, 10000)

# Calculo paso temporal y frecuencia de sampleo
tstep = tmax/N # paso temporal
fsamp = 1/tstep # frecuencia de sampleo

# Una función de prueba.
f0 = 7
f1 = 20
V = np.sin(2*np.pi*f0*t) + np.sin(2*np.pi*f1*t) 

# Graficamos la función de prueba
plt.figure(1)
plt.clf()
fig, ax = plt.subplots(1,1,num=1)
ax.plot(t, V)
ax.set_ylabel('Potencia')
ax.set_xlabel('Tiempo [s]')



#%% Hacemos la trasnformada de fourier y graficamos.
# Hacer la FFT
fft = np.fft.fft(V)

# Tomamos solo la primera mitad y normalizamos.
fft2 = 2.0/N * np.abs(fft[:N//2])
# Calular el vector de frecuencias.
frecs2 = np.linspace(0, fsamp/2, int(N/2))

# Graficamos la tasnformada de fourier
plt.figure(2)
plt.clf()
fig, ax = plt.subplots(1,1,num=2)
ax.plot(frecs2,np.abs(fft2))
ax.set_xlim([0,30]) # Elijo (restrinjo) el eje horizontal
ax.set_ylabel('Potencia')
ax.set_xlabel('Frecuencia [Hz]')
   

    


























