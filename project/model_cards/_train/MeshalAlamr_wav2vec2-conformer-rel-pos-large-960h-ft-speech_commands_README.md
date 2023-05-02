---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-conformer-rel-pos-large-960h-ft-speech_commands
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-conformer-rel-pos-large-960h-ft-speech_commands

This model is a fine-tuned version of [facebook/wav2vec2-conformer-rel-pos-large-960h-ft](https://huggingface.co/facebook/wav2vec2-conformer-rel-pos-large-960h-ft) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6823
- Accuracy: 0.9612

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
| 2.554         | 1.0   | 165  | 2.2488          | 0.8784   |
| 1.645         | 2.0   | 330  | 1.3390          | 0.9100   |
| 1.2462        | 3.0   | 495  | 0.9315          | 0.9589   |
| 1.0438        | 4.0   | 660  | 0.7401          | 0.9603   |
| 0.9908        | 5.0   | 825  | 0.6823          | 0.9612   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
