# ------------------------------------------------------------------------ #
# Author: Brandon Bickerton
# Python Version: 3.7.2
# Description: This is meant to be a basic version of battling
# based on the Pokemon game series.
# This is designed to be easily expandable.
# ------------------------------------------------------------------------ #

from random import randint
import time
import mon_creation


# This is not pokemon
# the only types so far
type_list = ['fire', 'water', 'grass']
# empty list for attacks they get added from the attack class below
attack_list = []
# creating the pokemon class
mon_list = []


# ------------------------------------------------------------------------ #
# Initial class used to make pokemon
# Initializes variables to make them available later in
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
        mon_list.append(mon)

# ------------------------------------------------------------------------ #
# creating attacks and adding them to the attack_list
# ------------------------------------------------------------------------ #

class create_attack:
    def __init__(self, attack_name, attack_type, attack_power):
        self.attack_name = attack_name
        self.attack_type = attack_type
        self.attack_power = attack_power
        # creates attack as list
        attack = {'attack name': attack_name, 'attack type': attack_type, 'attack_power': attack_power}
        attack_list.append(attack)


# ------------------------------------------------------------------------ #
# The battle class is the most complex part of the program
# There are two turns that call upon each other
# Turn 1 is where the user will type in the name of the
# attack for their mon to use.
# Turn 2 has the opposing mon (which will end up being chosen
# at random) use a random move.
# ------------------------------------------------------------------------ #

class battle:
    def __init__(self, mon1, mon2, attack1, attack2, damage_done, player1_mon_list):
        self.mon1 = mon1
        self.mon2 = mon2
        self.attack1 = attack1
        self.attack2 = attack2
        self.damage_done = damage_done
        self.player1_mon_list = player1_mon_list

    def turn1(self, mon1, mon2):

        print("{}'s attacks are:".format(mon1.mon_name))
        for i in mon1.mon_attack_list:
            print("Attack Name: {}, Type: {}, Power: {},".format(i.attack_name, i.attack_type.title(), i.attack_power))
            # ------------------------------------------------------------------------ #
            # Having wait statements staggers the information being printed to the screen
            # This makes the information more accessible
            # ------------------------------------------------------------------------ #
            time.sleep(.2)

        attack_chosen = False
        while attack_chosen == False:
            # ------------------------------------------------------------------------ #
            # While loop makes it so that if the user types an attack incorrectly
            # They will go back into the loop and have to enter it again
            # Until they enter an attack name correctly
            # ------------------------------------------------------------------------ #
            attack1 = input('Type the name of the attack for ' + mon1.mon_name + ' to use! \n').title()
            for i in mon1.mon_attack_list:
                if attack1 == i.attack_name:
                    attack1 = i
                    attack_chosen = True

                    dmg_calc.dmg_done_calc(mon1, mon2, attack1)
                    # ------------------------------------------------------------------------ #
                    # Turns attack2 (the attack used by the opponent  into a random attack
                    # from their attack list
                    # ------------------------------------------------------------------------ #
                    attack2 = mon2.mon_attack_list[randint(0, (len(mon2.mon_attack_list) - 1))]
                    is_dead(mon2)
                    battle.print_turn_dmg(battle, attack1, mon2)
                    # ------------------------------------------------------------------------ #
                    # First checks if the pokemon is dead (if the hp is 0)
                    # If it does then it is removed from the list
                    # Checks if the list of the opponents pokemon has any pokemon left in it
                    # If they do the battle will continue, they will send out another random
                    # pokemon and turn 1 will start again
                    # If not, you win will print and the battle will end
                    # ------------------------------------------------------------------------ #
                    if mon2.dead == True:
                        mon_creation.player2_mon_list.remove(mon2)
                        print('{} has fainted!'.format(mon2.mon_name))
                        if len(mon_creation.player2_mon_list) > 0:
                            #battle.print_turn_dmg.battle_txt = "{} has fainted!".format(mon2)
                            mon2 = mon_creation.player2_mon_list[randint(0, len(mon_creation.player2_mon_list) - 1)]
                            print("Trainer Joey sent out {}".format(mon2.mon_name))
                            battle.turn1(self, mon1, mon2)

                        else:
                            print("You win!")
                    else:
                        battle.turn2(self, mon2, mon1, attack2)

    # ------------------------------------------------------------------------ #
    # Turn 2 is very similar to turn 1, it just runs with the mons reversed
    # and having to add attack 2 since which is chosen randomly.
    # The other parts of the function work the same.
    # ------------------------------------------------------------------------ #
    def turn2(self, mon2, mon1, attack2):

        dmg_calc.dmg_done_calc(mon2, mon1, attack2)
        is_dead(mon1)
        battle.print_turn_dmg(battle, attack2, mon1)

        if mon1.dead == True:
            print('{} has fainted!'.format(mon1.mon_name))
            mon_creation.player1_mon_list.remove(mon1)
            if len(mon_creation.player1_mon_list) > 0:
                mon1 = battle.mon_selection(battle, mon_creation.player1_mon_list)
                attack2 = mon_creation.fainted
                if attack2 == mon_creation.fainted:
                    battle.battle_txt = "Nothing here"
                    battle.turn2(self, mon2, mon1, mon_creation.fainted)


            else:
                print("All of your pokemon have fainted! Better luck next time!")

        else:
            print(end_of_turn[randint(0, len(end_of_turn) - 1)])
            battle.turn1(self, mon1, mon2)

    # ------------------------------------------------------------------------ #
    # Mon selection assigns the user inputted mon to mon1 for turns 1 and 2
    # This runs a similar while loop to as the attack selection one.
    #
    # ------------------------------------------------------------------------ #
    def mon_selection(self, player1_mon_list):
        for mon in player1_mon_list:
            print(mon.mon_name)
        mon_chosen = False

        while mon_chosen == False:
            mon1 = input("Choose your pokemon!\n").title()
            for i in player1_mon_list:
                # for j in mon1.mon_attack_list.attack_name:
                if mon1 == i.mon_name:
                    mon1 = i
                    mon_chosen = True
                    print("{}, I choose you!".format(mon1.mon_name))
                    time.sleep(.3)
                    return mon1

    # ------------------------------------------------------------------------ #
    # Prints the formatted attack data with damage done, hp remaining and
    # attack used.  Uses the super effective function choose which statement to
    # print
    # ------------------------------------------------------------------------ #
    def print_turn_dmg(self, attack, mon):
        attack_type = attack.attack_type
        mon_type = mon.mon_type1
        if attack == mon_creation.fainted:
            print(" ")
        elif super_effective(attack_type, mon_type) == True:
            battle_txt = ('{} used {}, it\'s super effective! {} took {} damage and has {} hp remaining'.format(
                mon.mon_name, attack.attack_name,
                mon.mon_name, dmg_calc.dmg_done,
                mon.hp_stat))
            if attack == mon_creation.fainted:
                battle_txt = "Nothing here"
            print(battle_txt)
            time.sleep(.5)
        elif super_effective(attack_type, mon_type) == False:
            print(attack.attack_type)
            battle_txt = ('{} used {}, it\'s not very effective... {} took {} damage and has {} hp remaining'.format(
                mon.mon_name, attack.attack_name,
                mon.mon_name, dmg_calc.dmg_done,
                mon.hp_stat))
            print(battle_txt)
            time.sleep(.5)
        elif super_effective(attack_type, mon_type) == None:
            battle_txt = ('{} used {}, {} took {} damage and has {} hp remaining'.format(
                mon.mon_name, attack.attack_name,
                mon.mon_name, dmg_calc.dmg_done,
                mon.hp_stat))
            print(battle_txt)
            time.sleep(.5)

# ------------------------------------------------------------------------ #
# The start battle function that is the core of the program (for now)
# ------------------------------------------------------------------------ #

class start_battle:
    def new_battle(self, mon_list1):
        mon1 = battle.mon_selection(battle, mon_list1)
        mon2 = mon_creation.player2_mon_list[randint(0, len(mon_creation.player2_mon_list) - 1)]
        print("Trainer Joey sent out {}!".format(mon2.mon_name))
        time.sleep(.6)
        # mon1 = battle.mon_selection.mon1
        battle.turn1(battle, mon1, mon2)


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


class dmg_calc:
    def __init__(self, dmg_done):
        self.dmg_done = dmg_done

    def dmg_done_calc(mon1, mon2, attack):
        if attack == mon_creation.fainted:
            dmg_calc.dmg_done = 0
        elif super_effective(attack.attack_type, mon2.mon_type1) == True:
            dmg_calc.dmg_done = ((1 / 2 * mon1.atk_stat) + attack.attack_power) * 2
            mon2.hp_stat = mon2.hp_stat - dmg_calc.dmg_done
            return mon2.hp_stat
        elif super_effective(attack.attack_type, mon2.mon_type1) == False:
            dmg_calc.dmg_done = ((1 / 2 * mon1.atk_stat) + attack.attack_power) / 2
            mon2.hp_stat = mon2.hp_stat - dmg_calc.dmg_done
            return mon2.hp_stat

        else:
            dmg_calc.dmg_done = ((1 / 2 * mon1.atk_stat) + attack.attack_power)
            mon2.hp_stat = mon2.hp_stat - dmg_calc.dmg_done
            return mon2.hp_stat
        # damage_formula = move_attack_power + super_effective * 1/2 mon_atk_stat


# ------------------------------------------------------------------------ #
# Simple damage chart that is used to determine if the
# damage done by an attack is doubled or halved
# ------------------------------------------------------------------------ #


def super_effective(attack_type, mon_type):
    # ------------------------------------------------------------------------ #
    # used for damage calculation.  If true does double damage. If false does half (for now)
    # 2 = super effective
    # 1 = not very effective
    # 0 = neutral
    # ------------------------------------------------------------------------ #
    if mon_type == 'fire' and attack_type == 'water':
        return True
    elif mon_type == 'water' and attack_type == 'grass':
        return True
    elif mon_type == 'grass' and attack_type == 'fire':
        return True
    else:
        return False


def is_dead(mon):
    # ------------------------------------------------------------------------ #
    # checks if mon.hp_stat <= 0.  If so dead = true, prints message
    # and sets hp to 0 to prevent printing hp < 0
    # ------------------------------------------------------------------------ #

    if mon.hp_stat <= 0:
        mon.dead = True
        mon.hp_stat = 0

# ------------------------------------------------------------------------ #
# The large section above is all about creating the functions.  Below will
# Be the section where I use the functions to create Attacks and Pokemon
# ------------------------------------------------------------------------ #

# ------------------------------------------------------------------------ #
# The list of phrases that are printed at the end of each turn
# Helps to break up the turns
# ------------------------------------------------------------------------ #

end_of_turn = ["Your Pokemon is strong, keep it up!\n", "The enemy is getting weaker!\n", "Keep fighting!\n",
               "The battle is heating up!\n"]


if __name__ == "main":
    pass
