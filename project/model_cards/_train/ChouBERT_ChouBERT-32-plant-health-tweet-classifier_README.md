---
language:
- fr
pipeline_tag: text-classification
widget:
- text: "Voila les limaces de retour. Ça faisait longtemps que j’en avais pas vu sur blé."
  example_title: "Observation - limace"
- text: "C’est bon le maïs , pour la pyrale. Dans le 64, les larves les plus âgées prennent des force avant de se chrysalider et faire une 2 è génération début août. ⁦@Arvalisofficiel⁩ ⁦@Fragritwittos⁩ https://t.co/JLypU2zFFe"
  example_title: "Observation - Pyrale de maïs"
- text: "JNO sur céréales à paille : de nombreux retours témoignent de dégâts importants aux quatre coins de l’Hexagone !"
  example_title: "Observation - JNO"
- text: "Ravageurs sur les maïs, 90% de la parcelle perdue. Impressionnant à voir, difficile à vivre pour l'éleveur #choucas #morbihan https://t.co/DMw3c4EtyQ"
  example_title: "Observation - Corbeau"
- text: "Visite des plateformes d’essais dans les #Vosges on observe un flétrissement des feuilles de #maïs et surprise on trouve un Taupin. #lorraine #babycorn https://t.co/xh4NExMvDv"
  example_title: "Observation - Taupin"
- text: "Erreur le taupin creuse dans la tige du maïs, à croire que vous n avez jamais vu de dégâts ! La seule solution pour l instant c est la chimie le reste c est de la poudre de perlinpinpin"
  example_title: "Information général-Taupin"
- text: "Lol taupin ? Toi qui critiquait le programme de classe prépa LoL ! "
  example_title: "Hors sujet - Taupin"
- text: "En attendant grâce au Bt je n’ai jamais vu de pyrale dans un champ de maïs grain de toute ma vie."
  example_title: "Non-observation - Pyrale"
- text: "Protection des cultures corvidé, pigeon. Étude scientifique baguage gibier d'eau et bécasse pour mieux connaître les animaux migrateurs. Étude menée par les chasseurs sur les sangliers. Plantation de de plusieurs km de haie(refuge pour la petite et moyenne faune)"
  example_title: "Non-observation - Corbeau"
- text: "RT C'est un #puceron des #céréales! ... qui transmet le #virus de la #JNO . Pas un puceron de l'#agriconventionnelle ou de l'#agr…"
  example_title: "Non-observation - JNO"
---
### How to use

You can use this model directly with a pipeline for text-classification:

```python
from transformers import pipeline
pipe = pipeline(model="ChouBERT/ChouBERT-32-plant-health-tweet-classifier")
pipe("Voila les limaces de retour. Ça faisait longtemps que j’en avais pas vu sur blé.")
```

Here is how to use this model to get the features of a given text in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("ChouBERT/ChouBERT-32-plant-health-tweet-classifier")
model = AutoModelForSequenceClassification.from_pretrained("ChouBERT/ChouBERT-32-plant-health-tweet-classifier")
text = "Il y a 7 jours le blé ne pointait pas encore. Aujourd’hui 1,5 feuille et dégat de limace. Intervention a venir."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```