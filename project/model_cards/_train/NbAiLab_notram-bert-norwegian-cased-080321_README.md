---
language: no
license: cc-by-4.0
tags:
- norwegian
- bert
pipeline_tag: fill-mask
widget:
- text: På biblioteket kan du [MASK] en bok.
- text: Dette er et [MASK] eksempel.
- text: Av og til kan en språkmodell gi et [MASK] resultat. 
- text: Som ansat får du [MASK] for at bidrage til borgernes adgang til dansk kulturarv, til forskning og til samfundets demokratiske udvikling.
---

## Results
|**Model** | **NoRec** | **NorNe-NB**| **NorNe-NN** | **NorDial** | **DaNe** | **Da-Angry-Tweets** |
|:-----------|------------:|------------:|------------:|------------:|------------:|------------:|
|roberta-base (English) | 51.77 | 79.01/79.53| 79.79/83.02 |  67.18| 75.44/78.07 | 55.51 |
|mBERT-cased | 63.91 | 83.72/86.12| 83.05/87.12 |  66.23| 80.00/81.43 | 57.67 |
|nb-bert-base | 75.60 |**91.98**/**92.95** |**90.93**/**94.06**|69.39| 81.95/84.83| 64.18|
|notram-bert-norwegian-cased | 72.47 | 91.77/93.12|89.79/93.70| **78.55**| **83.69**/**86.55**| **64.19** |
|notram-bert-norwegian-uncased |  73.47 | 89.28/91.61 |87.23/90.23 |74.21 | 80.29/82.31| 61.18|
|notram-bert-norwegian-cased-pod | **76.18** | 91.24/92.24| 90.88/93.21| 76.21| 81.82/84.99| 62.16 |
|nb-roberta-base | 68.77 |87.99/89.43 | 85.43/88.66| 76.34| 75.91/77.94| 61.50 | 
|nb-roberta-base-scandinavian | 67.88 | 87.73/89.14| 87.39/90.92| 74.81| 76.22/78.66 | 63.37 |
|nb-roberta-base-v2-200k | 46.87 | 85.57/87.04| - |  64.99| - | - |
|test_long_w5 200k| 60.48  | 88.00/90:00 | 83.93/88.45 | 68.41 |75.22/78.50| 57.95 |
|test_long_w5_roberta_tokenizer 200k| 63.51| 86.28/87.77| 84.95/88.61 | 69.86 | 71.31/74.27 | 59.96 |
|test_long_w5_roberta_tokenizer 400k| 59.76 |87.39/89.06 | 85.16/89.01 | 71.46 | 72.39/75.65| 39.73 |
|test_long_w5_dataset 400k| 66.80 | 86.52/88.55 | 82.81/86.76 | 66.94 | 71.47/74.20| 55.25 |
|test_long_w5_dataset 600k| 67.37 | 89.98/90.95 | 84.53/88.37 | 66.84 | 75.14/76.50| 57.47 |
|roberta-jan-128_ncc - 400k - 128| 67.79 | 91.45/92.33 | 86.41/90.19 | 67.20 | 81.00/82.39| 59.65 |
|roberta-jan-128_ncc - 1000k - 128| 68.17 | 89.34/90.74 | 86.89/89.87 | 68.41 | 80.30/82.17| 61.63 |