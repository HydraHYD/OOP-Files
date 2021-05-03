from pyPokemon import *
from pyTrainer import *
import random as r

Ponyta = Pokemon('Ponyta', 'Fire', None, 'Rapidash', [2,20,200,2000,2000,2000])
Rapidash = Pokemon('Rapidash', 'Fire', None, None, [3,30,300,3000,3000,3000])

Ponyta.evolve(Rapidash)
Ponyta.ivmod(28)

for i in Ponyta.stats:
    print(i)
trainerBadges = ['Stone', '', '', '', '', '', '', '']
Gold = Trainer('Gold', trainerBadges ,0)
Gold.newPokemon(Rapidash)

