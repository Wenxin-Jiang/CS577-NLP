---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Sultannn/bert-base-ft-ner-xtreme-id
  results: []
  
widget:
- text: Nama saya Tono, saya bekerja di Gotot dan tinggal di Mars. 
    
language: id
datasets:
- xtreme
---
    
    
<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Sultannn/bert-base-ft-ner-xtreme-id

This model is a fine-tuned version of [bert-base-multilingual-uncased](https://huggingface.co/bert-base-multilingual-uncased) on an [xtreme PAN-X.id](https://huggingface.co/datasets/xtreme/viewer/PAN-X.id/test) for **NER** downstream task.

## Details of the downstream task (NER) - Dataset

| Dataset                | # Examples |
| ---------------------- | ----- |
| Train                  | 35 K |
| Validation             | 5 K |

## Metrics on evaluation set

| Metrics                | Score  |
| ---------------------- | ----- |
| Accuracy               | **97.18** |
| F1                     | **93.26** |
| Precision              | **92.36** |
| Recall                 | **94.18** |


## Training hyperparameters

- Optimizer = AdamW
- LearningRate = 4e-5
- WeightDecay = 1e-2
- Warmup = 500


## Example of usage

```python 
# pipeline example

from transformers import pipeline

model_checkpoint = "Sultannn/bert-base-ft-ner-xtreme-id"
token_classifier = pipeline(
    "token-classification", model=model_checkpoint, aggregation_strategy="simple")

text = "nama saya Tono saya bekerja di Facebook dan tinggal di Jawa"

token_classifier(text)

```

## Framework versions

- Transformers 4.18.0
- TensorFlow 2.8.0
- Datasets 2.1.0
- Tokenizers 0.12.1

> [Fine-tune on NER script provided by @Sultan](https://github.com/sultanbst123)

> Made with <span style="color: #e25555;">&hearts;</span> in 🌏
