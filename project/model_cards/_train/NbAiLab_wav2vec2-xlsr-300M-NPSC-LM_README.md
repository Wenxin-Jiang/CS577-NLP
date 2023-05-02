---
language:
- nb-NO
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- false
- nb-NO
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- NbAiLab/NPSC
model-index:
- name: XLS-R-300M-LM - Norwegian
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: NPSC
      type: NbAiLab/NPSC
    metrics:
    - name: Eval WER
      type: wer
      value: 15.4
    - name: Eval CER
      type: cer
      value: 5.48
---


# XLS-R-300M-LM - Norwegian

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the Norwegian [NPSC](https://huggingface.co/datasets/NbAiLab/NPSC) dataset.
 
### Scores without Language Model
Without using a language model, it achieves the following scores on the NPSC Eval set
It achieves the following results on the evaluation set without a language model:
- WER: 0.2110
- CER: 0.0622

### Scores with Language Model
A 5-gram KenLM was added to boost the models performance. The language model was created on a corpus mainly consisting of online newspapers, public reports and Wikipedia data. After this we are getting these values.

- WER: 0.1540
- CER: 0.0548

## Team
The model is developed by Rolv-Arild Braaten, Per Egil Kummervold, Andre Kåsen, Javier de la Rosa, Per Erik Solberg, and Freddy Wetjen. Name in alphabetic order.

## Model description
This current version is based on checkpoint 8500 of [NbAiLab/wav2vec2-xlsr-300M-NPSC-OH](https://huggingface.co/NbAiLab/wav2vec2-xlsr-300M-NPSC-OH).

## Intended uses & limitations
Demo version only. The model will be updated later this week.

## Training and evaluation data
The model is trained and evaluated on [NPSC](https://huggingface.co/datasets/NbAiLab/NPSC). Unfortunately there is no Norwegian test data in Common Voice, and currently the model is only evaluated on the validation set of NPSC..

## Training procedure
### Training hyperparameters
The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 30.0 (But interrupted after 8500 steps, approx 6 epochs)
- mixed_precision_training: Native AMP


