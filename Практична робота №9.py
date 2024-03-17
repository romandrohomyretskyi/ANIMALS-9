''''Клас BrownBear наслідує метод appearance() як від Herbivores, так і від Carnivores через клас Beers.
Коли Python знаходить метод appearance у класі Beers, він використовує перший метод який знаходить у своєму ланцюжку успадкування
А з класом Cobra проблем немає, то причині наслідування тільки від CoolBlooded'''



class Animals:
    def appearance(self):
        return "Це тварина"

class Herbivores(Animals):
    def appearance(self):
        return "Це травоїдна тварина"

class Carnivores(Animals):
    def appearance(self):
        return "Це хижа тварина"

class WarmBlooded(Animals):
    def appearance(self):
        return "Це теплокровна тварина"

class CoolBlooded(Animals):
    def appearance(self):
        return "Це холоднокровна тварина"

class Artiodactyls(Herbivores, WarmBlooded):
    def appearance(self):
        return "Ця тварина має копита"

class Beers(Herbivores, Carnivores, WarmBlooded):
    pass

class Snakes(CoolBlooded, Carnivores):
    pass

class Cows(Artiodactyls):
    pass

class BrownBear(Beers):
    pass

class GrizzlyBear(Beers):
    pass

class Poisonus(Snakes):
    pass
    
class Cobra(Poisonus):
    pass

class Nonpoisonus(Snakes):
    pass

class Adcler(Nonpoisonus):
    pass

Кобра = Cobra()
print (Кобра.appearance())
МішаБурий = BrownBear()
print (МішаБурий.appearance())
