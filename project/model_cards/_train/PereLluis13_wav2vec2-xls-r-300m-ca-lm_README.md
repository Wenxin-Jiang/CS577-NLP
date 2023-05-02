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
- name: wav2vec2-xls-r-300m-ca-lm
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
      value: 6.771703090587865
    - name: Test CER
      type: cer
      value: 2.1007777843712293
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
      value: 5.565360630662431
    - name: Test CER
      type: cer
      value: 1.8594390167034354
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
      value: 13.53312545713516
    - name: Test CER
      type: cer
      value: 8.684635913340556
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
      value: 26.04515843400164
    - name: Test CER
      type: cer
      value: 15.056890012642224
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
      value: 17.68
---

# wav2vec2-xls-r-300m-ca-lm

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - CA, the [tv3_parla](https://huggingface.co/datasets/collectivat/tv3_parla) and [parlament_parla](https://huggingface.co/datasets/projecte-aina/parlament_parla) datasets.
It achieves the following results on the evaluation set (for the three datasets and without the LM):
- Loss: 0.2472
- Wer: 0.1499

## Model description

Please check the original [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) Model card. This is just a finetuned version of that model.

## Intended uses & limitations

As any model trained on crowdsourced data, this model can show the biases and particularities of the data and model used to train this model. Moreover, since this is a speech recognition model, it may underperform for some lower-resourced dialects for the catalan language.

## Training and evaluation data

More information needed

## Training procedure

The data is preprocessed to remove characters not on the catalan alphabet. Moreover, numbers are verbalized using code provided by [@ccoreilly](https://github.com/ccoreilly), which can be found on the text/ folder or [here](https://github.com/CollectivaT-dev/catotron-cpu/blob/master/text/numbers_ca.py).

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 18.0
- mixed_precision_training: Native AMP

### Training results

Check the Tensorboard tab to check the training profile and evaluation results along training. The model was evaluated on the test splits for each of the datasets used during training.

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 6.2099        | 0.09  | 500   | 3.4125          | 1.0    |
| 2.9961        | 0.18  | 1000  | 2.9224          | 1.0    |
| 2.2147        | 0.26  | 1500  | 0.6521          | 0.5568 |
| 1.3017        | 0.35  | 2000  | 0.3153          | 0.2761 |
| 1.1196        | 0.44  | 2500  | 0.2444          | 0.2367 |
| 1.0712        | 0.53  | 3000  | 0.2324          | 0.2132 |
| 1.052         | 0.62  | 3500  | 0.2173          | 0.2032 |
| 1.2813        | 2.13  | 4000  | 0.3326          | 0.2099 |
| 1.2365        | 2.4   | 4500  | 0.3224          | 0.2003 |
| 1.2193        | 2.66  | 5000  | 0.3198          | 0.1957 |
| 1.2072        | 2.93  | 5500  | 0.3063          | 0.1933 |
| 1.213         | 3.2   | 6000  | 0.3051          | 0.1980 |
| 1.2074        | 3.46  | 6500  | 0.3012          | 0.1879 |
| 1.1918        | 3.73  | 7000  | 0.2947          | 0.1829 |
| 1.1893        | 4.0   | 7500  | 0.2895          | 0.1807 |
| 1.1751        | 4.26  | 8000  | 0.2878          | 0.1776 |
| 1.1628        | 4.53  | 8500  | 0.2835          | 0.1731 |
| 1.1577        | 4.79  | 9000  | 0.2816          | 0.1761 |
| 1.1448        | 5.06  | 9500  | 0.2757          | 0.1740 |
| 1.1407        | 5.33  | 10000 | 0.2768          | 0.1798 |
| 1.1401        | 5.59  | 10500 | 0.2780          | 0.1816 |
| 1.1333        | 5.86  | 11000 | 0.2748          | 0.1750 |
| 1.1571        | 6.13  | 11500 | 0.2808          | 0.1708 |
| 1.1505        | 6.39  | 12000 | 0.2726          | 0.1692 |
| 1.1519        | 6.66  | 12500 | 0.2749          | 0.1654 |
| 1.136         | 6.93  | 13000 | 0.2765          | 0.1643 |
| 1.1326        | 7.19  | 13500 | 0.2706          | 0.1668 |
| 1.1342        | 7.46  | 14000 | 0.2665          | 0.1638 |
| 1.1286        | 7.72  | 14500 | 0.2669          | 0.1636 |
| 1.1243        | 7.99  | 15000 | 0.2619          | 0.1623 |
| 1.1173        | 8.26  | 15500 | 0.2652          | 0.1604 |
| 1.1129        | 8.52  | 16000 | 0.2610          | 0.1598 |
| 1.1091        | 8.79  | 16500 | 0.2608          | 0.1584 |
| 1.1053        | 9.06  | 17000 | 0.2633          | 0.1664 |
| 1.1004        | 9.32  | 17500 | 0.2594          | 0.1662 |
| 1.0995        | 9.59  | 18000 | 0.2623          | 0.1569 |
| 1.0964        | 9.86  | 18500 | 0.2624          | 0.1597 |
| 1.09          | 10.12 | 19000 | 0.2577          | 0.1578 |
| 1.089         | 10.39 | 19500 | 0.2574          | 0.1531 |
| 1.0864        | 10.66 | 20000 | 0.2556          | 0.1546 |
| 1.0806        | 10.92 | 20500 | 0.2548          | 0.1583 |
| 1.0842        | 11.19 | 21000 | 0.2550          | 0.1542 |
| 1.0805        | 11.45 | 21500 | 0.2561          | 0.1524 |
| 1.0722        | 11.72 | 22000 | 0.2540          | 0.1566 |
| 1.0763        | 11.99 | 22500 | 0.2549          | 0.1572 |
| 1.0835        | 12.25 | 23000 | 0.2586          | 0.1521 |
| 1.0883        | 12.52 | 23500 | 0.2583          | 0.1519 |
| 1.0888        | 12.79 | 24000 | 0.2551          | 0.1582 |
| 1.0933        | 13.05 | 24500 | 0.2628          | 0.1537 |
| 1.0799        | 13.32 | 25000 | 0.2600          | 0.1508 |
| 1.0804        | 13.59 | 25500 | 0.2620          | 0.1475 |
| 1.0814        | 13.85 | 26000 | 0.2537          | 0.1517 |
| 1.0693        | 14.12 | 26500 | 0.2560          | 0.1542 |
| 1.0724        | 14.38 | 27000 | 0.2540          | 0.1574 |
| 1.0704        | 14.65 | 27500 | 0.2548          | 0.1626 |
| 1.0729        | 14.92 | 28000 | 0.2548          | 0.1601 |
| 1.0724        | 15.18 | 28500 | 0.2511          | 0.1512 |
| 1.0655        | 15.45 | 29000 | 0.2498          | 0.1490 |
| 1.0608        | 15.98 | 30000 | 0.2487          | 0.1481 |
| 1.0541        | 16.52 | 31000 | 0.2468          | 0.1504 |
| 1.0584        | 17.05 | 32000 | 0.2467          | 0.1493 |
| 1.0507        | 17.58 | 33000 | 0.2481          | 0.1517 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0

# Thanks

Want to thank both [@ccoreilly](https://github.com/ccoreilly) and [@gullabi](https://github.com/gullabi) who have contributed with their own resources and knowledge into making this model possible.
