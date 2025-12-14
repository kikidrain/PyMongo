
class Entity: #entity pour éviter du code inutiles avec class perso et monstre 
    def __init__(self, name, attack, defense, health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = health
        self.health = health
    
    def __str__(self):
        return f"{self.name} - {self.attack} ATK - {self.defense} DEF - {self.health} HEALTH"
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        reduction = self.defense * 0.15
        actual_damage = int(max(1, damage - reduction))
        self.health -= actual_damage
        if self.health < 0:
            self.health = 0
        return actual_damage
    
    def attack_target(self, target):
        return target.take_damage(self.attack)