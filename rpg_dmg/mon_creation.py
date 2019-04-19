from not_pokemon_func import create_attack, mon
from super_effective import grass, fire, water, normal, fighting, flying
from super_effective import rock, bug, ghost, steel, electric, psychic
from super_effective import dragon, dark, fairy, poison, ground, ice

# ------------------------------------------------------------------------ #
# creates first attacks.
# Format: func(attack name, attack type, attack power)
# ------------------------------------------------------------------------ #

# ------------------------------------------------------------------------ #
# Fire attacks
# ------------------------------------------------------------------------ #
blastburn = create_attack('Blast Burn', fire, 25)
fireblast = create_attack('Fire Blast', fire, 20)
flamethrower = create_attack('Flamethrower', fire, 15)
# ------------------------------------------------------------------------ #
# Water attacks
# ------------------------------------------------------------------------ #
hydrocannon = create_attack('Hydro Cannon', water, 25)
hydropump = create_attack('Hydro Pump', water, 20)
surf = create_attack('Surf', water, 15)
# ------------------------------------------------------------------------ #
# Grass attacks
# ------------------------------------------------------------------------ #
frenzyplant = create_attack('Frenzy Plant', grass, 25)
solarbeam = create_attack('Solarbeam', grass, 20)
giga_drain = create_attack('Giga Drain', grass, 15)
# ------------------------------------------------------------------------ #
# Normal attacks
# ------------------------------------------------------------------------ #
hyperbeam = create_attack('Hyper Beam', normal, 30)
trash = create_attack('Trash', normal, 15)
mega_punch = create_attack('Mega Punch', normal, 20)
# ------------------------------------------------------------------------ #
# Rock attacks
# ------------------------------------------------------------------------ #
stoneedge = create_attack("Stone Edge", rock, 15)
rock_wrecker = create_attack('Rock Wrecker', rock, 25)
diamond_storm = create_attack('Diamond Storm', rock, 20)
# ------------------------------------------------------------------------ #
# Earthquke attacks
# ------------------------------------------------------------------------ #
earthquake = create_attack('Earthquake', ground, 20)
bulldoze = create_attack('Bulldoze', ground, 15)
tectonic_rage = create_attack('Tectonic Rage', ground, 25)
# ------------------------------------------------------------------------ #
# Ice attacks
# ------------------------------------------------------------------------ #
icebeam = create_attack('Ice Beam', ice, 20)
blizzard = create_attack('Blizzard', ice, 25)
freeze_dry = create_attack('Freeze Dry', ice, 15)
# ------------------------------------------------------------------------ #
# Psychic attacks
# ------------------------------------------------------------------------ #
pyschic_atk = create_attack('Psychic', psychic, 20)
psyshock = create_attack('Psyshock', psychic, 20)
psystrike = create_attack('Psystrike', psychic, 25)
# ------------------------------------------------------------------------ #
# Dark attacks
# ------------------------------------------------------------------------ #
crunch = create_attack('Crunch', dark, 15)
knock_off = create_attack('Knock Off', dark, 20)
dark_pulse = create_attack('Dark Pulse', dark, 20)
# ------------------------------------------------------------------------ #
# Fighting attacks
# ------------------------------------------------------------------------ #
close_combat = create_attack('Close Combat', fighting, 25)
drain_punch = create_attack('Drain Punch', fighting, 15)
dynamic_punch = create_attack('Dynamic Punch', fighting, 20)
# ------------------------------------------------------------------------ #
# Flying attacks
# ------------------------------------------------------------------------ #
sky_attack = create_attack('Sky Attack', flying, 25)
aerial_ace = create_attack('Aerial Ace', flying, 15)
brave_bird = create_attack('Brave Bird', flying, 20)
# ------------------------------------------------------------------------ #
# Poison attacks
# ------------------------------------------------------------------------ #
sludge_bomb = create_attack('Sludge Bomb', poison, 20)
gunk_shot = create_attack('Gunk Shot', poison, 25)
poison_fang = create_attack('Poison Fang', poison, 15)
# ------------------------------------------------------------------------ #
# Bug attacks
# ------------------------------------------------------------------------ #
u_turn = create_attack('U-turn', bug, 10)
bug_bite = create_attack('Bug Bite', bug, 15)
x_scissor = create_attack('X-Scissor', bug, 20)
# ------------------------------------------------------------------------ #
# Ghost attacks
# ------------------------------------------------------------------------ #
shadow_ball = create_attack('Shadow Ball', ghost, 15)
shadow_force = create_attack('Shadow Force', ghost, 25)
moongeist_beam = create_attack('Moongeist Beam', ghost, 20)
# ------------------------------------------------------------------------ #
# Steel attacks
# ------------------------------------------------------------------------ #
meteor_mash = create_attack('Meteor Mash', steel, 20)
iron_head = create_attack('Iron Head', steel, 15)
doom_desire = create_attack('Doom Desire', steel, 25)
# ------------------------------------------------------------------------ #
# Electric attacks
# ------------------------------------------------------------------------ #
thunderbolt = create_attack('Thunderbolt', electric, 20)
thunder = create_attack('Thunder', electric, 25)
volt_switch = create_attack('Volt Switch', electric, 15)
# ------------------------------------------------------------------------ #
# Dragon attacks
# ------------------------------------------------------------------------ #
outrage = create_attack('Outrage', dragon, 20)
draco_meteor = create_attack('Draco Meteor', dragon, 25)
dragon_breah = create_attack('Dragon Breath', dragon, 15)
# ------------------------------------------------------------------------ #
# Fairy attacks
# ------------------------------------------------------------------------ #
moon_blast = create_attack('Moonblast', fairy, 20)
dazzling_gleam = create_attack('Dazzling Gleam', fairy, 15)
fleur_cannon = create_attack('Fleur Cannon', fairy, 25)
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
