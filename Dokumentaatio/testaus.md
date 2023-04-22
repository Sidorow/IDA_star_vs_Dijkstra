## Kattavuus:
[![codecov](https://codecov.io/gh/Sidorow/IDA_star_vs_Dijkstra/branch/main/graph/badge.svg?token=0ROMBGJ0HK)](https://codecov.io/gh/Sidorow/IDA_star_vs_Dijkstra)

# Testaus

## Mitä testattu?

- Molempia algoritmeja, jotta ne palauttavat esimerkkiverkosta oikean lyhimmmän polun. Dijkstralla myös solmujen oikeat etäisyydet.

- Kekoa/prioriteettijonoa, jotta tästä saadaan aina pienin arvo ulos.

- Verkkogeneraattori WIP

## Toistettavuus

- Testit toimivat automaattisilla yksikkötesteillä.

- Ohjelma tuottaa suoritettaessa graafisen verkon, jossa solmujen väliset painot on laskettu niiden euklidisen etäisyyden perusteella. Empiirisesti voidaan katsoa, että algoritmi löytää oikean lyhimmän reitin kahden solmun välillä, jos sellainen polku löytyy.
