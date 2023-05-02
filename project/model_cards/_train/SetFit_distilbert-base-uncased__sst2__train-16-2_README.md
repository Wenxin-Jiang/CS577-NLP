---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-16-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-16-2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6748
- Accuracy: 0.6315

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7043        | 1.0   | 7    | 0.7054          | 0.2857   |
| 0.6711        | 2.0   | 14   | 0.7208          | 0.2857   |
| 0.6311        | 3.0   | 21   | 0.7365          | 0.2857   |
| 0.551         | 4.0   | 28   | 0.7657          | 0.5714   |
| 0.5599        | 5.0   | 35   | 0.6915          | 0.5714   |
| 0.3167        | 6.0   | 42   | 0.7134          | 0.5714   |
| 0.2489        | 7.0   | 49   | 0.7892          | 0.5714   |
| 0.1985        | 8.0   | 56   | 0.6756          | 0.7143   |
| 0.0864        | 9.0   | 63   | 0.8059          | 0.5714   |
| 0.0903        | 10.0  | 70   | 0.8165          | 0.7143   |
| 0.0429        | 11.0  | 77   | 0.7947          | 0.7143   |
| 0.0186        | 12.0  | 84   | 0.8570          | 0.7143   |
| 0.0146        | 13.0  | 91   | 0.9346          | 0.7143   |
| 0.011         | 14.0  | 98   | 0.9804          | 0.7143   |
| 0.0098        | 15.0  | 105  | 1.0136          | 0.7143   |
| 0.0086        | 16.0  | 112  | 1.0424          | 0.7143   |
| 0.0089        | 17.0  | 119  | 1.0736          | 0.7143   |
| 0.0068        | 18.0  | 126  | 1.0808          | 0.7143   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
