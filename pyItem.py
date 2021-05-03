import random as r
from pyTrainer import *

class Item():
    def __init__(self, Name, Value):
        self.Name = Name
        self.Value = Value

class Pokeball(Item):
    def setVariables(self, catchRate):
        self.catchRate = catchRate

    def useItem(self, pokemon):
        if pokemon.wild == True:
            if r.randint(0,100) < catchRate:
                pokemon.wild = False



        