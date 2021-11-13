# Määrittelydokumentti

- Käytän projektin toteutukseen Pythonia. Osaan myös käyttää Javaa riittävän hyvin vertaisarvioidakseni sillä tehtyjä projekteja (voin tarvittaessa myös siirtyä toteuttamaan kurssia itse Javalla, jos ohjaaja sitä ehdottomasti suosittelee)
- Toteutan työssäni minimax-algoritmin, joka hyödyntää alpha-beta karsinaa
- Pyrin toteuttamaan Gomoku-peliä pelaavan algoritmin joka voi pelata ihmistä vastaan. Tutustuttuani aiheeseen päädyin siihen tulokseen, että minimax-algoritmi sopii tähän tehtävään, koska sillä voidaan vertailla siirtojen kannattavuutta halutulla tavalla. Karsinnasta on hyötyä, koska sillä voidaan huomattavasti tehostaa tällaista algoritmia.
- Ohjelma saa syötteiksi vastustajan (ihmisen) siirtoja yksi kerrallaan ja ne muuttavat asetelmaa josta minimax-haku suoritetaan.
-Pelkän Minimaxin aikavaativuus on O(b^d) ja tilavaativuus on O(bd) jossa b on tutkittavien siirtojen määrä ja d on tutkinnan syvyys, koska kyseessä on puita tutkiva algoritmi. Tarkoitus olisi alpha-beta karsinnan avulla saavuttaa parempi tilanne.

*Olen tietojenkäsittelytieteen kandidaattiopiskelija, dokumentaatiossa käytetty kieli on suomi*