import wave
import simpleaudio as sa
import PySimpleGUI as sg
from readaudio import *
import os
import soundfile as sf

def calculatelufs(filename):
    data, rate = sf.read(filename)
    meter = pln.Meter(rate)
    loudness = meter.integrated_loudness(data)
    return loudness
    

def playwav(file):
    wave_read = wave.open(file,'rb')
    audio_data = wave_read.readframes(wave_read.getnframes())
    num_channels = wave_read.getnchannels()
    bytes_per_sample = wave_read.getsampwidth() 
    sample_rate = wave_read.getframerate()
    play_obj = sa.play_buffer(audio_data,num_channels,bytes_per_sample,\
			sample_rate)
    #play_obj.wait_done()
    return play_obj


def makewindow(number):
    layout = []
    for i in range(1,number+1):
        layout += [sg.FileBrowse("Click to Add File",target=f"-file{i}-"),
                sg.VSeperator(),
                sg.InputText(key=f"-file{i}-",change_submits=True),
                sg.VSeperator(),
                sg.Button("Play",key=f"play_{i}"),
                sg.VSeperator(),
                sg.Button("Stop",key=f"stop_{i}"),
                sg.VSeperator(),
                sg.Multiline(default_text="00.00",size=(10),no_scrollbar=True,\
                            key=f"start_{i}",change_submits=True),
		sg.VSeperator()],
    layout += [[sg.Button("+",key="add_row")]]
    layout += [[sg.Listbox(values=["none","delay","reverb","filter"],enable_events=True,\
    			    expand_x=True,expand_y=True,key="effectbox")]]
    return layout


def ifplaypressed(row,values,effect):
    error1 = "start time must be form xx.xx!"
    error2 = "file must be .wav file!"
    error3 = "this is out of file length range!"
    
    file = values[f"-file{row}-"]
    start = values[f"start_{row}"]
    if file[-4:len(file)] != ".wav":
        print(error2)
    elif len(start) != 5:
        print(error1)
    elif start[2] != ".":
        print(error1)
    else:
        try:
            start_00 = start[0:2]
            start_99 = start[3:5]
            int(start_00)
            int(start_99)
        except:
            print(error1)
        print("loading song")
        song, samplerate = readwavfileslow(file)
        ##
        if effect == 'none':
            pass
        elif effect == 'filter':
            print("here")
            song = LPF(song)
        elif effect == 'reverb':
            pass
        elif effect == 'delay':
            pass
        ##
        start_secs = min_sec_2sec(start)
        if (start_secs*samplerate >= len(song)):
            print(error3)
            return None
        else:
            song = trim(song,samplerate,start)
            if start == '00.00':
                play_obj = playwav(file)
            else:
                trimmedfile = createwav('temporary_file.wav',samplerate,song)
                play_obj = playwav(trimmedfile)
                os.remove('temporary_file.wav')
            return play_obj
    


def LPF(song):
    song = np.array(song) / (2**24)
    for i in range(3,len(song)):
        song[i] = (0.5)*song[i] + (0.25)*song[i-1] + (0.25)*song[i-2]
    #for i in range(3,len(song)):
     #   song[i] = song[i] + song[i-1] + song[i-2] + song[i-3]
    #for i in range(3,len(song)):
    #    song[i] = song[i] + song[i-1] + song[i-2] + song[i-3]
    song = np.tanh(song)
    song = (song*(2**24)).tolist()
    return song





    
