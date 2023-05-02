---
language: es
license: cc-by-4.0
---
# NER-fine-tuned-BETO: model fine-tuned from BETO for NER task.
---
Language: es
Datasets:
- conll2002
- Babelscape/wikineural

## Introduction
[NER-fine-tuned-BETO] is a NER model that was fine-tuned from BETO on the 2002 Conll and the WikiNEuRal spanish datasets.
Model was trained on the Conll 2002 train dataset (~8320 sentences) and a bootstrapped dataset of WikiNEuRal, where we re-evaluate the dataset and only keep the sentences where all the labels matched the predictions made.
Model was evaluated on the test dataset of Conll2002.

## Training data
Training data was classified as follow:
|Abbreviation|  Description  |
|:----------:|:-------------:|
|     O      | Outside of NE |
|    PER     | Person’s name |
|    ORG     | Organization  |
|    LOC     |  Location     |
|   MISC     | Miscellaneous |

Alongside the IOB formatting, this is:
  - B-LABEL if the word is at the beggining of the entity.
  - I-LABEL if the word is part of the entity name, but not the first word.
  
## How to use NER-fine-tuned-BETO with HuggingFace
Load the model and its tokenizer :

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("NazaGara/NER-fine-tuned-BETO", use_auth_token=True)
model = AutoModelForTokenClassification.from_pretrained("NazaGara/NER-fine-tuned-BETO", use_auth_token=True)

nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
nlp('Ignacio se fue de viaje por Buenos aires')

[{'entity_group': 'PER',
  'score': 0.9997764,
  'word': 'Ignacio',
  'start': 0,
  'end': 7},
 {'entity_group': 'LOC',
  'score': 0.9997932,
  'word': 'Buenos aires',
  'start': 28,
  'end': 40}]

```
## Model Performance
Overall
| precision | recall | f1-score |
|:---------:|:------:|:--------:|
| 0.9833    | 0.8950 | 0.8998   |

By classes
| class  | precision | recall | f1-score |
|:------:|:---------:|:------:|:--------:|
| O      | 0.9958    | 0.9965 | 0.990    |
| B-PER  | 0.9572    | 0.9741 | 0.9654   |
| I-PER  | 0.9487    | 0.9921 | 0.9699   |
| B-ORG  | 0.8823    | 0.9264 | 0.9038   |
| I-ORG  | 0.9253    | 0.9264 | 0.9117   |
| B-LOC  | 0.8967    | 0.8736 | 0.8850   |
| I-LOC  | 0.8870    | 0.8215 | 0.8530   |
| B-MISC | 0.7541    | 0.7964 | 0.7747   |
| I-MISC | 0.9026    | 0.7827 | 0.8384   |
