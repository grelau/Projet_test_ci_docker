from Module import Person, Wizard, HealthPotion
import numpy as np

user_1 = Person("Hero")
user_2 = Wizard("Wizard")
"sdf"
while user_1.is_dead() == False and user_2.is_dead() == False:
    random = np.random.randint(2)
    
    if random == 1:
        user_1.hit(user_2)
    else:
        user_2.hit(user_1)

    random_health_potion_use = np.random.randint(3)
        
    if random_health_potion_use == 0:
        HealthPotion.was_used_by(user_1)
    elif random_health_potion_use == 1:
        HealthPotion.was_used_by(user_2)
    else:
        pass

if user_1.get_life_points() <= 0:
    print(user_1.name + " wins")
if user_2.get_life_points() <= 0:
    print(user_2.name + " wins")


