# ------------------------------------------------------------------------ #
# Below is the type chart.  It is a dictionary that maps a type to the
# multiplier to determine how much stronger an attack will be based on typing
# 2 is super effective, 1 is neutral, .5 is resisted 0 is immune
# ------------------------------------------------------------------------ #

grass = {
    "grass": .5,
    "fire": .5,
    "water": 2
}
water = {
    "grass": .5,
    "fire": 2,
    "water": .5
}
fire = {
    "grass": 2,
    "fire": .5,
    "water": .5
}


def effective(attack_type, mon_type):

    # ------------------------------------------------------------------------ #
    # Takes the mon type and decides how to find the multiplier. It will place
    # a string representation of the pokemon's type into the dictionary
    # where the attack type is the is a stand in for the specific
    # type dictionary.
    # ------------------------------------------------------------------------ #

    if mon_type == grass:

        multiplier = attack_type['grass']
        print(multiplier)
        return multiplier

    elif mon_type == fire:

        multiplier = attack_type['fire']
        print(multiplier)
        return multiplier
    elif mon_type == water:

        multiplier = attack_type['water']
        print(multiplier)
        return multiplier