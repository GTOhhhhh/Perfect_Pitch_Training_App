import os
from typing import List
from pydub import AudioSegment
from pydub.playback import play
import random

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

s1 = AudioSegment.from_wav("./notes/A/A-1.wav")
s2 = AudioSegment.from_wav("./notes/D/D-1.wav")
c = s1.overlay(s2)
play(c)


def mix_chords(num_chords: int, num_notes: int, notes: list) -> List[AudioSegment]:
    """randomly mix chords with n notes"""
    audio_segments = []
    for i in num_chords:
        note_paths: List[str] = []
        for j in num_notes:
            note = random.sample
            path: str = "./notes/" + note + '/' + random.choice(os.listdir("./notes/" + note + "/"))
            note_paths.append()
    return audio_segments

print(os.listdir("./notes/"))



