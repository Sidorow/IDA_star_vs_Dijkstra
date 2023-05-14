# Määrittely

Ohjelman tavoitteena on vertailla IDA* -ja Dijkstran algoritmeja suunnatussa painotetussa verkossa. Ohjelma toteutetaan Python -kielellä. Vertaisarviointia varten myös javakoodin lukeminen onnistuu.

## Algoritmit ja tietorakenteet

Työssä toteutetaan IDA* ja Dijkstran algoritmi. Tietorakenteina toimivat Pythonin taulukko, jota käytetään pinon tavoin. Sama onnistuisi myös Collections -kirjaston deque:lla. Dijkstran prioriteettijono toteutetaan kurssin ohjeiden mukaisesti itse tehokkaasti keolla.

## Ongelma ja syötteet

Ongelmana toimii painotettu verkko, josta halutaan päästä lyhimmällä polulla pisteestä X pisteeseen Y. Olen ennen tutustunut A* -algoritmiin, joten tälle sukua oleva IDA* kiinnostaa. Syötteenä ohjelma saa verkon (random generoitu), josta se pyrkii löytämään lyhimmän/halvimman polun pisteestä pisteeseen. Ohjelma toteuttaa samalle verkolle sekä IDA*- että Dijkstran algoritmin, joista sitten otetaan ulos mm aika ja käytyjen solmujen määrä ja myös jonkinlainen visuaalinen representaatio läpikäydystä polusta.

## Tavoitteena olevat aika- ja tilavaativuudet

### IDA*

- Aikavaativuus
	- O(n^m)

- Tilavaativuus
	- O(n)       

### Dijkstra

- Aikavaativuus
	- O(n + m log m)

- Tilavaativuus
	- O(n2)

## Kurssiin liittyvät asiat

- Opinto-ohjelma tietojenkäsittelytieteen kandidaatti (TKT)

- Projektin kieli Suomi
