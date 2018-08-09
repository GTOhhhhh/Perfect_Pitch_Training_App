import sounddevice as sd
import soundfile as sf
from AP_recognition import all_pitches

print(all_pitches)

for pitch in all_pitches:
    data, fs = sf.read('./piano/' + pitch + '.aiff', frames=10 ** 5)
    print('playing pitch {}'.format(pitch))
    sd.play(data, fs, blocking=True)
