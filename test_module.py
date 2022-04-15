from Module import Person, Wizard, HealthPotion

def test_person():
    person = Person("person")

    # a person have a name
    assert person.name == "person", "a person should have a name"

    # a person can hit, loose hp and die
    assert person.get_life_points() == person.life_points, "get_life_points should return hp"
    assert person.get_life_points() == 100, "a person should have 100 base hp"

    for _ in range(10):
        person.hit(person)

    assert person.get_life_points() == 0, "a person should hit and loose 10hp"
    assert person.is_dead(), "a person should be dead after loosing all his hp"
    
    # a person can heal and revive
    person.life_points = 0
    person.gained_life_points(10)
    assert person.get_life_points() == 10, "a person can be healed"
    assert not person.is_dead(), "a person can be revived"

def test_wizard():
    wizard = Wizard("wizard")

    # a wizard have a name
    assert wizard.name == "wizard", "a wizard should have a name"

    # a wizard can hit, loose hp and die
    assert wizard.get_life_points() == wizard.life_points, "get_life_points should return hp"
    assert wizard.get_life_points() == 80, "a wizard should have 100 base hp"

    for _ in range(6):
        wizard.hit(wizard)

    assert wizard.get_life_points() == -10, "a wizard should hit and loose 15hp"
    assert wizard.is_dead(), "a wizard should be dead after loosing all his hp"
    
    # a wizard can heal and revive
    wizard.life_points = 0
    wizard.gained_life_points(10)
    assert wizard.get_life_points() == 10, "a person can be healed"
    assert not wizard.is_dead(), "a person can be revived"

def test_health_potion():
    person = Person("lambda")
    HealthPotion.was_used_by(person)

    assert person.life_points == 110, "potion should heal 10hp"

""
