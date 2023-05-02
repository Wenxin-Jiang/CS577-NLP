---
tags:
- automatic-speech-recognition
- generated_from_trainer
license: mit
language:
- lb
metrics:
- wer
pipeline_tag: automatic-speech-recognition

model-index:
- name: Lemswasabi/wav2vec2-base-luxembourgish-4h
  results:
  - task:
      type: automatic-speech-recognition             # Required. Example: automatic-speech-recognition
      name: Speech Recognition             # Optional. Example: Speech Recognition
    metrics:
      - type: wer
        value: 23.95
        name: Dev WER
      - type: wer 
        value: 23.09
        name: Test WER
      - type: cer
        value: 7.97
        name: Dev CER
      - type: cer 
        value: 7.63
        name: Test CER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

## Model description

We pre-trained a wav2vec 2.0 base model on 842h of unlabelled Luxembourgish speech
collected from [RTL.lu](https://www.rtl.lu/). Then the model was fine-tuned on 4h of labelled
Luxembourgish Speech from the same domain.

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 3
- eval_batch_size: 3
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 12
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 50.0
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1

## Citation

This model is a result of our paper `IMPROVING LUXEMBOURGISH SPEECH RECOGNITION WITH CROSS-LINGUAL SPEECH REPRESENTATIONS` submitted to the [IEEE SLT 2022 workshop](https://slt2022.org/)

```
@misc{lb-wav2vec2,
  author = {Nguyen, Le Minh and Nayak, Shekhar and Coler, Matt.},
  keywords = {Luxembourgish, multilingual speech recognition, language modelling, wav2vec 2.0 XLSR-53, under-resourced language},
  title = {IMPROVING LUXEMBOURGISH SPEECH RECOGNITION WITH CROSS-LINGUAL SPEECH REPRESENTATIONS},
  year = {2022},
  copyright = {2023 IEEE}
}
```