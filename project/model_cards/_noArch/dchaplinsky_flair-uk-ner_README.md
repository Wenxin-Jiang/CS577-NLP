---
tags:
- flair
- token-classification
- sequence-tagger-model
language: uk
datasets:
- ner-uk
model-index:
- name: flair-uk-ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8616
    - name: NER Recall
      type: recall
      value: 0.8593
    - name: NER F Score
      type: f_score
      value: 0.8605
widget:
- text: "Президент Володимир Зеленський пояснив, що наразі діалог із режимом Володимира путіна неможливий, адже агресор обрав курс на знищення українського народу. За словами Зеленського цей режим РФ виявляє неповагу до суверенітету і територіальної цілісності України."
license: mit
---

# flair-uk-ner

## Model description

**flair-uk-ner** is a Flair model that is ready to use for **Named Entity Recognition**. It is based on flair embeddings, that I've trained for Ukrainian language (available [here](https://huggingface.co/dchaplinsky/flair-uk-backward) and [here](https://huggingface.co/dchaplinsky/flair-uk-forward)) and has nice performance and a very **small size** (just 72mb!).

It has been trained to recognize four types of entities: location (LOC), organizations (ORG), person (PERS) and Miscellaneous (MISC). 

Results:
- F-score (micro) **0.8605**
- F-score (macro) **0.7472**
- Accuracy **0.8033**

| by class     | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| **PERS**     | 0.9305    | 0.9422 | 0.9363   | 1678    |
| **LOC**      | 0.8150    | 0.8678 | 0.8406   | 401     |
| **ORG**      | 0.6653    | 0.6092 | 0.6360   | 261     |
| **MISC**     | 0.6202    | 0.5375 | 0.5759   | 240     |
| micro avg    | 0.8616    | 0.8593 | 0.8605   | 2580    |
| macro avg    | 0.7577    | 0.7392 | 0.7472   | 2580    |
| weighted avg | 0.8569    | 0.8593 | 0.8575   | 2580    |

The model was fine-tuned on the [NER-UK dataset](https://github.com/lang-uk/ner-uk), released by the [lang-uk](https://lang.org.ua).
Training code is also available [here](https://github.com/lang-uk/flair-ner).


Copyright: [Dmytro Chaplynskyi](https://twitter.com/dchaplinsky), [lang-uk project](https://lang.org.ua), 2022