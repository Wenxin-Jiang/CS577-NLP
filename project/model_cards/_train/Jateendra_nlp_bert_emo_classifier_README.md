---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
model-index:
- name: nlp_bert_emo_classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# nlp_bert_emo_classifier

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2791

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.8887        | 0.25  | 500  | 0.4212          |
| 0.3216        | 0.5   | 1000 | 0.3192          |
| 0.2649        | 0.75  | 1500 | 0.2746          |
| 0.2535        | 1.0   | 2000 | 0.2573          |
| 0.163         | 1.25  | 2500 | 0.2157          |
| 0.1868        | 1.5   | 3000 | 0.2118          |
| 0.1258        | 1.75  | 3500 | 0.2319          |
| 0.1726        | 2.0   | 4000 | 0.1853          |
| 0.1035        | 2.25  | 4500 | 0.2146          |
| 0.1135        | 2.5   | 5000 | 0.2207          |
| 0.1117        | 2.75  | 5500 | 0.2496          |
| 0.1145        | 3.0   | 6000 | 0.2482          |
| 0.0726        | 3.25  | 6500 | 0.2654          |
| 0.0828        | 3.5   | 7000 | 0.2622          |
| 0.0817        | 3.75  | 7500 | 0.2775          |
| 0.0689        | 4.0   | 8000 | 0.2791          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.10.3
