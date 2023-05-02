---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-xls-r-300m-arabic_speech_commands_10s_one_speaker
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-arabic_speech_commands_10s_one_speaker

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0825
- Accuracy: 0.9833

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 80

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 0.92  | 3    | 1.6103          | 0.2      |
| No log        | 1.92  | 6    | 1.6087          | 0.2      |
| No log        | 2.92  | 9    | 1.6056          | 0.3033   |
| 1.7251        | 3.92  | 12   | 1.6021          | 0.2      |
| 1.7251        | 4.92  | 15   | 1.5831          | 0.2533   |
| 1.7251        | 5.92  | 18   | 1.5251          | 0.5367   |
| 1.6654        | 6.92  | 21   | 1.3294          | 0.74     |
| 1.6654        | 7.92  | 24   | 1.0468          | 0.7567   |
| 1.6654        | 8.92  | 27   | 0.9286          | 0.8533   |
| 1.2188        | 9.92  | 30   | 0.7191          | 0.83     |
| 1.2188        | 10.92 | 33   | 0.6482          | 0.87     |
| 1.2188        | 11.92 | 36   | 0.6057          | 0.8433   |
| 1.2188        | 12.92 | 39   | 0.3797          | 0.9467   |
| 0.6897        | 13.92 | 42   | 0.3407          | 0.9267   |
| 0.6897        | 14.92 | 45   | 0.2305          | 0.95     |
| 0.6897        | 15.92 | 48   | 0.2806          | 0.92     |
| 0.2498        | 16.92 | 51   | 0.2146          | 0.9467   |
| 0.2498        | 17.92 | 54   | 0.2850          | 0.9233   |
| 0.2498        | 18.92 | 57   | 0.1945          | 0.9467   |
| 0.0658        | 19.92 | 60   | 0.0825          | 0.9833   |
| 0.0658        | 20.92 | 63   | 0.1280          | 0.9767   |
| 0.0658        | 21.92 | 66   | 0.1024          | 0.98     |
| 0.0658        | 22.92 | 69   | 0.1102          | 0.9767   |
| 0.044         | 23.92 | 72   | 0.0780          | 0.98     |
| 0.044         | 24.92 | 75   | 0.2282          | 0.94     |
| 0.044         | 25.92 | 78   | 0.0923          | 0.9767   |
| 0.153         | 26.92 | 81   | 0.0950          | 0.9767   |
| 0.153         | 27.92 | 84   | 0.1508          | 0.9633   |
| 0.153         | 28.92 | 87   | 0.0844          | 0.9833   |
| 0.0301        | 29.92 | 90   | 0.1224          | 0.97     |
| 0.0301        | 30.92 | 93   | 0.1852          | 0.95     |
| 0.0301        | 31.92 | 96   | 0.2527          | 0.94     |
| 0.0301        | 32.92 | 99   | 0.3035          | 0.9367   |
| 0.0092        | 33.92 | 102  | 0.4948          | 0.8967   |
| 0.0092        | 34.92 | 105  | 0.3825          | 0.9167   |
| 0.0092        | 35.92 | 108  | 0.1381          | 0.9733   |
| 0.0437        | 36.92 | 111  | 0.1392          | 0.9667   |
| 0.0437        | 37.92 | 114  | 0.1889          | 0.95     |
| 0.0437        | 38.92 | 117  | 0.2354          | 0.94     |
| 0.006         | 39.92 | 120  | 0.2462          | 0.9433   |
| 0.006         | 40.92 | 123  | 0.1140          | 0.97     |
| 0.006         | 41.92 | 126  | 0.3629          | 0.94     |
| 0.006         | 42.92 | 129  | 0.1350          | 0.97     |
| 0.0458        | 43.92 | 132  | 0.0908          | 0.98     |
| 0.0458        | 44.92 | 135  | 0.1091          | 0.98     |
| 0.0458        | 45.92 | 138  | 0.1283          | 0.9733   |
| 0.0063        | 46.92 | 141  | 0.1448          | 0.9733   |
| 0.0063        | 47.92 | 144  | 0.1495          | 0.9633   |
| 0.0063        | 48.92 | 147  | 0.1628          | 0.9633   |
| 0.0161        | 49.92 | 150  | 0.1812          | 0.96     |
| 0.0161        | 50.92 | 153  | 0.1954          | 0.96     |
| 0.0161        | 51.92 | 156  | 0.2043          | 0.96     |
| 0.0161        | 52.92 | 159  | 0.1715          | 0.9567   |
| 0.0989        | 53.92 | 162  | 0.1482          | 0.9633   |
| 0.0989        | 54.92 | 165  | 0.1305          | 0.97     |
| 0.0989        | 55.92 | 168  | 0.1269          | 0.97     |
| 0.0084        | 56.92 | 171  | 0.1302          | 0.9667   |
| 0.0084        | 57.92 | 174  | 0.1351          | 0.9667   |
| 0.0084        | 58.92 | 177  | 0.1408          | 0.9667   |
| 0.0054        | 59.92 | 180  | 0.1194          | 0.9767   |
| 0.0054        | 60.92 | 183  | 0.1110          | 0.98     |
| 0.0054        | 61.92 | 186  | 0.1064          | 0.98     |
| 0.0054        | 62.92 | 189  | 0.1050          | 0.9767   |
| 0.0031        | 63.92 | 192  | 0.1051          | 0.9767   |
| 0.0031        | 64.92 | 195  | 0.1047          | 0.98     |
| 0.0031        | 65.92 | 198  | 0.1121          | 0.98     |
| 0.0061        | 66.92 | 201  | 0.1170          | 0.9767   |
| 0.0061        | 67.92 | 204  | 0.1183          | 0.9733   |
| 0.0061        | 68.92 | 207  | 0.1181          | 0.9733   |
| 0.0032        | 69.92 | 210  | 0.1179          | 0.9733   |
| 0.0032        | 70.92 | 213  | 0.1000          | 0.98     |
| 0.0032        | 71.92 | 216  | 0.0883          | 0.98     |
| 0.0032        | 72.92 | 219  | 0.0787          | 0.9833   |
| 0.0029        | 73.92 | 222  | 0.0715          | 0.98     |
| 0.0029        | 74.92 | 225  | 0.0668          | 0.98     |
| 0.0029        | 75.92 | 228  | 0.0639          | 0.98     |
| 0.0027        | 76.92 | 231  | 0.0621          | 0.98     |
| 0.0027        | 77.92 | 234  | 0.0611          | 0.98     |
| 0.0027        | 78.92 | 237  | 0.0607          | 0.9833   |
| 0.0022        | 79.92 | 240  | 0.0606          | 0.9833   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1