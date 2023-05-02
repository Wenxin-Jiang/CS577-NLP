---
license: mit
tags:
- generated_from_trainer
datasets: SetFit/subj
metrics:
- accuracy
model-index:
- name: microsoft-deberta-v3-large_cls_subj
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# microsoft-deberta-v3-large_cls_subj

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on [subj](https://huggingface.co/datasets/SetFit/subj) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1525
- Accuracy: 0.976

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.2
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.2629        | 1.0   | 500  | 0.1519          | 0.955    |
| 0.1232        | 2.0   | 1000 | 0.1121          | 0.974    |
| 0.0535        | 3.0   | 1500 | 0.1341          | 0.974    |
| 0.0152        | 4.0   | 2000 | 0.1794          | 0.969    |
| 0.0043        | 5.0   | 2500 | 0.1525          | 0.976    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
