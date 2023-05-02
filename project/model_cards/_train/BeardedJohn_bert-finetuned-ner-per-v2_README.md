---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: bert-finetuned-ner-per-v2
  results: []
datasets:
- wikiann
- BeardedJohn/NERPERDemo
- BeardedJohn/ubb-endava-conll-assistant-ner-only-misc-v2
language:
- en
library_name: transformers
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner-per-v2

This model is a fine-tuned version of [BERT](https://huggingface.co/bert-base-cased) on three datasets:

- [conll-endava mixed dataset, second version](https://huggingface.co/datasets/BeardedJohn/ubb-endava-conll-assistant-ner-only-misc-v2)
- [NERPERDemo dataset](https://huggingface.co/datasets/BeardedJohn/NERPERDemo)
- 12000 instances of the [wikiann, english version dataset](https://huggingface.co/datasets/wikiann/viewer/en/train).

It achieves the following results on the conll-endava mixed, second version evaluation set:
- Train Loss: 0.0190
- Validation Loss: 0.0310
- Epoch: 2

It achieves the following results on the NERPERDemo evaluation set:
- Train Loss: 0.0005
- Validation Loss: 0.0002
- Epoch: 2

It achieves the following results on the wikiann evaluation set:
- Train Loss: 0.1217
- Validation Loss: 0.3073
- Epoch: 2

## Model description

The model is a fine-tuned version of BERT with the intent of solving the NER task. It is trained to recognize four classes of entities:

- Person (PER)
- Organisation (ORG)
- Location (LOC)
- Miscellaneous (MISC)*

* The MISC label maps data corresponding to the [conll-endava](https://huggingface.co/datasets/BeardedJohn/ubb-endava-conll-assistant-ner-only-misc-v2) dataset.

## Intended uses & limitations

It can be used as a general purpose model for recognizing the 4 mentioned entities, but it may have some phrase specific bias introduced by the two datasets (conll-endava and NERPERDemo). 
The model is part of a project and is fine-tuned to meet the specific requirements, but feel free to test it in your own environment as it has fine-tuned on general data too.

## Training and evaluation data

Training and evaluation data are from the three mentioned datasets.

## Training procedure

Training is inspired from [HuggingFace tutorial](https://huggingface.co/course/chapter7/2?fw=tf).

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 1875, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

On conll-endava mixed, second version:

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 0.2091     | 0.0391          | 0     |
| 0.0336     | 0.0322          | 1     |
| 0.0190     | 0.0310          | 2     |


On NERPERDemo:

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 0.0202     | 0.0005          | 0     |
| 0.0009     | 0.0002          | 1     |
| 0.0005     | 0.0002          | 2     |

On wikiann:

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 0.2975     | 0.2869          | 0     |
| 0.1755     | 0.2934          | 1     |
| 0.1217     | 0.3073          | 2     |

### Framework versions

- Transformers 4.25.1
- TensorFlow 2.9.2
- Datasets 2.8.0
- Tokenizers 0.13.2