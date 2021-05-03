from pyItem import *

class Trainer():
    def __init__(self, name, badges, money):
        self.name = name
        self.badges = badges
        self.money = money
        self.pokemon = []
        self.team = [0,0,0,0,0,0]
        self.inventory = []

    def addMoney(self, amount):
        self.money += amount

    def newPokemon(self, pokemon):
        if pokemon.wild = False:
            self.pokemon.append(pokemon)

    def setTeam(self, p1, p2, p3, p4, p5, p6):
        p1 = self.team[0]
        p2 = self.team[1]
        p3 = self.team[2]
        p4 = self.team[3]
        p5 = self.team[4]
        p6 = self.team[5]
    
    def teamRemove(self, pos):
        self.team.pop(pos)

    def newItem(self, item):
        self.inventory.append[item]

    def useItem(self, pos, pokemon):
        self.inventory[pos].useItem(pokemon)
        self.inventory.pop(pos)

