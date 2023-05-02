---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- Langame/starter
model-index:
- name: distilgpt2-starter
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilgpt2-starter

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on the Langame/starter dataset.
It achieves the following results on the evaluation set:
- Loss: 6.0234

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 500.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| No log        | 66.67  | 200  | 3.6445          |
| No log        | 133.33 | 400  | 4.5703          |
| 1.0101        | 200.0  | 600  | 5.2109          |
| 1.0101        | 266.67 | 800  | 5.5430          |
| 0.0681        | 333.33 | 1000 | 5.7227          |
| 0.0681        | 400.0  | 1200 | 5.8672          |
| 0.0681        | 466.67 | 1400 | 5.9961          |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.18.1
- Tokenizers 0.11.0
