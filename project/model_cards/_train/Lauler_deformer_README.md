---
widget:
- text: "dem har sökt upp de för att prata."
  example_title: "de/dem exempel 1"
- text: "Jag såg de komma runt hörnet och gå i riktning mot dem byggnaderna."
  example_title: "de/dem exempel 2"
---

## DeFormer

DeFormer är en modell som har tränats på att skilja mellan `de` och `dem` i svenska meningar. Modellen kan testas direkt i panelerna till höger under **Hosted Inference API** genom att skriva in en mening och trycka på **Compute**. 

**Instruktioner (VIKTIGT):**
Använd endast de/dem med små bokstäver vid testning. I träningen av modellen gjordes alla "De" och "Dem" om till gemener. Avsluta meningen med skiljetecken (punkt, frågetecken, osv) för bäst möjliga resultat. 

## Träningsdata
DeFormer har tränats på meningar från Europarlamentet och svenskspråkiga Wikimedia. Dessa hämtades från [OPUS](https://opus.nlpl.eu/). Källorna valdes ut för att de antogs ha ett korrekt språkbruk. 

Endast meningar innehållandes `de` eller `dem` -- eller bägge två -- behölls i konstruktionen av träningsdataset. I tabellen nedan återfinns beskrivande statistik över antalet meningar som behölls från respektive dataset, samt frekvenser över förekomsten av `de/dem`. 

| Datakälla                                                                                     | Meningar    |  # De   | # Dem   | De/Dem ratio |
| -----------                                                                                   | ----------- | ------- | ------- | ------------ |
| [Europaparl sv.txt.gz](https://opus.nlpl.eu/download.php?f=Europarl/v8/mono/sv.txt.gz)           | 500660      | 465977      | 54331       | 8.57x        |
| [JRC-Acquis raw.sv.gz](https://opus.nlpl.eu/download.php?f=JRC-Acquis/mono/JRC-Acquis.raw.sv.gz) | 417951      | 408576      | 17028       | 23.99x       |
| [Wikimedia sv.txt.gz](https://opus.nlpl.eu/download.php?f=wikimedia/v20210402/mono/sv.txt.gz)    | 630601      | 602393      | 38852       | 15.48x       |
| **Total**                                                                                        | **1549212** | **1476946** | **110211**  | **13.40x**   |

Vid träningen av DeFormer introducerades slumpmässiga substitioner, där `de` eller `dem` byttes ut mot den motsatta formen. Modellen utmanades sedan att klassificera huruvida ett givet ord tillhörde ett av följande kategorier

1. **`ord`** (alla bakgrundsord som inte är de/dem tillhör denna kategori) 
2. **`DE`**
3. **`DEM`**

Innan observationerna skickades in till modellträning byttes `de` ut mot `dem` med 47 procent sannolikhet, medan `dem` byttes till `de` i 40 procent av fallen.

## Träffsäkerhet/Accuracy

DeFormer utvärderades på ett valideringsset bestående av 31200 meningar från samma datakälla (svenska wiki + europaparlamentet + JRC) som modellen tränats på. Slumpmässiga fel introducerades för att utmana modellen. 47 procent av förekommande `de` i ursprungsmeningarna ändrades till `dem`, medan 40 procent av förekommande `dem` ändrades till `de`. Tabellen nedan visar att DeFormer är väldigt träffsäker. De få "felaktiga" prediktioner som modellen outputtar är nästan samtliga `de/dem som`-konstruktioner med bisatser. Majoriteten av dessa är egentligen inte att anse som felaktiga, eftersom [båda formerna är accepterade](https://www4.isof.se/cgi-bin/srfl/visasvar.py?sok=dem%20som&svar=79718&log_id=705355).

|             | Accuracy    |
| ----------- | ----------- |
| de          | 99.9\%      |
| dem         | 98.6\%      |