# winsound library is used to provide sound playing machinery provided by the Windows platform

import winsound

# for i in range(3000, 4000, 100):
 #   Beep(i, 1000)               # Beep is library function from 32 to 32767 Hz, time in milliseconds

# PlaySound("C:\\Users\\Vin\\Downloads\\Astrud Gilberto -- The Gentle Rain (RJD2 Remix) (2005) (mp3cut.net).mp3", SND_APPLICATION)

print(*dir(winsound), sep='\n')

# winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)    # plays wav files or audio data as a string of bytes

# SND_LOOP: plays the sound repeatedly
# SND_PURGE: stops all instances of specified sound
# SND_ASYNC: plays sound and returns immediately
# SND_FILENAME: sound specified is a .wav file

"""
symphony = {'f': 349, 'e': 329, 'e': 329, 'f': 349, 'e': 329, 'e': 329, 'f': 349, 'g': 390, 'f': 349, 'f': 349, 'e': 329, 'e': 329}
notes = "f e e f e e f g f f e e".split()
for note in notes:
    winsound.Beep(symphony[note], 500)
"""

winsound.MessageBeep(winsound.MB_ICONHAND)
