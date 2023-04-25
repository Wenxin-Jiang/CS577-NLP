---
tags:
- spacy
- token-classification
language: uk
datasets:
- ner-uk
license: mit
model-index:
- name: uk_ner_web_trf_base
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8987742191
    - name: NER Recall
      type: recall
      value: 0.8810077519
    - name: NER F Score
      type: f_score
      value: 0.8898023096
widget:
- text: "Президент Володимир Зеленський пояснив, що наразі діалог із режимом Володимира путіна неможливий, адже агресор обрав курс на знищення українського народу. За словами Зеленського цей режим РФ виявляє неповагу до суверенітету і територіальної цілісності України."
---
# uk_ner_web_trf_base

## Model description

**uk_ner_web_trf_base** is a fine-tuned [XLM-Roberta model](https://huggingface.co/xlm-roberta-base) that is ready to use for **Named Entity Recognition** and achieves a performance close to **SoA** for the NER task for Ukrainian language. It has been trained to recognize four types of entities: location (LOC), organizations (ORG), person (PERS) and Miscellaneous (MISC). 

The model was fine-tuned on the [NER-UK dataset](https://github.com/lang-uk/ner-uk), released by the [lang-uk](https://lang.org.ua).
A bigger model, trained on xlm-roberta-large with the **State-of-the-Art** performance is available [here](https://huggingface.co/dchaplinsky/uk_ner_web_trf_large).


Copyright: [Dmytro Chaplynskyi](https://twitter.com/dchaplinsky), [lang-uk project](https://lang.org.ua), 2022
