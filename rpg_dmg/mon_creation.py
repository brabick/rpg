import not_pokemon_func
from not_pokemon_func import battle, dmg_calc

#Attack creation
blastburn = not_pokemon_func.create_attack('Blast Burn', 'fire', 25)
hydrocannon = not_pokemon_func.create_attack('Hydro Cannon', 'water', 25)
grassattack = not_pokemon_func.create_attack('Frenzy Plant', 'grass', 25)
fireblast = not_pokemon_func.create_attack('Fire Blast', 'fire', 20)
hydropump = not_pokemon_func.create_attack('Hydro Pump', 'water', 20)
solarbeam = not_pokemon_func.create_attack('Solar Beam', 'grass', 20)


#Create attack lists
char_attacks = [blastburn, hydrocannon, grassattack]
ven_attacks = [solarbeam, grassattack, hydropump]
blas_attacks = [hydrocannon, hydropump, fireblast]


#Create pokemon
Charizard = not_pokemon_func.mon('Charizard', 'fire', None, 150, 10, 10, char_attacks)
Blastoise = not_pokemon_func.mon('Blastoise', 'water', None, 150, 10, 9, char_attacks)
Venusaur = not_pokemon_func.mon('Venusaur', 'grass', None, 150, 10, 10, ven_attacks)


venblas = battle.turn1(battle, Venusaur, Blastoise, ven_attacks, blas_attacks)
