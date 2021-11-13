class minimaxeri():

    def __init__(self,syvyys,koko,arvo):
        self.syvyys = syvyys
        self.koko = koko
        self.arvo = arvo
        self.lauta = [[0 for i in range(koko)] for j in range(koko)]

    def arvioi(lauta):
        #TODO
        #Koodi jollain tavoin arvioi laudan ja kykenee pisteyttämään eri tilanteita
        #Esim viiden rivit ja estämättömät neljän rivi pisteytetään todella korkeiksi koska ovat varmoja voittotilanteita  
        #(toistetaan useita, useita kertoja haun aikana)
        
        #Palauttaa rivipaikat ja arvot jossain muodossa?
        
        return

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

        self.arvioidut = self.arvioi(self.lauta)
        if oma_vuoro:
            for i in self.arvioidut:

# Tämä koko osuus vielä erittäin työn alla



        
