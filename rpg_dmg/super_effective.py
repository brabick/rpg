# ------------------------------------------------------------------------ #
# Below is the type chart.  It is a dictionary that maps a type to the
# multiplier to determine how much stronger an attack will be based on typing
# 2 is super effective, 1 is neutral, .5 is resisted 0 is immune
# think of it as name of dictionary (i.e. grass) v key in dictionary
# ------------------------------------------------------------------------ #

grass = {
    "grass": .5,
    "fire": .5,
    "water": 2,
    "normal": 1,
    "fighting": 1,
    "flying": .5,
    "poison": .5,
    "ground": 2,
    "rock": 2,
    "bug": .5,
    "ghost": 1,
    "steel": .5,
    "electric": 1,
    "psychic": 1,
    "ice": 1,
    "dragon": .5,
    "dark": 1,
    "fairy": 1
}

water = {
    "grass": .5,
    "fire": 2,
    "water": .5,
    "normal": 1,
    "fighting": 1,
    "flying": 1,
    "poison": 1,
    "ground": 2,
    "rock": 2,
    "bug": 1,
    "ghost": 1,
    "steel": 1,
    "electric": 1,
    "psychic": 1,
    "ice": 1,
    "dragon": .5,
    "dark": 1,
    "fairy": 1
}

fire = {
    "grass": 2,
    "fire": .5,
    "water": .5,
    "normal": 1,
    "fighting": 1,
    "flying": 1,
    "poison": 1,
    "ground": 1,
    "rock": .5,
    "bug": 2,
    "ghost": 1,
    "steel": 2,
    "electric": 1,
    "psychic": 1,
    "ice": 2,
    "dragon": .5,
    "dark": 1,
    "fairy": 1
}

rock = {
    "grass": 1,
    "fire": 2,
    "water": 1,
    "normal": 1,
    "fighting": .5,
    "flying": 2,
    "poison": 1,
    "ground": .5,
    "rock": 1,
    "bug": 2,
    "ghost": 1,
    "steel": .5,
    "electric": 1,
    "psychic": 1,
    "ice": 2,
    "dragon": 1,
    "dark": 1,
    "fairy": 1
}

ground = {
    "grass": .5,
    "fire": 2,
    "water": 1,
    "normal": 1,
    "fighting": 1,
    "flying": 0,
    "poison": 2,
    "ground": 1,
    "rock": 2,
    "bug": .5,
    "ghost": 1,
    "steel": 2,
    "electric": 2,
    "psychic": 1,
    "ice": 1,
    "dragon": 1,
    "dark": 1,
    "fairy": 1
}

ice = {
    "grass": 2,
    "fire": .5,
    "water": .5,
    "normal": 1,
    "fighting": 1,
    "flying": 2,
    "poison": 1,
    "ground": 2,
    "rock": 1,
    "bug": 1,
    "ghost": 1,
    "steel": .5,
    "electric": 2,
    "psychic": 1,
    "ice": .5,
    "dragon": 2,
    "dark": 1,
    "fairy": 1
}

normal = {
    "grass": 1,
    "fire": 1,
    "water": 1,
    "normal": 1,
    "fighting": 1,
    "flying": 1,
    "poison": 1,
    "ground": 1,
    "rock": .5,
    "bug": 1,
    "ghost": 0,
    "steel": .5,
    "electric": 1,
    "psychic": 1,
    "ice": 1,
    "dragon": 1,
    "dark": 1,
    "fairy": 1
}

fighting = {
    "grass": .5,
    "fire": 1,
    "water": 1,
    "normal": 2,
    "fighting": 1,
    "flying": .5,
    "poison": .5,
    "ground": 1,
    "rock": 2,
    "bug": .5,
    "ghost": 0,
    "steel": 2,
    "electric": 1,
    "psychic": .5,
    "ice": 2,
    "dragon": 1,
    "dark": 2,
    "fairy": .5
}

flying = {
    "grass": 2,
    "fire": 1,
    "water": 1,
    "normal": 1,
    "fighting": 2,
    "flying": 1,
    "poison": 1,
    "ground": 1,
    "rock": .5,
    "bug": 2,
    "ghost": 1,
    "steel": .5,
    "electric": .5,
    "psychic": 1,
    "ice": 1,
    "dragon": 1,
    "dark": 1,
    "fairy": 1
}

poison = {
    "grass": 2,
    "fire": 1,
    "water": 1,
    "normal": 1,
    "fighting": 1,
    "flying": 1,
    "poison": .5,
    "ground": .5,
    "rock": 1,
    "bug": 1,
    "ghost": 1,
    "steel": 0,
    "electric": 1,
    "psychic": 1,
    "ice": 1,
    "dragon": 1,
    "dark": 1,
    "fairy": 2
}

bug = {
    "grass": 2,
    "fire": .5,
    "water": 1,
    "normal": 1,
    "fighting": .5,
    "flying": .5,
    "poison": .5,
    "ground": 1,
    "rock": 2,
    "bug": .5,
    "ghost": .5,
    "steel": .5,
    "electric": 1,
    "psychic": 2,
    "ice": 1,
    "dragon": 1,
    "dark": 2,
    "fairy": .5
}

ghost = {
    "grass": 1,
    "fire": 1,
    "water": 1,
    "normal": 0,
    "fighting": 1,
    "flying": 1,
    "poison": 1,
    "ground": 1,
    "rock": 1,
    "bug": 1,
    "ghost": 2,
    "steel": 1,
    "electric": 1,
    "psychic": 2,
    "ice": 1,
    "dragon": 1,
    "dark": .5,
    "fairy": 1
}

steel = {
    "grass": 1,
    "fire": .5,
    "water": .5,
    "normal": 1,
    "fighting": 1,
    "flying": 1,
    "poison": 1,
    "ground": 1,
    "rock": 2,
    "bug": 1,
    "ghost": 1,
    "steel": .5,
    "electric": .5,
    "psychic": 1,
    "ice": 2,
    "dragon": 1,
    "dark": 1,
    "fairy": 2
}

electric = {
    "grass": .5,
    "fire": 1,
    "water": 2,
    "normal": 1,
    "fighting": 1,
    "flying": 2,
    "poison": 1,
    "ground": 0,
    "rock": 1,
    "bug": 1,
    "ghost": 1,
    "steel": 1,
    "electric": .5,
    "psychic": 1,
    "ice": 1,
    "dragon": 1,
    "dark": 1,
    "fairy": 1
}

psychic = {
    "grass": 1,
    "fire": 1,
    "water": 1,
    "normal": 1,
    "fighting": 2,
    "flying": 1,
    "poison": 2,
    "ground": 1,
    "rock": 1,
    "bug": 1,
    "ghost": 1,
    "steel": .5,
    "electric": 1,
    "psychic": .5,
    "ice": 1,
    "dragon": 1,
    "dark": 0,
    "fairy": 1
}

dragon = {
    "grass": 1,
    "fire": 1,
    "water": 1,
    "normal": 1,
    "fighting": 1,
    "flying": 1,
    "poison": 1,
    "ground": 1,
    "rock": 1,
    "bug": 1,
    "ghost": 1,
    "steel": .5,
    "electric": 1,
    "psychic": 1,
    "ice": 1,
    "dragon": 2,
    "dark": 1,
    "fairy": 0
}

dark = {
    "grass": 1,
    "fire": 1,
    "water": 1,
    "normal": 1,
    "fighting": .5,
    "flying": 1,
    "poison": 1,
    "ground": 1,
    "rock": 1,
    "bug": 1,
    "ghost": 2,
    "steel": 1,
    "electric": 1,
    "psychic": 2,
    "ice": 1,
    "dragon": 1,
    "dark": .5,
    "fairy": .5
}

fairy = {
    "grass": 1,
    "fire": .5,
    "water": 1,
    "normal": 1,
    "fighting": 2,
    "flying": 1,
    "poison": .5,
    "ground": 1,
    "rock": 1,
    "bug": 1,
    "ghost": 1,
    "steel": .5,
    "electric": 1,
    "psychic": 1,
    "ice": 1,
    "dragon": 2,
    "dark": 2,
    "fairy": 1
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
        return multiplier

    elif mon_type == fire:
        multiplier = attack_type['fire']
        return multiplier

    elif mon_type == water:
        multiplier = attack_type['water']
        return multiplier

    elif mon_type == ice:
        multiplier = attack_type['ice']
        return multiplier

    elif mon_type == rock:
        multiplier = attack_type['rock']
        return multiplier

    elif mon_type == ground:
        multiplier = attack_type['ground']
        return multiplier

    elif mon_type == fighting:
        multiplier = attack_type['fighting']
        return multiplier

    elif mon_type == poison:
        multiplier = attack_type['poison']
        return multiplier

    elif mon_type == bug:
        multiplier = attack_type['bug']
        return multiplier

    elif mon_type == ghost:
        multiplier = attack_type['ghost']
        return multiplier

    elif mon_type == steel:
        multiplier = attack_type['steel']
        return multiplier

    elif mon_type == electric:
        multiplier = attack_type['electric']
        return multiplier

    elif mon_type == psychic:
        multiplier = attack_type['psychic']
        return multiplier

    elif mon_type == dragon:
        multiplier = attack_type['dragon']
        return multiplier

    elif mon_type == dark:
        multiplier = attack_type['dark']
        return multiplier

    elif mon_type == fairy:
        multiplier = attack_type['fairy']
        return multiplier
    
    elif mon_type == normal:
        multiplier = attack_type['normal']
        return multiplier

    elif mon_type == flying:
        multiplier = attack_type['flying']
        return multiplier
