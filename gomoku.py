import gomoku_ai 
import copy

#import pygame Kun kaikki muu on valmista ja halutaan rakentaa visuaalinen näkymä;
#Ennen tätä voidaan jatkaa minimaalisella tekstikäyttöliittymällä
#Koska tärkeintä on että saadaan se algoritmi hoidettua

pelaaja1 = 1
pelaaja2 = 2


#Pelaajan tyyppi vastaa siitä, tekeekö algoritmi seuraavan valinnan, vai tekeekö ihminen. 
#Ennen tekoälyn luontia molempien pelaajien tyypin on oltava ihminen (True)
#Vastaavalla tavalla tilaa pelitekoälylle on yritetty jättää kaikkialle muuallekin
#Voi toki olla että rakennetta joudutaan muuttamaan jollakin merkittävällä tavalla vielä myöhemmin

ihminen = [False for i in range(3)]
ihminen[pelaaja1] = True
ihminen[pelaaja2] = False



laudan_koko = 15
tietokonepelaaja = gomoku_ai.minimaxeri(3,laudan_koko,2)


def peli():
    pelilauta = [[0 for i in range(laudan_koko)] for j in range(laudan_koko)]
    for i in pelilauta:
                print(i)

    vuoro = pelaaja1
    voittaja = 0

    while True:
        if ihminen[vuoro]:
            siirto = input()
            while not hyvaksytty_siirto(siirto,pelilauta,vuoro):
                siirto = input()
            for i in pelilauta:
                print(i)
            if tarkista_voitto(pelilauta):
                voittaja = vuoro
                break
            vuoro = vuoro_vaihda(vuoro)

        else:
            lauta = copy.deepcopy(pelilauta)
            siirto = tietokonepelaaja.minimax_alku(lauta)
            print (siirto)
            siirto2 = str(siirto[1]) + "," + str(siirto[2])

            if not hyvaksytty_siirto(siirto2,pelilauta,vuoro):
                print ("hups, jokin meni pieleen")
                break
            for i in pelilauta:
                print(i)
            if tarkista_voitto(pelilauta):
                voittaja = vuoro
                break
            vuoro = vuoro_vaihda(vuoro)
    print (f"\nPelaaja {voittaja} voitti!")



def vuoro_vaihda(vuoro):
    if vuoro == pelaaja2:
        vuoro = pelaaja1
    else: vuoro = pelaaja2
    return vuoro

def hyvaksytty_siirto(siirto_txt, pelilauta,vuoro):
    #Siirron "muodon" tarkistamiseen ei käytetä resursseja tässä vaiheessa
    #Tarkoitus on korvata tämä visuaalisella pygame-liittymällä myöhemmin, josta muoto otetaan automaattisesti oikein
    #Oikea muoto nykyisessä versiossa on "numero,numero"
    siirto = siirto_txt.split(",")
    x = int(siirto[1])
    y= int(siirto[0])
    if pelilauta[y][x] == 0:
        pelilauta[y][x] = vuoro
        return True
    else: return False


#Säännöillä, joilla yli 5 mittainenkin rivi voittaa
#Suomalaisille tämä versio pelistä on vähän tutumpi
def tarkista_voitto(pelilauta):
    for i in range(laudan_koko):
        for j in range(laudan_koko):
            if pelilauta[i][j] != 0:
                laskenta = 1
                arvo = pelilauta[i][j]
                if i <= laudan_koko-5:
                    while True:
                        if i + laskenta >= laudan_koko:
                            break
                        if pelilauta[i+laskenta][j] == arvo:
                            laskenta += 1
                        else: break
                if laskenta == 5:
                    return True
                laskenta = 1
                if j <= laudan_koko-5:
                    while True:
                        if j + laskenta >= laudan_koko:
                            break
                        if pelilauta[i][j+laskenta] == arvo:
                            laskenta += 1
                        else: break
                if laskenta == 5:
                    return True
                if i <= laudan_koko-5 and j <= laudan_koko-6:
                    while True:
                        if i + laskenta >= laudan_koko or j+laskenta>= laudan_koko:
                            break
                        if pelilauta[i+laskenta][j+laskenta] == arvo:
                            laskenta += 1
                        else: break
                if laskenta == 5:
                    return True
                if i <= laudan_koko-5 and j >= 4:
                    while True:
                        if i + laskenta >= laudan_koko or j-laskenta < 0:
                            break
                        if pelilauta[i+laskenta][j-laskenta] == arvo:
                            laskenta += 1
                        else: break
                if laskenta == 5:
                    return True
                







peli()

