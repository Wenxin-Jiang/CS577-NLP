---
language:
- de
license: apache-2.0
tags:
- automatic-speech-recognition
- de
- generated_from_trainer
- hf-asr-leaderboard
- mozilla-foundation/common_voice_7_0
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_7_0
model-index:
- name: XLS-R-300M - German
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: de
    metrics:
    - name: Test WER
      type: wer
      value: 20.16
    - name: Test CER
      type: cer
      value: 5.06
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: de
    metrics:
    - name: Test WER
      type: wer
      value: 39.79
    - name: Test CER
      type: cer
      value: 15.02
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: de
    metrics:
    - name: Test WER
      type: wer
      value: 47.95
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. 
eval results:
WER: 0.20161578657865786
CER: 0.05062357805269733
-->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - DE dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1768
- Wer: 0.2016

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

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
- num_epochs: 3.4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 5.7531        | 0.04  | 500   | 5.4564          | 1.0    |
| 2.9882        | 0.08  | 1000  | 3.0041          | 1.0    |
| 2.1953        | 0.13  | 1500  | 1.1723          | 0.7121 |
| 1.2406        | 0.17  | 2000  | 0.3656          | 0.3623 |
| 1.1294        | 0.21  | 2500  | 0.2843          | 0.2926 |
| 1.0731        | 0.25  | 3000  | 0.2554          | 0.2664 |
| 1.051         | 0.3   | 3500  | 0.2387          | 0.2535 |
| 1.0479        | 0.34  | 4000  | 0.2345          | 0.2512 |
| 1.0026        | 0.38  | 4500  | 0.2270          | 0.2452 |
| 0.9921        | 0.42  | 5000  | 0.2212          | 0.2353 |
| 0.9839        | 0.47  | 5500  | 0.2141          | 0.2330 |
| 0.9907        | 0.51  | 6000  | 0.2122          | 0.2334 |
| 0.9788        | 0.55  | 6500  | 0.2114          | 0.2270 |
| 0.9687        | 0.59  | 7000  | 0.2066          | 0.2323 |
| 0.9777        | 0.64  | 7500  | 0.2033          | 0.2237 |
| 0.9476        | 0.68  | 8000  | 0.2020          | 0.2194 |
| 0.9625        | 0.72  | 8500  | 0.1977          | 0.2191 |
| 0.9497        | 0.76  | 9000  | 0.1976          | 0.2175 |
| 0.9781        | 0.81  | 9500  | 0.1956          | 0.2159 |
| 0.9552        | 0.85  | 10000 | 0.1958          | 0.2191 |
| 0.9345        | 0.89  | 10500 | 0.1964          | 0.2158 |
| 0.9528        | 0.93  | 11000 | 0.1926          | 0.2154 |
| 0.9502        | 0.98  | 11500 | 0.1953          | 0.2149 |
| 0.9358        | 1.02  | 12000 | 0.1927          | 0.2167 |
| 0.941         | 1.06  | 12500 | 0.1901          | 0.2115 |
| 0.9287        | 1.1   | 13000 | 0.1936          | 0.2090 |
| 0.9491        | 1.15  | 13500 | 0.1900          | 0.2104 |
| 0.9478        | 1.19  | 14000 | 0.1931          | 0.2120 |
| 0.946         | 1.23  | 14500 | 0.1914          | 0.2134 |
| 0.9499        | 1.27  | 15000 | 0.1931          | 0.2173 |
| 0.9346        | 1.32  | 15500 | 0.1913          | 0.2105 |
| 0.9509        | 1.36  | 16000 | 0.1902          | 0.2137 |
| 0.9294        | 1.4   | 16500 | 0.1895          | 0.2086 |
| 0.9418        | 1.44  | 17000 | 0.1913          | 0.2183 |
| 0.9302        | 1.49  | 17500 | 0.1884          | 0.2114 |
| 0.9418        | 1.53  | 18000 | 0.1894          | 0.2108 |
| 0.9363        | 1.57  | 18500 | 0.1886          | 0.2132 |
| 0.9338        | 1.61  | 19000 | 0.1856          | 0.2078 |
| 0.9185        | 1.66  | 19500 | 0.1852          | 0.2056 |
| 0.9216        | 1.7   | 20000 | 0.1874          | 0.2095 |
| 0.9176        | 1.74  | 20500 | 0.1873          | 0.2078 |
| 0.9288        | 1.78  | 21000 | 0.1865          | 0.2097 |
| 0.9278        | 1.83  | 21500 | 0.1869          | 0.2100 |
| 0.9295        | 1.87  | 22000 | 0.1878          | 0.2095 |
| 0.9221        | 1.91  | 22500 | 0.1852          | 0.2121 |
| 0.924         | 1.95  | 23000 | 0.1855          | 0.2042 |
| 0.9104        | 2.0   | 23500 | 0.1858          | 0.2105 |
| 0.9284        | 2.04  | 24000 | 0.1850          | 0.2080 |
| 0.9162        | 2.08  | 24500 | 0.1839          | 0.2045 |
| 0.9111        | 2.12  | 25000 | 0.1838          | 0.2080 |
| 0.91          | 2.17  | 25500 | 0.1889          | 0.2106 |
| 0.9152        | 2.21  | 26000 | 0.1856          | 0.2026 |
| 0.9209        | 2.25  | 26500 | 0.1891          | 0.2133 |
| 0.9094        | 2.29  | 27000 | 0.1857          | 0.2089 |
| 0.9065        | 2.34  | 27500 | 0.1840          | 0.2052 |
| 0.9156        | 2.38  | 28000 | 0.1833          | 0.2062 |
| 0.8986        | 2.42  | 28500 | 0.1789          | 0.2001 |
| 0.9045        | 2.46  | 29000 | 0.1769          | 0.2022 |
| 0.9039        | 2.51  | 29500 | 0.1819          | 0.2073 |
| 0.9145        | 2.55  | 30000 | 0.1828          | 0.2063 |
| 0.9081        | 2.59  | 30500 | 0.1811          | 0.2049 |
| 0.9252        | 2.63  | 31000 | 0.1833          | 0.2086 |
| 0.8957        | 2.68  | 31500 | 0.1795          | 0.2083 |
| 0.891         | 2.72  | 32000 | 0.1809          | 0.2058 |
| 0.9023        | 2.76  | 32500 | 0.1812          | 0.2061 |
| 0.8918        | 2.8   | 33000 | 0.1775          | 0.1997 |
| 0.8852        | 2.85  | 33500 | 0.1790          | 0.1997 |
| 0.8928        | 2.89  | 34000 | 0.1767          | 0.2013 |
| 0.9079        | 2.93  | 34500 | 0.1735          | 0.1986 |
| 0.9032        | 2.97  | 35000 | 0.1793          | 0.2024 |
| 0.9018        | 3.02  | 35500 | 0.1778          | 0.2027 |
| 0.8846        | 3.06  | 36000 | 0.1776          | 0.2046 |
| 0.8848        | 3.1   | 36500 | 0.1812          | 0.2064 |
| 0.9062        | 3.14  | 37000 | 0.1800          | 0.2018 |
| 0.9011        | 3.19  | 37500 | 0.1783          | 0.2049 |
| 0.8996        | 3.23  | 38000 | 0.1810          | 0.2036 |
| 0.893         | 3.27  | 38500 | 0.1805          | 0.2056 |
| 0.897         | 3.31  | 39000 | 0.1773          | 0.2035 |
| 0.8992        | 3.36  | 39500 | 0.1804          | 0.2054 |
| 0.8987        | 3.4   | 40000 | 0.1768          | 0.2016 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0

#### Evaluation Commands
1. To evaluate on `mozilla-foundation/common_voice_7_0` with split `test`

```bash
python ./eval.py --model_id AndrewMcDowell/wav2vec2-xls-r-300m-german-de --dataset mozilla-foundation/common_voice_7_0 --config de --split test --log_outputs
```

2. To evaluate on test dev data
```bash
python ./eval.py --model_id AndrewMcDowell/wav2vec2-xls-r-300m-german-de --dataset speech-recognition-community-v2/dev_data --config de --split validation --chunk_length_s 5.0 --stride_length_s 1.0
```