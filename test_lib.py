from Module import Person, Wizard, HealthPotion


def test_Person_name():
    value = Person('James')
    except_value = 'James'
    assert value.name == except_value


def test_Person_life():
    value = Person('James')
    assert value.life_points == 100


def test_Person_a_life():
    james = Person('James')
    assert james.is_dead() == False


def test_Person_hit_Person():
    attacker = Person('James')
    defender = Person('Bond')
    attacker.hit(defender)
    defender.life_points
    assert defender.life_points == 90


def test_Person_hit_low():
    attacker = Person('James')
    defender = Person('Bond')
    for i in range(0, 10):
        attacker.hit(defender)
    assert defender.life_points == 0


def test_Wizard_hit_Person():
    attacker = Wizard('James')
    defender = Person('Bond')
    attacker.hit(defender)
    assert defender.life_points == 85


def test_Person_hit_Wizard():
    attacker = Person('James')
    defender = Wizard('Bond')
    attacker.hit(defender)
    assert defender.life_points == 70


def test_Person_hit_Person_dead():
    attacker = Person('James')
    defender = Person('Bond')
    for i in range(0, 10):
        attacker.hit(defender)
    defender.life_points
    assert defender.is_dead() == True


def test_Person_dead():
    defender = Person('James')
    defender.life_points = 0
    assert defender.is_dead() == True


def test_gained_life_points_30():
    james = Person('James')
    james.gained_life_points(30)
    result = james.life_points
    except_result = 130
    assert except_result == result


def test_gained_life_points_health_potion_on_Person():
    james = Person('James')
    life_points_before = james.get_life_points()
    popo = HealthPotion()
    life_given = popo.get_given_life_points()
    popo.was_used_by(james)
    result = james.life_points
    except_result = life_points_before + life_given
    assert result == except_result

def test_gained_life_points_health_potion_on_Wizard():
    james = Wizard('James')
    life_points_before = james.get_life_points()
    popo = HealthPotion()
    life_given = popo.get_given_life_points()
    popo.was_used_by(james)
    result = james.life_points
    except_result = life_points_before + life_given
    assert result == except_result

# test_gained_life_points_health_potion_on_Wizard()
