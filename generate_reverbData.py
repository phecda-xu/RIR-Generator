# coding:utf-8
# Date : 2019.07.8
# author: phecda
#
#
# ********************************


import os
import random
import json
import numpy as np
import math
import multiprocessing as mp
import pyrirgen as RG
import soundfile as sf
from scipy import signal
from tqdm import tqdm
from data import AudioProcessor
from utils import extractWavLoudestArray


class AudioReverbing(object):
    def __init__(self):
        self.c = 340  # Sound velocity (m/s)
        self.sr = 16000  # Sample rate (samples/s)

    def hFilter(self, sig_length):
        rp = 1  # Receiver position
        sp =random.randint(2, 6) # Source position
        r = [2, rp, 2]  # Receiver position [x y z] (m)
        s = [2, sp, 2]  # Source position [x y z] (m)
        L = [5, 4, 6]  # Room dimensions [x y z] (m)
        rt = round(random.uniform(0.2, 0.8), 1)  # Reflections Coefficients
        n = sig_length  # Number of samples
        mtype = 'omnidirectional'  # Type of microphone 默认 omnidirectional 全方向的
        order = 1  # Reflection order
        dim = 3  # Room dimension
        ori = round(random.uniform(0, 2 * math.pi), 2)
        orientation = [ori, 0]  # Microphone orientation (rad)
        hp_filter = 1  # Enable high-pass filter
        h = RG.rir_generator(self.c, self.sr, s, r, L, reverbTime=rt, nSamples=n, micType=mtype, nOrder=order, nDim=dim,
                             orientation=orientation, isHighPassFilter=hp_filter)
        self.reverb_file_name = '_reverb_{}_{}_{}_{}_{}.wav'.format(rp, sp, rt, ori, n)
        return h

    def genReverbWav(self, wavfile):
        sig, sr = sf.read(wavfile)
        sig = extractWavLoudestArray(sig, 1000, sr, len(sig))
        durations = round(float(len(sig) / 16000.0), 2)
        h = self.hFilter(len(sig))*5
        reverb_sig = signal.lfilter(h, 1, sig)
        out_file_name = str(os.path.basename(wavfile).split('.')[0]) + self.reverb_file_name
        out_file_path = os.path.dirname(os.path.dirname(wavfile)) + '/pos_reverb/' + out_file_name
        sf.write(out_file_path, reverb_sig, sr)

        relative_out_file_path = 'pos_reverb/' + out_file_name
        return relative_out_file_path, durations
        
    def genReverbWavWithSet(self, wavfile, set, dataPath):
        if not os.path.exists(os.path.join(dataPath, 'pos_reverb', set)):
            os.makedirs(os.path.join(dataPath, 'pos_reverb', set))
        sig, sr = sf.read(wavfile)
        sig = extractWavLoudestArray(sig, 1000, sr, len(sig))
        durations = round(float(len(sig) / 16000.0), 2)
        h = self.hFilter(len(sig))*5
        reverb_sig = signal.lfilter(h, 1, sig)
        out_file_name = str(os.path.basename(wavfile).split('.')[0]) + self.reverb_file_name
        out_file_path = dataPath + 'pos_reverb/{}/'.format(set) + out_file_name
        sf.write(out_file_path, reverb_sig, sr)
        relative_out_file_path = 'pos_reverb/{}/'.format(set) + out_file_name
        return relative_out_file_path, durations


def processor(data_list, out_file, set_name, dataPath, audio_reverb):
    reverb_list = []
    for i in tqdm(data_list):
        audio_file = os.path.join(dataPath, i['audio_file_path'])
        wav_reverb_filepath, duratios = audio_reverb.genReverbWavWithSet(audio_file, set_name, dataPath)
        i['audio_file_path'] = wav_reverb_filepath
        i['duration'] = duratios
        i['id'] = i['id'] + 'reverb'
        reverb_list.append(i)
    with open(os.path.join(dataPath, 'pos_reverb', out_file), 'w') as f:
        json.dump(reverb_list, f)


def process_reverb():
    dataPath = "../../data/hey_snips/"
    audio_reverb = AudioReverbing()
    ad = AudioProcessor(dataPath + 'pos_orignal/train_pos.json',
                        dataPath + 'pos_orignal/test_pos.json',
                        dataPath + 'pos_orignal/dev_pos.json')
    train_pos = ad.data_index['train_pos']
    test_pos = ad.data_index['test_pos']
    dev_pos = ad.data_index['dev_pos']

    funcs = [train_pos, test_pos, dev_pos]
    out_file_list = ['train_reverb.json', 'test_reverb.json', 'dev_reverb.json']
    set_list = ["train", "test", "dev"]
    threads = []
    for i in range(len(funcs)):
        t=mp.Process(target=processor, args=(funcs[i], out_file_list[i], set_list[i], dataPath, audio_reverb), name="processor_")
        threads.append(t)
        
    for th in range(len(funcs)):
        threads[th].start()
    
    for th in range(len(funcs)):
        threads[th].join()


if __name__ == "__main__":
    process_reverb()
