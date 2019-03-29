from random import randint


# This is not pokemon
# the only types so far
type_list = ['fire', 'water', 'grass']
# empty list for attacks they get added from the attack class below
attack_list = []
# creating the pokemon class
mon_list = []


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




# creating attacks and adding them to the attack_list
class create_attack:
    def __init__(self, attack_name, attack_type, attack_power):
        self.attack_name = attack_name
        self.attack_type = attack_type
        self.attack_power = attack_power
        # creates attack as list
        attack = {'attack name': attack_name, 'attack type': attack_type, 'attack_power': attack_power}
        attack_list.append(attack)



class battle:
    def __init__(self, mon1, mon2, attack1, attack2, damage_done):
        self.mon1 = mon1
        self.mon2 = mon2
        self.attack1 = attack1
        self.attack2 = attack2
        self.damage_done = damage_done

    # sets the base_damage to 2. Then checks if
    # super_effective returns true
    # if returns true damage_done is doubled
    # else it is halved

    def turn1(self, mon1, mon2, attack1, attack2):
        for i in mon1.mon_attack_list:
            print(mon1.mon_name + ' has ' + ' ' + i.attack_name)
            # trying to get user input for the attacks
            # try if statement?  if input == attack name

        attack1 = input('Enter the attack for ' + mon1.mon_name + ' to use! ')
        for i in mon1.mon_attack_list:
            #for j in mon1.mon_attack_list.attack_name:
            if attack1 == i.attack_name:
                attack1 = i
                #return attack1

                attack2 = mon2.mon_attack_list[randint(0,1)]
                dmg_calc.dmg_done_calc(mon1, mon2, attack1)
                is_dead(mon2)
                print('{} used {}. {} took {} damage and has {} hp remaining'.format(mon1.mon_name, attack1.attack_name,
                                                                                     mon2.mon_name, dmg_calc.dmg_done,
                                                                                     mon2.hp_stat))
        if mon2.dead == True:
            print('dead ' + mon2.mon_name)
        else:
            battle.turn2(self, mon1, mon2, attack1, attack2)

    def turn2(self, mon1, mon2, attack1, attack2):
        dmg_calc.dmg_done_calc(mon2, mon1, attack2)
        is_dead(mon1)
        print('{} used {}. {} took {} damage and has {} hp remaining'.format(mon2.mon_name, attack2.attack_name,
                                                                             mon1.mon_name, dmg_calc.dmg_done,
                                                                             mon1.hp_stat))
        if mon1.dead == True:
            print('dead ' + mon1.mon_name)
        else:
            battle.turn1(self, mon1, mon2, attack1, attack2)


def spd_check(mon1, mon2):
    if mon1.spd_stat > mon2.spd_stat:
        return True
    else:
        return False


class dmg_calc:
    def __init__(self, dmg_done):
        self.dmg_done = dmg_done

    def dmg_done_calc(mon1, mon2, attack):
        if super_effective(attack.attack_type, mon2.mon_type1) == True:
            dmg_calc.dmg_done = ((1 / 2 * mon1.atk_stat) + attack.attack_power) * 2
            mon2.hp_stat = mon2.hp_stat - dmg_calc.dmg_done
            return mon2.hp_stat, dmg_calc.dmg_done
        else:
            dmg_calc.dmg_done = ((1 / 2 * mon1.atk_stat) + attack.attack_power) / 2
            mon2.hp_stat = mon2.hp_stat - dmg_calc.dmg_done
            return mon2.hp_stat
        # damage_formula = move_attack_power + super_effective * 1/2 mon_atk_stat


def super_effective(attack_type, mon_type):
    # used for damage calculation.  If true does double damage. If false does half (for now)
    if mon_type == 'fire' and attack_type == 'water':
        print('Stopping at fire')
        return True
    elif mon_type == 'water' and attack_type == 'grass':
        print('Stopping at water')
        return True
    elif mon_type == 'grass' and attack_type == 'fire':
        print('Stopping at grass')
        return True
    else:
        print('Stopping at false')
        return False


def is_dead(mon):
    # checks if mon.hp_stat <= 0.  If so dead = true, prints message
    # and sets hp to 0 to prevent printing hp < 0

    if mon.hp_stat <= 0:
        mon.dead = True
        mon.hp_stat = 0


# creates first attacks



# print(Blastoise.mon_type1)
#print(attack_list)
# print(grass_attack[1])
# print(Venusaur.stats)

# combat1 = super_effective('grass', 'grass')
# print(combat1)
# combat2 = super_effective('fire', 'water')
# print(combat2)
# combat3 = super_effective('grass', 'water')
# print(combat3)

# first battle
#venblas = battle.turn1(battle, Venusaur, mon_creation.Blastoise, mon_creation.ven_attacks, mon_creation.blastoise_attacks)

# venblas2 = battle.turn2(battle, Venusaur, Blastoise, grass_attack, water_attack)
# print(venblas)

#print(dmg_calc.dmg_done_calc(Venusaur, Blastoise, grass_attack))

#print(Venusaur.mon_attack_list)

#for i in Venusaur.mon_attack_list:
    #print(i.attack_name)

