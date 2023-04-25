---
tags:
- spacy
- token-classification
language:
- uk
license: mit
widget:
 - text: "Могила Тараса Шевченка — місце поховання видатного українського поета Тараса Шевченка в місті Канів (Черкаська область) на Чернечій горі, над яким із 1939 року височіє бронзовий пам'ятник роботи скульптора Матвія Манізера."
model-index:
- name: uk_core_news_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8891135827
    - name: NER Recall
      type: recall
      value: 0.8895133191
    - name: NER F Score
      type: f_score
      value: 0.889313406
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9833735418
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9611670877
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.9619342309
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.9462333693
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9300427148
---
Spacy transformer pipeline for Ukrainian language ([XLM-Roberta based](https://huggingface.co/ukr-models/xlm-roberta-base-uk)). Components: transformer, ner, morphologizer, parser.
[Training details](https://github.com/kurnosovv/ukr-spacy)