---
language:
- ca
license: apache-2.0
tags:
- automatic-speech-recognition
- collectivat/tv3_parla
- generated_from_trainer
- hf-asr-leaderboard
- mozilla-foundation/common_voice_8_0
- projecte-aina/parlament_parla
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_8_0
- collectivat/tv3_parla
- projecte-aina/parlament_parla
model-index:
- name: wav2vec2-xls-r-1b-ca
  results:
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_8_0 ca
      type: mozilla-foundation/common_voice_8_0
      args: ca
    metrics:
    - name: Test WER
      type: wer
      value: 11.030639657300516
    - name: Test CER
      type: cer
      value: 2.8405630530040634
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: projecte-aina/parlament_parla ca
      type: projecte-aina/parlament_parla
      args: clean
    metrics:
    - name: Test WER
      type: wer
      value: 6.483115660665961
    - name: Test CER
      type: cer
      value: 2.0212863746191828
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: collectivat/tv3_parla ca
      type: collectivat/tv3_parla
      args: ca
    metrics:
    - name: Test WER
      type: wer
      value: 17.917773414943988
    - name: Test CER
      type: cer
      value: 8.872589572206396
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Catalan Dev Data
      type: speech-recognition-community-v2/dev_data
      args: ca
    metrics:
    - name: Test WER
      type: wer
      value: 27.126683954209097
    - name: Test CER
      type: cer
      value: 14.213308815078726
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: ca
    metrics:
    - name: Test WER
      type: wer
      value: 18.7
---
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-1b-ca

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - CA, the [tv3_parla](https://huggingface.co/datasets/collectivat/tv3_parla) and [parlament_parla](https://huggingface.co/datasets/projecte-aina/parlament_parla) datasets.

## Model description

Please check the original [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) Model card. This is just a finetuned version of that model.

## Intended uses & limitations

As any model trained on crowdsourced data, this model can show the biases and particularities of the data and model used to train this model. Moreover, since this is a speech recognition model, it may underperform for some lower-resourced dialects for the catalan language.

## Training and evaluation data

## Training procedure

The data is preprocessed to remove characters not on the catalan alphabet. Moreover, numbers are verbalized using code provided by [@ccoreilly](https://github.com/ccoreilly), which can be found on the text/ folder or [here](https://github.com/CollectivaT-dev/catotron-cpu/blob/master/text/numbers_ca.py).

### Training results

Check the Tensorboard tab to check the training profile and evaluation results along training. The model was evaluated on the test splits for each of the datasets used during training.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 10.0
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0

# Thanks

Want to thank both [@ccoreilly](https://github.com/ccoreilly) and [@gullabi](https://github.com/gullabi) who have contributed with their own resources and knowledge into making this model possible.