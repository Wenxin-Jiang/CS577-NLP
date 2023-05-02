---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bertweet-base-cased-covid19-hateval
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bertweet-base-cased-covid19-hateval

This model is a fine-tuned version of [vinai/bertweet-covid19-base-cased](https://huggingface.co/vinai/bertweet-covid19-base-cased) on the HatEval dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4817
- Accuracy: 0.773
- F1: 0.7722

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Accuracy | F1     | Validation Loss |
|:-------------:|:-----:|:----:|:--------:|:------:|:---------------:|
| 0.6925        | 0.99  | 70   | 0.573    | 0.3643 | 0.6827          |
| 0.6823        | 1.99  | 140  | 0.573    | 0.3643 | 0.6736          |
| 0.6713        | 2.99  | 210  | 0.587    | 0.3993 | 0.6568          |
| 0.6468        | 3.99  | 280  | 0.7      | 0.6708 | 0.6210          |
| 0.6047        | 4.99  | 350  | 0.732    | 0.7286 | 0.5785          |
| 0.5648        | 5.99  | 420  | 0.733    | 0.7319 | 0.5537          |
| 0.536         | 6.99  | 490  | 0.739    | 0.7381 | 0.5406          |
| 0.5175        | 7.99  | 560  | 0.744    | 0.7431 | 0.5308          |
| 0.5018        | 8.99  | 630  | 0.751    | 0.7504 | 0.5235          |
| 0.4874        | 9.99  | 700  | 0.749    | 0.7479 | 0.5145          |
| 0.4749        | 10.99 | 770  | 0.754    | 0.7533 | 0.5104          |
| 0.4666        | 11.99 | 840  | 0.761    | 0.7605 | 0.5052          |
| 0.456         | 12.99 | 910  | 0.761    | 0.7604 | 0.5017          |
| 0.4489        | 13.99 | 980  | 0.764    | 0.7635 | 0.4986          |
| 0.4375        | 14.99 | 1050 | 0.764    | 0.7625 | 0.4932          |
| 0.4319        | 15.99 | 1120 | 0.762    | 0.7608 | 0.4917          |
| 0.427         | 16.99 | 1190 | 0.77     | 0.7693 | 0.4918          |
| 0.4226        | 17.99 | 1260 | 0.772    | 0.7711 | 0.4889          |
| 0.4167        | 18.99 | 1330 | 0.769    | 0.7681 | 0.4874          |
| 0.4127        | 19.99 | 1400 | 0.768    | 0.7673 | 0.4868          |
| 0.4095        | 20.99 | 1470 | 0.774    | 0.7731 | 0.4836          |
| 0.4066        | 21.99 | 1540 | 0.77     | 0.7690 | 0.4829          |
| 0.405         | 22.99 | 1610 | 0.773    | 0.7721 | 0.4822          |
| 0.3993        | 23.99 | 1680 | 0.77     | 0.7692 | 0.4827          |
| 0.3977        | 24.99 | 1750 | 0.4831   | 0.772  | 0.7712          |
| 0.398         | 25.99 | 1820 | 0.4830   | 0.774  | 0.7733          |
| 0.3969        | 26.99 | 1890 | 0.4815   | 0.771  | 0.7701          |
| 0.3945        | 27.99 | 1960 | 0.4818   | 0.772  | 0.7712          |
| 0.3929        | 28.99 | 2030 | 0.4818   | 0.773  | 0.7722          |
| 0.3887        | 29.99 | 2100 | 0.4817   | 0.773  | 0.7722          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.0.0
- Tokenizers 0.11.6
