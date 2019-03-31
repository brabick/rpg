# ------------------------------------------------------------------------ #
# Author: Brandon Bickerton
# Python Version: 3.7.2
# Description: This is meant to be a basic version of battling
# based on the Pokemon game series.
# This is designed to be easily expandable.
# ------------------------------------------------------------------------ #

from random import randint

# This is not pokemon
# the only types so far
type_list = ['fire', 'water', 'grass']
# empty list for attacks they get added from the attack class below
attack_list = []
# creating the pokemon class
mon_list = []


# ------------------------------------------------------------------------ #
# Initial class used to make pokemon
# Initializes variables to make them accesible later in
# Program
# ------------------------------------------------------------------------ #

class mon:
    # default dead = false
    def __init__(self, mon_name, mon_type1, mon_type2, hp_stat, atk_stat, spd_stat, mon_attack_list, dead=False):
        self.dead = dead
        self.mon_name = mon_name
        self.hp_stat = hp_stat
        self.atk_stat = atk_stat
        self.spd_stat = spd_stat
        self.mon_type1 = mon_type1
        self.mon_type2 = mon_type2
        self.stats = {'hp': hp_stat, 'atk': atk_stat, 'spd': spd_stat}
        self.mon_attack_list = mon_attack_list

    def __repr__(self):
        return self.mon_attack_list

    def __str__(self):
        return str(self.__dict__), str(self.__class__), str(self.mon_attack_list)


# ------------------------------------------------------------------------ #
# creating attacks and adding them to the attack_list
# ------------------------------------------------------------------------ #

class create_attack:

    def __init__(self, attack_name, attack_type, attack_power, mon_attack_list, num_lists_to_add):
        self.attack_name = attack_name
        self.attack_type = attack_type
        self.attack_power = attack_power
        self.mon_attack_list = mon_attack_list
        self.num_lists_to_add = num_lists_to_add
        # creates attack as list

    def make_attack(self, attack_name, attack_type, attack_power, num_lists_to_add):
        attack = [attack_name, attack_type, attack_power]
        attack_list.append(attack)
        for i in num_lists_to_add:
            i = mon_attack_list
            mon_attack_list.append(attack)


    def add_attack(self, attack, mon_attack_list):
            mon_attack_list.append(attack)


# ------------------------------------------------------------------------ #
# The battle class is the most complex part of the program
# There are two turns that call upon each other
# Turn 1 is where the user will type in the name of the
# attack for their mon to use.
# Turn 2 has the opposing mon (which will end up being chosen
# at random) use a random move.
# ------------------------------------------------------------------------ #

class battle:
    def __init__(self, mon1, mon2, attack_list1, attack2, dmg_done):
        self.mon1 = mon1
        self.mon2 = mon2
        self.attack_list1 = attack_list1
        self.attack2 = attack2
        self.dmg_done = dmg_done


    # sets the base_damage to 2. Then checks if
    # super_effective returns true
    # if returns true damage_done is doubled
    # else it is halved

    def turn1(self, mon1, mon2, attack1, attack2):
        """for i in mon1.mon_attack_list:
            print(mon1.mon_name + ' has ' + ' ' + i.attack_name)

        attack1 = input('Enter the attack for ' + mon1.mon_name + ' to use! ').title()
        for i in mon1.mon_attack_list:
            # for j in mon1.mon_attack_list.attack_name:
            if attack1 == i.attack_name:
                attack1 = i
                print(i)
                print(attack1)"""

        battle.attack_selection(self, mon1, attack1)

        attack2 = mon2.mon_attack_list[randint(0, (len(mon2.mon_attack_list) - 1))]

        # try:
        battle.dmg_done_calc(mon1, mon2, attack1)

        '''except AttributeError:

            print("Please enter an attack from the attack list.")
            attack1 = input('Enter the attack for ' + mon1.mon_name + ' to use! \n').title()
            for i in mon1.mon_attack_list:
                # for j in mon1.mon_attack_list.attack_name:
                if attack1 == i.attack_name:
                    attack1 = i
                    print(i)
                    print(attack1.attack_name)'''

        # finally:
        is_dead(mon2)
        print('{} used {}. {} took {} damage and has {} hp remaining'
              .format(mon1.mon_name, attack1[0],
                      mon2.mon_name, battle.dmg_done,
                      mon2.hp_stat))

        if mon2.dead == True:
            print('dead ' + mon2.mon_name)
        else:
            battle.turn2(self, mon1, mon2, attack1, attack2)

    def turn2(self, mon1, mon2, attack1, attack2):
        battle.dmg_done_calc(mon2, mon1, attack2)
        is_dead(mon1)
        print('{} used {}. {} took {} damage and has {} hp remaining \n'.
              format(mon2.mon_name, attack2[0],
                     mon1.mon_name, battle.dmg_done,
                     mon1.hp_stat))

        if mon1.dead == True:
            print('dead ' + mon1.mon_name)
        else:
            battle.turn1(self, mon1, mon2, attack1, attack2)

    def attack_selection(self, mon1, attack1):
        for i in mon1.mon_attack_list:
            print(mon1.mon_name + ' has ' + ' ' + i)

        attack1 = input('Enter the attack for ' + mon1.mon_name + ' to use! ').title()
        for j in mon1.mon_attack_list:
            # for j in mon1.mon_attack_list.attack_name:
            if attack1 == j[0]:
                attack1 = j
                print(type(attack1))
                return attack1

    def dmg_done_calc(mon1, mon2, attack):
        if super_effective(attack[1], mon2.mon_type1) == True:
            dmg_done = ((1 / 2 * mon1.atk_stat) + attack[2]) * 2
            mon2.hp_stat = mon2.hp_stat - dmg_done
            return mon2.hp_stat, dmg_done
        else:
            dmg_done = ((1 / 2 * mon1.atk_stat) + attack[2]) / 2
            mon2.hp_stat = mon2.hp_stat - dmg_done
            return mon2.hp_stat, dmg_done


# ------------------------------------------------------------------------ #
# spd_check will end up being used to determine which
# mon goes first.  This has not been implemented yet
# ------------------------------------------------------------------------ #

def spd_check(mon1, mon2):
    if mon1.spd_stat > mon2.spd_stat:
        return True
    else:
        return False


# ------------------------------------------------------------------------ #
# dmg_calc is a simple equation to determine the battle
# that is done.  It is called in both turns using the
# opposing mon's attack stats and attack power
# ------------------------------------------------------------------------ #


# ------------------------------------------------------------------------ #
# Simple damage chart that is used to determine if the
# damage done by an attack is doubled or halved
# ------------------------------------------------------------------------ #


def super_effective(attack_type, mon_type):
    # used for damage calculation.  If true does double damage. If false does half (for now)
    if mon_type == 'fire' and attack_type == 'water':
        return True
    elif mon_type == 'water' and attack_type == 'grass':
        return True
    elif mon_type == 'grass' and attack_type == 'fire':
        return True
    else:
        return False


def is_dead(mon):
    # checks if mon.hp_stat <= 0.  If so dead = true, prints message
    # and sets hp to 0 to prevent printing hp < 0

    if mon.hp_stat <= 0:
        mon.dead = True
        mon.hp_stat = 0


# ------------------------------------------------------------------------ #
# The large section above is all about creating the functions.  Below will
# Be the section where I use the functions to create Attacks and Pokemon
# ------------------------------------------------------------------------ #

# ------------------------------------------------------------------------ #
# creates first attacks.
# Format: func(attack name, attack type, attack power)
# ------------------------------------------------------------------------ #

blastburn = create_attack.make_attack(create_attack, 'Blast Burn', 'fire', 25)
hydrocannon = create_attack.make_attack(create_attack, 'Hydro Cannon', 'water', 25)
grassattack = create_attack.make_attack(create_attack, 'Frenzy Plant', 'grass', 25)
fireblast = create_attack.make_attack(create_attack, 'Fire Blast', 'fire', 20)
hydropump = create_attack.make_attack(create_attack, 'Hydro Pump', 'water', 20)
solarbeam = create_attack.make_attack(create_attack, 'Solarbeam', 'grass', 20)

# ------------------------------------------------------------------------ #
# creates list of attacks for each mon.
# ------------------------------------------------------------------------ #

char_attacks = []
ven_attacks = []
blas_attacks = []

create_attack.add_attack(create_attack, blastburn, char_attacks)

# ------------------------------------------------------------------------ #
# creates pokemon.
# Format: func(Mon name, mon type1, mon type 2, hp,
# attack, speed, attack list)
# ------------------------------------------------------------------------ #

Charizard = mon('Charizard', 'fire', None, 150, 10, 10, char_attacks)
Blastoise = mon('Blastoise', 'water', None, 150, 10, 9, blas_attacks)
Venusaur = mon('Venusaur', 'grass', None, 150, 10, 10, ven_attacks)

# print(Blastoise.mon_type1)
# print(attack_list)
# print(grass_attack[1])
# print(Venusaur.stats)


# first battle
# venblas = battle.turn1(battle, Venusaur, mon_creation.Blastoise, mon_creation.ven_attacks, mon_creation.blastoise_attacks)

# venblas2 = battle.turn2(battle, Venusaur, Blastoise, grass_attack, water_attack)
# print(venblas)

# print(dmg_calc.dmg_done_calc(Venusaur, Blastoise, grass_attack))

# print(Venusaur.mon_attack_list)

# for i in Venusaur.mon_attack_list:
# print(i.attack_name)

if __name__ == "main":
    pass
