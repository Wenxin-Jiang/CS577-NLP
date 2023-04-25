---
language:
- uk
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_7_0
- generated_from_trainer
- uk
datasets:
- mozilla-foundation/common_voice_7_0
model-index:
- name: wav2vec2-xls-r-300m-uk-with-lm
  results:
  - task: 
      name: Automatic Speech Recognition 
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: uk
    metrics:
       - name: Test WER
         type: wer
         value: 26.47
       - name: Test CER
         type: cer
         value: 2.90
---


# Ukrainian STT model (with Language Model)

🇺🇦 Join Ukrainian Speech Recognition Community - https://t.me/speech_recognition_uk

⭐ See other Ukrainian models - https://github.com/egorsmkv/speech-recognition-uk

- Have a look on an updated 300m model: https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-with-small-lm
- Have a look on a better model with more parameters: https://huggingface.co/Yehor/wav2vec2-xls-r-1b-uk-with-lm

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - UK dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3015
- Wer: 0.3377
- Cer: 0.0708

The above results present evaluation without the language model.

## Model description

On 100 test example the model shows the following results:

Without LM:

- WER: 0.2647
- CER: 0.0469

With LM:

- WER: 0.1568
- CER: 0.0289


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 20
- total_train_batch_size: 160
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 3.0255        | 7.93  | 500  | 2.5514          | 0.9921 | 0.9047 |
| 1.3809        | 15.86 | 1000 | 0.4065          | 0.5361 | 0.1201 |
| 1.2355        | 23.8  | 1500 | 0.3474          | 0.4618 | 0.1033 |
| 1.1956        | 31.74 | 2000 | 0.3617          | 0.4580 | 0.1005 |
| 1.1416        | 39.67 | 2500 | 0.3182          | 0.4074 | 0.0891 |
| 1.0996        | 47.61 | 3000 | 0.3166          | 0.3985 | 0.0875 |
| 1.0427        | 55.55 | 3500 | 0.3116          | 0.3835 | 0.0828 |
| 0.9961        | 63.49 | 4000 | 0.3137          | 0.3757 | 0.0807 |
| 0.9575        | 71.42 | 4500 | 0.2992          | 0.3632 | 0.0771 |
| 0.9154        | 79.36 | 5000 | 0.3015          | 0.3502 | 0.0740 |
| 0.8994        | 87.3  | 5500 | 0.3004          | 0.3425 | 0.0723 |
| 0.871         | 95.24 | 6000 | 0.3016          | 0.3394 | 0.0713 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.18.1.dev0
- Tokenizers 0.11.0
