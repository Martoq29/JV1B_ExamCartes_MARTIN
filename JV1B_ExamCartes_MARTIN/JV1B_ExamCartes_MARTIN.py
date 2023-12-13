class Mage:
    def __init__(self,name,pointdevie,manatotal,cbn_mana):
        self.mana = manatotal
        self.manatot = manatotal
        self.nom = name
        self.pv = pointdevie
        self.cbn_mana = 100
        self.main = []
        self.defausse = []
        self.zonedejeu = []
    attaque = int(input("ecrire le nombre de degats"))

    def getName(self):
        return self.nom
    def getpv(self):
        return self.pv
    def getmana(self):
        return self.mana


    def jouer_une_carte(self,carte,cbn_mana):
        if carte in self.main and carte.cbn_mana <= self.mana:
            self.mana -= cbn_mana
            self.main.remove(carte)
            self.zonedejeu.append(carte)
            print(f"vous avez joue la carte"[self.carte])
        else:
            print(f"impossible de jouer la carte")

    def recup_son_mana(self,mana):
        self.mana = self.manatot
        print(f"{self.nom} a recupere du mana.")

    def attaquer(self,atk):
        if isinstance(self,Mage):
            print(f"{self.nom}attaque la creature!")
        else:
            print("Impossible d'attaquer cette cible.")

class creature:
    def __init__(self,nom,puissance):
        self.nom = nom
        self.puissance = puissance


Mage1 = Mage("joueur1",70,100,45)
Mage2 = Mage("joueur2",50,130,65)

creature1 = creature("Creature1",50)
creature2 = creature("Creature2",40)

Mage1.main.append(creature1)
Mage2.main.append(creature2)

Mage1.attaquer(Mage2)

class Cristal:
    def __init__(self,cout_mana):
        self.managenere = cout_mana
    def getmangenere(self):
        return self.managenere

class Blast:
    def __init__(self,degat,point_de_vie_en_moin):
        self.dgts= degat
        self.pv_moins = point_de_vie_en_moin
    def getdgts(self):
        return self.dgts
    def getpv(self):
        return self.pv_moins
