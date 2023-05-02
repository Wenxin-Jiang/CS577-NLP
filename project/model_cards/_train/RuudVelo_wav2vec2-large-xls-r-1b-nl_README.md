---
language:
- nl
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- nl
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-1b-nl
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: 11.12
    - name: Test CER
      type: cer
      value: 3.2
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: 31.92
    - name: Test CER
      type: cer
      value: 13.87
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: 32.17
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - NL dataset. This model is also available with a language model which improves these results. This model can be found at https://huggingface.co/RuudVelo/wav2vec2-large-xls-r-1b-nl-lm. The Common Voice 8 Dutch test Wer is 9.73 of that model. 
It achieves the following results on the evaluation set:
- Loss: 0.1479
- Wer: 0.1156

## Model description

Model fine-tuned using the wav2vec-als-r-1b model architecture

## Intended uses & limitations

More information needed

## Training and evaluation data

Model has been trained on Common Voice 8 Dutch

## Training procedure

### Training hyperparameters

Model parameters can be found under Files and versions in the run.sh file.

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 1.2223        | 0.52  | 500   | 0.3866          | 0.3425 |
| 1.0748        | 1.03  | 1000  | 0.2574          | 0.2169 |
| 1.0416        | 1.55  | 1500  | 0.2177          | 0.1946 |
| 0.9951        | 2.06  | 2000  | 0.2008          | 0.1760 |
| 0.975         | 2.58  | 2500  | 0.1961          | 0.1751 |
| 0.9461        | 3.1   | 3000  | 0.1989          | 0.1782 |
| 0.9381        | 3.61  | 3500  | 0.1928          | 0.1699 |
| 0.934         | 4.13  | 4000  | 0.1923          | 0.1633 |
| 0.9322        | 4.64  | 4500  | 0.1871          | 0.1634 |
| 0.9012        | 5.16  | 5000  | 0.1890          | 0.1702 |
| 0.9045        | 5.68  | 5500  | 0.1882          | 0.1740 |
| 0.8826        | 6.19  | 6000  | 0.1856          | 0.1575 |
| 0.8848        | 6.71  | 6500  | 0.1861          | 0.1617 |
| 0.8723        | 7.22  | 7000  | 0.1927          | 0.1646 |
| 0.8725        | 7.74  | 7500  | 0.1798          | 0.1531 |
| 0.8573        | 8.26  | 8000  | 0.1781          | 0.1587 |
| 0.8633        | 8.77  | 8500  | 0.1852          | 0.1628 |
| 0.8603        | 9.29  | 9000  | 0.1833          | 0.1601 |
| 0.8421        | 9.8   | 9500  | 0.1788          | 0.1543 |
| 0.8404        | 10.32 | 10000 | 0.1844          | 0.1556 |
| 0.8342        | 10.84 | 10500 | 0.1770          | 0.1538 |
| 0.8161        | 11.35 | 11000 | 0.1821          | 0.1567 |
| 0.8371        | 11.87 | 11500 | 0.1909          | 0.1629 |
| 0.8083        | 12.38 | 12000 | 0.1778          | 0.1498 |
| 0.806         | 12.9  | 12500 | 0.1802          | 0.1547 |
| 0.8013        | 13.42 | 13000 | 0.1859          | 0.1584 |
| 0.7913        | 13.93 | 13500 | 0.1875          | 0.1517 |
| 0.8063        | 14.45 | 14000 | 0.1799          | 0.1571 |
| 0.7991        | 14.96 | 14500 | 0.1792          | 0.1538 |
| 0.7843        | 15.48 | 15000 | 0.1753          | 0.1464 |
| 0.7905        | 16.0  | 15500 | 0.1784          | 0.1508 |
| 0.7808        | 16.51 | 16000 | 0.1771          | 0.1485 |
| 0.7743        | 17.03 | 16500 | 0.1795          | 0.1491 |
| 0.7833        | 17.54 | 17000 | 0.1722          | 0.1484 |
| 0.7763        | 18.06 | 17500 | 0.1767          | 0.1518 |
| 0.7698        | 18.58 | 18000 | 0.1720          | 0.1460 |
| 0.7571        | 19.09 | 18500 | 0.1735          | 0.1478 |
| 0.7673        | 19.61 | 19000 | 0.1817          | 0.1511 |
| 0.7415        | 20.12 | 19500 | 0.1763          | 0.1481 |
| 0.751         | 20.64 | 20000 | 0.1742          | 0.1484 |
| 0.7563        | 21.16 | 20500 | 0.1810          | 0.1611 |
| 0.7423        | 21.67 | 21000 | 0.1817          | 0.1557 |
| 0.7242        | 22.19 | 21500 | 0.1690          | 0.1446 |
| 0.7251        | 22.7  | 22000 | 0.1684          | 0.1446 |
| 0.7302        | 23.22 | 22500 | 0.1735          | 0.1430 |
| 0.733         | 23.74 | 23000 | 0.1720          | 0.1454 |
| 0.7128        | 24.25 | 23500 | 0.1668          | 0.1383 |
| 0.7184        | 24.77 | 24000 | 0.1635          | 0.1377 |
| 0.7015        | 25.28 | 24500 | 0.1646          | 0.1389 |
| 0.7198        | 25.8  | 25000 | 0.1775          | 0.1462 |
| 0.7178        | 26.32 | 25500 | 0.1705          | 0.1419 |
| 0.7199        | 26.83 | 26000 | 0.1649          | 0.1416 |
| 0.6981        | 27.35 | 26500 | 0.1724          | 0.1418 |
| 0.6886        | 27.86 | 27000 | 0.1633          | 0.1382 |
| 0.6922        | 28.38 | 27500 | 0.1698          | 0.1420 |
| 0.6833        | 28.9  | 28000 | 0.1611          | 0.1351 |
| 0.6798        | 29.41 | 28500 | 0.1639          | 0.1365 |
| 0.6711        | 29.93 | 29000 | 0.1668          | 0.1358 |
| 0.6762        | 30.44 | 29500 | 0.1682          | 0.1355 |
| 0.6594        | 30.96 | 30000 | 0.1629          | 0.1345 |
| 0.6664        | 31.48 | 30500 | 0.1625          | 0.1321 |
| 0.6838        | 31.99 | 31000 | 0.1597          | 0.1372 |
| 0.6603        | 32.51 | 31500 | 0.1583          | 0.1302 |
| 0.6468        | 33.02 | 32000 | 0.1595          | 0.1322 |
| 0.6464        | 33.54 | 32500 | 0.1609          | 0.1315 |
| 0.6623        | 34.06 | 33000 | 0.1622          | 0.1366 |
| 0.6414        | 34.57 | 33500 | 0.1587          | 0.1330 |
| 0.6242        | 35.09 | 34000 | 0.1614          | 0.1337 |
| 0.632         | 35.6  | 34500 | 0.1568          | 0.1272 |
| 0.6346        | 36.12 | 35000 | 0.1583          | 0.1274 |
| 0.6143        | 36.64 | 35500 | 0.1576          | 0.1264 |
| 0.6208        | 37.15 | 36000 | 0.1621          | 0.1263 |
| 0.6185        | 37.67 | 36500 | 0.1623          | 0.1270 |
| 0.6128        | 38.18 | 37000 | 0.1604          | 0.1268 |
| 0.6151        | 38.7  | 37500 | 0.1593          | 0.1246 |
| 0.6082        | 39.22 | 38000 | 0.1532          | 0.1238 |
| 0.6           | 39.73 | 38500 | 0.1524          | 0.1224 |
| 0.6032        | 40.25 | 39000 | 0.1521          | 0.1212 |
| 0.6016        | 40.76 | 39500 | 0.1551          | 0.1215 |
| 0.6009        | 41.28 | 40000 | 0.1523          | 0.1215 |
| 0.5875        | 41.8  | 40500 | 0.1541          | 0.1216 |
| 0.608         | 42.31 | 41000 | 0.1536          | 0.1209 |
| 0.5876        | 42.83 | 41500 | 0.1567          | 0.1211 |
| 0.5714        | 43.34 | 42000 | 0.1532          | 0.1217 |
| 0.5756        | 43.86 | 42500 | 0.1516          | 0.1196 |
| 0.5719        | 44.38 | 43000 | 0.1491          | 0.1191 |
| 0.5829        | 44.89 | 43500 | 0.1497          | 0.1193 |
| 0.5664        | 45.41 | 44000 | 0.1487          | 0.1173 |
| 0.5707        | 45.92 | 44500 | 0.1470          | 0.1164 |
| 0.5696        | 46.44 | 45000 | 0.1479          | 0.1161 |
| 0.5767        | 46.96 | 45500 | 0.1492          | 0.1175 |
| 0.5573        | 47.47 | 46000 | 0.1471          | 0.1165 |
| 0.5625        | 47.99 | 46500 | 0.1484          | 0.1168 |
| 0.5671        | 48.5  | 47000 | 0.1474          | 0.1162 |
| 0.5484        | 49.02 | 47500 | 0.1479          | 0.1158 |
| 0.555         | 49.54 | 48000 | 0.1477          | 0.1157 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0
