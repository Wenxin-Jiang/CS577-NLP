---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-base-uncased-finetuned-classification_ds30
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-classification_ds30

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 41.1515
- Mse: 41.1515
- Mae: 4.7002
- R2: 0.7675
- Accuracy: 0.2685
- Msev: 0.0243

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Mse     | Mae    | R2     | Accuracy | Msev   |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:------:|:--------:|:------:|
| 10.1514       | 1.0   | 5215  | 40.1844         | 40.1844 | 4.6065 | 0.7730 | 0.2644   | 0.0249 |
| 3.7754        | 2.0   | 10430 | 39.4067         | 39.4067 | 4.5926 | 0.7774 | 0.2803   | 0.0254 |
| 2.2314        | 3.0   | 15645 | 44.9527         | 44.9527 | 4.8825 | 0.7460 | 0.2680   | 0.0222 |
| 1.6468        | 4.0   | 20860 | 40.3435         | 40.3435 | 4.6496 | 0.7721 | 0.2702   | 0.0248 |
| 1.2442        | 5.0   | 26075 | 40.8178         | 40.8178 | 4.6934 | 0.7694 | 0.2657   | 0.0245 |
| 1.0992        | 6.0   | 31290 | 42.6644         | 42.6644 | 4.7802 | 0.7590 | 0.2620   | 0.0234 |
| 0.9911        | 7.0   | 36505 | 40.0627         | 40.0627 | 4.6277 | 0.7737 | 0.2751   | 0.0250 |
| 0.8167        | 8.0   | 41720 | 40.6918         | 40.6918 | 4.6755 | 0.7701 | 0.2693   | 0.0246 |
| 0.7862        | 9.0   | 46935 | 41.9593         | 41.9593 | 4.7363 | 0.7629 | 0.2693   | 0.0238 |
| 0.8136        | 10.0  | 52150 | 41.1515         | 41.1515 | 4.7002 | 0.7675 | 0.2685   | 0.0243 |


### Framework versions

- Transformers 4.22.0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
