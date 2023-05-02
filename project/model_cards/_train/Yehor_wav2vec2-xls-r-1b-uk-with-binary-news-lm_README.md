---
language:
- uk
license: cc-by-nc-sa-4.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_7_0
- generated_from_trainer
- uk
xdatasets:
- mozilla-foundation/common_voice_7_0
---

# Ukrainian STT model (with the Big Language Model formed on News Dataset)

🇺🇦 Join Ukrainian Speech Recognition Community - https://t.me/speech_recognition_uk

⭐ See other Ukrainian models - https://github.com/egorsmkv/speech-recognition-uk

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - UK dataset.

Attribution to the dataset of Language Model:

- Chaplynskyi, D. et al. (2021) lang-uk Ukrainian Ubercorpus [Data set]. https://lang.org.ua/uk/corpora/#anchor4

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 20
- total_train_batch_size: 160
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 1.2815        | 7.93  | 500  | 0.3536          | 0.4753 | 0.1009 |
| 1.0869        | 15.86 | 1000 | 0.2317          | 0.3111 | 0.0614 |
| 0.9984        | 23.8  | 1500 | 0.2022          | 0.2676 | 0.0521 |
| 0.975         | 31.74 | 2000 | 0.1948          | 0.2469 | 0.0487 |
| 0.9306        | 39.67 | 2500 | 0.1916          | 0.2377 | 0.0464 |
| 0.8868        | 47.61 | 3000 | 0.1903          | 0.2257 | 0.0439 |
| 0.8424        | 55.55 | 3500 | 0.1786          | 0.2206 | 0.0423 |
| 0.8126        | 63.49 | 4000 | 0.1849          | 0.2160 | 0.0416 |
| 0.7901        | 71.42 | 4500 | 0.1869          | 0.2138 | 0.0413 |
| 0.7671        | 79.36 | 5000 | 0.1855          | 0.2075 | 0.0394 |
| 0.7467        | 87.3  | 5500 | 0.1884          | 0.2049 | 0.0389 |
| 0.731         | 95.24 | 6000 | 0.1877          | 0.2060 | 0.0387 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.18.1.dev0
- Tokenizers 0.11.0
