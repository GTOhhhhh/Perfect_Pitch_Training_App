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
weak = ['A#', 'C#', 'F', 'F#', 'G#']
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


def run_seq(test_seq, hard=False):
    for target in test_seq:
        print('target: ', target)
        target_seq = gen_seq(target) if not hard else gen_seq(target, 72)

        if target in naturals:
            play('./notes/sung/{}s.wav'.format(target))
            time.sleep(0.1)
        else:
            play('./notes/sung/{}.wav'.format(target))

        time.sleep(0.5)

        for note in target_seq:
            path = "./notes/" + note + '/' + random.choice(os.listdir("./notes/" + note + "/"))
            play(path)
            time.sleep(1.5)
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

            time.sleep(.1)



def run(test_seq):
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'A':
            random.shuffle(test_seq)
            run_seq(test_seq)

        else:
            test_seq = [input('What pitch to test? ')]
            hard = True if input('Hard mode? ') == 'Y' else False
            run_seq(test_seq, hard)


run(all)
run(all)

# to remove octave numbers
# regex = re.compile('[^a-zA-Z]')
# [regex.sub('', i) for i in pitches]
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
