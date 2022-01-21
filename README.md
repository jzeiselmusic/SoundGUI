# SoundGUI
:: simple audio .wav player ::


This is intended to be a simple expandable audio player written with python

Theoretically this could be used for all sorts of purposes:
 - testing audio filters and effects 
 - measuring loudness and distortion levels

The current limitations are:
 - only accepts 8,16,or 32 bit .wav files currently
 - the list of tracks clears itself with you add a new row
 - There are still print statements in the code because it is still in testing 

*IMPORTANT
- when entering the start time for a track, it must be in the form "xx.xx" (min.sec). For example, if you want to start the song at time 3:00, type in 03.00


In order to use GUI, simply run soundgui.py


Python Library Dependencies:
 - PySimpleGUI
 - simpleaudio
 - wave
 - os
 - soundfile
 - struct
 - scipy
 - array