---
tags:
- generated_from_trainer
model-index:
- name: DNADebertaSentencepiece30k
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DNADebertaSentencepiece30k

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 6.3257

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
| 7.9373        | 0.41  | 5000   | 7.8263          |
| 7.8005        | 0.81  | 10000  | 7.7871          |
| 7.7704        | 1.22  | 15000  | 7.7630          |
| 7.7477        | 1.62  | 20000  | 7.6857          |
| 7.6058        | 2.03  | 25000  | 7.5543          |
| 7.5281        | 2.44  | 30000  | 7.4839          |
| 7.4487        | 2.84  | 35000  | 7.3801          |
| 7.3368        | 3.25  | 40000  | 7.2603          |
| 7.1923        | 3.66  | 45000  | 7.0365          |
| 6.9858        | 4.06  | 50000  | 6.8793          |
| 6.8639        | 4.47  | 55000  | 6.7839          |
| 6.7877        | 4.87  | 60000  | 6.7176          |
| 6.728         | 5.28  | 65000  | 6.6680          |
| 6.6826        | 5.69  | 70000  | 6.6258          |
| 6.6414        | 6.09  | 75000  | 6.5847          |
| 6.6057        | 6.5   | 80000  | 6.5571          |
| 6.5794        | 6.91  | 85000  | 6.5279          |
| 6.5525        | 7.31  | 90000  | 6.5059          |
| 6.5354        | 7.72  | 95000  | 6.4816          |
| 6.5125        | 8.12  | 100000 | 6.4674          |
| 6.4958        | 8.53  | 105000 | 6.4486          |
| 6.4817        | 8.94  | 110000 | 6.4317          |
| 6.4674        | 9.34  | 115000 | 6.4195          |
| 6.4549        | 9.75  | 120000 | 6.4072          |
| 6.4409        | 10.16 | 125000 | 6.3945          |
| 6.4302        | 10.56 | 130000 | 6.3861          |
| 6.4214        | 10.97 | 135000 | 6.3755          |
| 6.4118        | 11.37 | 140000 | 6.3659          |
| 6.4058        | 11.78 | 145000 | 6.3604          |
| 6.3985        | 12.19 | 150000 | 6.3560          |
| 6.3899        | 12.59 | 155000 | 6.3473          |
| 6.3837        | 13.0  | 160000 | 6.3417          |
| 6.3782        | 13.41 | 165000 | 6.3361          |
| 6.3753        | 13.81 | 170000 | 6.3309          |
| 6.3733        | 14.22 | 175000 | 6.3285          |
| 6.3706        | 14.62 | 180000 | 6.3277          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0
- Datasets 2.2.2
- Tokenizers 0.12.1
