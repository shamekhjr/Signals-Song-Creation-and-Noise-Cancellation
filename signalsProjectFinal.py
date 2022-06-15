"""
Signals Project Milestone 1&2
Code Authors:
Mohamed Tarek Shamekh 52-0989
Omar Sayed Nour 52-2179
T20
Supervised by: Eng. Maha El-Feshawy
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
from time import sleep

#Milestone 1

# fi is right hand frequency
# Fi is left hand frequency
# N is number of pairs of notes
# i is pair number

t = np.linspace(0, 3, 12 * 1024)
F = np.zeros(np.shape(t), dtype=int)
f = np.zeros(np.shape(t), dtype=int)
Fi = [493.88, 0, 493.88, 0, 493.88, 0, 329.63, 0, 493.88]
fi = [246.93, 0, 246.93, 0, 246.93, 0, 164.81, 0, 246.93]
Ti = [0, 0.5, 0.6, 0.9, 1.1, 1.6, 1.8, 2.1, 2.3]
ti = [0.5, 0.6, 0.9, 1.1, 1.6, 1.8, 2.1, 2.3, 3]

for i in range(len(Fi)):
    F[np.logical_and(t > Ti[i], t <= ti[i])] = Fi[i]
    f[np.logical_and(t > Ti[i], t <= ti[i])] = fi[i]

x = np.sin(2 * np.pi * F * t) + np.sin(2 * np.pi * f * t) #x(t) (No Noise)
sd.play(x, 3 * 1024) #Sound without noise

sleep(4)

#Milestone 2

N = 3*1024 #setting the number of samples to duration of song
freq = np.linspace(0, 512, int(N/2)) #creating the frequency vector

x_f = fft(x) #X(jw) (No Noise)
x_f = 2/N * np.abs(x_f [0:int(N/2)])


#Creating random noise frequencies
nf1, nf2= np.random.randint(1, 512, 2)
noise = np.sin(2*np.pi*nf1*t) + np.sin(2*np.pi*nf2*t) #n(t)

xn = x + noise #xn(t) (With Noise)
sd.play(xn, 3*1024) #Sound with Noise


sleep(4)
xn_f = fft(xn) #Xn(jw) (With Noise)
xn_f = 2/N * np.abs(xn_f [0:int(N/2)])

#Sorting the Xn(jw) vector so that the largest 2 values can be extracted easily
sortedXNF = np.sort(xn_f)
xn_fMax = sortedXNF[-1]
xn_fSecondLargest = sortedXNF[-2]
res1 = np.where(xn_f == xn_fMax)
res2 = np.where(xn_f == xn_fSecondLargest)

#np.where returns an array, thus we use the very first index of the array to get a single value instead
f1 = round(freq[res1[0][0]])
f2 = round(freq[res2[0][0]])


x_filtered = xn - (np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t))
x_filtered_f = fft(x_filtered)
x_filtered_f = 2/N * np.abs(x_filtered_f [0:int(N/2)])
sd.play(x_filtered,3*1024) #Sound with noise removed

"""""
plt.figure()
plt.plot(t,x) #Time Domain Signal (No Noise)
plt.title ('Time Domain Signal (Without Noise)')
plt.xlabel ('Time (s)')
plt.ylabel ('Amplitude')

plt.figure()
plt.plot(freq,x_f) #Frequency Domain Signal (No Noise)
plt.title ('Frequency Domain Signal (Without Noise)')
plt.xlabel ('Frequency (Hz)')
plt.ylabel ('Magnitude')

plt.figure()
plt.plot(t,xn) #Time Domain Signal (With Noise)
plt.title ('Time Domain Signal (With Noise)')
plt.xlabel ('Time (s)')
plt.ylabel ('Amplitude')

plt.figure()
plt.plot(freq,xn_f) #Frequency Domain Signal (With Noise)
plt.title ('Frequency Domain Signal (With Noise)')
plt.xlabel ('Frequency (Hz)')
plt.ylabel ('Magnitude')

plt.figure()
plt.plot(t,x_filtered) #Time Domain Signal (Noise Removed)
plt.title ('Time Domain Signal (Noise Removed)')
plt.xlabel ('Time (s)')
plt.ylabel ('Amplitude')

plt.figure()
plt.plot(freq,x_filtered_f) #Frequency Domain Signal (Noise Removed)
plt.title ('Frequency Domain Signal (Noise Removed)')
plt.xlabel ('Frequency (Hz)')
plt.ylabel ('Magnitude')
"""
plt.figure()
plt.subplot(3,1,1)
plt.plot(t,x) #Time Domain Signal (No Noise)
plt.subplot(3,1,2)
plt.plot(t,xn) #Time Domain Signal (With Noise)
plt.subplot(3,1,3)
plt.plot(t,x_filtered) #Time Domain Signal (Noise Removed)


plt.figure()
plt.subplot(3,1,1)
plt.plot(freq,x_f) #Frequency Domain Signal (No Noise)
plt.subplot(3,1,2)
plt.plot(freq,xn_f) #Frequency Domain Signal (With Noise)
plt.subplot(3,1,3)
plt.plot(freq,x_filtered_f) #Frequency Domain Signal (Noise Removed)




