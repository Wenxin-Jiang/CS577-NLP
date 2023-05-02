---
language: multilingual
tags:
- text-classification
- pytorch
- nli
- xnli
- de
datasets:
- xnli

pipeline_tag: zero-shot-classification
widget:
- text: "Letzte Woche gab es einen Selbstmord in einer nahe gelegenen kolonie"
  candidate_labels: "Verbrechen,Tragödie,Stehlen"
  hypothesis_template: "In deisem geht es um {}." 

---

# German Zeroshot

## Model Description

This model has [GBERT Large](https://huggingface.co/deepset/gbert-large) as base model and fine-tuned it on xnli de dataset.
The default hypothesis template is in English: `This text is {}`. While using this model , change it to "In deisem geht es um {}." or something different. While inferencing through huggingface api may give poor results as it uses by default english template. Since model is monolingual and not multilingual, hypothesis template needs to be changed accordingly.

## XNLI DEV (german)
Accuracy: 85.5

## XNLI TEST (german)
Accuracy: 83.6

#### Zero-shot classification pipeline

```python
from transformers import pipeline
classifier = pipeline("zero-shot-classification",
                      model="Sahajtomar/German_Zeroshot")
sequence = "Letzte Woche gab es einen Selbstmord in einer nahe gelegenen kolonie"
candidate_labels = ["Verbrechen","Tragödie","Stehlen"]
hypothesis_template = "In deisem geht es um {}."    ## Since monolingual model,its sensitive to hypothesis template. This can be experimented

classifier(sequence, candidate_labels, hypothesis_template=hypothesis_template)
"""{'labels': ['Tragödie', 'Verbrechen', 'Stehlen'],
 'scores': [0.8328856854438782, 0.10494536352157593, 0.06316883927583696],
 'sequence': 'Letzte Woche gab es einen Selbstmord in einer nahe gelegenen Kolonie'}"""
```


