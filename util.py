# init
import os
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.gridspec as gridspec
import numpy as np
# packages for PyTorch
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, TensorDataset
import torch.nn.functional as F
import random
from sklearn.utils import shuffle

if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
print("Using device:", device)

# Genre Mapping
game_map={} # shooter, rpg, racing, strategy, puzzle
game_map['Advance Wars'] = 'strategy'
game_map['Apex Legends'] = 'shooter'
game_map['Assetto Corsa'] = 'racing'
game_map['Automobilista 2'] = 'racing'
game_map['Bad Rats'] = 'puzzle'
game_map['Baldur\'s Gate 3'] = 'rpg'
game_map['Ballisticng'] = 'racing'
game_map['BATTLEFIELD 1'] = 'shooter'
game_map['BeamNG.drive'] = 'racing'
game_map['Cities Skylines'] = 'strategy'
game_map['Civilization VI'] = 'strategy'
game_map['Company of Heroes 2'] = 'strategy'
game_map['Counter-strike  Global Offensive'] = 'shooter'
game_map['Counter-strike 2'] = 'shooter'
game_map['Crying Suns'] = 'strategy'
game_map['Dead Cells'] = 'rpg'
game_map['Destiny 2'] = 'shooter'
game_map['Dirt Rally 2'] = 'racing'
game_map['Dirt Rally'] = 'racing'
game_map['Dr Mario'] = 'puzzle'
game_map['Dragon Quest XI'] = 'rpg'
game_map['Elden Ring'] = 'rpg'
game_map['Elite Dangerous'] = 'rpg'
game_map['Enter the Gungeon'] = 'shooter'
game_map['Europa Universalis IV'] = 'strategy'
game_map['Final Fantasy VII'] = 'rpg'
game_map['Fortnite'] = 'shooter'
game_map['Forza Horizon 5'] = 'racing'
game_map['F-Zero GX'] = 'racing'
game_map['F-Zero 99 '] = 'racing'
game_map['Gears Of War'] = 'shooter'
game_map['Half-Life 2'] = 'shooter'
game_map['Hearts of Iron IV'] = 'strategy'
game_map['Hell Let Loose'] = 'shooter'
game_map['Insurgency Sandstorm'] = 'shooter'
game_map['Lumines Arise'] = 'puzzle'
game_map['Lumines PSP'] = 'puzzle'
game_map['Mario Kart World'] = 'racing'
game_map['MAX PAYNE'] = 'shooter'
game_map['Metal Gear Solid V  The Phantom Pain'] = 'shooter'
game_map['Modded Minecraft'] = 'strategy'
game_map['Morrowind'] = 'rpg'
game_map['Picross 3D'] = 'puzzle'
game_map['Pokemon Green'] = 'rpg'
game_map['Puyo Puyo Tetris'] = 'puzzle'
game_map['Quake III Arena'] = 'shooter'
game_map['Remnant  From the Ashes'] = 'shooter'
game_map['Satisfactory'] = 'puzzle'
game_map['Satisfactory'] = 'puzzle'
game_map['Sea of Thieves'] = 'shooter'
game_map['Skyrim Special Edition'] = 'rpg'
game_map['Spec Ops The Line'] = 'shooter'
game_map['StarCraft II'] = 'strategy'
game_map['Tetris Effect'] = 'puzzle'
game_map['The Finals'] = 'shooter'
game_map['The Legend of Zelda： Link\'s Awakening'] = 'rpg'
game_map['Titanfall2'] = 'shooter'
game_map['Tom Clancy\'s Rainbow Six  Siege'] = 'shooter'
game_map['Warframe'] = 'rpg'
game_map['Wipeout Pure'] = 'racing'
game_map['Wrc'] = 'racing'

game_map['racing'] = 'racing'
game_map['puzzle'] = 'puzzle'
game_map['shooter'] = 'shooter'
game_map['strategy'] =  'strategy'
game_map['rpg'] = 'rpg'

def get_genre(filename):
    genre = game_map[get_title(filename)]
    return genre

def get_title(filename):
    game_name = filename.split(';;')[0]
    return game_name

def n_games(genre, images): # n games in set
    distinct = set()
    for image in images[1]:
        if get_genre(image) == genre:
            distinct.add(get_title(image))
    return len(distinct)