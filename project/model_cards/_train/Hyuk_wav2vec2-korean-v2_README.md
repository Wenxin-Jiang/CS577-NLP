---
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-korean-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-korean-v2

This model is a fine-tuned version of [teddy322/hyuk_Second_SON](https://huggingface.co/teddy322/hyuk_Second_SON) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4514
- Wer: 0.1679

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 400
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0289        | 0.41  | 300  | 0.4758          | 0.1605 |
| 0.0481        | 0.82  | 600  | 0.4885          | 0.1867 |
| 0.0578        | 1.22  | 900  | 0.4700          | 0.1862 |
| 0.0599        | 1.63  | 1200 | 0.4733          | 0.1857 |
| 0.0575        | 2.04  | 1500 | 0.4504          | 0.1844 |
| 0.0547        | 2.45  | 1800 | 0.4741          | 0.1865 |
| 0.0495        | 2.86  | 2100 | 0.4473          | 0.1794 |
| 0.045         | 3.27  | 2400 | 0.4559          | 0.1782 |
| 0.0426        | 3.67  | 2700 | 0.4502          | 0.1722 |
| 0.0466        | 4.08  | 3000 | 0.4464          | 0.1697 |
| 0.0369        | 4.49  | 3300 | 0.4487          | 0.1665 |
| 0.0342        | 4.9   | 3600 | 0.4514          | 0.1679 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
