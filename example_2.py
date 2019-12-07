import pyrirgen as RG


c = 340						# Sound velocity (m/s)
fs = 16000					# Sample frequency (samples/s)
r = [2,1.5,2]				# Receiver position [x y z] (m)
s = [2,3.5,2]				# Source position [x y z] (m)
L = [5,4,6]					# Room dimensions [x y z] (m)
rt = 0.4					# Reflections Coefficients
n = 2048					# Number of samples
mtype = 'omnidirectional'	# Type of microphone
order = 2					# Reflection order
dim = 3						# Room dimension
orientation = [0,0]				# Microphone orientation (rad)
hp_filter = 1				# Enable high-pass filter

h = RG.rir_generator(c, fs, s, r, L, reverbTime=rt, nSamples=n, micType=mtype, nOrder=order, nDim=dim, orientation=orientation, isHighPassFilter=hp_filter)
print(len(h))

