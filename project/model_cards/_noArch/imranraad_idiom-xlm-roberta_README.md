---
tags:
- autotrain
- token-classification
language:
- en
widget:
- text: >-
    He at the last appointed him on one, And let all others from his hearte gon,
    And chose her of his own authority; For love is blind all day, and may not
    see.
- text: >-
    I’m sorry but I just can’t seem to wrap my head around it. - I’m sorry but I
    just can’t seem to understand.
- text: Why are you so bent out of shape? - Why are you so upset?
- text: Listen, it is easier said than done, many people lack commitment.
co2_eq_emissions:
  emissions: 0.04215761331893144
license: mit
library_name: transformers
pipeline_tag: token-classification
---

# Fine-tune datasets
 - MAGPIE corpus: https://aclanthology.org/2020.lrec-1.35/
 - EPIE corpus: https://link.springer.com/content/pdf/10.1007/978-3-030-58323-1.pdf


# Model Trained Using AutoTrain

- Problem type: Entity Extraction
- Model ID: 1595156286
- CO2 Emissions (in grams): 0.0422

## Validation Metrics

- Loss: 0.012
- Accuracy: 0.996
- Precision: 0.000
- Recall: 0.000
- F1: 0.000

## Usage

### You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/imranraad/autotrain-magpie-epie-combine-xlmr-metaphor-1595156286
```

### Or Python API:

```
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained("imranraad/autotrain-magpie-epie-combine-xlmr-metaphor-1595156286", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("imranraad/autotrain-magpie-epie-combine-xlmr-metaphor-1595156286", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```

### How to get the idioms:

```
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

model = AutoModelForTokenClassification.from_pretrained("imranraad/idiom-xlm-roberta")

tokenizer = AutoTokenizer.from_pretrained("imranraad/idiom-xlm-roberta")

pipeline_idioms = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

text = "Why are you so bent out of shape? - Why are you so upset?"

idioms = pipeline_idioms(text)
for idiom in idioms:
    if idiom['entity_group'] == '1':
        print(idiom['word'])
```