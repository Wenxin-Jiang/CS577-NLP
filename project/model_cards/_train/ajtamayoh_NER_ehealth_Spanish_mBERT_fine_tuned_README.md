---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: NER_ehealth_Spanish_mBERT_fine_tuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NER_ehealth_Spanish_mBERT_fine_tuned

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6563
- Precision: 0.8094
- Recall: 0.8330
- F1: 0.8210
- Accuracy: 0.9051

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
- num_epochs: 12

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 100  | 0.5335          | 0.8018    | 0.8307 | 0.8160 | 0.9047   |
| No log        | 2.0   | 200  | 0.5034          | 0.8110    | 0.8253 | 0.8181 | 0.9067   |
| No log        | 3.0   | 300  | 0.5632          | 0.7932    | 0.8230 | 0.8078 | 0.9038   |
| No log        | 4.0   | 400  | 0.5904          | 0.8004    | 0.8299 | 0.8149 | 0.9027   |
| 0.017         | 5.0   | 500  | 0.5958          | 0.7993    | 0.8330 | 0.8158 | 0.9071   |
| 0.017         | 6.0   | 600  | 0.6168          | 0.7980    | 0.8352 | 0.8162 | 0.9022   |
| 0.017         | 7.0   | 700  | 0.6219          | 0.8079    | 0.8314 | 0.8195 | 0.9062   |
| 0.017         | 8.0   | 800  | 0.6441          | 0.8046    | 0.8299 | 0.8171 | 0.9038   |
| 0.017         | 9.0   | 900  | 0.6338          | 0.8086    | 0.8253 | 0.8168 | 0.9051   |
| 0.0066        | 10.0  | 1000 | 0.6482          | 0.8021    | 0.8261 | 0.8139 | 0.9029   |
| 0.0066        | 11.0  | 1100 | 0.6578          | 0.8039    | 0.8291 | 0.8163 | 0.9038   |
| 0.0066        | 12.0  | 1200 | 0.6563          | 0.8094    | 0.8330 | 0.8210 | 0.9051   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
