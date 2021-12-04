rivit_katki = {
#näitä vedetty hatusta, vähän sinne päin ja niin edelleen. Millaiset rivit hyviä?
[1,1,1,1,1]:99999999,
[1,1,0,1,1]:9000,
[1,1,1,1,0]:90,
[1,1,0,0,0]: 5,
[1,0,1,0,0]: 5,

[1,1,1,0,1]:20,
[1,1,0,1,1]:20,

[1,1,1,0,0]:3,
[1,1,0,1,0]:3,

[0,0,0,0,0]:0,


}

rivit_auki = {
    [1,1,0,1,1]:9000,
    [1,1,1,1,0]:9000,
    [1,1,0,1,0]:90,
    [0,1,1,1,0]:90,
    [1,1,1,1,0]:900,
    [1,0,1,0,0]: 10,
    [1,1,0,0,0]: 10,
    [1,1,0,0,-1]: 5,
    [1,0,1,0,-1]: 5,
    [1,0,0,0,0]:0,
    
}

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
                    laudan_arvo += self.arvio_apuri(j,i,vuoro)
        
        return laudan_arvo
    
    def hae_siirrot(self):
        #hakee tyhjät
        siirrot = []
        for i in range(self.koko):
            for j in range(self.koko):
                if self.lauta[i][j] == 0:
                    siirrot.append([i,j])
        siirrot.sort(key=self.jarjestysapuri)
        return siirrot
    
    def jarjestysapuri(self,x):
        #keskellä olevat siirrot tutkimukseni perusteella parempia, hakee etäisyyksiä keskustaan järjestyksen avuksi
        #se miten minimax kuuluisi tapahtua käyttää hyväksi sitä että otollisemmat siirrot tutkitaan ensin.
        return (abs(self.koko/2 - x[0]) + abs(self.koko/2 - x[1]))
    
    def arvio_apuri(self, x, y, vuoro):
        rivien_arvo = 0
        skip = False
        #vasemmalta oikealle:
        if x <= self.koko-5:
            if not x == 0 or self.lauta[y][x-1] == 0:
                katki = False
            else: katki = True
            self.arvioija[0] = 1
            for i in range(4):
                arvo = self.lauta[y][x+1+i]
                if arvo == vuoro:
                    arvo = 1
                elif arvo != 0:
                    if katki:
                        skip = True
                    else:
                        arvo = -1
                self.arvioija[x+i+1] = arvo
            if not skip:
                if self.lauta[y][x+5] != 0:
                    katki = True
                try:
                    if katki:
                        rivien_arvo += rivit_katki[self.arvioija]
                    else:
                        rivien_arvo += rivit_auki[self.arvioija]
                except:
                    rivien_arvo += sum(self.arvioija)
                #Ei-arvioinnin arvoisille tilanteille ja niille joita ei ole vielä kirjoitettu
        
        self.arvioija = [0 for i in range(5)]
        #sama ylhäältä alas
        skip = False
        if y <= self.koko-5:
            if not x == 0 or self.lauta[y-1][x] == 0:
                katki = False
            else: katki = True
            self.arvioija[0] = 1
            for i in range(4):
                arvo = self.lauta[y+1+i][x]
                if arvo == vuoro:
                    arvo = 1
                elif arvo != 0:
                    if katki:
                        skip = True
                    else:
                        arvo = -1
                self.arvioija[x+i+1] = arvo
            if self.lauta[y+5][x] != 0:
                katki = True
            if not skip:
                try:
                    if katki:
                        rivien_arvo += rivit_katki[self.arvioija]
                    else:
                        rivien_arvo += rivit_auki[self.arvioija]
                except:
                    rivien_arvo += sum(self.arvioija)
            
            self.arvioija = [0 for i in range(5)]
                #kulmittain:
            skip = False
            if x <= self.koko-5:
                if not x == 0 or y == 0 or self.lauta[y-1][x-1] == 0:
                    katki = False
                else:
                    katki = True

                self.arvioija[0] = 1
                for i in range(4):
                    arvo = self.lauta[y+1+i][x+1+i]
                    if arvo == vuoro:
                        arvo = 1
                    elif arvo != 0:
                        if katki:
                            skip = True
                        else:
                            arvo = -1
                    self.arvioija[x+i+1] = arvo
                if self.lauta[y+5][x+5] != 0:
                    katki = True
                if not skip:
                    try:
                        if katki:
                            rivien_arvo += rivit_katki[self.arvioija]
                        else:
                            rivien_arvo += rivit_auki[self.arvioija]
                    except:
                        rivien_arvo += sum(self.arvioija)
            self.arvioija = [0 for i in range(5)]
            skip = False
            if x >= 4:
                if not x == self.koko or y == 0 or self.lauta[y-1][x+1] == 0:
                    katki = False
                else:
                    katki = True

                self.arvioija[0] = 1
                for i in range(4):
                    arvo = self.lauta[y+1+i][x-1-i]
                    if arvo == self.arvo:
                        arvo = 1
                    elif arvo != 0:
                        if katki:
                            skip = True
                        else:
                            arvo = -1
                    self.arvioija[x-i-1] = arvo
                if self.lauta[y+5][x-5] != 0:
                    katki = True
                if not skip:
                    try:
                        if katki:
                            rivien_arvo += rivit_katki[self.arvioija]
                        else:
                            rivien_arvo += rivit_auki[self.arvioija]
                    except:
                        rivien_arvo += sum(self.arvioija)
            self.arvioija = [0 for i in range(5)]

        return rivien_arvo
                
        
        



        
            



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

        if syvyys <= 0: return self.paras

        siirrot = self.hae_siirrot()
        if oma_vuoro:            
            for i in siirrot:
                self.lauta[i[0]][i[1]] = self.arvo
                arvo = self.arvioi(self.lauta,self.arvo)
                if arvo >= self.paras[0]:
                    self.paras = [self.minimax(syvyys-1,False),i[0],i[1]]
                self.lauta[i[0]][i[1]] = 0
        
        else:
            for i in siirrot:
                hjalp = [0,0,0]
                self.lauta[i[0]][i[1]] = 3-self.arvo
                arvo = self.arvioi(self.lauta,3-self.arvo)
                if arvo > hjalp[0]:
                    hjalp = [arvo,i[0],i[1]]
                self.lauta[i[0]][i[1]] = 0
            self.lauta[hjalp[1]][hjalp[2]] = 3-self.arvo
            self.paras = [self.minimax(syvyys-1,True),hjalp[1],hjalp[2]]
        
        return self.paras




        
