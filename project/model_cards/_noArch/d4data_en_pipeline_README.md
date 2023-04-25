---
tags:
- spacy
- token-classification

language:
- en
widget:
- text: "Billie Eilish issues apology for mouthing an anti-Asian derogatory term in a resurfaced video."
  example_title: "Biased example 1"
- text: "Christians should make clear that the perpetuation of objectionable vaccines and the lack of alternatives is a kind of coercion."
  example_title: "Biased example 2"
- text: "But, whether this switch constitutes a true win for the racist right or not, it’s clear that MAGA conservatives are highly attuned to how decisions are made in the White House and which positions they want to control."
  example_title: "Biased example 3"
- text: "The fact that the abortion rate among American blacks is far higher than the rate for whites is routinely chronicled and mourned."
  example_title: "Biased example 4" 
model-index:
- name: en_bias
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.6642
    - name: NER Recall
      type: recall
      value: 0.6485
    - name: NER F Score
      type: f_score
      value: 0.6022
      
---
## About the Model 
This model is trained on MBAD Dataset to recognize the biased word/phrases in a sentence. This model was built on top of roberta-base offered by Spacy transformers.

This model is in association with https://huggingface.co/d4data/bias-detection-model

| Feature | Description |
| --- | --- |
| **Name** | `Bias Recognizer Model` |
| **Version** | `1.0` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |

## Author
This model is part of the Research topic "Bias and Fairness in AI" conducted by Deepak John Reji, Shaina Raza. If you use this work (code, model or dataset), please star at:
> Bias & Fairness in AI, (2022), GitHub repository, <https://github.com/dreji18/Fairness-in-AI>