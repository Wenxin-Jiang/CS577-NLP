---
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model_index:
- name: hackMIT-finetuned-sst2
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: sst2
    metric:
      name: Accuracy
      type: accuracy
      value: 0.8027522935779816
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hackMIT-finetuned-sst2

This model is a fine-tuned version of [Blaine-Mason/hackMIT-finetuned-sst2](https://huggingface.co/Blaine-Mason/hackMIT-finetuned-sst2) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1086
- Accuracy: 0.8028

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2.033238621168611e-06
- train_batch_size: 16
- eval_batch_size: 8
- seed: 30
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0674        | 1.0   | 4210 | 1.1086          | 0.8028   |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3
