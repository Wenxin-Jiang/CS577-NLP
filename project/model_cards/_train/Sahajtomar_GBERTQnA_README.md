
---
language: de
tags:
- pytorch
- tf
- bert
datasets:
- mlqa
metrics:
- f1
- em
---

### QA Model trained on MLQA dataset for german langauge.

MODEL used for fine tuning is GBERT Large by deepset.ai



## MLQA DEV (german)
EM: 63.82 
F1: 77.20

## XQUAD TEST (german)
EM: 65.96 
F1: 80.85

## Model inferencing:
```python
!pip install -q transformers
from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="Sahajtomar/GBERTQnA",
    tokenizer="Sahajtomar/GBERTQnA"
)

qa_pipeline({
    'context': "Vor einigen Jahren haben Wissenschaftler ein wichtiges Mutagen identifiziert, das in unseren eigenen Zellen liegt: APOBEC, ein Protein, das normalerweise als Schutzmittel gegen Virusinfektionen fungiert. Heute hat ein Team von Schweizer und russischen Wissenschaftlern unter der Leitung von Sergey Nikolaev, Genetiker an der Universität Genf (UNIGE) in der Schweiz, entschlüsselt, wie APOBEC eine Schwäche unseres DNA-Replikationsprozesses ausnutzt, um Mutationen in unserem Genom zu induzieren.",
    'question': "Welches Mutagen schützt vor Virusinfektionen?"
    
})

# output

{'answer': 'APOBEC', 'end': 121, 'score': 0.9815779328346252, 'start': 115} 

## Even complex queries can be answered pretty well

qa_pipeline({
    "context": 'Im Juli 1944 befand sich die Rote Armee tief auf polnischem Gebiet und verfolgte die Deutschen in Richtung Warschau. In dem Wissen, dass Stalin der Idee eines unabhängigen Polens feindlich gegenüberstand, gab die polnische Exilregierung in London der unterirdischen Heimatarmee (AK) den Befehl, vor dem Eintreffen der Roten Armee zu versuchen, die Kontrolle über Warschau von den Deutschen zu übernehmen. So begann am 1. August 1944, als sich die Rote Armee der Stadt näherte, der Warschauer Aufstand. Der bewaffnete Kampf, der 48 Stunden dauern sollte, war teilweise erfolgreich, dauerte jedoch 63 Tage. Schließlich mussten die Kämpfer der Heimatarmee und die ihnen unterstützenden Zivilisten kapitulieren. Sie wurden in Kriegsgefangenenlager in Deutschland transportiert, während die gesamte Zivilbevölkerung ausgewiesen wurde. Die Zahl der polnischen Zivilisten wird auf 150.000 bis 200.000 geschätzt.'
    'question': "Wer wurde nach Deutschland transportiert?"

#output

{'answer': 'die Kämpfer der Heimatarmee und die ihnen unterstützenden Zivilisten',
 'end': 693,
 'score': 0.23357819020748138,
 'start': 625}
    

```

Try it on a Colab:
 
 <a href="https://github.com/Sahajtomar/Question-Answering/blob/main/Sahajtomar_GBERTQnA.ipynb" target="_parent"><img src="https://camo.githubusercontent.com/52feade06f2fecbf006889a904d221e6a730c194/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667" alt="Open In Colab" data-canonical-src="https://colab.research.google.com/assets/colab-badge.svg"></a>
