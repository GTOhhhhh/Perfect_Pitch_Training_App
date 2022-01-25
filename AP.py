import soundfile as sf
import sounddevice as sd
import time
import random
import os
import sys
from termcolor import colored
from colorama import init

all = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
sharps = ['A#', 'C#', 'D#', 'F#', 'G#']
temp = ['A#', 'F', 'C', 'C#', 'A', 'D']
# weak = ['G#', 'A#', 'C', 'C#',  'D#']
# weak = ['A', 'A#', 'B', 'C', 'C#']
weak = ['D']

weak = list(reversed(weak))
naturals = list(set(all) - set(sharps))

# initialize terminal colors
init()


# 32 notes for each tone, target note added 4, 5 or  times
def gen_seq(target, k=180, add=12):
    seq = list(all)
    seq.remove(target)
    seq = random.choices(seq, k=k)
    for i in range(add):
        seq.append(target)
    random.shuffle(seq)
    return seq


def play(path):
    data, fs = sf.read(path, frames=10 ** 5)
    sd.play(data, fs, blocking=False)


def run_seq(test_seq, hard=False, speed=0.7, display=False):
    for target in test_seq:
        print('target: ', target)
        target_seq = gen_seq(target) if not hard else gen_seq(target, 90)

        # if target in naturals:
        #     play('./notes/sung/{}s.wav'.format(target))
        #     time.sleep(0.1)
        # else:
        #     play('./notes/sung/{}.wav'.format(target))

        time.sleep(2.5)

        for note in target_seq:
            path = "./notes/" + note + '/' + random.choice(os.listdir("./notes/" + note + "/"))
            print(path)
            play(path)

            time.sleep(speed)
            
            if note == target:
                print(colored('that was the target note', 'green'))
            else:
                if display:
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
    args = len(sys.argv)
    display = False
    speed = 0.68
    if args == 1:
        sys.argv.append('A')
    if args >= 2:
        print(sys.argv[1])
        if sys.argv[2] == 'F':
            speed = 1.35
        elif sys.argv[2] == 'S':
            speed = 1.8
    if args >= 3:
        if sys.argv[2] == 'W':
            test_seq = weak
            print(f"{test_seq}")
        elif sys.argv[2] == 'D':
            display = True

    if args >= 4:
        if sys.argv[3] == 'D':
            display = True
    random.shuffle(test_seq)
    run_seq(test_seq, speed=speed, display=display)

    # else:
    #     test_seq = [input('What pitch to test? ')]
    #     hard = True if input('Hard mode? ') == 'Y' else False
    #     run_seq(test_seq, hard)
    #     return


run(all)

