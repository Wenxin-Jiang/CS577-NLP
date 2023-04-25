---
language: 
  - es
license: isc
library_name: flair
tags:
- flair
- token-classification
metrics:
- f1
- precision
- recall
- accuracy
widget:
- text: "Jean Paul Gaultier Classique - 50 ML Eau de Parfum  Damen Parfum"
---

# What is YODA

YODA is a series of models for Google Feed product optimization. We aim to increase the market reach for ecommerce by augmenting and improving certain metadata like short titles, colors, measures and more. YODA is being used in production by +300 companies with +3.5M products.

## What we use NER for

We have trained a NER model for product feature extraction. We retrieve data like colors, sizes, brands and energy labels. Trained with +3M lines of product metadata, the model returns the next scores:

Results:
- F-score (micro) 0.972
- F-score (macro) 0.9692
- Accuracy 0.9461

By class:
|        | precision | recall | f1-score | support |
| ------ | --------- | ------ | -------- | ------- |
| size   | 0.9734    | 0.9793 | 0.9764   | 26707   |
| brand  | 0.9618    | 0.9788 | 0.9702   | 15621   |
| color  | 0.9566    | 0.9612 | 0.9589   | 6785    |
| energy | 0.9444    | 1.0000 | 0.9714   | 119     |

|              | precision | recall | f1-score | support |
| ------------ | --------- | ------ | -------- | ------- |
| micro avg    | 0.9673    | 0.9767 | 0.9720   | 49232   |
| macro avg    | 0.9591    | 0.9798 | 0.9692   | 49232   |
| weighted avg | 0.9674    | 0.9767 | 0.9720   | 49232   |

### Demo: How to use in Flair
Requires:
- **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("lighthousefeed/yoda-ner")

# make example sentence
sentence = Sentence("Jean Paul Gaultier Classique - 50 ML Eau de Parfum  Damen Parfum.")

# predict NER tags
tagger.predict(sentence)

# print sentence
print(sentence)

# print predicted NER spans
print('The following NER tags are found:')

# iterate over entities and print
for entity in sentence.get_spans('ner'):
    print(entity)
```

## Contact

Contact the lead ML developer [Iván R. Gázquez](mailto:ivan@gazquez.com) for any inquiry. We love hearing what you used this model for!