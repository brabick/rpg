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
import super_effective as se

# This is not pokemon

# ------------------------------------------------------------------------ #
# Class to represent a player, either human or CPU
# Members:
#   name:            Player name for printing.
#
#   type:#           Valid types are 'human' or 'cpu'.
#                    If human, ask for input when it's
#                    this player's turn to attack;
#                    If cpu, then run the attack automatically. (randomly?)
#
#   monsters:        player's list of mon objects for the battle
#
#   active_monster:  The current fighter.
# ------------------------------------------------------------------------ #

class player:
    def __init__(self, name, playerType, monList):
        self.name = name
        self.type = playerType
        self.monsters = monList
        self.active_monster = None

    def choose(self):
        if self.active_monster != None:
            return
        
        if self.type == 'human':
            for mon in self.monsters:
                print(mon.mon_name)
            mon_chosen = False

            while mon_chosen == False:
                mon1 = input("Choose your pokemon!\n").title()
                for i in self.monsters:
                    if mon1 == i.mon_name:
                        self.active_monster = i
                        mon_chosen = True
                        print("{}, I choose you!".format(self.active_monster.mon_name))
                        time.sleep(.3)
                        return
        else: # cpu
            self.active_monster = self.monsters[randint(0, len(self.monsters) - 1)]
            print("Trainer {} (CPU) sent out {}".format(self.name, self.active_monster.mon_name))

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

# ------------------------------------------------------------------------ #
# The battle class is the most complex part of the program
# There are two turns that call upon each other
# Turn 1 is where the user will type in the name of the
# attack for their mon to use.
# Turn 2 has the opposing mon (which will end up being chosen
# at random) use a random move.
# ------------------------------------------------------------------------ #

class battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def run_turn(self):
        # first, make sure both players have an active monster
        self.player1.choose()
        self.player2.choose()

        attackingPlayer = self.player1
        defendingPlayer = self.player2
        print(1)

        print("{}'s attacks are:".format(attackingPlayer.active_monster.mon_name))
        for i in attackingPlayer.active_monster.mon_attack_list:
            print("Attack Name: {}, Power: {},".format(i.attack_name, i.attack_power))
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
            attack = input(
                'Type the name of the attack for ' + attackingPlayer.active_monster.mon_name + ' to use! \n').title()
            for i in attackingPlayer.active_monster.mon_attack_list:
                if attack == i.attack_name:
                    attack = i
                    attack_chosen = True
                    # First mon damage calc
                    dmg_calc.dmg_done_calc(attackingPlayer.active_monster, defendingPlayer.active_monster, attack)
                    # checks if the defending mon is dead
                    is_dead(defendingPlayer.active_monster)
                    self.print_turn_dmg(attack, attackingPlayer.active_monster, defendingPlayer.active_monster)
                    # Second mon attacks w/ damage calc

                    attack = defendingPlayer.active_monster.mon_attack_list[
                        randint(0, (len(defendingPlayer.active_monster.mon_attack_list) - 1))]
                    dmg_calc.dmg_done_calc(defendingPlayer.active_monster, attackingPlayer.active_monster, attack)
                    self.print_turn_dmg(attack, defendingPlayer.active_monster, attackingPlayer.active_monster)
                    # cpu is attacking
                    if mon_creation.just_died == True:
                        attack = mon_creation.fainted
                        mon_creation.just_died = False


                    # now, perform the attack


                    # check for death
                    is_dead(defendingPlayer.active_monster)


        # print the battle results

        # ------------------------------------------------------------------------ #
        # First checks if the pokemon is dead (if the hp is 0)
        # If it does then it is removed from the list.
        # ------------------------------------------------------------------------ #

        if defendingPlayer.active_monster.dead == True:
            defendingPlayer.monsters.remove(defendingPlayer.active_monster)
            print('{} has fainted!'.format(defendingPlayer.active_monster.mon_name))
            defendingPlayer.active_monster = None
            mon_creation.just_died = True

    # ------------------------------------------------------------------------ #
    # Prints the formatted attack data with damage done, hp remaining and
    # attack used.  Uses the super effective function choose which statement to
    # print
    # mon1 is the attacker
    # mon2 is the defender
    # ------------------------------------------------------------------------ #
    def print_turn_dmg(self, attack, mon1, mon2):
        attack_type = attack.attack_type
        mon_type = mon1.mon_type1

        if attack == mon_creation.fainted:
            print("")
        elif se.effective(attack.attack_type, mon2.mon_type1, mon2.mon_type2) >= 2:
            battle_txt = ('{} used {}, it\'s super effective! {} took {} damage and has {} hp remaining'.format(
                mon1.mon_name, attack.attack_name,
                mon2.mon_name, dmg_calc.dmg_done,
                mon2.hp_stat))
            print(battle_txt)
            time.sleep(.5)
        elif se.effective(attack.attack_type, mon2.mon_type1, mon2.mon_type2) == 0:
            battle_txt = ('{} used {}, It doesn\'t affect {}... {} took {} damage and has {} hp remaining'.format(
                mon1.mon_name, attack.attack_name, mon2.mon_name,
                mon2.mon_name, dmg_calc.dmg_done,
                mon2.hp_stat))
            print(battle_txt)
            time.sleep(.5)
        elif se.effective(attack.attack_type, mon2.mon_type1, mon2.mon_type2) < 1:
            battle_txt = ('{} used {}, it\'s not very effective... {} took {} damage and has {} hp remaining'.format(
                mon1.mon_name, attack.attack_name,
                mon2.mon_name, dmg_calc.dmg_done,
                mon2.hp_stat))
            print(battle_txt)
            time.sleep(.5)
        elif se.effective(attack.attack_type, mon2.mon_type1, mon2.mon_type2) == 1:
            battle_txt = ('{} used {}, {} took {} damage and has {} hp remaining'.format(
                mon1.mon_name, attack.attack_name,
                mon2.mon_name, dmg_calc.dmg_done,
                mon2.hp_stat))
            print(battle_txt)
            time.sleep(.5)

    def battle_is_over(self):
        if len(self.player1.monsters) == 0:
            print("{} won!".format(self.player2.name))
            return True
            
        if len(self.player2.monsters) == 0:
            print("{} won!".format(self.player1.name))
            return True
        
        return False

# ------------------------------------------------------------------------ #
# The start battle function that is the core of the program (for now)
# ------------------------------------------------------------------------ #

    def run_battle(self):
        while(True):
            self.run_turn()
            if (self.battle_is_over()):
                break
            self.run_turn()
            if (self.battle_is_over()):
                break

    print("Hope you enjoyed the battle.")

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

    # -----------------------------------------
    # This function reduces mon2's hit points
    # based on the attack by mon1.
    # -----------------------------------------
    def dmg_done_calc(mon1, mon2, attack):
        if attack == mon_creation.fainted:
            dmg_calc.dmg_done = 0
        else:
            dmg_calc.dmg_done = ((1 / 2 * mon1.atk_stat) + attack.attack_power) * se.effective(attack.attack_type, mon2.mon_type1, mon2.mon_type2)
            mon2.hp_stat = mon2.hp_stat - dmg_calc.dmg_done
            return mon2.hp_stat

# ------------------------------------------------------------------------ #
# Simple damage chart that is used to determine if the
# damage done by an attack is doubled or halved
# ------------------------------------------------------------------------ #


def is_dead(mon):

    # ------------------------------------------------------------------------ #
    # checks if mon.hp_stat <= 0.  If so dead = true, prints message
    # and sets hp to 0 to prevent printing hp < 0
    # ------------------------------------------------------------------------ #

    if mon.hp_stat <= 0:
        mon.dead = True
        mon.hp_stat = 0
        mon_creation.just_died = True


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
