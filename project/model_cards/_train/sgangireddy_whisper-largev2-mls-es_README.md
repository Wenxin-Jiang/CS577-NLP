---
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- facebook/multilingual_librispeech
metrics:
- wer
model-index:
- name: Whisper largeV2 Spanish MLS
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: facebook/multilingual_librispeech spanish
      type: facebook/multilingual_librispeech
      config: spanish
      split: test
      args: spanish
    metrics:
    - name: Wer
      type: wer
      value: 3.4677966101694913
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper largeV2 Spanish MLS

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the facebook/multilingual_librispeech spanish dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0910
- Wer: 3.4678

## Model description

The model is fine-tuned for 4000 updates/steps on multilingual librispeech Spanish train data.

- Zero-shot                        - 4.2 (MLS Spanish test)
- Fine-tune MLS spanish train      - 3.46 (MLS Spanish test) (-17.61%)

------------------------------------------------------------------------------
- Zero-shot                      - 6.3 (CV11 test)
- Fine-tune MLS spanish train    - 8.38 (CV11 test)

When the model is fine-tuned on specific dataset, the model loose its ability to generalise across datasets.
Here the model is fine-tuned on MLS Spanish and evaluated on CV11 Spanish test. We can observe the drop in performance on CV11 test data.

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.2176        | 0.25  | 1000 | 0.1200          | 5.3932 |
| 0.1845        | 0.5   | 2000 | 0.1055          | 4.2    |
| 0.4516        | 0.75  | 3000 | 0.0977          | 3.6768 |
| 0.1549        | 1.14  | 4000 | 0.0910          | 3.4678 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
