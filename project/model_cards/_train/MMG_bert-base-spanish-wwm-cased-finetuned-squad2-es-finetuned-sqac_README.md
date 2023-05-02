---
tags:
- generated_from_trainer
datasets:
- sqac
model-index:
- name: bert-base-spanish-wwm-cased-finetuned-squad2-es-finetuned-sqac
  results: []
  
language:
- es
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-spanish-wwm-cased-finetuned-squad2-es-finetuned-sqac

This model is a fine-tuned version of [ockapuh/bert-base-spanish-wwm-cased-finetuned-squad2-es](https://huggingface.co/ockapuh/bert-base-spanish-wwm-cased-finetuned-squad2-es) on the sqac dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9263
- {'exact_match': 65.55793991416309, 'f1': 82.72322701572416}

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3
