---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: parrot_paraphraser_on_T5-finetuned-xsum-v5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# parrot_paraphraser_on_T5-finetuned-xsum-v5

This model is a fine-tuned version of [prithivida/parrot_paraphraser_on_T5](https://huggingface.co/prithivida/parrot_paraphraser_on_T5) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0345
- Rouge1: 86.5078
- Rouge2: 84.8978
- Rougel: 86.4798
- Rougelsum: 86.4726
- Gen Len: 17.8462

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
| 0.0663        | 1.0   | 2002 | 0.0539          | 86.0677 | 84.063  | 86.0423 | 86.0313   | 17.8671 |
| 0.0449        | 2.0   | 4004 | 0.0388          | 86.4564 | 84.7606 | 86.432  | 86.4212   | 17.8501 |
| 0.0269        | 3.0   | 6006 | 0.0347          | 86.4997 | 84.8907 | 86.4814 | 86.4744   | 17.8501 |
| 0.023         | 4.0   | 8008 | 0.0345          | 86.5078 | 84.8978 | 86.4798 | 86.4726   | 17.8462 |


### Framework versions

- Transformers 4.22.0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
