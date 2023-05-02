---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- recall
- precision
model-index:
- name: distilbert-undersampled
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-undersampled

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0826
- Accuracy: 0.9811
- F1: 0.9810
- Recall: 0.9811
- Precision: 0.9812

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 33
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     | Recall | Precision |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|:------:|:---------:|
| 0.0959        | 0.2   | 2000  | 0.0999          | 0.9651   | 0.9628 | 0.9651 | 0.9655    |
| 0.0618        | 0.41  | 4000  | 0.0886          | 0.9717   | 0.9717 | 0.9717 | 0.9731    |
| 0.159         | 0.61  | 6000  | 0.0884          | 0.9719   | 0.9720 | 0.9719 | 0.9728    |
| 0.0513        | 0.81  | 8000  | 0.0785          | 0.9782   | 0.9782 | 0.9782 | 0.9788    |
| 0.0219        | 1.01  | 10000 | 0.0680          | 0.9779   | 0.9779 | 0.9779 | 0.9783    |
| 0.036         | 1.22  | 12000 | 0.0745          | 0.9787   | 0.9787 | 0.9787 | 0.9792    |
| 0.0892        | 1.42  | 14000 | 0.0675          | 0.9786   | 0.9786 | 0.9786 | 0.9789    |
| 0.0214        | 1.62  | 16000 | 0.0760          | 0.9799   | 0.9798 | 0.9799 | 0.9801    |
| 0.0882        | 1.83  | 18000 | 0.0800          | 0.9800   | 0.9800 | 0.9800 | 0.9802    |
| 0.0234        | 2.03  | 20000 | 0.0720          | 0.9813   | 0.9813 | 0.9813 | 0.9815    |
| 0.0132        | 2.23  | 22000 | 0.0738          | 0.9803   | 0.9803 | 0.9803 | 0.9805    |
| 0.0136        | 2.43  | 24000 | 0.0847          | 0.9804   | 0.9804 | 0.9804 | 0.9806    |
| 0.0119        | 2.64  | 26000 | 0.0826          | 0.9811   | 0.9810 | 0.9811 | 0.9812    |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
