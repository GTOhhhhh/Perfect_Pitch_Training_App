import soundfile as sf
import sounddevice as sd
import random
import csv
from datetime import datetime as dt

# piano samples
all_pitches = ['C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4', 'C5', 'Db5', 'D5', 'Eb5',
               'E5', 'F5', 'Gb5', 'G5', 'Ab5', 'A5', 'Bb5', 'B5']
pitches = ['C4', 'D4', 'E4', 'F4', 'G4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A4', 'A5']

# to remove octave numbers
# regex = re.compile('[^a-zA-Z]')
#[regex.sub('', i) for i in pitches]

def play_pitches(pitches):
    answers = []
    responses = []
    input('Press any key to hear the first pitch. ')
    pitch = random.choice(pitches)
    answers.append(pitch)
    while True:
        data, fs = sf.read('./piano/' + pitch + '.aiff', frames=10 ** 5)
        sd.play(data, fs, blocking=True)
        res = input('Press enter to hear the pitch again. Otherwise input your answer.\n')
        if not res:
            continue
        confirm = input('You answered {}, press enter to confirm. '.format(res))
        if not confirm:  # enter will give an empty string, not confirm -> confirmed
            responses.append(res)
            end = input('Answer recorded. Press q to quit or any key to hear another pitch. ')
            if end == 'q':
                break
            else:
                pitch = random.choice(pitches)
                answers.append(pitch)
                continue
        else:
            continue  # go back to play the tone again
    modded = [i[:-1] for i in answers]
    count = 0
    session_time = dt.now()
    with open('log.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for idx, response in enumerate(responses):
            if modded[idx] == response:
                count += 1
            writer.writerow([response, modded[idx], answers[idx], session_time, pitches])

    print('\nYour answers', responses)
    print('Correct answers', answers)
    print('{}/{} correct. '.format(count, len(answers)))




if __name__ == '__main__':
    play_pitches(pitches)
