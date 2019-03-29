import sqlite3
#import not_pokemon_func

conn = sqlite3.connect('rpg_db')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_mons(\
            mon_id INTEGER PRIMARY KEY AUTOINCREMENT, \
            mon_name TEXT, \
            hp_stat INTEGER, \
            atk_stat INTEGER, \
            spd_stat INTEGER,\
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
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            attack_name TEXT, \
            attack_type TEXT,\
            attack_power INTEGER\
            )')
    conn.commit()
conn.close()

conn = sqlite3.connect('rpg_db')
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Venusaur(\
            attack_name TEXT,\
            attack_id INTEGER, \
            FOREIGN KEY(attack_id) REFERENCES tbl_atks(id) \
            )')
    conn.commit()
conn.close()
conn = sqlite3.connect('rpg_db')
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Blastoise(\
            attack_name TEXT,\
            attack_id INTEGER, \
            FOREIGN KEY(attack_id) REFERENCES tbl_atks(id) \
            )')
    conn.commit()
conn.close()
conn = sqlite3.connect('rpg_db')
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Charizard(\
            attack_name TEXT,\
            attack_id INTEGER, \
            FOREIGN KEY(attack_id) REFERENCES tbl_atks(id) \
            )')
    conn.commit()
conn.close()

'''conn = sqlite3.connect('rpg_db')
with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_atks(attack_name, attack_type, attack_power) '
                'VALUES ( ?, ?, ?)',
                ('Frenzy Plant', 'Grass', 45))
    cur.execute('INSERT INTO tbl_atks(attack_name, attack_type, attack_power) '
                'VALUES (?, ?, ?)',
                ('Blast Burn',  'Fire', 45))
    cur.execute('INSERT INTO tbl_atks(attack_name, attack_type, attack_power) '
                'VALUES (?, ?, ?)',
                ('Hydro Cannon', 'Water', 45))
    conn.commit()
conn.close()'''

'''conn = sqlite3.connect('rpg_db')
with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_atks(attack_name, attack_type, attack_power) '
                'VALUES ( ?, ?, ?)',
                ('Leaf Storm', 'Grass', 35))
    cur.execute('INSERT INTO tbl_atks(attack_name, attack_type, attack_power) '
                'VALUES (?, ?, ?)',
                ('Earthquake', 'Ground', 25))
    cur.execute('INSERT INTO tbl_atks(attack_name, attack_type, attack_power) '
                'VALUES (?, ?, ?)',
                ('Sludge Bomb', 'Poison', 25))
    conn.commit()
conn.close()
conn = sqlite3.connect('rpg_db')'''

'''with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO Venusaur(attack_name, attack_id) '
                'VALUES (?, ?)',
                ('Frenzy Plant', 1))
    cur.execute('INSERT INTO Venusaur(attack_name, attack_id) '
                'VALUES (?, ?)',
                ('Earthquake', 8))
    cur.execute('INSERT INTO Venusaur(attack_name, attack_id) '
                'VALUES (?, ?)',
                ('Blast Burn', 2))
    conn.commit()
conn.close()
conn = sqlite3.connect('rpg_db')
with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO Blastoise(attack_name, attack_id) '
                'VALUES (?, ?)',
                ('Hydro Cannon', 3))
    cur.execute('INSERT INTO Blastoise(attack_name, attack_id) '
                'VALUES (?, ?)',
                ('Earthquake', 8))
    cur.execute('INSERT INTO Blastoise(attack_name, attack_id) '
                'VALUES (?, ?)',
                ('Blast Burn', 2))
    conn.commit()
conn.close()
conn = sqlite3.connect('rpg_db')
with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO Charizard(attack_name, attack_id) '
                'VALUES (?, ?)',
                ('Frenzy Plant', 1))
    cur.execute('INSERT INTO Charizard(attack_name, attack_id) '
                'VALUES (?, ?)',
                ('Earthquake', 8))
    cur.execute('INSERT INTO Charizard(attack_name, attack_id) '
                'VALUES (?, ?)',
                ('Blast Burn', 2))
    conn.commit()
conn.close()
'''


