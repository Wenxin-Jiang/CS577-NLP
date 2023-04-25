---
license: mit
tags:
- generated_from_trainer
datasets:
- wsj_markets
metrics:
- rouge
model_index:
- name: bart-large-finetuned-xsum
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: wsj_markets
      type: wsj_markets
      args: default
    metric:
      name: Rouge1
      type: rouge
      value: 15.3934
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-finetuned-xsum

This model is a fine-tuned version of [facebook/bart-large](https://huggingface.co/facebook/bart-large) on the wsj_markets dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8497
- Rouge1: 15.3934
- Rouge2: 7.0378
- Rougel: 13.9522
- Rougelsum: 14.3541
- Gen Len: 20.0

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
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.0964        | 1.0   | 1735 | 0.9365          | 18.703  | 12.7539 | 18.1293 | 18.5397   | 20.0    |
| 0.95          | 2.0   | 3470 | 0.8871          | 19.5223 | 13.0938 | 18.9148 | 18.8363   | 20.0    |
| 0.8687        | 3.0   | 5205 | 0.8587          | 15.0915 | 7.142   | 13.6693 | 14.5975   | 20.0    |
| 0.7989        | 4.0   | 6940 | 0.8569          | 18.243  | 11.4495 | 17.4326 | 17.489    | 20.0    |
| 0.7493        | 5.0   | 8675 | 0.8497          | 15.3934 | 7.0378  | 13.9522 | 14.3541   | 20.0    |


### Framework versions

- Transformers 4.8.2
- Pytorch 1.9.0+cu102
- Datasets 1.10.0
- Tokenizers 0.10.3
