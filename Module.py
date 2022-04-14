class Person:
    def __init__(self, name):
        self.name = name
        self.life_points = 100
        
    def hit(self, person):
        person.life_points -= 10
        
    def is_dead(self):
        if self.life_points > 0 :
            return False
        return True
        
    def gained_life_points(self, amount):
        self.life_points += amount
        
    def get_life_points(self):
        
        return self.life_points

class Wizard(Person):
    def __init__(self, name):
        super().__init__(name)
        self.life_points = 80
        
    def hit(self, person):
        person.life_points -= 15
        return person
        
        
class HealthPotion:
    def __init__(self):
        self.life_given=10
        
    def get_given_life_points(self):
        return self.life_given
    
    def was_used_by(self, person):
        person.gained_life_points(10)