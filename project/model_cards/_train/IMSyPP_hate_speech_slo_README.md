---
pipeline_tag: text-classification

inference: true

widget:
- text: "Sem Mark in živim v Ljubljani. Sem doktorski študent na Mednarodni podiplomski šoli Jožefa Stefana."
language: 
  - sl
license: mit
---

# Hate Speech Classifier for Social Media Content in Slovenian Language

A monolingual model for hate speech classification of social media content in Slovenian language. The model was trained on 50,000 Twitter comments and tested on an independent test set of 10,000 Twitter comments. It is based on multilingual CroSloEngual BERT pre-trained language model.

## Tokenizer

During training the text was preprocessed using the original CroSloEngual BERT tokenizer. We suggest the same tokenizer is used for inference.

## Model output

The model classifies each input into one of four distinct classes:
* 0 - acceptable
* 1 - inappropriate
* 2 - offensive
* 3 - violent