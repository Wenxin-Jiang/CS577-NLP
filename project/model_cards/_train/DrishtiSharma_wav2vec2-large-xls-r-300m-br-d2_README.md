---
language:
- br
license: apache-2.0
tags:
- generated_from_trainer
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
metrics:
- wer
model-index:
- name: wav2vec2-large-xls-r-300m-br-d2
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      type: mozilla-foundation/common_voice_8_0
      name: Common Voice 8
      args: br
    metrics:
    - type: wer
      value: 0.49770598355954887
      name: Test WER
    - name: Test CER
      type: cer
      value: 0.18090500890299605
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: br
    metrics:
    - name: Test WER
      type: wer
      value: NA
    - name: Test CER
      type: cer
      value: NA
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-br-d2

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - BR dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1257
- Wer: 0.4631

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-br-d2 --dataset mozilla-foundation/common_voice_8_0 --config br --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Breton language isn't available in speech-recognition-community-v2/dev_data

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.00034
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 750
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 14.0379       | 0.68  | 100  | 5.6808          | 1.0    |
| 3.9145        | 1.35  | 200  | 3.1970          | 1.0    |
| 3.0293        | 2.03  | 300  | 2.9513          | 1.0    |
| 2.0927        | 2.7   | 400  | 1.4545          | 0.8887 |
| 1.1556        | 3.38  | 500  | 1.0966          | 0.7564 |
| 0.9628        | 4.05  | 600  | 0.9808          | 0.7364 |
| 0.7869        | 4.73  | 700  | 1.0488          | 0.7355 |
| 0.703         | 5.41  | 800  | 0.9500          | 0.6881 |
| 0.6657        | 6.08  | 900  | 0.9309          | 0.6259 |
| 0.5663        | 6.76  | 1000 | 0.9133          | 0.6357 |
| 0.496         | 7.43  | 1100 | 0.9890          | 0.6028 |
| 0.4748        | 8.11  | 1200 | 0.9469          | 0.5894 |
| 0.4135        | 8.78  | 1300 | 0.9270          | 0.6045 |
| 0.3579        | 9.46  | 1400 | 0.8818          | 0.5708 |
| 0.353         | 10.14 | 1500 | 0.9244          | 0.5781 |
| 0.334         | 10.81 | 1600 | 0.9009          | 0.5638 |
| 0.2917        | 11.49 | 1700 | 1.0132          | 0.5828 |
| 0.29          | 12.16 | 1800 | 0.9696          | 0.5668 |
| 0.2691        | 12.84 | 1900 | 0.9811          | 0.5455 |
| 0.25          | 13.51 | 2000 | 0.9951          | 0.5624 |
| 0.2467        | 14.19 | 2100 | 0.9653          | 0.5573 |
| 0.2242        | 14.86 | 2200 | 0.9714          | 0.5378 |
| 0.2066        | 15.54 | 2300 | 0.9829          | 0.5394 |
| 0.2075        | 16.22 | 2400 | 1.0547          | 0.5520 |
| 0.1923        | 16.89 | 2500 | 1.0014          | 0.5397 |
| 0.1919        | 17.57 | 2600 | 0.9978          | 0.5477 |
| 0.1908        | 18.24 | 2700 | 1.1064          | 0.5397 |
| 0.157         | 18.92 | 2800 | 1.0629          | 0.5238 |
| 0.159         | 19.59 | 2900 | 1.0642          | 0.5321 |
| 0.1652        | 20.27 | 3000 | 1.0207          | 0.5328 |
| 0.141         | 20.95 | 3100 | 0.9948          | 0.5312 |
| 0.1417        | 21.62 | 3200 | 1.0338          | 0.5328 |
| 0.1514        | 22.3  | 3300 | 1.0513          | 0.5313 |
| 0.1365        | 22.97 | 3400 | 1.0357          | 0.5291 |
| 0.1319        | 23.65 | 3500 | 1.0587          | 0.5167 |
| 0.1298        | 24.32 | 3600 | 1.0636          | 0.5236 |
| 0.1245        | 25.0  | 3700 | 1.1367          | 0.5280 |
| 0.1114        | 25.68 | 3800 | 1.0633          | 0.5200 |
| 0.1088        | 26.35 | 3900 | 1.0495          | 0.5210 |
| 0.1175        | 27.03 | 4000 | 1.0897          | 0.5095 |
| 0.1043        | 27.7  | 4100 | 1.0580          | 0.5309 |
| 0.0951        | 28.38 | 4200 | 1.0448          | 0.5067 |
| 0.1011        | 29.05 | 4300 | 1.0665          | 0.5137 |
| 0.0889        | 29.73 | 4400 | 1.0579          | 0.5026 |
| 0.0833        | 30.41 | 4500 | 1.0740          | 0.5037 |
| 0.0889        | 31.08 | 4600 | 1.0933          | 0.5083 |
| 0.0784        | 31.76 | 4700 | 1.0715          | 0.5089 |
| 0.0767        | 32.43 | 4800 | 1.0658          | 0.5049 |
| 0.0769        | 33.11 | 4900 | 1.1118          | 0.4979 |
| 0.0722        | 33.78 | 5000 | 1.1413          | 0.4986 |
| 0.0709        | 34.46 | 5100 | 1.0706          | 0.4885 |
| 0.0664        | 35.14 | 5200 | 1.1217          | 0.4884 |
| 0.0648        | 35.81 | 5300 | 1.1298          | 0.4941 |
| 0.0657        | 36.49 | 5400 | 1.1330          | 0.4920 |
| 0.0582        | 37.16 | 5500 | 1.0598          | 0.4835 |
| 0.0602        | 37.84 | 5600 | 1.1097          | 0.4943 |
| 0.0598        | 38.51 | 5700 | 1.0976          | 0.4876 |
| 0.0547        | 39.19 | 5800 | 1.0734          | 0.4825 |
| 0.0561        | 39.86 | 5900 | 1.0926          | 0.4850 |
| 0.0516        | 40.54 | 6000 | 1.1579          | 0.4751 |
| 0.0478        | 41.22 | 6100 | 1.1384          | 0.4706 |
| 0.0396        | 41.89 | 6200 | 1.1462          | 0.4739 |
| 0.0472        | 42.57 | 6300 | 1.1277          | 0.4732 |
| 0.0447        | 43.24 | 6400 | 1.1517          | 0.4752 |
| 0.0423        | 43.92 | 6500 | 1.1219          | 0.4784 |
| 0.0426        | 44.59 | 6600 | 1.1311          | 0.4724 |
| 0.0391        | 45.27 | 6700 | 1.1135          | 0.4692 |
| 0.0362        | 45.95 | 6800 | 1.0878          | 0.4645 |
| 0.0329        | 46.62 | 6900 | 1.1137          | 0.4668 |
| 0.0356        | 47.3  | 7000 | 1.1233          | 0.4687 |
| 0.0328        | 47.97 | 7100 | 1.1238          | 0.4653 |
| 0.0323        | 48.65 | 7200 | 1.1307          | 0.4646 |
| 0.0325        | 49.32 | 7300 | 1.1242          | 0.4645 |
| 0.03          | 50.0  | 7400 | 1.1257          | 0.4631 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
