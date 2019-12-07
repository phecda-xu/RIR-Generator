import pyrirgen as RG


c = 340					# Sound velocity (m/s)
fs = 16000				# Sample frequency (samples/s)
r = [2,1.5,2]			# Receiver position [x y z] (m)
s = [2,3.5,2]			# Source position [x y z] (m)
L = [5,4,6]				# Room dimensions [x y z] (m)
rt = 0.4				# Reverberation time (s)
n = 4096				# Number of samples

h = RG.rir_generator(c, fs, s, r, L, reverbTime=rt, nSamples=n)
print(len(h))

