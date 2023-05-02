---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: parrot_paraphraser_on_T5-finetuned-xsum-v6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# parrot_paraphraser_on_T5-finetuned-xsum-v6

This model is a fine-tuned version of [prithivida/parrot_paraphraser_on_T5](https://huggingface.co/prithivida/parrot_paraphraser_on_T5) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0428
- Rouge1: 86.1908
- Rouge2: 84.358
- Rougel: 86.1439
- Rougelsum: 86.1806
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
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 0.0783        | 1.0   | 2000 | 0.0467          | 86.0347 | 84.0897 | 85.9987 | 86.0282   | 17.889  |
| 0.058         | 2.0   | 4000 | 0.0428          | 86.1908 | 84.358  | 86.1439 | 86.1806   | 17.887  |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
