---
tags:
- generated_from_trainer
model-index:
- name: torgo-TestedSpeakerM01-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# torgo-TestedSpeakerM01-finetuned

This model is a fine-tuned version of [yongjian/wav2vec2-large-a](https://huggingface.co/yongjian/wav2vec2-large-a) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3416
- Wer: 0.7714

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 28.3192       | 0.84  | 500   | 1.5650          | 1.1343 |
| 0.4741        | 1.69  | 1000  | 0.3845          | 1.2286 |
| 0.4324        | 2.53  | 1500  | 0.3041          | 1.2849 |
| 0.3128        | 3.37  | 2000  | 0.3093          | 1.3337 |
| 0.2875        | 4.22  | 2500  | 0.2870          | 1.1972 |
| 0.2763        | 5.06  | 3000  | 0.3064          | 1.0553 |
| 0.2719        | 5.9   | 3500  | 0.2424          | 0.9534 |
| 0.2436        | 6.75  | 4000  | 0.2772          | 1.0163 |
| 0.2262        | 7.59  | 4500  | 0.2532          | 0.9989 |
| 0.2248        | 8.43  | 5000  | 0.2495          | 0.9133 |
| 0.2267        | 9.27  | 5500  | 0.2771          | 0.9155 |
| 0.1923        | 10.12 | 6000  | 0.2918          | 0.8862 |
| 0.1905        | 10.96 | 6500  | 0.2306          | 0.8700 |
| 0.184         | 11.8  | 7000  | 0.2470          | 0.8949 |
| 0.1747        | 12.65 | 7500  | 0.2411          | 0.8256 |
| 0.1641        | 13.49 | 8000  | 0.3096          | 0.8949 |
| 0.1783        | 14.33 | 8500  | 0.2523          | 0.8776 |
| 0.1575        | 15.18 | 9000  | 0.2606          | 0.8223 |
| 0.1658        | 16.02 | 9500  | 0.2713          | 0.8364 |
| 0.141         | 16.86 | 10000 | 0.2423          | 0.8061 |
| 0.1302        | 17.71 | 10500 | 0.3030          | 0.7952 |
| 0.1285        | 18.55 | 11000 | 0.2719          | 0.7811 |
| 0.203         | 19.39 | 11500 | 0.3074          | 0.8061 |
| 0.1198        | 20.24 | 12000 | 0.3035          | 0.8017 |
| 0.109         | 21.08 | 12500 | 0.3218          | 0.8082 |
| 0.109         | 21.92 | 13000 | 0.3668          | 0.8202 |
| 0.1114        | 22.77 | 13500 | 0.2767          | 0.8007 |
| 0.0949        | 23.61 | 14000 | 0.2965          | 0.7844 |
| 0.0955        | 24.45 | 14500 | 0.3319          | 0.7692 |
| 0.0913        | 25.3  | 15000 | 0.3034          | 0.7833 |
| 0.0912        | 26.14 | 15500 | 0.2944          | 0.7736 |
| 0.0794        | 26.98 | 16000 | 0.3479          | 0.7736 |
| 0.0818        | 27.82 | 16500 | 0.3524          | 0.7790 |
| 0.0836        | 28.67 | 17000 | 0.3467          | 0.7714 |
| 0.0878        | 29.51 | 17500 | 0.3406          | 0.7746 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.13.2
