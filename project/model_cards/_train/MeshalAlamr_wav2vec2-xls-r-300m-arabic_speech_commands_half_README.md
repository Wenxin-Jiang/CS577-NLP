---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-xls-r-300m-arabic_speech_commands_half
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-arabic_speech_commands_half

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2678
- Accuracy: 0.9975

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 3.6816        | 0.99  | 28   | 3.4693          | 0.1575   |
| 3.0227        | 1.99  | 56   | 2.5330          | 0.2775   |
| 2.3345        | 2.99  | 84   | 1.8723          | 0.5925   |
| 1.6785        | 3.99  | 112  | 1.2944          | 0.8092   |
| 1.2606        | 4.99  | 140  | 0.8933          | 0.9425   |
| 1.0024        | 5.99  | 168  | 0.6041          | 0.9817   |
| 0.6478        | 6.99  | 196  | 0.3814          | 0.9933   |
| 0.4768        | 7.99  | 224  | 0.2678          | 0.9975   |
| 0.4143        | 8.99  | 252  | 0.2198          | 0.9967   |
| 0.3278        | 9.99  | 280  | 0.1993          | 0.9967   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
