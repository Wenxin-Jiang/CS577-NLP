---
tags:
- flair
- token-classification
- sequence-tagger-model
language: uk
model-index:
- name: flair-uk-pos
  results:
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS F Score
      type: f_score
      value: 0.9793
widget:
- text: "Президент Володимир Зеленський пояснив, що наразі діалог із режимом Володимира путіна неможливий, адже агресор обрав курс на знищення українського народу. За словами Зеленського цей режим РФ виявляє неповагу до суверенітету і територіальної цілісності України."
license: mit
---

# flair-uk-ner

## Model description

**flair-uk-pos** is a Flair model that is ready to use for part-of-speech (upos) tagging. It is based on flair embeddings, that I've trained for Ukrainian language (available [here](https://huggingface.co/dchaplinsky/flair-uk-backward) and [here](https://huggingface.co/dchaplinsky/flair-uk-forward)) and has superior performance and a very **small size** (just 72mb!).


Results:
- F-score (micro) **0.9793**
- F-score (macro) **0.9275**
- Accuracy **0.9793**

| By class:    | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| NOUN         | 0.9857    | 0.9851 | 0.9854   | 4549    |
| PUNCT        | 0.9984    | 1.0000 | 0.9992   | 3097    |
| ADJ          | 0.9772    | 0.9852 | 0.9812   | 1959    |
| ADP          | 0.9956    | 0.9968 | 0.9962   | 1584    |
| VERB         | 0.9891    | 0.9910 | 0.9900   | 1552    |
| ADV          | 0.9630    | 0.9118 | 0.9367   | 714     |
| CCONJ        | 0.9685    | 0.9746 | 0.9715   | 630     |
| PROPN        | 0.9279    | 0.9472 | 0.9375   | 625     |
| DET          | 0.9729    | 0.9698 | 0.9713   | 629     |
| PRON         | 0.9706    | 0.9631 | 0.9669   | 515     |
| PART         | 0.9235    | 0.8693 | 0.8956   | 375     |
| NUM          | 0.9722    | 0.9804 | 0.9763   | 357     |
| SCONJ        | 0.8768    | 0.9577 | 0.9154   | 260     |
| AUX          | 0.8906    | 0.9500 | 0.9194   | 120     |
| X            | 0.9833    | 0.9593 | 0.9712   | 123     |
| SYM          | 1.0000    | 0.7059 | 0.8276   | 17      |
| INTJ         | 0.5556    | 0.5000 | 0.5263   | 10      |
| accuracy     |           |        | 0.9793   | 17116   |
| macro avg    | 0.9383    | 0.9204 | 0.9275   | 17116   |
| weighted avg | 0.9794    | 0.9793 | 0.9792   | 17116   |


The model was fine-tuned on the [Ukrainian (UD) corpus](https://universaldependencies.org/treebanks/uk_iu/index.html), released by the [non-profit organization Institute for Ukrainian](https://mova.institute).
Training code is also available [here](https://github.com/lang-uk/flair-pos).

## [Usage demo](https://github.com/egorsmkv/flair-nlp-uk/blob/main/part_of_speech.py)
```python
from flair.data import Sentence
from flair.models import SequenceTagger

from pprint import pprint

tagger = SequenceTagger.load("dchaplinsky/flair-uk-pos")

sentence = Sentence("Я люблю Україну. Моє імʼя Марія Шевченко, я навчаюся в Київській політехніці.")

tagger.predict(sentence)

print(sentence)
print('---')

print('The following POS tags are found:')

pos_items = []
for label in sentence.get_labels():
    all_labels = []
    keys = label.data_point.annotation_layers.keys()
    
    for key in keys:
        all_labels.extend(
            [
                {'label': label.value, 'score': round(label.score, 4)}
                for label in label.data_point.get_labels(key)
                if label.data_point == label
            ]
        )

    pos_items.append({
        'text': label.data_point.text,
        'all_labels': all_labels,
    })

pprint(pos_items)

# Result:
"""
Sentence: "Я люблю Україну . Моє імʼя Марія Шевченко , я навчаюся в Київській політехніці ." → ["Я"/PRON, "люблю"/VERB, "Україну"/PROPN, "."/PUNCT, "Моє"/DET, "імʼя"/NOUN, "Марія"/PROPN, "Шевченко"/PROPN, ","/PUNCT, "я"/PRON, "навчаюся"/VERB, "в"/ADP, "Київській"/ADJ, "політехніці"/NOUN, "."/PUNCT]
---
The following POS tags are found:
[{'all_labels': [{'label': 'PRON', 'score': 1.0}], 'text': 'Я'},
 {'all_labels': [{'label': 'VERB', 'score': 1.0}], 'text': 'люблю'},
 {'all_labels': [{'label': 'PROPN', 'score': 1.0}], 'text': 'Україну'},
 {'all_labels': [{'label': 'PUNCT', 'score': 1.0}], 'text': '.'},
 {'all_labels': [{'label': 'DET', 'score': 0.9999}], 'text': 'Моє'},
 {'all_labels': [{'label': 'NOUN', 'score': 1.0}], 'text': 'імʼя'},
 {'all_labels': [{'label': 'PROPN', 'score': 1.0}], 'text': 'Марія'},
 {'all_labels': [{'label': 'PROPN', 'score': 1.0}], 'text': 'Шевченко'},
 {'all_labels': [{'label': 'PUNCT', 'score': 1.0}], 'text': ','},
 {'all_labels': [{'label': 'PRON', 'score': 1.0}], 'text': 'я'},
 {'all_labels': [{'label': 'VERB', 'score': 1.0}], 'text': 'навчаюся'},
 {'all_labels': [{'label': 'ADP', 'score': 1.0}], 'text': 'в'},
 {'all_labels': [{'label': 'ADJ', 'score': 1.0}], 'text': 'Київській'},
 {'all_labels': [{'label': 'NOUN', 'score': 1.0}], 'text': 'політехніці'},
 {'all_labels': [{'label': 'PUNCT', 'score': 1.0}], 'text': '.'}]
"""
```

Copyright: [Dmytro Chaplynskyi](https://twitter.com/dchaplinsky), [lang-uk project](https://lang.org.ua), 2022