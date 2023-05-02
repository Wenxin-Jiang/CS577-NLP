---
language:
- nl
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Large v2 Dutch
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 nl
      type: mozilla-foundation/common_voice_11_0
      config: nl
      split: test
      args: nl
    metrics:
    - name: Wer
      type: wer
      value: 5.895082837397793
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Large v2 Dutch

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the mozilla-foundation/common_voice_11_0 nl dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1310
- Wer: 5.8951

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 12000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.138         | 0.08  | 1000  | 0.2101          | 11.5288 |
| 0.121         | 0.17  | 2000  | 0.1987          | 10.4458 |
| 0.1413        | 0.25  | 3000  | 0.1956          | 10.4672 |
| 0.1158        | 0.33  | 4000  | 0.1778          | 9.3729  |
| 0.1056        | 0.42  | 5000  | 0.1795          | 9.7792  |
| 0.056         | 1.05  | 6000  | 0.1560          | 7.6927  |
| 0.0323        | 1.14  | 7000  | 0.1460          | 7.1445  |
| 0.0213        | 1.22  | 8000  | 0.1491          | 7.2844  |
| 0.051         | 1.3   | 9000  | 0.1457          | 6.9587  |
| 0.0196        | 1.39  | 10000 | 0.1420          | 6.6086  |
| 0.019         | 2.02  | 11000 | 0.1303          | 6.0553  |
| 0.0124        | 2.11  | 12000 | 0.1310          | 5.8951  |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
