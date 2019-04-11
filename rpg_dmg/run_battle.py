import mon_creation
from not_pokemon_func import battle, player

Player1 = player('You', 'human', mon_creation.player1_mon_list)
Player2 = player('Joey', 'cpu', mon_creation.player2_mon_list)

TheBattle = battle(Player1, Player2)
TheBattle.run_battle()


#battle.attack_selection(battle, not_pokemon_func.Blastoise)

#mon = not_pokemon_func.battle.mon_selection(battle, not_pokemon_func.player1_mon_list)

#new_battle = battle.mon_selection(battle, not_pokemon_func.player1_mon_list)
