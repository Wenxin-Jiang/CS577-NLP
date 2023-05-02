---
language:
- fr
pipeline_tag: token-classification
widget:
- text: "La # pyrale du # buis à l'air très friande du # tournesol # semences."
  example_title: "1 ravageur"
- text: "Quelles tactiques le producteur de la # SaskAg utilise-t-il pour protéger ses 13 800 acres de la cécidomyie du blé , de la fausse-teigne des crucifères , des vers-gris et des pucerons."
  example_title: "4 ravageurs"
- text: "puceron cendré sur # colza à surveiller à l ’ automne - symptômes classiques de déformation et décoloration de feuilles ( ici en Normandie ) virus transmis : mosaïque du chou-fleur et / ou du navet ( rare )."
  example_title: "Ravageur & maladie"
- text: "Traitement juste après le triage , un traitement contre la fusariose et contre la mouche grise sur cette variété car elle sera semé après betteraves."
  example_title: "Maladie & ravageur"
- text: "Nous voulons des coquelicots ! Le coquelicot héberge notamment les virus de la jaunisse grave , jaunisse modérée et occidentale de la betterave , virus latent italien de l'artichaut , virus de la mosaïque du navet , virus X de la pomme de terre et le virus du flétrissement de la fève."
  example_title: "5 maladies"
- text: "Plus j’ai du recul sur ma situation d’ancien taupin plus je me dis qu’il faut vraiment cramer les prepas et les écoles d’ingé/de commerce."
  example_title: "Taupin - prépa"
- text: "Vous savez Taupin et ses problèmes de gonades mal hydratées ?Bah c'est aussi sec, la Loire."
  example_title: "Taupin - sec"
- text: "#MercrediCestPermis je vous présente taupin et scuti. Un fléau qui va grandir avec l'arrêt des neonicotinoide. Deux ravageurs de racines qui sont friands de blé maïs pomme de terre  et autres cultures Peut provoquer la perte totale. #agriculture #FrAgTW"
  example_title: "Taupin - ravageur"
- text: "Thon juste saisi , crème de betterave , une petite rouille dont j'ignore la constitution , légumes de saison Ça va comme ça ? "
  example_title: "Rouille - sauce"
- text: "Rouille de la # betterave sucrière causée par # Uromyces betae # urédospores # phytopathologie"
  example_title: "Rouille - maladie"
- text: "Colzas qui rougissaient précocement , avec de l ’ oidium , dégâts de campagnols , mouche du chou . . ."
  example_title: "Mouche - ravageur"
- text: "Vacances de Noël : les touristes français visitent Paris à bord d’un bateau mouche."
  example_title: "Mouche - bateau"
---

### How to use

You can use this model directly with a pipeline for token classification:

```python
>>>from transformers import pipeline
>>>pipe = pipeline(model="ChouBERT/CamemBERT-plant-health-ner", aggregation_strategy="simple")
>>>pipe(" Attaque de rouille brune en Dordogne sur du blé tendre variété Oregrain !")
[]
>>>pipe("Soupe de poisson toute prête de carrefour avec fromage râpé, croûtons à l'ail et rouille #TeamFeignasse.")
[{'entity_group': 'Maladie',
  'score': 0.80249035,
  'word': '',
  'start': 11,
  'end': 12},
 {'entity_group': 'Maladie',
  'score': 0.80133665,
  'word': 'rouille brune',
  'start': 12,
  'end': 25}]
```
