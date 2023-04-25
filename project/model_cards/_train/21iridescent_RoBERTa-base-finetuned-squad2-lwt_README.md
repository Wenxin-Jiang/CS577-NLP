---
--license: mit
tags:
- generated_from_trainer
datasets:
- squad_v2
model-index:
- name: roberta-base-finetuned-squad2-lwt
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

## Model description

#### Finetuned on SQUAD2.0 Dataset
#### F1: 83.738696142672

Trained on single V100 GPU

Everyone is welcome to use~ 

Hope you have a nice day


## Performance

 - HasAns_exact': 77.1255060728745, 'HasAns_f1': 83.87812741260885, 'HasAns_total': 5928,
 - 'NoAns_exact': 83.59966358284272, 'NoAns_f1': 83.59966358284272, 'NoAns_total': 5945,
 - 'best_exact': 80.36721974227238, 'best_exact_thresh': 0.0, 
 - 'best_f1': 83.7386961426719, 'best_f1_thresh': 0.0,
 
 - 'exact': 80.36721974227238, 
 - 'f1': 83.738696142672, 
 - 'total': 11873

# roberta-base-finetuned-squad2-lwt

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the squad_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9441


More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.871         | 1.0   | 8239  | 0.8156          |
| 0.6787        | 2.0   | 16478 | 0.8494          |
| 0.4867        | 3.0   | 24717 | 0.9441          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6


