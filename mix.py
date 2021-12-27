from pydub import AudioSegment
from pydub.playback import play
import ast

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

s1 = AudioSegment.from_wav("./notes/A/A-1.wav")
s2 = AudioSegment.from_wav("./notes/D/D-1.wav")
c = s1.overlay(s2)
play(c)

def gen_seq() -> list:
    """generate """
