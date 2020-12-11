# coding:utf-8
# Date : 2019.07.8
# author: phecda
#
#
# ********************************


import os
import random
import numpy as np
import math
import pyrirgen as RG
import soundfile as sf
from scipy import signal


class AudioReverbing(object):
    def __init__(self):
        self.c = 340  # Sound velocity (m/s)
        self.sr = 16000  # Sample rate (samples/s)

    def hFilter(self, T60):
        rp = 1  # Receiver position
        sp =random.randint(2, 5) # Source position
        r = [2, rp, 2]  # Receiver position [x y z] (m)
        s = [4, sp, 3]  # Source position [x y z] (m)
        L = [4, 5, 6]  # Room dimensions [x y z] (m)
        rt = round(random.uniform(0.8, 1.0), 1)  # Reflections Coefficients
        n = int(T60 * self.sr)  # Number of samples
        mtype = 'omnidirectional'  # Type of microphone 默认 omnidirectional 全方向的
        order = 8  # Reflection order
        dim = 3  # Room dimension
        ori = round(random.uniform(0, 2 * math.pi), 2)
        orientation = [ori, 0]  # Microphone orientation (rad)
        hp_filter = 1  # Enable high-pass filter
        h = RG.rir_generator(self.c, self.sr, s, r, L, reverbTime=rt, nSamples=n, micType=mtype, nOrder=order, nDim=dim,
                             orientation=orientation, isHighPassFilter=hp_filter)
        self.reverb_file_name = '_reverb_{}_{}_{}_{}_{}.wav'.format(rp, sp, rt, ori, n)
        return np.array(h)

    def genReverbWav(self, wavfile):
        sig, sr = sf.read(wavfile)
        # sig = extractWavLoudestArray(sig, 1000, sr, len(sig))
        durations = round(float(len(sig) / 16000.0), 2)
        T60 = random.uniform(0.4, 1.2)
        h = self.hFilter(T60)
        reverb_sig = signal.lfilter(h, 1, sig)
        reverb_sig = reverb_sig / max(h)
        out_file_name = str(os.path.basename(wavfile).split('.')[0]) + self.reverb_file_name
        out_file_path = os.path.dirname(os.path.dirname(wavfile)) + 'pos_reverb/' + out_file_name
        sf.write(out_file_path, reverb_sig, sr)

        relative_out_file_path = 'pos_reverb/' + out_file_name
        return relative_out_file_path, durations

