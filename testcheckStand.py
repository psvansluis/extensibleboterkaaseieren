def checkHorizontaalWinnaar():
    spel = BoterKaasEieren(6,4,5)
    ## Check horizontaal
    spel.bord[3][1] = 'O'
    spel.bord[3][2] = 'O'
    spel.bord[3][3] = 'O'
    spel.bord[3][4] = 'O'
    spel.checkStand()
    print(spel)
    assert spel.winnaar == 'O'

def checkVerticaalWinnaar():
    spel = BoterKaasEieren(5,3,5)
    ## Check verticaal
    spel.bord[1][3] = 'O'
    spel.bord[2][3] = 'O'
    spel.bord[3][3] = 'O'
    spel.checkStand()
    print(spel)
    assert spel.winnaar == 'O'

def checkDiagonaalLinksbovenRechtsonderWinnaar():
    spel = BoterKaasEieren(6,3,5)
    # Check diagonaal \
    spel.bord[1][1] = 'O'
    spel.bord[2][2] = 'O'
    spel.bord[3][3] = 'O'
    spel.checkStand()
    print(spel)
    assert spel.winnaar == 'O'

def checkDiagonaalRechtsBovenLinksonderWinnaar():
    spel = BoterKaasEieren(6,3,5)
    # Check diagonaal \
    spel.bord[3][1] = 'O'
    spel.bord[2][2] = 'O'
    spel.bord[1][3] = 'O'
    spel.checkStand()
    print(spel)
    assert spel.winnaar == 'O'

def checkPat():
    spel = BoterKaasEieren(2,2,4)
    spel.bord[0][1] = 'X'
    spel.bord[1][0] = 'A'
    spel.bord[0][0] = 'B'
    spel.bord[1][1] = 'O'
    spel.checkStand()
    print(spel)
    assert spel.winnaar == 'Niemand'

def checkStandAlles():
    checkHorizontaalWinnaar()
    checkVerticaalWinnaar()
    checkDiagonaalLinksbovenRechtsonderWinnaar()
    checkDiagonaalRechtsBovenLinksonderWinnaar()
    checkPat()
