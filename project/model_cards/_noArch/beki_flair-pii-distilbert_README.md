---
tags:
- flair
- token-classification
- sequence-tagger-model
language: en
widget:
- text: "SELECT shipping FROM users WHERE shipping = '201 Thayer St Providence RI 02912'"
---

## English PII in Flair

This is the large 5-class NER model for English trained on protocol trace data generated by [Privy](https://github.com/pixie-io/pixie/tree/main/src/datagen/pii/privy/)

F1-Score: **0.9522**

Predicts 5 tags:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| PER         | person name | 
| LOC         | location name | 
| ORG         | organization name | 
| DATE_TIME   | dates and times | 
| NRP         | nationalities, religious and political groups | 

Uses distilbert embeddings.

---