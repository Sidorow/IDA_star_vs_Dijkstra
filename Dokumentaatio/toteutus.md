# Ohjelman yleisrakenne

Ohjelmassa on konsoliin perustuva käyttöliittymä, johon voidaan kirjoittaa komentoja. GraphGen-luokka huolehtii verkon muodostamisesta ja/tai sen satunnaistamisesta. Dijkstra sekä IDA* on ulkoistettu omiin luokkiinsa ja Dijkstran prioriteettijonona toimiva keko on omassa luokassaan. Ohjelmassa voidaan piirtää ruudulle satunnainen tasoverkko ja hakea valituilla lähtö- ja maalisolmuilla lyhin reitti näiden välillä. 

## Algoritmit

### IDA*

IDA* tai Iterative Deepening A* on reitinhakualgoritmi, joka löytää painotetussa verkossa lyhimmän polun kahden solmun välillä. Se on variantti Iterative Deepening Depth-First Search tai [IDDFS](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search), mutta hyödyntää A*:ista tuttua heuristiikkafunktiota. Ohjelmassa solmut on asetettu tasolle koordinaattien mukaan, josta IDA*:in heuristiikkafunktio laskee euklidisen (linnuntie) etäisyyden solmusta maalisolmuun. Koska IDA* hyödyntää syvyyshakua, sen muistinkäyttö on pienempi kuin A*.

### Dijkstra

Dijkstra on myös reitinhakualgoritmi, jolla löydetään painotetussa verkossa lyhin polku lähtösolmusta kaikkiin muihin solmuihin. Haku voidaan kuitenkin päättää maalisolmun löydettyä. IDA*:iin verrattuna Dijkstra käyttää enemmän muistia, sillä se tallettaa jokaisen läpikäydyn solmun pinoon. 

## Algoritmien Aika- ja tilavaativuudet

### IDA*

- Aikavaativuus
	- O(n^m)
	- Jossa n on keskimääräinen solmun aste ja m on ratkaisun syvyys.

- Tilavaativuus
	- O(n)
	- IDA* ei tallenna läpikäytyjä solmuja, joten tilavaativuus on pieni.       

### Dijkstra

- Aikavaativuus
	- O(n + m log m)
	- Jossa m on solmujen määrä ja n kaarien määrä.

- Tilavaativuus
	- O(2n)
	- Kun käytetään kekoa prioriteettijonon lailla.

### Vertailu

Suorituskykyvertailua [testidokumentaatiossa](https://github.com/Sidorow/IDA_star_vs_Dijkstra/blob/main/Dokumentaatio/testaus.md)

Dijkstra ja IDA* molemmat löytävät useimmissa tilanteissa hyvässä ajassa lyhimmän polun kahden solmun välillä. Riippuu myös monesta asiasta, milloin kumpikin on toista nopeampi. Esimerkiksi verkolla ja sen solmujen asteella on suuri vaikutus IDA*:in toimivuuteen. Joissain tilanteissa IDA* saattaa olla hitaampi, mutta pienemmän muistinkäytön ansiosta se voi olla mieluisampi. IDA*:in heuristiikkafunktiolla on suuri vaikutus sen toimivuuteen sekä nopeuteen, joten on tärkeää että se on hyvin implementoitu ja että edes käytetään ongelmaan sopivaa heuristiikkaa. Tässä ohjelmassa tasoverkon solmujen koordinaatteihin sopii hyvin euklidinen etäisyys heuristiikkafunktiona.

### Paranneltavaa

IDA*:in heuristiikka vaikuttaisi toimivan suhteellisen hyvin pienemmillä verkoilla. Kuitenkin tuli huomattua suuremmissa planaarisissa verkoissa, että algoritmi jäi helposti junnaamaan lähes paikalleen. En ole täysin varma mistä ongelma voisi johtua. Ehkä verkon solmujen ja kaarien generoinnissa on jotain, mikä vaikuttaa negatiivisesti IDA*:iin.

### Lähteet

https://en.wikipedia.org/wiki/Iterative_deepening_A*#Properties

https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search

https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search#Time_complexity

https://fi.wikipedia.org/wiki/Dijkstran_algoritmi

Tietorakenteet ja Algoritmit -kurssikirja
