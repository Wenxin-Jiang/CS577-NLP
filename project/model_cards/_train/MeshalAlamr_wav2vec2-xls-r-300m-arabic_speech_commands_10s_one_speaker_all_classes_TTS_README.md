---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-xls-r-300m-arabic_speech_commands_10s_one_speaker_all_classes_TTS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-arabic_speech_commands_10s_one_speaker_all_classes_TTS

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2062
- Accuracy: 0.9579

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 60

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 3.6865        | 0.99  | 34   | 3.6873          | 0.025    |
| 3.6155        | 1.99  | 68   | 3.4150          | 0.2188   |
| 2.6933        | 2.99  | 102  | 2.4527          | 0.4625   |
| 1.789         | 3.99  | 136  | 1.5249          | 0.7246   |
| 0.8812        | 4.99  | 170  | 0.7804          | 0.8708   |
| 0.4054        | 5.99  | 204  | 0.6304          | 0.8558   |
| 0.3481        | 6.99  | 238  | 0.5552          | 0.8667   |
| 0.238         | 7.99  | 272  | 0.4142          | 0.9113   |
| 0.1981        | 8.99  | 306  | 0.3007          | 0.9354   |
| 0.1254        | 9.99  | 340  | 0.2556          | 0.9479   |
| 0.1356        | 10.99 | 374  | 0.5148          | 0.8825   |
| 0.1263        | 11.99 | 408  | 0.3228          | 0.9308   |
| 0.1074        | 12.99 | 442  | 0.3085          | 0.9279   |
| 0.0756        | 13.99 | 476  | 0.4546          | 0.9029   |
| 0.0763        | 14.99 | 510  | 0.4045          | 0.9133   |
| 0.0902        | 15.99 | 544  | 0.3123          | 0.9287   |
| 0.1134        | 16.99 | 578  | 0.2054          | 0.9504   |
| 0.0943        | 17.99 | 612  | 0.2871          | 0.93     |
| 0.0511        | 18.99 | 646  | 0.3628          | 0.9292   |
| 0.0525        | 19.99 | 680  | 0.2228          | 0.9471   |
| 0.0769        | 20.99 | 714  | 0.3069          | 0.9329   |
| 0.0564        | 21.99 | 748  | 0.2658          | 0.9358   |
| 0.0319        | 22.99 | 782  | 0.2886          | 0.9387   |
| 0.0485        | 23.99 | 816  | 0.2342          | 0.9467   |
| 0.0542        | 24.99 | 850  | 0.3723          | 0.9287   |
| 0.0478        | 25.99 | 884  | 0.2890          | 0.9396   |
| 0.0373        | 26.99 | 918  | 0.2849          | 0.9383   |
| 0.0437        | 27.99 | 952  | 0.3886          | 0.9237   |
| 0.02          | 28.99 | 986  | 0.2672          | 0.9387   |
| 0.0379        | 29.99 | 1020 | 0.2946          | 0.9363   |
| 0.0253        | 30.99 | 1054 | 0.2499          | 0.9433   |
| 0.0256        | 31.99 | 1088 | 0.2967          | 0.9337   |
| 0.029         | 32.99 | 1122 | 0.2577          | 0.9458   |
| 0.0427        | 33.99 | 1156 | 0.2899          | 0.9396   |
| 0.0167        | 34.99 | 1190 | 0.2984          | 0.9437   |
| 0.0334        | 35.99 | 1224 | 0.4822          | 0.9175   |
| 0.0288        | 36.99 | 1258 | 0.2802          | 0.9417   |
| 0.017         | 37.99 | 1292 | 0.2233          | 0.9504   |
| 0.0064        | 38.99 | 1326 | 0.2657          | 0.9429   |
| 0.0176        | 39.99 | 1360 | 0.2062          | 0.9579   |
| 0.0307        | 40.99 | 1394 | 0.3633          | 0.9275   |
| 0.0208        | 41.99 | 1428 | 0.3059          | 0.9421   |
| 0.0091        | 42.99 | 1462 | 0.2488          | 0.9483   |
| 0.0121        | 43.99 | 1496 | 0.2397          | 0.9496   |
| 0.0106        | 44.99 | 1530 | 0.2958          | 0.9413   |
| 0.0176        | 45.99 | 1564 | 0.2243          | 0.9525   |
| 0.0153        | 46.99 | 1598 | 0.2293          | 0.9537   |
| 0.011         | 47.99 | 1632 | 0.2654          | 0.9496   |
| 0.0237        | 48.99 | 1666 | 0.2252          | 0.9533   |
| 0.0053        | 49.99 | 1700 | 0.2380          | 0.9483   |
| 0.0142        | 50.99 | 1734 | 0.2590          | 0.9467   |
| 0.0259        | 51.99 | 1768 | 0.2363          | 0.9508   |
| 0.0062        | 52.99 | 1802 | 0.2451          | 0.9496   |
| 0.0123        | 53.99 | 1836 | 0.2546          | 0.9479   |
| 0.011         | 54.99 | 1870 | 0.2578          | 0.9487   |
| 0.0143        | 55.99 | 1904 | 0.2770          | 0.945    |
| 0.015         | 56.99 | 1938 | 0.2869          | 0.9421   |
| 0.0099        | 57.99 | 1972 | 0.2922          | 0.9429   |
| 0.0086        | 58.99 | 2006 | 0.2783          | 0.9437   |
| 0.013         | 59.99 | 2040 | 0.2748          | 0.9433   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
