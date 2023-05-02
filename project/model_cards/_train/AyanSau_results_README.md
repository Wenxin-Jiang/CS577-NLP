---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2057
- Rouge2 Precision: 0.3564
- Rouge2 Recall: 0.2124
- Rouge2 Fmeasure: 0.256

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge2 Precision | Rouge2 Recall | Rouge2 Fmeasure |
|:-------------:|:-----:|:----:|:---------------:|:----------------:|:-------------:|:---------------:|
| No log        | 1.0   | 240  | 0.3146          | 0.2121           | 0.1134        | 0.1424          |
| No log        | 2.0   | 480  | 0.2444          | 0.2855           | 0.1519        | 0.19            |
| 0.6451        | 3.0   | 720  | 0.2195          | 0.3225           | 0.1821        | 0.223           |
| 0.6451        | 4.0   | 960  | 0.2078          | 0.355            | 0.2113        | 0.2548          |
| 0.2978        | 5.0   | 1200 | 0.2057          | 0.3564           | 0.2124        | 0.256           |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+cpu
- Datasets 2.4.0
- Tokenizers 0.12.1
