class Perso:
    
    def __init__(self, name, attack, defense, health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.max_health = health
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def take_damage(self, damage):
        degats = damage - self.defense
        if degats < 0:
            degats = 0
        self.health = self.health - degats
        if self.health < 0:
            self.health = 0
        return degats
    
    def attack_target(self, target):
        degats_infliges = target.take_damage(self.attack)
        return degats_infliges

class Monstre