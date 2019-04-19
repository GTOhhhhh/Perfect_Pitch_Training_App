import soundfile as sf
import sounddevice as sd
import time
import random
import os
import sys
from termcolor import colored
from colorama import init

all = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
test_seq = ['A#', 'C#', 'D#', 'F#', 'G#']
weak = ['A#', 'C#', 'F', 'C', 'B', 'D#', 'E']
naturals = list(set(all) - set(test_seq))


# initialize terminal colors
init()


# 32 notes for each tone, target note added 4, 5 or  times
def gen_seq(target, k=28, add=(4, 5, 6)):
    seq = list(all)
    seq.remove(target)
    seq = random.choices(seq, k=k)
    add = random.choice(add)
    for i in range(add):
        seq.append(target)
    random.shuffle(seq)
    return seq


def play(path):
    data, fs = sf.read(path, frames=10 ** 5)
    sd.play(data, fs, blocking=True)


def run_seq(test_seq, hard=False, speed=1.5):
    for target in test_seq:
        print('target: ', target)
        target_seq = gen_seq(target) if not hard else gen_seq(target, 72)

        if target in naturals:
            play('./notes/sung/{}s.wav'.format(target))
            time.sleep(0.1)
        else:
            play('./notes/sung/{}.wav'.format(target))

        time.sleep(0.7)

        for note in target_seq:
            path = "./notes/" + note + '/' + random.choice(os.listdir("./notes/" + note + "/"))
            play(path)

            time.sleep(speed)

            if note == target:
                print(colored('that was the target note', 'green'))
            else:
                if len(sys.argv) >= 3:
                    if sys.argv[2] == 'D':
                        out = note
                        if out == 'C#':
                            out = 'Db'
                        elif out == 'D#':
                            out = 'Eb'
                        elif out == 'G#':
                            out = 'Ab'
                        elif out == 'A#':
                            out = 'Bb'
                        print(colored('that was not the target note ({})'.format(out), 'red'))
                else:
                    print(colored('that was not the target note', 'red'))




def run(test_seq):
    if len(sys.argv) == 1:
        sys.argv.append('A')
        sys.argv.append('D')

    if len(sys.argv) >= 2:
        if sys.argv[1] == 'F':
            random.shuffle(test_seq)
            run_seq(test_seq, speed=0.4)

        elif sys.argv[1] == 'S':
            random.shuffle(test_seq)            
            run_seq(test_seq, speed=1.5)

        else:
            test_seq = [input('What pitch to test? ')]
            hard = True if input('Hard mode? ') == 'Y' else False
            run_seq(test_seq, hard)

run(all)
run(all)