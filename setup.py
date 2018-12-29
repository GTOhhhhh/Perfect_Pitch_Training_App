import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

packages = ['soundfile', 'sounddevice', 'termcolor', 'colorama']

for package in packages:
    install(package)