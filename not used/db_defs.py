'''class attack_selection:
    def __init__(self, attack, mon, varAll):
        self.attack = attack
        self.mon = mon
        self.varAll = varAll

    def print_all_attacks(self):

        attack = input("Enter the attack to use! ")
        conn = sqlite3.connect('rpg_db')
        cur = conn.cursor()
        #runs through the attack table and checks if the attack is in the list
        with conn:
            cur.execute(
                'SELECT tbl_atks.attack_name, tbl_atks.attack_power, tbl_atks.attack_type '
                'FROM tbl_atks '
                'WHERE tbl_atks.attack_name = ?', (attack.title(),)
                )
            varAll = cur.fetchall()
            for i in varAll:
                print(i[0])
                print(i[1])
                print(i[2])
        conn.close()

    def print_venusaur_attacks(self):
        attack_selection.print_all_attacks(attack_selection)
        attack = "Frenzy Plant"
        mon = "Venusaur"
        conn = sqlite3.connect('rpg_db')
        cur = conn.cursor()
        with conn:
            cur.execute(
                'SELECT attack_name '
                'FROM Venusaur',
                )
            venAll = cur.fetchall()
            for i in venAll:
                print(i[0])'''


