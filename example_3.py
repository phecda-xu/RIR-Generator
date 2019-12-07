import numpy as np
import pyrirgen as RG
import matplotlib.pyplot as plt

c = 340						# Sound velocity (m/s)
fs = 16000					# Sample frequency (samples/s)
r = [[2,1.5,2],[1,1.5,2]]	# Receiver positions [x_1 y_1 z_1 ; x_2 y_2 z_2] (m)
s = [2,3.5,2]				# Source position [x y z] (m)
L = [5,4,6]					# Room dimensions [x y z] (m)
rt = 0.4					# Reverberation time (s)
n = 4096					# Number of samples
mtype = 'omnidirectional'	# Type of microphone
order = -1					# -1 equals maximum reflection order!
dim = 3						# Room dimension
orientation = [0, 0]				# Microphone orientation (rad)
hp_filter = 1				# Enable high-pass filter

h = RG.rir_generator(c, fs, s, r, L, reverbTime=rt, nSamples=n, micType=mtype, nOrder=order, nDim=dim, orientation=orientation, isHighPassFilter=hp_filter)
print(len(h[0]), len(h[1]))