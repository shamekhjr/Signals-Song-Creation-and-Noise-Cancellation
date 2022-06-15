# Signals-Song-Creation-and-Noise-Cancellation
In this project, we use the Python programming language along with the ```numpy```, ```matplotlib```, ```sounddevice``` and ```scipy``` Python libraries to create a song and simulate the process of removing noise from it

## Process Explanation

### 1. Creating the Song

We're imagining that the sound of our song is going to be created by a piano where we assume we have only the 3rd and 4th octaves at our disposal, the 4th octave being played with the right hand and the 3rd octave being played with the left hand. To generate a song, we needed a number of single tone frequencies summed together, using the following formula: 

![song equation](https://snipboard.io/nrz6VJ.jpg)

With N being the number of pairs (of right hand and left-hand frequencies, which the more there are of them the more complex the song becomes), i being the pair number, F_i being the left-hand frequency, f_i being the right-hand frequency, t_i being the pressing starting time and T_i being how long we will press both keys. 

The duration of the song will be 3 seconds, so our ```t``` variable will be bound between 0 and 3, and for t to look continuous in code we used the ```linspace``` function in the ```numpy``` library with 0 as start and 3 as stop with 12*1024 divisions between them. And to play our song, we used the play function in the ```sounddevice``` library. Using t as a vector containing increasing values simulates the sigma notation in the formula above. 
  
We initially set the F and f to be vectors the same length of t but populated with zeros. We will then set some values of the vector to have non-zero values according to the song we want to output, thus the need for additional arrays to act as unit step functions is thus eliminated. 

We then modified the f and F vectors to add the frequencies corresponding the notes we want to play, we mostly used B4 and E4 for the left hand and B3 and E3 for the right hand. The output song bears some similarity to Michael Giacchino’s score for *The Batman (2022)*. The use of the ```plot``` function from the ```matplotlib``` library to plot the final multi-tone signal generated x(t) created the following figure:

![Time Domain Signal Without Noise](https://snipboard.io/vUJVpc.jpg)


### 2. Adding the Noise

For this part of the process, we first needed to add noise to our time domain signal, or song for that matter. We used the ```random.randint``` function from the ```numpy``` library to pick two random frequencies from 1 to 512 Hz, and plugged these values in to the formula for the noise function: 

![noise equation](https://snipboard.io/ER2Lrw.jpg)

with fn1 and fn2 being the two randomly picked frequencies. We then added the above function to the time domain signal we generated previously:

![singal with noise equation](https://snipboard.io/FGqhRH.jpg)

Applying the previous formula on the signal we created in the previous step gives us the following signal which was ploted using the ```plot``` function from the ```matplotlib``` library:

![Time Domain Signal With Noise](https://snipboard.io/heOKP1.jpg)

### 3. Removing the Noise

To remove the now-added noise, we needed to perform a few steps, the first one being to transition to the frequency domain. We converted both the signal with noise and the original signal (since we will need it for comparison later on) from the time domain to the frequency domain using the ```fft()``` which was imported from the ```scipy``` library. This function creates the Fourier Transform of the given Time-Domain signal.

<u>This is our original signal (or song after we converted it from the time domain to the frequency domain):</u>

![Frequency Domain Signal Without Noise](https://snipboard.io/ISNCPu.jpg)

<u>For comparison, here is our signal in the frequency domain after the noise was added:</u>

![Frequency Domain Signal With Noise](https://snipboard.io/Yo3bTU.jpg)

As we can see from the graph, there are more peaks compared to the graph of the original signal. In addition, some of the peaks are higher than the maximum peak of our original signal (> 2.5 in our case). 

The logic behind how to find the noise frequencies and thus remove them is to compare both signals in the frequency domains. The noise frequencies will correspond to frequencies at which there are peaks that are higher than the maximum peak in the original signal in the frequency domain. We should then remove those frequencies from the time domain expression according to the following formula:

![x_filtered formula](https://snipboard.io/JSrEkj.jpg)

Using the previous formula should get us our original song back without the distortions caused by the noise. 

While our code essentially implements the logic described above, there were a few slight adjustments. For example, instead of comparing peaks of the frequency signal with noise and comparing it with the maximum peak of the frequency signal without noise, we simply extracted the frequencies that correspond to the highest peaks in the frequency domain of the signal with noise. 

We implemented this approach by sorting the ```xn_f``` array which is the frequency domain of the signal with noise so that we can easily extract the largest two values by simply taking the last two items of the sorted array. We then used the ```np.where``` function which returns an array of all frequencies for which we get the max values of ```xn_f```, but since we only need one frequency and not the whole array we take the value at the very first index and round it to the nearest integer. We then remove the noise using the formula described above and regain our original sound before the noise was added. 


(Feel free to run our codes and take a look at the plots that will be generated as well as the sounds that will be outputted)

## Contributors 

- [Mohamed Shamekh](https://github.com/shamekhjr)
- [Omar Nour](https://github.com/Omar-Nour)

