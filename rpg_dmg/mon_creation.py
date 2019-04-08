from not_pokemon_func import create_attack, mon

# ------------------------------------------------------------------------ #
# creates first attacks.
# Format: func(attack name, attack type, attack power)
# ------------------------------------------------------------------------ #

blastburn = create_attack('Blast Burn', 'fire', 25)
hydrocannon = create_attack('Hydro Cannon', 'water', 25)
frenzyplant = create_attack('Frenzy Plant', 'grass', 25)
fireblast = create_attack('Fire Blast', 'fire', 20)
hydropump = create_attack('Hydro Pump', 'water', 20)
solarbeam = create_attack('Solarbeam', 'grass', 20)
hyperbeam = create_attack('Hyper Beam', 'normal', 30)
fainted = create_attack('fainted', None, 0)
# ------------------------------------------------------------------------ #
# creates list of attacks for each mon.
# ------------------------------------------------------------------------ #

char_attacks = [blastburn, hydrocannon, frenzyplant]
ven_attacks = [solarbeam, frenzyplant, hydropump, hyperbeam]
blas_attacks = [hydrocannon, hydropump, fireblast]

# ------------------------------------------------------------------------ #
# creates pokemon.
# Format: func(Mon name, mon type1, mon type 2, hp,
# attack, speed, attack list)
# ------------------------------------------------------------------------ #

# ------------------------------------------------------------------------ #
# Creates the player mon lists
# ------------------------------------------------------------------------ #

player1_mon_list = [
    mon('Charizard', 'fire', None, 80, 10, 10, char_attacks),
    mon('Blastoise', 'water', None, 10, 10, 9, blas_attacks),
    mon('Venusaur', 'grass', None, 10, 10, 10, ven_attacks)
]

player2_mon_list = [
    mon('Charizard', 'fire', None, 50, 10, 10, char_attacks),
    mon('Blastoise', 'water', None, 50, 10, 9, blas_attacks),
    mon('Venusaur', 'grass', None, 50, 10, 10, ven_attacks)
]