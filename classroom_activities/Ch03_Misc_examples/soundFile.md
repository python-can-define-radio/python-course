# Audio Processing

[SoundFile](https://pysoundfile.readthedocs.io) is a Python library for reading and writing sound files.

### Notes: 
- You may need to install `soundfile` to begin.
  - `pip install soundfile` (from the terminal) 

### Exercises

### Create a `.wav` file

```python3
## 1
## This creates a mono `.wav` file that plays three tones.
import soundfile as sf
import numpy as np


samplerate = 24000
maxtime = 0.5

timestamps = np.linspace(0, maxtime, int(maxtime*samplerate), endpoint=False)
tone1 = np.sin(250   * 2 * np.pi * timestamps)
tone2 = np.sin(375   * 2 * np.pi * timestamps)
tone3 = np.sin(312.5 * 2 * np.pi * timestamps)

in_sequence = np.concatenate([tone1, tone2, tone3])

sf.write('threetone.wav', in_sequence, samplerate)
```

```
## 2
## This creates a stereo `.wav` file. It plays different tones on each speaker.
TODO
```

### Read a `.wav` file

```python3
## 1
## You'll need to provide your own .wav file for this example.
import soundfile as sf

data, samplerate = sf.read('input_file.wav')
print(data)
```

If your `.wav` file is stereo (two channels -- left and right), your data will look something like this:

```
[[-3.35693359e-04 -4.57763672e-04]
 [ 9.15527344e-05 -9.15527344e-05]
 [-6.71386719e-04 -3.35693359e-04]
 ...
 [ 3.35693359e-04 -9.15527344e-05]
 [ 2.13623047e-04 -9.15527344e-05]
 [ 4.57763672e-04  0.00000000e+00]]
```

Notice that there are two columns of numbers, representing the two channels. Each number is a _sample_ of the audio signal. The idea of taking measurements (samples) of a signal will be one of the core concepts discussed in our [sdr-course](https://github.com/python-can-define-radio/sdr-course/).

If your `.wav` file is mono (one channel), your data will only have one dimension, and may be displayed horizontally:

```
[-3.35693359e-04  9.15527344e-05 -6.71386719e-04 ...  3.35693359e-04
  2.13623047e-04  4.57763672e-04]
```

You can specify that `soundfile` should always return a two-dimensional array. You'll only be able to see a difference if you are working with a mono (single channel) `.wav` file. If you are working with a stereo `.wav` file, `always_2d=True` has no effect.

```python3
## 2
import soundfile as sf
data, samplerate = sf.read('input_file.wav', always_2d=True)
print(data)
## This will print...
# [[-3.35693359e-04]
#  [ 9.15527344e-05]
#  [-6.71386719e-04]
#  ...
#  [ 3.35693359e-04]
#  [ 2.13623047e-04]
#  [ 4.57763672e-04]]
```

We'll show the usefulness of the `always_2d` argument below.

### Convert a `.wav` file to `.raw`

Some programs need a certain file format. For example, the SDRangel [WFM Modulator plugin](https://github.com/f4exb/sdrangel/blob/master/plugins/channeltx/modwfm/readme.md) requires mono 48 kHz F32LE raw format. The example below converts a `.wav` file to the needed format.

```python3
## 3
## This works for either stereo or mono files
import numpy as np
import soundfile as sf
data, samplerate = sf.read('input_file.wav', always_2d=True)
channels_added = np.sum(data, axis=1)
sf.write('output_file.raw', channels_added, samplerate, subtype='FLOAT', endian='LITTLE')
```

The above code works for either mono or stereo input files. You could simplify if you know whether the source data is mono or stereo:

```python3
## 3a
## This only works for stereo files
import soundfile as sf
data, samplerate = sf.read('input_file.wav')
channels_added = np.sum(data, axis=1)
sf.write('output_file.raw', oneChannel, samplerate, subtype='FLOAT', endian='LITTLE')

## 3b
## This only works for mono files
import soundfile as sf
data, samplerate = sf.read('input_file.wav')
sf.write('output_file.raw', data, samplerate, subtype='FLOAT', endian='LITTLE')
```

You'll see this applied in the [SDR Angel lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Applications/060_SDRangel.md).


### Encryption proof-of-concept

```python3
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np



key = [0.5, 0.1, 0.8, -0.2, 0.3, -0.5, -0.9, 0.3, -0.1, -0.2]
position = 0
data, samplerate = sf.read('Ouch-6.wav')
encrypted = np.empty_like(data)
for item in data:
    cyc = position % 3
    shift = key[cyc]
    encrypted[position] = item + shift
    position += 1
plt.plot(data, "bo")
plt.plot(encrypted, "ro")
plt.show()
```
