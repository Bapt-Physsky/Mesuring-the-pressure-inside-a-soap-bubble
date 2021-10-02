# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:35:23 2021

@author: Baptiste

Programme faisant des graphes pour le projet expérimental :

"Mesurer la pression dans une bulle de savon"

"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sip

g = 9.81 # accélération gravité terrestre
data = 'M4H06911.txt'

diametre = np.loadtxt(data, dtype=float, usecols=(0)) # diametre mesuré sur l'écran, en cm
masse = np.loadtxt(data, dtype=float, usecols=(1)) # masse mesuré sur la balance, en mg

Diametre = diametre*1.08 # conversion des valeurs en taille réelles (rapport d'échelle de 1.08)
Masse = masse*1E-6 # conversion des valeurs des milligrammes en kilogramme


plt.figure(figsize=(9, 6), dpi=320)
plt.plot(Diametre, masse, 'r+')
plt.xlabel('Diamètre de la bulle, en cm')
plt.xlim(2.0, 0.5)
plt.ylabel('Masse mesurée par la balance, en mg')
plt.title('Rapport masse / diamètre')
plt.show()

Surface = ((27.9E-3/2)**2)*np.pi

def Pressure(m, S, g):
    """
    

    Parameters
    ----------
    m : TYPE
        Masse mesurée.
    S : TYPE
        DESCRIPTION.
    g : TYPE
        valeur de l'accélération de la Terre.

    Returns
    -------
    Pression : TYPE
        DESCRIPTION.

    """
    Pression = m * g / S
    return Pression

Atmosphere = Pressure(Masse, Surface, g)

plt.figure(figsize=(9, 6), dpi=320)
plt.plot(Diametre, Atmosphere, 'go')
plt.xlabel('Diamètre de la bulle, en cm')
plt.xlim(2.0, 0.5)
plt.ylabel('Pression, en Pa')
plt.ylim(3.0, 12.0)
plt.title('Pression déduite de l\'expérience (Fichier = M4H06911)')
plt.show()

def Gamma(P, D):
    gamma = (P*D)/2
    return gamma

Diamenmetre = Diametre * 1E-2
Yamma = Gamma(Atmosphere, Diamenmetre)
x = range(31)

plt.figure(figsize=(9, 6), dpi=320)
plt.plot(x, Yamma, 'bx')
plt.xlabel('numéro de la mesure')
plt.ylabel('Gamma')
plt.ylim(0, 0.1)
plt.title('Coefficient de Cémeaurs')
plt.show()
