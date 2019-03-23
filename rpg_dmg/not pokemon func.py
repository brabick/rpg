#This is not pokemon
#the only types so far
type_list = ['fire', 'water', 'grass']
#empty list for attacks they get added from the attack class below
attack_list = []
#creating the pokemon class
mon_list = []

#damage_formula = move_attack_power * super_effective * 1/2 mon_atk_stat


class mon:
    #default dead = false
    def __init__(self, mon_name, mon_type1, mon_type2, hp_stat, atk_stat, spd_stat, dead = False):
        self.mon_name = mon_name
        self.hp_stat = hp_stat
        self.atk_stat = atk_stat
        self.spd_stat = spd_stat
        self.mon_type1 = mon_type1
        self.mon_type2 = mon_type2
        self.stats = {'hp': hp_stat, 'atk': atk_stat, 'spd': spd_stat}


#creating attacks and adding them to the attack_list
def create_attack(attack_name, attack_type, attack_power):
    #creates attack as list
    attack = [attack_name, attack_type, attack_power]
    attack_list.append(attack)
    return attack


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

    def combat(self, mon1, mon2, attack1, attack2):
        #base damage = 2

        #checks speed. Faster moves first
        if spd_check(mon1, mon2):
            dmg_calc(mon1, mon2, attack)
            else:
                #not super effective
                # damage calculation (revist)
                damage_done /= 2
                mon2.hp_stat = mon2.hp_stat - damage_done
                is_dead(mon2)
                return mon2.mon_name, mon2.hp_stat
        # if mon2 has higher speed
        else:
            if super_effective(attack2[1], mon1.mon_type1):
                damage_done = attack2[2]
                damage_done *= 2
                mon1.hp_stat = mon1.hp_stat - damage_done
                is_dead(mon1)
                return mon1.mon_name, mon1.hp_stat
            else:
                damage_done /= 2
                mon1.hp_stat = mon1.hp_stat - damage_done
                is_dead(mon1)
                return mon1.mon_name, mon1.hp_stat

def spd_check(mon1, mon2):
    if mon1.spd_stat > mon2.spd_stat:
        return True
    else:
        return False

def dmg_done_calc(mon1, mon2, attack):
    if super_effective(attack[0], mon2.mon_type1):
        dmg_done = ((1 / 2 * mon1.atk_stat) + attack[2]) * 2
        return mon2.hp_stat - dmg_done
    else:
        dmg_done = ((1 / 2 * mon1.atk_stat) + attack[2]) / 2
        return mon2.hp_stat - dmg_done
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
        print(mon.mon_name + ' Fainted!')

# creates first attacks
fire_attack = create_attack('fire_attack', 'fire', 10)
water_attack = create_attack('water_attack', 'water', 10)
grass_attack = create_attack('grass_attack', 'grass', 10)
Charizard = mon('Charizard', 'fire', None, 100, 10, 10)
Blastoise = mon('Blastoise', 'water', None, 60, 10, 11)
Venusaur = mon('Venusaur', 'grass', None, 100, 10, 10)
print(Blastoise.mon_type1)
print(attack_list)
print(grass_attack[1])
#print(Venusaur.stats)

# combat1 = super_effective('grass', 'grass')
# print(combat1)
# combat2 = super_effective('fire', 'water')
# print(combat2)
# combat3 = super_effective('grass', 'water')
# print(combat3)

# first battle
venblas = battle.combat(battle, Charizard, Blastoise, fire_attack, water_attack)
print(venblas)
