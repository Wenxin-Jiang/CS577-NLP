---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-conformer-rope-large-960h-ft-speech_commands
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-conformer-rope-large-960h-ft-speech_commands

This model is a fine-tuned version of [facebook/wav2vec2-conformer-rope-large-960h-ft](https://huggingface.co/facebook/wav2vec2-conformer-rope-large-960h-ft) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7777
- Accuracy: 0.9727

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.6618        | 1.0   | 165  | 2.3731          | 0.8350   |
| 1.7932        | 2.0   | 330  | 1.4893          | 0.9278   |
| 1.3897        | 3.0   | 495  | 1.0531          | 0.9661   |
| 1.1663        | 4.0   | 660  | 0.8407          | 0.9714   |
| 1.1051        | 5.0   | 825  | 0.7777          | 0.9727   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
