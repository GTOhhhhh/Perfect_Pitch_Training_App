import soundfile as sf
import sounddevice as sd
import time
import random
import os
import sys
from termcolor import colored
from colorama import init

# all = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
scale = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C#', 'C', 'D', 'D#']
scale = scale[::-1]
fixed = ['C#', 'F', 'A#', 'C', 'A', 'D#', 'B', 'F#', 'G#', 'E', 'D', 'G']
sharps = ['A#', 'C#', 'D#', 'F#', 'G#']
# weak = ['G#', 'A#', 'C', 'C#',  'D#']
weak = ['A', 'A#', 'B', 'C', 'C#']
weak = reversed(weak)
naturals = list(set(scale) - set(sharps))

# initialize terminal colors
init()


# 32 notes for each tone, target note added 4, 5 or  times
def gen_seq(target, k=90, add=14):
    seq = list(scale)
    seq.remove(target)
    seq = random.choices(seq, k=k)
    for i in range(add):
        seq.append(target)
    random.shuffle(seq)
    return seq


def gen_seq_acc(targets, k=90, add=14):
    seq = list(set(scale) - set(targets))
    seq = random.choices(seq, k=k)
    # print(seq)
    # print(targets*add)
    for i in range(add):
        seq.extend(targets)
    random.shuffle(seq)
    # print(seq)
    return seq


def play(path):
    data, fs = sf.read(path, frames=10 ** 5)
    sd.play(data, fs, blocking=False)


def accumulate_seq(test_seq, hard=False, speed=0.65):
    targets = []
    for idx, target in enumerate(test_seq):
        if idx == 0:
            continue
        # accumulate targets
        # active targets have note name displayed and green text
        targets.append(target)

        if len(targets) < 2:
            targets.append(test_seq[idx-1])
            targets = targets[::-1]
        if len(targets) > 3:
            targets.pop(0)
        print('targets: ', targets)
        target_seq = gen_seq_acc(targets) if not hard else gen_seq(target, 90)

        time.sleep(2.5)

        for note in target_seq:
            # print(note)
            path = "./notes/" + note + '/' + random.choice(os.listdir("./notes/" + note + "/"))
            play(path)

            time.sleep(speed)

            if note in targets:
                if note == 'C#':
                    note = 'Db'
                elif note == 'D#':
                    note = 'Eb'
                elif note == 'G#':
                    note = 'Ab'
                elif note == 'A#':
                    note = 'Bb'
                print(colored('that was the target note ({})'.format(note), 'green'))
            else:
                print(colored('that was not the target note', 'red'))


def run_seq(test_seq, hard=False, speed=0.65, display=False):
    for target in test_seq:
        print('target: ', target)
        target_seq = gen_seq(target) if not hard else gen_seq(target, 90)

        time.sleep(2.5)
        for note in target_seq:
            path = "./notes/" + note + '/' + random.choice(os.listdir("./notes/" + note + "/"))
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


def run(notes):
    # args = len(sys.argv)
    # display = False
    # speed = 0.75
    # if args == 1:
    #     sys.argv.append('A')
    # if args >= 2:
    #     print(sys.argv[1])
    #     if sys.argv[2] == 'F':
    #         speed = 0.75
    #     elif sys.argv[2] == 'S':
    #         speed = 1.8
    # if args >= 3:
    #     if sys.argv[2] == 'W':
    #         notes = weak
    #         print(f"{notes}")
    #     elif sys.argv[2] == 'D':
    #         display = True
    #
    # if args >= 4:
    #     if sys.argv[3] == 'D':
    #         display = True
    # random.shuffle(notes)
    accumulate_seq(notes, False, 0.78)
    # run_seq(test_seq, speed=speed, display=display)

    # else:
    #     test_seq = [input('What pitch to test? ')]
    #     hard = True if input('Hard mode? ') == 'Y' else False
    #     run_seq(test_seq, hard)
    #     return


run(scale)
