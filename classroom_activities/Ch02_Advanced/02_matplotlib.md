# Matplotlib module

### Install the necessary modules
`pip install matplotlib`  
`pip install numpy`

### Import the module

- We will use numpy to plot waves so it will need to be imported as well.

```python3
import matplotlib.pyplot as plt
import numpy as np
```
### Plotting with y as the variable (x is default) or plotting x and y together

```python3
## 1
## Try this.
y = [1, 2, 2, 3, 4, 3, 2, 2, 1]
plt.plot(y)
plt.show()
```
- This is the minimum required to plot anything (define the y-axis, plot the y-axis, and show the plot).
- without defining `x` it will default to the index of the y-axis element (0,1,2 etc.) up to the length of the y-axis

```python3
## 2
## Now lets add a background grid and a title.
y = [1, 2, 2, 3, 4, 3, 2, 2, 1]
plt.plot(y)
plt.grid()
plt.title("First Plot")
plt.show()
```
- Now lets add the x-axis.

```python3
## 3
## Try this.
y = [1, 2, 2, 3, 4, 3, 2, 2, 1]
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
plt.plot(x, y)
plt.grid()
plt.title("First Plot")
plt.show()


## 4
## Copy and modify the previous example and remove a single point of either x or y.
## What happened? See answer below.
```
<details><summary>Answer</summary>

- You should have gotten an error similar to this:  
  `ValueError: x and y must have same first dimension, but have shapes (9,) and (8,).`
  
- This means that the length of the lists `x` and `y` must be the same length.
</details>

### Specifying markers, colors, linestyle, legends 

- [Here](https://matplotlib.org/stable/api/markers_api.html) is a list of available markers.
- [Here](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html) is a list of available linestyles.
- [Here](https://matplotlib.org/stable/gallery/color/named_colors.html) is a list of available colors.

```python3
## 5
## Try this.
## feel free to experiment.
amplitude = [1, 2, 2, 3, 4, 3, 2, 2, 1]
time = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
plt.plot(time, amplitude, marker="*", markersize=10, color="red", linestyle="--")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.title("Second Plot")
plt.show()

## The plot function also accepts a short form which combines the marker, color, and linestyle arguments like this.
## Try replacing your plt.plot command with this one.
plt.plot(time, amplitude, "*r--", markersize=10)
## The order of *, r, and -- do not matter.
```



### using subplots or multiple signals in a single plot and tight_layout

### Adding text onto our plot

```python3

amplitude = [1, 2, 2, 3, 4, 3, 2, 2, 1]
time = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
plt.plot(time, amplitude, "Pr--")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.text(0.2, 2.5, 'box with italic text at data coords: .2(x) and 2.5(y)', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.4, 'pad': 10})
plt.grid()
plt.title("Second Plot")
plt.show()
```






```python3
import numpy as np
from pcdr import ook_modulate, createTimestamps, makeComplexWave
import matplotlib.pyplot as plt

samp_rate = 50
modded = ook_modulate(data=[1, 0, 1, 0, 1, 0, 1, 1], 
                      bit_length=25)
t = len(modded) / samp_rate
timestamps = createTimestamps(seconds=t, num_samples=len(modded))
wave = makeComplexWave(timestamps, freq=4)
fully_modded = modded * wave
fully_modded.tofile("additional_practice_signal.complex")
retrieved = np.fromfile("additional_practice_signal.complex", dtype=np.complex64)
plt.subplot(311)
plt.plot(timestamps, modded, "o-", color="black", markersize=5, label="Modded")
plt.plot(timestamps, wave.real, "<-", color="blue", markersize=5, label="Real")
plt.plot(timestamps, wave.imag, ">-", color="red", markersize=5, label="Imag")
plt.legend(loc="upper right")
plt.subplot(312)
plt.plot(timestamps, fully_modded.real, "<-", color="blue", markersize=5, label="Real")
plt.plot(timestamps, fully_modded.imag, ">-", color="red", markersize=5, label="Imag")
plt.legend(loc="upper right")
plt.subplot(313)
plt.plot(timestamps, retrieved.real, "P-", label="RetReal")
plt.plot(timestamps, retrieved.imag, "p-", label="RetImag")
plt.legend(loc="upper right")
plt.show()
```
### Links for further exploration

[Link to matplotlib docs](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#)  
[Quick start guide](https://matplotlib.org/stable/tutorials/introductory/quick_start.html)  
[A simple plot](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html)
