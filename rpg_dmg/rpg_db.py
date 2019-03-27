import sqlite3
#import not_pokemon_func

conn = sqlite3.connect('rpg_db')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_mons(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            mon_name TEXT, \
            hp_stat INT, \
            atk_stat INT, \
            spd_stat INT,\
            mon_type1 TEXT,\
            mon_type2 TEXT\
            )')
    conn.commit()
conn.close()

'''conn = sqlite3.connect('rpg_db')
with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_mons(mon_name, hp_stat, atk_stat,\
                spd_stat, mon_type1, mon_type2) VALUES (?, ?, ?, ?, ?, ?)',
                ('Venusaur', 150, 30, 25, 'Grass', None))
    cur.execute('INSERT INTO tbl_mons(mon_name, hp_stat, atk_stat,\
                    spd_stat, mon_type1, mon_type2) VALUES (?, ?, ?, ?, ?, ?)',
                ('Blastoise', 150, 35, 20, 'Water', None))
    cur.execute('INSERT INTO tbl_mons(mon_name, hp_stat, atk_stat,\
                        spd_stat, mon_type1, mon_type2) VALUES (?, ?, ?, ?, ?, ?)',
                ('Charizard', 120, 45, 30, 'Fire', None))
    conn.commit()
conn.close()'''

conn = sqlite3.connect('rpg_db')
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_atks(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            attack_name TEXT, \
            attack_type TEXT,\
            attack_power INT\
            )')
    conn.commit()
conn.close()

conn = sqlite3.connect('rpg_db')
with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_atks(attack_name, attack_type, attack_power) '
                'VALUES (?, ?, ?)',
                ('Frenzy Plant', 'Grass', 45))
    cur.execute('INSERT INTO tbl_atks(attack_name, attack_type, attack_power) '
                'VALUES (?, ?, ?)',
                ('Blast Burn', 'Fire', 45))
    cur.execute('INSERT INTO tbl_atks(attack_name, attack_type, attack_power) '
                'VALUES (?, ?, ?)',
                ('Hydro Cannon', 'Water', 45))
    conn.commit()
conn.close()
