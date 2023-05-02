---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
model-index:
- name: sentence_eval1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sentence_eval1

This model is a fine-tuned version of [roberta-large-mnli](https://huggingface.co/roberta-large-mnli) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4766
- Precision: {'precision': 0.863681451041519}
- Recall: {'recall': 0.8702170188463735}
- F1: {'f1': 0.8669369177156675}
- Acc: {'accuracy': 0.8073120494335736}

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
- train_batch_size: 48
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision                         | Recall                         | F1                         | Acc                              |
|:-------------:|:-----:|:----:|:---------------:|:---------------------------------:|:------------------------------:|:--------------------------:|:--------------------------------:|
| 0.437         | 1.0   | 1771 | 0.4753          | {'precision': 0.9119431443924424} | {'recall': 0.7511422044545973} | {'f1': 0.8237688874970641} | {'accuracy': 0.7681771369721936} |
| 0.367         | 2.0   | 3542 | 0.4342          | {'precision': 0.8658256880733946} | {'recall': 0.8623643632210166} | {'f1': 0.8640915593705294} | {'accuracy': 0.8043254376930999} |
| 0.2915        | 3.0   | 5313 | 0.4766          | {'precision': 0.863681451041519}  | {'recall': 0.8702170188463735} | {'f1': 0.8669369177156675} | {'accuracy': 0.8073120494335736} |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
