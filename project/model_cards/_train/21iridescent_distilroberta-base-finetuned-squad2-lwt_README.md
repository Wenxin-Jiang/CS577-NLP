---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad_v2
model-index:
- name: distilroberta-base-finetuned-squad2-lwt
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilroberta-base-finetuned-squad2-lwt

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the squad_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1356

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.1702        | 1.0   | 4120  | 1.1220          |
| 0.9787        | 2.0   | 8240  | 1.0500          |
| 0.8153        | 3.0   | 12360 | 1.1356          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

{'HasAns_exact': 71.39001349527665,
 'HasAns_f1': 77.71740687727831,
 'HasAns_total': 5928,
 'NoAns_exact': 68.59545836837678,
 'NoAns_f1': 68.59545836837678,
 'NoAns_total': 5945,
 'best_exact': 69.9991577528847,
 'best_exact_thresh': 0.0,
 'best_f1': 73.1583245993857,
 'best_f1_thresh': 0.0,
 'exact': 69.99073528173166,
 'f1': 73.1499021282327,
 'total': 11873}