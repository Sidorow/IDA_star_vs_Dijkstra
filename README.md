# IDA-star-VS-Dijkstra
## TKT-kandidaatin tutkinnon tietorakenteet ja algoritmit -harjoitustyö

[Määrittely](https://github.com/Sidorow/IDA-star-VS-Dijkstra/blob/main/Dokumentaatio/maarittely.md)

[Testaus](https://github.com/Sidorow/IDA_star_vs_Dijkstra/blob/main/Dokumentaatio/testaus.md)

[Toteutus](https://github.com/Sidorow/IDA_star_vs_Dijkstra/blob/main/Dokumentaatio/toteutus.md)

## Käyttöohjeet:

## Asennus

```bash
poetry install
```
 
## Käynnistäminen

```bash
poetry run invoke start
```

## Käyttäminen
Kirjoittamalla konsoliin "help" saa listan käytettävistä komennoista.
- "exit": Poistuu ohjelmasta. 
- "plot": Piirtää ruudulle matplot:in avulla kuvan nykyisestä verkosta.
- "gen": Generoi satunnaisen 20 solmun tasoverkon.
- "choose": Ottaa numeromuotoisen syötteen konsolista lähtösolmulle ja maalisolmulle.
- "path": Piirtää ruudulle kuvan nykyisestä verkosta ja korostaa punaisella lyhimmän löydetyn reitin ja tulostaa konsoliin algoritmien ajoajat. Ajat myös tallennetaan listalle.
- "times": Tulostaa konsoliin molempien algoritmien ajoaikojen keskiarvot. "path" -komennolla voidaan tallentaa aikoja.
- "clear": Tyhjentää aikalistan.
- "compare": Vertailee alogoritmien ajoaikoja täysin satunnaistetuissa verkoissa nostaen solmujen määrää askeleittain. Polut ovat suhteellisen lyhyitä. 

## Testit

```bash
poetry run invoke test
```
