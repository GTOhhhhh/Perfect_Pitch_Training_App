import soundfile as sf
import sounddevice as sd
import csv
import time
import pandas as pd
import random
import os
from datetime import datetime as dt
from termcolor import colored
from colorama import init

# piano samples
# all_pitches = ['C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4', 'C5', 'Db5', 'D5', 'Eb5',
#                'E5', 'F5', 'Gb5', 'G5', 'Ab5', 'A5', 'Bb5', 'B5']
# pitches = ['C4', 'D4', 'E4', 'F4', 'G4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A4', 'A5']
test_seq = ['F#', 'C#', 'G#', 'D#', 'A#', 'F', 'C', 'G', 'D', 'A', 'E', 'B']

init()


# 32 notes for each tone, 4 of which are target
def gen_seq(target):
    seq = list(test_seq)
    seq.remove(target)
    seq = random.choices(seq, k=28)
    for i in range(4):
        seq.append(target)
    random.shuffle(seq)
    return seq


def play(path):
    data, fs = sf.read(path, frames=10 ** 5)
    sd.play(data, fs, blocking=True)


def run():
    input('Press any key to start. ')
    for target in test_seq:
        print('target: ', target)
        target_seq = gen_seq(target)
        for i in range(5):
            play('./notes/' + target + '/{}.wav'.format(target))
        for note in target_seq:
            path = "./notes/" + note + '/' + random.choice(os.listdir("./notes/" + note + "/"))
            play(path)

            time.sleep(1)

            if note == target:
                print(colored('that was the target note', 'blue'))
            else:
                print(colored('that was note the target note', 'red'))


run()

# to remove octave numbers
# regex = re.compile('[^a-zA-Z]')
# [regex.sub('', i) for i in pitches]
print(colored('blah', 'red'))
#
# def play_pitches(pitches):
#     answers = []
#     responses = []
#     pitch = random.choice(pitches)
#     answers.append(pitch)
#     while True:
#         data, fs = sf.read('./piano/' + pitch + '.aiff', frames=10 ** 5)
#         res = input('Press enter to hear the pitch again. Otherwise input your answer.\n')
#         if not res:
#             continue
#         confirm = input('You answered {}, press enter to confirm. '.format(res))
#         if not confirm:  # enter will give an empty string, not confirm -> confirmed
#             responses.append(res)
#             end = input('Answer recorded. Press q to quit or any key to hear another pitch. ')
#             if end == 'q':
#                 break
#             else:
#                 pitch = random.choice(pitches)
#                 answers.append(pitch)
#                 continue
#         else:
#             continue  # go back to play the tone again
#     modded = [i[:-1] for i in answers]
#     count = 0
#     session_time = dt.now()
#     with open('log.csv', 'a', newline='') as f:
#         writer = csv.writer(f)
#         for idx, response in enumerate(responses):
#             if modded[idx] == response:
#                 count += 1
#             writer.writerow([response, modded[idx], answers[idx], session_time, pitches])
#
#     print('\nYour answers', responses)
#     print('Correct answers', answers)
#     print('{}/{} correct. '.format(count, len(answers)))
#
#


# if __name__ == '__main__':
#     play_pitches(pitches)
