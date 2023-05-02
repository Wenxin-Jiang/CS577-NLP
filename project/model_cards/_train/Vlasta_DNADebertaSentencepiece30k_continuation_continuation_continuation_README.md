---
tags:
- generated_from_trainer
model-index:
- name: DNADebertaSentencepiece30k_continuation_continuation_continuation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DNADebertaSentencepiece30k_continuation_continuation_continuation

This model is a fine-tuned version of [Vlasta/DNADebertaSentencepiece30k_continuation_continuation](https://huggingface.co/Vlasta/DNADebertaSentencepiece30k_continuation_continuation) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 5.9319

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 6.0844        | 0.41  | 5000   | 6.0623          |
| 6.0962        | 0.81  | 10000  | 6.0659          |
| 6.0903        | 1.22  | 15000  | 6.0566          |
| 6.0874        | 1.62  | 20000  | 6.0550          |
| 6.082         | 2.03  | 25000  | 6.0485          |
| 6.0756        | 2.44  | 30000  | 6.0446          |
| 6.0722        | 2.84  | 35000  | 6.0429          |
| 6.0698        | 3.25  | 40000  | 6.0317          |
| 6.0627        | 3.66  | 45000  | 6.0297          |
| 6.0606        | 4.06  | 50000  | 6.0301          |
| 6.0521        | 4.47  | 55000  | 6.0224          |
| 6.0526        | 4.87  | 60000  | 6.0159          |
| 6.0473        | 5.28  | 65000  | 6.0140          |
| 6.0435        | 5.69  | 70000  | 6.0076          |
| 6.039         | 6.09  | 75000  | 6.0022          |
| 6.032         | 6.5   | 80000  | 6.0037          |
| 6.0319        | 6.91  | 85000  | 5.9979          |
| 6.0232        | 7.31  | 90000  | 5.9937          |
| 6.0279        | 7.72  | 95000  | 5.9844          |
| 6.0198        | 8.12  | 100000 | 5.9854          |
| 6.0165        | 8.53  | 105000 | 5.9796          |
| 6.0153        | 8.94  | 110000 | 5.9741          |
| 6.0111        | 9.34  | 115000 | 5.9722          |
| 6.0082        | 9.75  | 120000 | 5.9679          |
| 6.0035        | 10.16 | 125000 | 5.9654          |
| 5.999         | 10.56 | 130000 | 5.9624          |
| 5.998         | 10.97 | 135000 | 5.9572          |
| 5.9926        | 11.37 | 140000 | 5.9535          |
| 5.9927        | 11.78 | 145000 | 5.9533          |
| 5.9903        | 12.19 | 150000 | 5.9517          |
| 5.986         | 12.59 | 155000 | 5.9459          |
| 5.9816        | 13.0  | 160000 | 5.9439          |
| 5.9786        | 13.41 | 165000 | 5.9390          |
| 5.9781        | 13.81 | 170000 | 5.9357          |
| 5.9779        | 14.22 | 175000 | 5.9346          |
| 5.9756        | 14.62 | 180000 | 5.9339          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0
- Datasets 2.2.2
- Tokenizers 0.12.1
