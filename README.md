# Signals-Song-Creation-and-Noise-Cancellation
In this project, we use the Python programming language along with the ```numpy```, ```matplotlib```, ```sounddevice``` and ```scipy``` Python libraries to create a song and simulate the process of removing noise from it

## Process Explanation

We're imagining that the sound of our song is going to be created by a piano where we assume we have only the 3rd and 4th octaves at our disposal, the 4th octave being played with the right hand and the 3rd octave being played with the left hand. To generate a song, we needed a number of single tone frequencies summed together, using the following formula: 
[equation](https://snipboard.io/nrz6VJ.jpg)

With N being the number of pairs (of right hand and left-hand frequencies, which the more there are of them the more complex the song becomes), i being the pair number, F_i being the left-hand frequency, f_i being the right-hand frequency, t_i being the pressing starting time and T_i being how long we will press both keys. 

The duration of the song will be 3 seconds, so our t variable will be bound between 0 and 3, and for t to look continuous in code we used the linspace function in the numpy library with 0 as start and 3 as stop with 12*1024 divisions between them. And to play our song, we used the play function in the sounddevice library. Using t as a vector containing increasing values simulates the sigma notation in the formula above. 
  
We initially set the F and f to be vectors the same length of t but populated with zeros. We will then set some values of the vector to have non-zero values according to the song we want to output, thus the need for additional arrays to act as unit step functions is thus eliminated. 

We then modified the f and F vectors to add the frequencies corresponding the notes we want to play, we mostly used B4 and E4 for the left hand and B3 and E3 for the right hand. The output song bears some similarity to Michael Giacchino’s score for *The Batman (2022)*.

 

## Contributors 

- [Mohamed Shamekh](https://github.com/shamekhjr)
- [Omar Nour](https://github.com/Omar-Nour)

