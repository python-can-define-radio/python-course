# Matplotlib module

## plotting with y as the variable (x is default) or plotting x and y together
## specifying markers, colors, connecting line, legends, title, tight_layout
## using subplots or multiple signals in a single plot
## plt.show() is required similar to turtle.mainloop()

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
