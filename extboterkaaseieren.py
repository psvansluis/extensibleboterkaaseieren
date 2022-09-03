class BoterKaasEieren:
    def __init__(self, dimbord, dimwinst, nspelers):
        self.dimbord = dimbord
        self.dimwinst = dimwinst
        self.nspelers = nspelers
        self.bord = [[None for y in range(dimbord)] for x in range(dimbord)]
        self.spelerfiches = ['X', 'O'] + \
            [chr(i) for i in range(65,63+self.nspelers) if i != 79 and i != 88]
        self.winnaar = None

    def __str__(self):
        out = []
        for j in range(self.dimbord):
            out.append([' ' if i is None else i for i in self.bord[j]])
            out[j] = '|'.join(out[j])
        horizontalbar = "\n" + "-+" * (self.dimbord - 1) + '-\n'
        if self.winnaar == None: 
            status = f"Er zijn {self.nspelers} spelers." + \
                f"\n{self.dimwinst} op een rij om te winnen." + \
                f"\n{self.spelerfiches[0]} is aan de beurt." 
        else: 
            status = f"Het spel is afgelopen.\n{self.winnaar} heeft gewonnen!"  
        return horizontalbar.join(out) + "\n\n" + status

    def geefBeurtDoor(self):
        self.spelerfiches = self.spelerfiches[1:] + [self.spelerfiches[0]]

    def checkWinnaar(self):
        def checkHorizontaal(bord):
            for rij in range(self.dimbord):
                for fiche in self.spelerfiches:
                    count = 0
                    maxcount = 0
                    for kolom in bord[rij]:
                        if kolom == fiche:
                            count +=1
                        elif count > maxcount:
                            maxcount = count
                            count = 0
                        else:
                            count = 0
                    if count > maxcount: 
                        maxcount = count
                    if maxcount >= self.dimwinst:
                        self.winnaar = fiche
                        return fiche
                        
        def transponeer(bord):
            out = []
            for i in range(len(bord)):
                out.append([item[i] for item in bord])
            return out

        def checkDiagonaal(bord):
            startcoordinaten = [(i,0) for i in range(self.dimbord)] + [(0,i) for i in range(1,self.dimbord)]
            diagonalen = []
            for coord in startcoordinaten:
                diagonaal = [coord]
                while (diagonaal[-1][0] < self.dimbord-1 \
                    and diagonaal[-1][1] < self.dimbord-1):
                    diagonaal.append((diagonaal[-1][0] + 1, diagonaal[-1][1]+1))
                diagonalen.append(diagonaal)
            for diagonaal in diagonalen:
                for fiche in self.spelerfiches:
                    count = 0
                    maxcount = 0
                    for coordinate in diagonaal:
                        if bord[coordinate[0]][coordinate[1]] == fiche:
                            count +=1
                        elif count > maxcount:
                            maxcount = count
                            count = 0
                        else: 
                            count = 0
                    if count > maxcount:
                        maxcount = count
                    if maxcount >= self.dimwinst:
                        self.winnaar = fiche
                        return fiche

        def spiegel(bord):
            return list(reversed(bord))

        ##Check winnaar
        checkHorizontaal(self.bord) ## horizontaal -
        checkHorizontaal(transponeer(self.bord)) ## verticaal |
        checkDiagonaal(self.bord) ## diagonaal \
        checkDiagonaal(spiegel(self.bord)) ## diagonaal / 

    def checkBordVol(self):
        volleRijTeller = 0
        for rij in self.bord:
            if None not in rij:
                volleRijTeller += 1
        if volleRijTeller >= self.dimbord: 
            self.winnaar = "Niemand"
            return "Niemand"

    def checkStand(self):
        out = None
        out = self.checkBordVol()
        out = self.checkWinnaar()
        return out

    def actie(self, rij, kolom):
        ## Check of input binnen bord valt
        if not ((self.dimbord >= rij > 0) and (self.dimbord >= kolom > 0)): 
            raise IndexError("Input valt buiten het bord!")
        ## Check voor leeg vak
        if not self.bord[rij-1][kolom-1] == None:
            raise IndexError("Er is al een zet gedaan in dit vak!")            
        ## Doe zet
        self.bord[rij-1][kolom-1] = self.spelerfiches[0]
        ## Check stand
        self.checkStand()
        ## Geef beurt door
        self.geefBeurtDoor()    

def inputZet(spel):
    rij = input(f"{spel.spelerfiches[0]}, kies een rij (1 t/m {spel.dimbord}): ")
    kol = input(f"{spel.spelerfiches[0]}, kies een kolom (1 t/m {spel.dimbord}): ")
    spel.actie(int(rij),int(kol))

def nieuwSpel():
    bordformaat = input("Voer een getal in voor het formaat bord (N*N): ")
    nwinst = input("Kies het aantal fiches op een rij voor winst: ")
    nspelers = input("Kies het aantal spelers: ")
    return BoterKaasEieren(int(bordformaat),int(nwinst),int(nspelers))

spel = nieuwSpel()
while True:
    print(spel)
    inputZet(spel)
    if spel.winnaar is not None:
        print(spel)
        spel = nieuwSpel()

