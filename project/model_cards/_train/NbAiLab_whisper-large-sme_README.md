---
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- audiofolder
language:
- se
metrics:
- wer
model-index:
- name: "Whisper Large Northern S\xE1mi"
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: audiofolder
      type: audiofolder
      config: default
      split: test
      args: default
    metrics:
    - name: Wer
      type: wer
      value: 24.914285714285715
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Large Northern Sámi

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the audiofolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5559
- Wer: 24.9143

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
- train_batch_size: 12
- eval_batch_size: 6
- seed: 42
- distributed_type: multi-GPU
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 60000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer     |
|:-------------:|:------:|:-----:|:---------------:|:-------:|
| 0.4665        | 58.0   | 1000  | 0.8572          | 54.5143 |
| 0.3041        | 117.0  | 2000  | 0.6711          | 44.1143 |
| 0.2671        | 176.0  | 3000  | 0.5794          | 39.7714 |
| 0.1761        | 235.0  | 4000  | 0.5357          | 35.0857 |
| 0.2089        | 294.0  | 5000  | 0.5094          | 33.6    |
| 0.1456        | 352.0  | 6000  | 0.4959          | 33.0286 |
| 0.1514        | 411.0  | 7000  | 0.4864          | 32.5714 |
| 0.1203        | 470.0  | 8000  | 0.4625          | 31.4286 |
| 0.0879        | 529.0  | 9000  | 0.4916          | 45.4857 |
| 0.0825        | 588.0  | 10000 | 0.4962          | 30.6286 |
| 0.0753        | 647.0  | 11000 | 0.4723          | 31.2    |
| 0.0812        | 705.0  | 12000 | 0.4574          | 28.6857 |
| 0.062         | 764.0  | 13000 | 0.4628          | 28.8000 |
| 0.0604        | 823.0  | 14000 | 0.4668          | 28.0000 |
| 0.0666        | 882.0  | 15000 | 0.4697          | 28.6857 |
| 0.0405        | 941.0  | 16000 | 0.4908          | 54.6286 |
| 0.0349        | 999.0  | 17000 | 0.4728          | 28.4571 |
| 0.0409        | 1058.0 | 18000 | 0.4884          | 28.4571 |
| 0.0292        | 1117.0 | 19000 | 0.4576          | 27.3143 |
| 0.0247        | 1176.0 | 20000 | 0.4734          | 28.9143 |
| 0.0229        | 1235.0 | 21000 | 0.4899          | 29.9429 |
| 0.0271        | 1294.0 | 22000 | 0.4790          | 28.1143 |
| 0.0271        | 1352.0 | 23000 | 0.5012          | 30.1714 |
| 0.0184        | 1411.0 | 24000 | 0.5008          | 27.3143 |
| 0.0211        | 1470.0 | 25000 | 0.5118          | 27.6571 |
| 0.0183        | 1529.0 | 26000 | 0.5398          | 30.0571 |
| 0.0164        | 1588.0 | 27000 | 0.5006          | 27.3143 |
| 0.0169        | 1647.0 | 28000 | 0.5059          | 27.0857 |
| 0.0147        | 1705.0 | 29000 | 0.5325          | 27.7714 |
| 0.0104        | 1764.0 | 30000 | 0.4818          | 26.1714 |
| 0.0128        | 1823.0 | 31000 | 0.5259          | 28.3429 |
| 0.0145        | 1882.0 | 32000 | 0.5299          | 26.2857 |
| 0.0075        | 1941.0 | 33000 | 0.5082          | 27.4286 |
| 0.0087        | 1999.0 | 34000 | 0.5144          | 26.6286 |
| 0.005         | 2058.0 | 35000 | 0.5590          | 27.0857 |
| 0.0099        | 2117.0 | 36000 | 0.5546          | 28.9143 |
| 0.007         | 2176.0 | 37000 | 0.5364          | 26.8571 |
| 0.0045        | 2235.0 | 38000 | 0.5574          | 27.2000 |
| 0.0064        | 2294.0 | 39000 | 0.5051          | 25.7143 |
| 0.0079        | 2352.0 | 40000 | 0.5247          | 25.9429 |
| 0.0083        | 2411.0 | 41000 | 0.5514          | 25.6    |
| 0.0101        | 2470.0 | 42000 | 0.5710          | 25.6    |
| 0.0062        | 2529.0 | 43000 | 0.5830          | 28.0000 |
| 0.0046        | 2588.0 | 44000 | 0.5828          | 26.8571 |
| 0.0053        | 2647.0 | 45000 | 0.5621          | 27.4286 |
| 0.0047        | 2705.0 | 46000 | 0.5673          | 25.9429 |
| 0.0045        | 2764.0 | 47000 | 0.5220          | 25.6    |
| 0.0065        | 2823.0 | 48000 | 0.5704          | 27.7714 |
| 0.0039        | 2882.0 | 49000 | 0.5741          | 27.7714 |
| 0.0027        | 2941.0 | 50000 | 0.5762          | 26.0571 |
| 0.0019        | 2999.0 | 51000 | 0.5559          | 24.9143 |
| 0.0015        | 3058.0 | 52000 | 0.5777          | 28.5714 |
| 0.0026        | 3117.0 | 53000 | 0.5589          | 25.2571 |
| 0.0032        | 3176.0 | 54000 | 0.6061          | 26.9714 |
| 0.0025        | 3235.0 | 55000 | 0.5776          | 25.1429 |
| 0.0046        | 3294.0 | 56000 | 0.5753          | 27.3143 |
| 0.0015        | 3352.0 | 57000 | 0.5736          | 27.2000 |
| 0.003         | 3411.0 | 58000 | 0.5933          | 25.6    |
| 0.002         | 3470.0 | 59000 | 0.6036          | 25.6    |
| 0.0007        | 58.0   | 60000 | 0.5975          | 25.2571 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.11.0
