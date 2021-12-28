import wave
import struct
import numpy as np
from scipy.io.wavfile import write
import array
import os

def readwavfileslow(filename,read=True,debug=False):
	mode = 'r' if read else 'w'
	sizes = {1:'b',2:'h',4:'i'}
	wav = wave.open(filename,mode)
	chunk = 256
	samplerate = wav.getframerate()
	channels = wav.getnchannels()
	fmt_size = sizes[wav.getsampwidth()]
	fmt = "<" + fmt_size* channels * chunk
	ret = []
	while wav.tell() < wav.getnframes():
		try:
			
			decoded = struct.unpack(fmt,wav.readframes(chunk))
			ret.append(decoded)
		except struct.error:
			tmp_size = wav.getnframes() - wav.tell()
			tmp_fmt = "<" + fmt_size * channels * tmp_size
			decoded = struct.unpack(tmp_fmt,wav.readframes(tmp_size))
			ret.append(decoded)
	ret2 = []
	for i in range(len(ret)-1):
		temp = ret[i]
		for k in range(len(temp)):
			ret2.append(temp[k])
	return ret2, samplerate


def readwavfilefast(filename):
        mode = 'rb'
        sizes = {1:'b',2:'h',4:'i'}
        wav = wave.open(filename,mode)
        samplerate = wav.getframerate()
        fmt_size = sizes[wav.getsampwidth()]
        a = array.array(fmt_size)
        a.fromfile(open(filename,mode),int(os.path.getsize(\
                filename)/a.itemsize))
        a = a.tolist()
        return a, samplerate

			
def trim(data,samplerate,start):
	start_min = int(start[0:2])
	start_sec = int(start[3:5])
	start_seconds = start_min*60 + start_sec
	start_samples = int(start_seconds * samplerate)
	newdata = data[start_samples:len(data)]
	return newdata

def makestereo(data):
	L2 = []
	for i in range(0,len(data),2):
		L2.append((data[i],data[i+1]))
	return L2


def createwav(filename, rate, data):
	npdata = makestereo(data)
	npdata = np.array(npdata)
	write(filename,rate,npdata.astype(np.int16))
	return filename




	
