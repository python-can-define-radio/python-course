# Audio Processing

[SoundFile](https://pysoundfile.readthedocs.io) is a Python library for reading and writing sound files.

### Notes: 
- You may need to install `soundfile` to begin.
  - `pip install soundfile` (from the terminal) 

### Exercises

### Example: read a `.wav` file

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

### Example: Read a file; write it as a different format

Some programs need a certain file format. For example, the SDRangel [WFM Modulator plugin](https://github.com/f4exb/sdrangel/blob/master/plugins/channeltx/modwfm/readme.md) requires mono 48 kHz F32LE raw format. The example below converts a `.wav` file to the needed format.

```python3
## 3
import soundfile as sf
data, samplerate = sf.read('input_file.wav', always_2d=True)
channels_added = np.sum(data, axis=1)
sf.write('output_file.raw', oneChannel, samplerate, subtype='FLOAT', endian='LITTLE')
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


