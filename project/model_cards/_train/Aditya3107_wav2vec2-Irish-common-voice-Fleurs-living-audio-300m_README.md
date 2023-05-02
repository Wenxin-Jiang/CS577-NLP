---
language: ga
datasets:
- common_voice
- google/fleurs
- living_audio_irish
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- ga-IE
- speech
- Irish
model-index:
- name: Wav2vec 2.0 300m XLS-R
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 10.0
      type: common_voice
      args: ga-IE
    metrics:
    - name: Test WER (Without LM)
      type: wer
      value: 19.98
    - name: Test WER (With LM)
      type: wer
      value: 13.87
    - name: Common Voice Irish Invalidated 281 utterances (Without LM)
      type: wer
      value: 39.19
    - name: Common Voice Irish Invalidated 281 utterances (With LM)
      type: wer
      value: 30.85
---


# wav2vec2-Irish-common-voice-Fleurs-living-audio-300m

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the GOOGLE/FLEURS - GA-IE, Common Voice Irish (Validated - (minus) Test) and Living audio Irish Speech dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3361
- Wer: 0.1963

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 3
- total_train_batch_size: 24
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 18.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 0.56  | 200  | 2.8832          | 1.0    |
| No log        | 1.11  | 400  | 1.1705          | 0.7788 |
| 3.3987        | 1.67  | 600  | 0.7739          | 0.5895 |
| 3.3987        | 2.23  | 800  | 0.6045          | 0.4902 |
| 0.8313        | 2.78  | 1000 | 0.5235          | 0.4394 |
| 0.8313        | 3.34  | 1200 | 0.4824          | 0.4002 |
| 0.8313        | 3.9   | 1400 | 0.4378          | 0.3754 |
| 0.5342        | 4.46  | 1600 | 0.4433          | 0.3634 |
| 0.5342        | 5.01  | 1800 | 0.4103          | 0.3485 |
| 0.3792        | 5.57  | 2000 | 0.3816          | 0.3310 |
| 0.3792        | 6.13  | 2200 | 0.3953          | 0.3225 |
| 0.3792        | 6.68  | 2400 | 0.3995          | 0.3132 |
| 0.2924        | 7.24  | 2600 | 0.3907          | 0.2930 |
| 0.2924        | 7.8   | 2800 | 0.3517          | 0.2740 |
| 0.2217        | 8.36  | 3000 | 0.3361          | 0.2591 |
| 0.2217        | 8.91  | 3200 | 0.3340          | 0.2451 |
| 0.2217        | 9.47  | 3400 | 0.3126          | 0.2448 |
| 0.1714        | 10.03 | 3600 | 0.3441          | 0.2556 |
| 0.1714        | 10.58 | 3800 | 0.3404          | 0.2521 |
| 0.1395        | 11.14 | 4000 | 0.3728          | 0.2518 |
| 0.1395        | 11.7  | 4200 | 0.3829          | 0.2396 |
| 0.1395        | 12.26 | 4400 | 0.3466          | 0.2361 |
| 0.1069        | 12.81 | 4600 | 0.3188          | 0.2241 |
| 0.1069        | 13.37 | 4800 | 0.3396          | 0.2197 |
| 0.0845        | 13.93 | 5000 | 0.3365          | 0.2206 |
| 0.0845        | 14.48 | 5200 | 0.3459          | 0.2209 |
| 0.0845        | 15.04 | 5400 | 0.3429          | 0.2194 |
| 0.0675        | 15.6  | 5600 | 0.3434          | 0.2182 |
| 0.0675        | 16.16 | 5800 | 0.3434          | 0.2083 |
| 0.0561        | 16.71 | 6000 | 0.3375          | 0.2036 |
| 0.0561        | 17.27 | 6200 | 0.3446          | 0.1987 |
| 0.0561        | 17.83 | 6400 | 0.3362          | 0.1978 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
