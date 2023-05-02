---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-libri-train100-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-libri-train100-colab

This model is a fine-tuned version of [GW12/wav2vec2-base-timit-demo-colab](https://huggingface.co/GW12/wav2vec2-base-timit-demo-colab) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2039
- Wer: 0.1190

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 2.9399        | 0.18  | 500   | 0.3129          | 0.2584 |
| 0.2556        | 0.36  | 1000  | 0.7132          | 0.2435 |
| 0.2184        | 0.54  | 1500  | 0.4794          | 0.2382 |
| 0.1878        | 0.72  | 2000  | 0.2399          | 0.1881 |
| 0.1764        | 0.91  | 2500  | 0.2089          | 0.1807 |
| 0.1524        | 1.09  | 3000  | 0.2328          | 0.1679 |
| 0.1319        | 1.27  | 3500  | 0.4081          | 0.2228 |
| 0.1325        | 1.45  | 4000  | 0.2202          | 0.1674 |
| 0.1315        | 1.63  | 4500  | 0.2055          | 0.1602 |
| 0.1205        | 1.81  | 5000  | 0.2152          | 0.1616 |
| 0.1199        | 1.99  | 5500  | 0.3416          | 0.1666 |
| 0.0978        | 2.17  | 6000  | 0.1856          | 0.1518 |
| 0.0947        | 2.35  | 6500  | 0.2043          | 0.1550 |
| 0.0971        | 2.54  | 7000  | 0.2786          | 0.1550 |
| 0.0969        | 2.72  | 7500  | 0.7752          | 0.1823 |
| 0.0957        | 2.9   | 8000  | 0.2138          | 0.1495 |
| 0.0863        | 3.08  | 8500  | 0.2073          | 0.1450 |
| 0.0773        | 3.26  | 9000  | 0.5881          | 0.1665 |
| 0.0765        | 3.44  | 9500  | 0.2214          | 0.1457 |
| 0.078         | 3.62  | 10000 | 0.1984          | 0.1421 |
| 0.0793        | 3.8   | 10500 | 0.1800          | 0.1419 |
| 0.0738        | 3.98  | 11000 | 0.1884          | 0.1399 |
| 0.0645        | 4.17  | 11500 | 0.1802          | 0.1365 |
| 0.0649        | 4.35  | 12000 | 0.1827          | 0.1346 |
| 0.0593        | 4.53  | 12500 | 0.1850          | 0.1368 |
| 0.0619        | 4.71  | 13000 | 0.1890          | 0.1363 |
| 0.0623        | 4.89  | 13500 | 0.1923          | 0.1339 |
| 0.0583        | 5.07  | 14000 | 0.1711          | 0.1311 |
| 0.0511        | 5.25  | 14500 | 0.1950          | 0.1330 |
| 0.049         | 5.43  | 15000 | 0.1857          | 0.1318 |
| 0.0527        | 5.61  | 15500 | 0.1881          | 0.1298 |
| 0.0513        | 5.8   | 16000 | 0.1904          | 0.1313 |
| 0.0506        | 5.98  | 16500 | 0.1795          | 0.1288 |
| 0.0447        | 6.16  | 17000 | 0.1924          | 0.1277 |
| 0.0434        | 6.34  | 17500 | 0.1979          | 0.1294 |
| 0.0418        | 6.52  | 18000 | 0.1971          | 0.1272 |
| 0.0415        | 6.7   | 18500 | 0.1932          | 0.1267 |
| 0.0425        | 6.88  | 19000 | 0.1902          | 0.1261 |
| 0.0384        | 7.06  | 19500 | 0.2078          | 0.1259 |
| 0.0349        | 7.24  | 20000 | 0.2167          | 0.1293 |
| 0.0325        | 7.42  | 20500 | 0.2150          | 0.1269 |
| 0.0344        | 7.61  | 21000 | 0.1923          | 0.1222 |
| 0.0337        | 7.79  | 21500 | 0.1955          | 0.1216 |
| 0.0336        | 7.97  | 22000 | 0.1932          | 0.1223 |
| 0.0286        | 8.15  | 22500 | 0.2115          | 0.1230 |
| 0.0306        | 8.33  | 23000 | 0.2015          | 0.1237 |
| 0.0274        | 8.51  | 23500 | 0.2110          | 0.1231 |
| 0.0284        | 8.69  | 24000 | 0.2094          | 0.1217 |
| 0.0282        | 8.87  | 24500 | 0.2030          | 0.1205 |
| 0.0257        | 9.05  | 25000 | 0.2092          | 0.1204 |
| 0.0267        | 9.24  | 25500 | 0.2093          | 0.1198 |
| 0.0252        | 9.42  | 26000 | 0.2070          | 0.1195 |
| 0.0248        | 9.6   | 26500 | 0.2056          | 0.1193 |
| 0.026         | 9.78  | 27000 | 0.2045          | 0.1193 |
| 0.0238        | 9.96  | 27500 | 0.2039          | 0.1190 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0
- Datasets 1.13.3
- Tokenizers 0.10.3
