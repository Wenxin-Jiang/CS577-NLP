---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: BiBert-Subjectivity
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BiBert-Subjectivity

This model is a fine-tuned version of [nlptown/bert-base-multilingual-uncased-sentiment](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1481
- Accuracy: 0.9583
- F1: 0.9581
- Mae: 0.0417
- Accuracy 2: 0.9583

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Mae   | Accuracy 2 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:-----:|:----------:|
| No log        | 1.0   | 112  | 0.1333          | 0.95     | 0.9508 | 0.05  | 0.95       |
| No log        | 2.0   | 224  | 0.1517          | 0.953    | 0.9531 | 0.047 | 0.953      |
| No log        | 3.0   | 336  | 0.2219          | 0.951    | 0.9505 | 0.049 | 0.951      |
| No log        | 4.0   | 448  | 0.2327          | 0.947    | 0.9479 | 0.053 | 0.947      |
| 0.0865        | 5.0   | 560  | 0.2557          | 0.953    | 0.9528 | 0.047 | 0.953      |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
