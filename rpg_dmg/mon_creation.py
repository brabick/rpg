from not_pokemon_func import create_attack, mon
from super_effective import fire, grass, water, rock, ice, ground, normal, psychic

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
stoneedge = create_attack("Stone Edge", rock, 15)
earthquake = create_attack('Earthquake', ground, 15)
icebeam = create_attack('Ice Beam', ice, 15)
pyschic_atk = create_attack('Psychic', psychic, 20)


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
test_list = [stoneedge, earthquake, icebeam, frenzyplant, hyperbeam, hydropump, fireblast]
mewtwo_attacks = [pyschic_atk, icebeam, fireblast, hyperbeam]
# ------------------------------------------------------------------------ #
# creates pokemon.
# Format: func(Mon name, mon type1, mon type 2, hp,
# attack, speed, attack list)
# ------------------------------------------------------------------------ #

# ------------------------------------------------------------------------ #
# Creates the player mon lists
# ------------------------------------------------------------------------ #

player1_mon_list = [
    mon('Charizard', 'fire', 'flying', 80, 10, 10, char_attacks),
    mon('Blastoise', 'water', None, 10, 10, 9, blas_attacks),
    mon('Venusaur', 'grass', 'poison', 10, 10, 10, ven_attacks),
    mon('Test', 'ground', None, 300, 15, 6, test_list),
    mon('Mewtwo', 'psychic', None, 150, 25, 12, mewtwo_attacks)
]

player2_mon_list = [
    mon('Trainer Joey\'s Charizard', 'fire', 'flying', 100, 10, 10, char_attacks),
    mon('Trainer Joey\'s Blastoise', 'water', None, 100, 10, 9, blas_attacks),
    mon('Trainer Joey\'s Venusaur', 'grass', 'poison', 100, 10, 10, ven_attacks)
]


just_died = False

if __name__ == "main":
    pass
