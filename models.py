
class Entity: #entity pour éviter du code inutiles avec class perso et montre 
    def __init__(self, name, attack, defense, health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = health
        self.health = health
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        if self.health < 0:
            self.health = 0
        return actual_damage
    
    def attack_target(self, target):
        return target.take_damage(self.attack)
