"""
realtime midi play-along with RL
model based on https://arxiv.org/pdf/2002.03082.pdf
trained on bach chorales
"""

# from tensorforce import Agent, Environment
from midiData.midiLoader import Midi_loader


# preprocess data (like in paper)
environment = Midi_loader()

environment.sample_random_csv()

print()
# make data feeding pipeline (this is the environemnt)


# make model (like in paper)


# train on google colab

