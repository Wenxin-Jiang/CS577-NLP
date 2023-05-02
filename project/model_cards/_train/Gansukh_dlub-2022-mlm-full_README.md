---
tags:
- generated_from_trainer
model-index:
- name: dlub-2022-mlm-full
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dlub-2022-mlm-full

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 8.4321

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
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 9.7318        | 1.0   | 21   | 9.4453          |
| 9.3594        | 2.0   | 42   | 9.1713          |
| 9.1176        | 3.0   | 63   | 9.0082          |
| 8.9335        | 4.0   | 84   | 8.8166          |
| 8.7735        | 5.0   | 105  | 8.7055          |
| 8.6841        | 6.0   | 126  | 8.6051          |
| 8.6166        | 7.0   | 147  | 8.5337          |
| 8.5258        | 8.0   | 168  | 8.4790          |
| 8.5259        | 9.0   | 189  | 8.4290          |
| 8.4628        | 10.0  | 210  | 8.4321          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
