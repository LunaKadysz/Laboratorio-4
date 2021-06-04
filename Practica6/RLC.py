#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 10:39:51 2021

@author: kenneths
"""

#%% Setup paths
import os
from scipy import fftpack
os.chdir(r'/home/tian/Desktop/labo4/Grupo5/Practica5/Grupo5/RP')
script_dir = os.path.abspath('/home/tian/Desktop/labo4/Grupo5/RP')
project_dir =  os.path.dirname(os.path.abspath('/home/tian/Desktop/labo4/Grupo5/RP'))
data_dir = os.path.join(project_dir, 'data')


from scipy import signal
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from time import sleep,time
import control_finn
from control_finn import RedPitayaApp, reg_labels

rp = RedPitayaApp('http://10.200.1.240/lock_in+pid_harmonic/?type=run', name='rp')
#%%


