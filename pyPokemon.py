class Pokemon():
    def __init__(self, name, type1, type2, nextstage, stats):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.nextstage = nextstage
        self.stats = stats
    
    def evolve(self, newPokemon):
        if self.nextstage == newPokemon.name:
            self.name = newPokemon.name
            self.type1 = newPokemon.type1
            self.type2 = newPokemon.type2
            self.nextstage = newPokemon.nextstage
            self.stats = newPokemon.stats

    def ivmod(self, modifier):
        self.modifier = modifier
        if self.modifier < 0:
            self.modifier = 0
        if self.modifier > 31:
            self.modifier = 31
        for i in self.stats:
            pos = self.stats.index(i)
            self.stats[pos] = i * (self.modifier/31)
            

    
    

    






