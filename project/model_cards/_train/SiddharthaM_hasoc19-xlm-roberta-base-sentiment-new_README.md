---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: hasoc19-xlm-roberta-base-sentiment-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hasoc19-xlm-roberta-base-sentiment-new

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3840
- Accuracy: 0.8726
- Precision: 0.8724
- Recall: 0.8726
- F1: 0.8725

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.4786        | 1.0   | 537  | 0.3999          | 0.8381   | 0.8391    | 0.8381 | 0.8363 |
| 0.349         | 2.0   | 1074 | 0.3443          | 0.8606   | 0.8603    | 0.8606 | 0.8603 |
| 0.2927        | 3.0   | 1611 | 0.3412          | 0.8669   | 0.8668    | 0.8669 | 0.8662 |
| 0.2471        | 4.0   | 2148 | 0.3408          | 0.8705   | 0.8708    | 0.8705 | 0.8706 |
| 0.2195        | 5.0   | 2685 | 0.3897          | 0.8726   | 0.8725    | 0.8726 | 0.8721 |
| 0.1849        | 6.0   | 3222 | 0.3840          | 0.8726   | 0.8724    | 0.8726 | 0.8725 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
