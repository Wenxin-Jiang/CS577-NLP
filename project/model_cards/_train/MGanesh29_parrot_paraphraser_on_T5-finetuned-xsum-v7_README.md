---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: parrot_paraphraser_on_T5-finetuned-xsum-v7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# parrot_paraphraser_on_T5-finetuned-xsum-v7

This model is a fine-tuned version of [prithivida/parrot_paraphraser_on_T5](https://huggingface.co/prithivida/parrot_paraphraser_on_T5) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0316
- Rouge1: 86.4178
- Rouge2: 84.901
- Rougel: 86.458
- Rougelsum: 86.4281
- Gen Len: 17.887

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
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 0.0752        | 1.0   | 2000 | 0.0439          | 86.0044 | 84.1284 | 86.0265 | 86.0167   | 17.895  |
| 0.0454        | 2.0   | 4000 | 0.0352          | 86.2948 | 84.6092 | 86.3256 | 86.293    | 17.88   |
| 0.0308        | 3.0   | 6000 | 0.0324          | 86.3316 | 84.7883 | 86.374  | 86.3355   | 17.887  |
| 0.0242        | 4.0   | 8000 | 0.0316          | 86.4178 | 84.901  | 86.458  | 86.4281   | 17.887  |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
