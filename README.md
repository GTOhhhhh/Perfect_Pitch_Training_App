# Perfect Pitch Training App
A simple app for practising absolute (perfect) pitch recognition. The app plays a series of random pitches sampled from multiple octaves
and a variety of instruments. In each sequence the target note is played 3-5 times interspersed with the random pitches.
The goal is to memorize the target pitch. After a short delay (1.7 seconds) a red message ('that was not the target pitch') or a green
message ('that was the targe pitch'). This is intended to facilitate memorizing the sound of the pitch without using relative pitch.

## Getting Started
- run setup.py to install required python packages
- run AP.py to launch

if you are on linux install following to satsify sounddevice dependencies:
sudo apt-get install libportaudio2


e.g. python AP.py X D

first argument can be X (prompt user to enter the pitch they wish to train) or A (all 12 pitches in random order)
second argument is optional to display the pitch that just played along with the target note message. i.e. 'that was not the target note (A)'

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

