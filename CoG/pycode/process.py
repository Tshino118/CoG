import pandas as pd
import numpy as np
from scipy import interpolate

def MoveAve(df,num):
    ma = df.rolling(window=num, center=True).mean().dropna()
    return ma
"""
def Fourier(df,inv=False):
    if inv == True:
        return np.fft.ifft(df)
    else:
        return np.fft.fft(df)
"""
def Sig2amp(time,sig,dt):
    N = len(sig)
    freq = np.linspace(0, 1.0/dt, N)
    F = np.fft.fft(sig)

    c_F = np.copy(F)
    imag_freq = max(freq)/2
    c_F[(freq>imag_freq)] = 0
    F_abs = np.abs(c_F)
    F_abs_amp = F_abs / N * 2
    F_abs_amp[0] = F_abs_amp[0] / 2
    amp = np.copy(F_abs_amp)
    return freq,amp,F
    
def Amp2sig(freq):
    F_ifft = np.fft.ifft(freq)
    sig = F_ifft.real
    return sig

def Interpolation(df):
    df = df.resample("0.01").interpolate(method="liner")
    return df

def Nomalize(df):
    nomal = 0
    return nomal

def cart2pol(x,y):
    rho = np.sqrt(x**2+y**2)
    phi = np.arctan2(y,x)
    return (rho,phi)

def pol2cart(rho,phi):
    x = rho*np.cos(phi)
    y = rho*np.sin(phi)
    return (x,y)
