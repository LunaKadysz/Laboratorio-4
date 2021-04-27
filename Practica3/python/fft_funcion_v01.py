#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:55:43 2020

@author: nico
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy.signal import find_peaks    


def MakeSpectralPlot(y, Fs, fignum=1):
    
    yfft = fftpack.fft(y)
    N = len(y)
    xf = np.linspace(0, Fs/2, int(N/2))
    yf = 2.0/N * np.abs(yfft[:N//2])
    PosicionPicos, IntensidadPicos = find_peaks(yf, height=yf[0])
    print(PosicionPicos)
    print(IntensidadPicos)
#    VectorFrecuenciaPicos = [xf[i] for i in PosicionPicos]
    plt.figure(fignum)
    plt.clf()
    plt.semilogx(xf, yf)
    plt.xlabel('Frecuencias (MHz)')
    plt.ylabel('Amplitud (AU)')
    plt.title('Descomposición espectral del ruido')
    return xf, yf

#%%
def MakeSpectralPlot2(y, Fs, fignum=1):
    
    yfft = fftpack.fft(y)
    N = len(y)
    xf = np.linspace(0, Fs/2, int(N/2))
    yf = 2.0/N * np.abs(yfft[:N//2])
    
    
    plt.figure(fignum)
    plt.clf()
    plt.semilogx(xf, yf)
    plt.xlabel('Frecuencias (MHz)')
    plt.ylabel('Amplitud (AU)')
    plt.title('Descomposición espectral del ruido')
    return xf, yf

#%%

#Ejemplo de plot
    
t = np.linspace(0, 10, 30000)
tstep = max(t)/len(t)
fsamp = 1/tstep

f0 = 1
f1 = 20
V = np.sin(2*np.pi*f0*t) + np.sin(2*np.pi*f1*t) 

plt.figure(2)
plt.clf()
plt.plot(t, V)

MakeSpectralPlot(V, fsamp)
MakeSpectralPlot2(V, fsamp,3)


























