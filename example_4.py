import math
import pyrirgen

c = 340                          # Sound velocity (m/s)
fs = 16000                       # Sample frequency (samples/s)
r = [[2, 1.5, 2]]                # Receiver position [x y z] (m)
s = [2, 3.5, 2]                  # Source position [x y z] (m)
L = [5, 4, 6]                    # Room dimensions [x y z] (m)
rt = 0.4                         # Reverberation time (s)
n = 4096                         # Number of samples
mtype = 'hypercardioid'          # Type of microphone
order = -1                       # Reflection order
dim = 3                          # Room dimension
orientation = [math.pi/2, 0]     # Microphone orientation (rad)
hp_filter = False                # Enable high-pass filter

h = pyrirgen.generateRir(L, s, r, soundVelocity=c, fs=fs, reverbTime=rt, nSamples=n, micType=mtype, nOrder=order, nDim=dim, isHighPassFilter=hp_filter)
print(len(h), len(h[0]))