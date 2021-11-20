rivit = {
#näitä vedetty hatusta, vähän sinne päin ja niin edelleen. Millaiset rivit hyviä?
[1,1,1,1,1]:99,
[0,1,1,1,1]:90,
[-1,1,1,1,1]:4,

[0,1,1,1,0]:90,
[0,1,1,0]: 2,
[0,1,0,1,0]: 2,

[-1,1,1,1,0,1]:4,
[0,1,1,0,1,1]:4,
[-1,1,1,0,1,1]:4,

[-1,1,1,1]:3,
[1,1,0,1]:3,
[1,1,0,1]:kolme,


}
#Korvaa omalla systeemillä myöhemmin? Dict on kiva :(

class minimaxeri():

    def __init__(self,syvyys,koko,arvo):
        self.syvyys = syvyys
        self.koko = koko
        self.arvo = arvo
        self.lauta = [[0 for i in range(koko)] for j in range(koko)]
        self.arvioija = [0 for i in range(5)]

    def arvioi(self, lauta,vuoro):
        laudan_arvo = 0
        for i in range(self.koko):
            for j in range(self.koko):
                if lauta[i][j] == vuoro:
                    laudan_arvo += self.arvio_apuri(j,i)
        
        return
    
    def arvio_apuri(self, x, y, vuoro):
        rivien_arvo = 0
        #vasemmalta oikealle:
        if not x == 0 or self.lauta[y][x-1] == 0:
            katki_vasen = False
        else: katki_vasen = True
        self.arvioija[0] = 1
            



    def minimax_alku(self,lauta):
        #TODO
        #Koodi joka käynnistää minimax haun ja lopettaa sen kun saadaan tulos
        self.lauta = lauta
        self.paras = self.minimax(self.syvyys, True)
        return self.paras
    
    def minimax(self, syvyys, oma_vuoro):
        #TODO
        #Varsinainen minimax haku
        #Jonka olisi tarkoitus antaa paras siirto
        paras = None

        if syvyys <= 0: return paras

        
        if oma_vuoro:
            self.arvioidut = self.arvioi(self.lauta,self.arvo)
            for i in self.arvioidut:

# Tämä koko osuus vielä erittäin työn alla



        
