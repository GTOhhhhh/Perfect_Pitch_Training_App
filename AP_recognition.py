import soundfile as sf
import sounddevice as sd
import time
import random
import os
from termcolor import colored
from colorama import init

all = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
test_seq = ['A#', 'C#', 'D#', 'F#', 'G#']

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

        for i in range(3):
            play('./notes/' + target + '/{}.wav'.format(target))

        for note in target_seq:
            path = "./notes/" + note + '/' + random.choice(os.listdir("./notes/" + note + "/"))
            play(path)
            time.sleep(1.25)
            if note == target:
                print(colored('that was the target note', 'green'))
            else:
                print(colored('that was not the target note', 'red'))
            time.sleep(.5)


def run(test_seq):
    resp = input('Press S for single tone or A for all ')
    if resp == 'A':
        if input('Shuffle? ') == 'Y':
            random.shuffle(test_seq)
        run_seq(test_seq)

    else:
        test_seq = [input('What pitch to test? ')]
        hard = True if input('Hard mode? ') == 'Y' else False
        run_seq(test_seq, hard)


run(test_seq)
run(test_seq)

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
