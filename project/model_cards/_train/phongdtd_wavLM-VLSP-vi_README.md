---
tags:
- automatic-speech-recognition
- phongdtd/VinDataVLSP
- generated_from_trainer
model-index:
- name: wavLM-VLSP-vi
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wavLM-VLSP-vi

This model is a fine-tuned version of [microsoft/wavlm-base-plus](https://huggingface.co/microsoft/wavlm-base-plus) on the PHONGDTD/VINDATAVLSP - NA dataset.
It achieves the following results on the evaluation set:
- Loss: 45.8892
- Wer: 0.9999
- Cer: 0.9973

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 2
- total_train_batch_size: 8
- total_eval_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 50.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:------:|:---------------:|:------:|:------:|
| 3.4482        | 9.41  | 40000  | 3.4480          | 0.9999 | 0.9974 |
| 3.4619        | 18.81 | 80000  | 3.4514          | 0.9999 | 0.9974 |
| 3.7961        | 28.22 | 120000 | 3.8732          | 0.9999 | 0.9974 |
| 24.3843       | 37.62 | 160000 | 22.5457         | 0.9999 | 0.9973 |
| 48.5691       | 47.03 | 200000 | 45.8892         | 0.9999 | 0.9973 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3
