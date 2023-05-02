---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-mc-weight0.25-epoch15-new-nosharing
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-mc-weight0.25-epoch15-new-nosharing

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.6937
- Cls loss: 2.9228
- Lm loss: 3.9625
- Cls Accuracy: 0.6046
- Cls F1: 0.5997
- Cls Precision: 0.6013
- Cls Recall: 0.6046
- Perplexity: 52.59

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Cls loss | Lm loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Perplexity |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:-------:|:------------:|:------:|:-------------:|:----------:|:----------:|
| 4.6729        | 1.0   | 3470  | 4.4248          | 1.5425   | 4.0392  | 0.5689       | 0.5448 | 0.5732        | 0.5689     | 56.78      |
| 4.3854        | 2.0   | 6940  | 4.3672          | 1.4634   | 4.0012  | 0.6121       | 0.6023 | 0.6288        | 0.6121     | 54.66      |
| 4.2559        | 3.0   | 10410 | 4.3660          | 1.5252   | 3.9844  | 0.6133       | 0.6086 | 0.6428        | 0.6133     | 53.75      |
| 4.1479        | 4.0   | 13880 | 4.4069          | 1.7167   | 3.9774  | 0.6075       | 0.6023 | 0.6134        | 0.6075     | 53.38      |
| 4.0501        | 5.0   | 17350 | 4.4152          | 1.7953   | 3.9661  | 0.6023       | 0.5971 | 0.6063        | 0.6023     | 52.78      |
| 3.964         | 6.0   | 20820 | 4.4789          | 2.0438   | 3.9676  | 0.6086       | 0.6035 | 0.6198        | 0.6086     | 52.86      |
| 3.8964        | 7.0   | 24290 | 4.5107          | 2.1849   | 3.9641  | 0.6052       | 0.5990 | 0.6096        | 0.6052     | 52.67      |
| 3.8441        | 8.0   | 27760 | 4.5674          | 2.4206   | 3.9618  | 0.6104       | 0.6043 | 0.6137        | 0.6104     | 52.55      |
| 3.8043        | 9.0   | 31230 | 4.5939          | 2.5361   | 3.9594  | 0.5954       | 0.5911 | 0.5980        | 0.5954     | 52.43      |
| 3.7743        | 10.0  | 34700 | 4.6247          | 2.6479   | 3.9623  | 0.5937       | 0.5906 | 0.5932        | 0.5937     | 52.58      |
| 3.7484        | 11.0  | 38170 | 4.6686          | 2.8241   | 3.9622  | 0.5983       | 0.5924 | 0.6000        | 0.5983     | 52.57      |
| 3.7305        | 12.0  | 41640 | 4.6729          | 2.8435   | 3.9616  | 0.6          | 0.5949 | 0.5958        | 0.6        | 52.54      |
| 3.7149        | 13.0  | 45110 | 4.6809          | 2.8759   | 3.9614  | 0.5931       | 0.5875 | 0.5899        | 0.5931     | 52.53      |
| 3.7047        | 14.0  | 48580 | 4.6895          | 2.9094   | 3.9617  | 0.5983       | 0.5928 | 0.5955        | 0.5983     | 52.55      |
| 3.6973        | 15.0  | 52050 | 4.6937          | 2.9228   | 3.9625  | 0.6046       | 0.5997 | 0.6013        | 0.6046     | 52.59      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
