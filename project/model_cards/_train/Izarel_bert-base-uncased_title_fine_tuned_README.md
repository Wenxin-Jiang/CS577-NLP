---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- recall
- precision
- f1
model-index:
- name: bert-base-uncased_title_fine_tuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased_title_fine_tuned

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3368
- Accuracy: {'accuracy': 0.8810840405146455}
- Recall: {'recall': 0.8611674554879423}
- Precision: {'precision': 0.890468422279189}
- F1: {'f1': 0.8755728689275893}

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy                         | Recall                         | Precision                         | F1                         |
|:-------------:|:-----:|:-----:|:---------------:|:--------------------------------:|:------------------------------:|:---------------------------------:|:--------------------------:|
| 0.3224        | 1.0   | 3045  | 0.3079          | {'accuracy': 0.8730358609362168} | {'recall': 0.8139508677034032} | {'precision': 0.915346597389431}  | {'f1': 0.861676110945422}  |
| 0.2818        | 2.0   | 6090  | 0.3153          | {'accuracy': 0.8814672871612373} | {'recall': 0.8299526707234618} | {'precision': 0.9182146864480738} | {'f1': 0.8718555785735426} |
| 0.2394        | 3.0   | 9135  | 0.3104          | {'accuracy': 0.8830002737476047} | {'recall': 0.8548568852828488} | {'precision': 0.8993479549496147} | {'f1': 0.8765382171124848} |
| 0.204         | 4.0   | 12180 | 0.3368          | {'accuracy': 0.8810840405146455} | {'recall': 0.8611674554879423} | {'precision': 0.890468422279189}  | {'f1': 0.8755728689275893} |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
