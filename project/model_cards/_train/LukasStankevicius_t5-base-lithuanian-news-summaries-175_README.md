---
language: lt
tags:
- t5
- Lithuanian
- summarization
widget:
- text: "Latvijos krepšinio legenda Valdis Valteris pirmadienį socialiniame tinkle pasidalino statistika, kurios viršūnėje yra Arvydas Sabonis. 1982 metais TSRS rinktinėje debiutavęs 222 cm ūgio vidurio puolėjas su raudona apranga sužaidė 52 rungtynes, per kurias rinko po 15,6 taško. Tai pats aukščiausias rezultatyvumo vidurkis tarp visų sovietų komandai atstovavusių žaidėjų, skaičiuojant tuos, kurie sužaidė ne mažiau nei 50 rungtynių. Antras šioje rikiuotėje kitas buvęs Kauno „Žalgirio“ krepšininkas Rimas Kurtinaitis. Jis debiutavo TSRS rinktinėje vėliau nei Sabas, – 1984 metais, bet irgi sužaidė 52 mačus. R.Kurtinaitis pelnė po 15 taškų. 25-ių rezultatyviausių žaidėjų sąrašu pasidalinęs latvis V.Valteris, pelnęs po 13,8 taško, yra trečias. Ketvirtas yra iš Kazachstano kilęs Valerijus Tichonenka, pelnęs po 13,7 taško per 79 rungtynes. Rezultatyviausią visų laikų TSRS rinktinės penketą uždaro Modestas Paulauskas. Lietuvos krepšinio legenda pelnė po 13,6 taško per 84 mačus. Dešimtuke taip pat yra Oleksandras Volkovas (po 13,5 taško), Sergejus Belovas (12,7), Anatolijus Myškinas (po 12,3), Vladimiras Tkačenka (11,7) ir Aleksandras Salnikovas (11,4). Dvyliktas šiame sąraše yra Valdemaras Chomičius, vidutiniškai rinkęs po 10 taškų, o keturioliktas dar vienas buvęs žalgirietis Sergejus Jovaiša (po 9,8 taško). Šarūno Marčiulionio rezultatyvumo vidurkis turėjo būti aukštesnis, bet jis sužaidė mažiau nei 50 rungtynių. Kaip žinia, Lietuvai išsilaisvinus ir atkūrus Nepriklausomybę, visi minėti mūsų šalies krepšininkai, išskyrus karjerą jau baigusį M.Paulauską, užsivilko žalią aprangą ir atstovavo savo tėvynei. A.Sabonis pagal rezultatyvumo vidurkį yra pirmas – jis Lietuvos rinktinei pelnė po 20 taškų. Antras pagal taškų vidurkį yra Artūras Karnišovas, rinkęs po 18,2 taško ir pelnęs iš viso daugiausiai taškų atstovaujant Lietuvos rinktinei (1453). Tarp žaidėjų, kurie sužaidė bent po 50 oficialių rungtynių Lietuvos rinktinėje, trečią vietą užima Ramūnas Šiškauskas (po 12,9), ketvirtąją Linas Kleiza (po 12,7 taško), o penktas – Saulius Štombergas (po 11,1 taško). Daugiausiai rungtynių Lietuvos rinktinėje sužaidęs ir daugiausiai olimpinių medalių (3) su ja laimėjęs Gintaras Einikis rinko po 9,6 taško, o pirmajame trejete pagal rungtynių skaičių ir pelnytus taškus esantis Šarūnas Jasikevičius pelnė po 9,9 taško."
license: apache-2.0
---
This is *t5-base* transformer model trained on Lithuanian news summaries for 175 000 steps.
It was created during the work [**Generating abstractive summaries of Lithuanian
news articles using a transformer model**](https://link.springer.com/chapter/10.1007/978-3-030-88304-1_27).

## Usage
```python
from transformers import pipeline
name= "LukasStankevicius/t5-base-lithuanian-news-summaries-175"
my_pipeline = pipeline(task="text2text-generation", model=name, framework="pt")
```
Given the following article body from [15min](https://www.15min.lt/24sek/naujiena/lietuva/tarp-penkiu-rezultatyviausiu-tsrs-rinktines-visu-laiku-zaideju-trys-lietuviai-875-1380030):
```
text = """
Latvijos krepšinio legenda Valdis Valteris pirmadienį socialiniame tinkle pasidalino statistika, kurios viršūnėje yra Arvydas Sabonis.
1982 metais TSRS rinktinėje debiutavęs 222 cm ūgio vidurio puolėjas su raudona apranga sužaidė 52 rungtynes, per kurias rinko po 15,6 taško. Tai pats aukščiausias rezultatyvumo vidurkis tarp visų sovietų komandai atstovavusių žaidėjų, skaičiuojant tuos, kurie sužaidė ne mažiau nei 50 rungtynių. Antras šioje rikiuotėje kitas buvęs Kauno „Žalgirio“ krepšininkas Rimas Kurtinaitis. Jis debiutavo TSRS rinktinėje vėliau nei Sabas, – 1984 metais, bet irgi sužaidė 52 mačus. R.Kurtinaitis pelnė po 15 taškų. 25-ių rezultatyviausių žaidėjų sąrašu pasidalinęs latvis V.Valteris, pelnęs po 13,8 taško, yra trečias.
Ketvirtas yra iš Kazachstano kilęs Valerijus Tichonenka, pelnęs po 13,7 taško per 79 rungtynes. Rezultatyviausią visų laikų TSRS rinktinės penketą uždaro Modestas Paulauskas. Lietuvos krepšinio legenda pelnė po 13,6 taško per 84 mačus.
Dešimtuke taip pat yra Oleksandras Volkovas (po 13,5 taško), Sergejus Belovas (12,7), Anatolijus Myškinas (po 12,3), Vladimiras Tkačenka (11,7) ir Aleksandras Salnikovas (11,4). Dvyliktas šiame sąraše yra Valdemaras Chomičius, vidutiniškai rinkęs po 10 taškų, o keturioliktas dar vienas buvęs žalgirietis Sergejus Jovaiša (po 9,8 taško). Šarūno Marčiulionio rezultatyvumo vidurkis turėjo būti aukštesnis, bet jis sužaidė mažiau nei 50 rungtynių. Kaip žinia, Lietuvai išsilaisvinus ir atkūrus Nepriklausomybę, visi minėti mūsų šalies krepšininkai, išskyrus karjerą jau baigusį M.Paulauską, užsivilko žalią aprangą ir atstovavo savo tėvynei.
A.Sabonis pagal rezultatyvumo vidurkį yra pirmas – jis Lietuvos rinktinei pelnė po 20 taškų. Antras pagal taškų vidurkį yra Artūras Karnišovas, rinkęs po 18,2 taško ir pelnęs iš viso daugiausiai taškų atstovaujant Lietuvos rinktinei (1453).
Tarp žaidėjų, kurie sužaidė bent po 50 oficialių rungtynių Lietuvos rinktinėje, trečią vietą užima Ramūnas Šiškauskas (po 12,9), ketvirtąją Linas Kleiza (po 12,7 taško), o penktas – Saulius Štombergas (po 11,1 taško). Daugiausiai rungtynių Lietuvos rinktinėje sužaidęs ir daugiausiai olimpinių medalių (3) su ja laimėjęs Gintaras Einikis rinko po 9,6 taško, o pirmajame trejete pagal rungtynių skaičių ir pelnytus taškus esantis Šarūnas Jasikevičius pelnė po 9,9 taško.
"""
text = ' '.join(text.strip().split())
```
The summary can be obtained by:
```python
my_pipeline(text)[0]["generated_text"]
```
Output from above would be:

Lietuvos krepšinio federacijos (LKF) prezidento Arvydo Sabonio rezultatyvumo vidurkis yra aukščiausias tarp visų Sovietų Sąjungos rinktinėje atstovavusių žaidėjų, skaičiuojant tuos, kurie sužaidė bent po 50 oficialių rungtynių.


If you find our work useful, please cite the following paper:
``` latex
@InProceedings{10.1007/978-3-030-88304-1_27,
author="Stankevi{\v{c}}ius, Lukas
and Luko{\v{s}}evi{\v{c}}ius, Mantas",
editor="Lopata, Audrius
and Gudonien{\.{e}}, Daina
and Butkien{\.{e}}, Rita",
title="Generating Abstractive Summaries of Lithuanian News Articles Using a Transformer Model",
booktitle="Information and Software Technologies",
year="2021",
publisher="Springer International Publishing",
address="Cham",
pages="341--352",
abstract="In this work, we train the first monolingual Lithuanian transformer model on a relatively large corpus of Lithuanian news articles and compare various output decoding algorithms for abstractive news summarization. We achieve an average ROUGE-2 score 0.163, generated summaries are coherent and look impressive at first glance. However, some of them contain misleading information that is not so easy to spot. We describe all the technical details and share our trained model and accompanying code in an online open-source repository, as well as some characteristic samples of the generated summaries.",
isbn="978-3-030-88304-1"
}
```