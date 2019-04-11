from not_pokemon_func import create_attack, mon
from super_effective import fire, grass, water, rock, ice, ground, normal

# ------------------------------------------------------------------------ #
# creates first attacks.
# Format: func(attack name, attack type, attack power)
# ------------------------------------------------------------------------ #

blastburn = create_attack('Blast Burn', fire, 10)
hydrocannon = create_attack('Hydro Cannon', water, 10)
frenzyplant = create_attack('Frenzy Plant', grass, 10)
fireblast = create_attack('Fire Blast', fire, 10)
hydropump = create_attack('Hydro Pump', water, 10)
solarbeam = create_attack('Solarbeam', grass, 10)
hyperbeam = create_attack('Hyper Beam', normal, 30)
stoneedge = create_attack("Stone Edge", rock, 5)
earthquake = create_attack('Earthquake', ground, 5)
icebeam = create_attack('Ice Beam', ice, 5)


# ------------------------------------------------------------------------ #
# Only used when a mon faints
# ------------------------------------------------------------------------ #
fainted = create_attack('fainted', None, 0)
# ------------------------------------------------------------------------ #
# creates list of attacks for each mon.
# ------------------------------------------------------------------------ #

char_attacks = [blastburn, hydrocannon, frenzyplant]
ven_attacks = [solarbeam, frenzyplant, hydropump]
blas_attacks = [hydrocannon, hydropump, fireblast]
test_list = [stoneedge, earthquake, icebeam, frenzyplant]
# ------------------------------------------------------------------------ #
# creates pokemon.
# Format: func(Mon name, mon type1, mon type 2, hp,
# attack, speed, attack list)
# ------------------------------------------------------------------------ #

# ------------------------------------------------------------------------ #
# Creates the player mon lists
# ------------------------------------------------------------------------ #

player1_mon_list = [
    mon('Charizard', fire, 'fire', 80, 10, 10, char_attacks),
    mon('Blastoise', water, 'water', 10, 10, 9, blas_attacks),
    mon('Venusaur', grass, 'grass', 10, 10, 10, ven_attacks),
    mon('Test', ground, 'ground', 100, 10, 6, test_list)
]

player2_mon_list = [
    mon('Trainer Joey\'s Charizard', fire, 'fire', 50, 10, 10, char_attacks),
    mon('Trainer Joey\'s Blastoise', water, 'water', 50, 10, 9, blas_attacks),
    mon('Trainer Joey\'s Venusaur', grass, 'grass', 50, 10, 10, ven_attacks)
]

if __name__ == "main":
    pass
