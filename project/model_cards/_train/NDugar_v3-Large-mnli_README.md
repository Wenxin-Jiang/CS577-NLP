---
language: en
tags: 
- deberta-v1
- deberta-mnli
tasks: mnli
thumbnail: https://huggingface.co/front/thumbnails/microsoft.png
license: mit
pipeline_tag: zero-shot-classification
---

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the GLUE MNLI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4103
- Accuracy: 0.9175
### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-06
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- num_epochs: 2.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.3631        | 1.0   | 49088 | 0.3129          | 0.9130   |
| 0.2267        | 2.0   | 98176 | 0.4157          | 0.9153   |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.15.2.dev0
- Tokenizers 0.10.3
