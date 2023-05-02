---
tags:
- generated_from_trainer
model-index:
- name: exp12-reducedTorgoOnly-predComparison
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# exp12-reducedTorgoOnly-predComparison

This model is a fine-tuned version of [yongjian/wav2vec2-large-a](https://huggingface.co/yongjian/wav2vec2-large-a) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2016
- Wer: 1.0412

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
| 35.9644       | 0.92  | 500   | 3.6081          | 1.0084 |
| 3.2094        | 1.83  | 1000  | 2.7519          | 1.0    |
| 2.8848        | 2.75  | 1500  | 2.7494          | 1.0014 |
| 2.7505        | 3.66  | 2000  | 2.5622          | 1.2840 |
| 2.6354        | 4.58  | 2500  | 2.3878          | 1.2819 |
| 2.3473        | 5.49  | 3000  | 2.0214          | 1.2666 |
| 2.0339        | 6.41  | 3500  | 1.8040          | 1.2394 |
| 1.7779        | 7.33  | 4000  | 1.5898          | 1.2289 |
| 1.5254        | 8.24  | 4500  | 1.7275          | 1.2080 |
| 1.4553        | 9.16  | 5000  | 1.3815          | 1.1786 |
| 1.3222        | 10.07 | 5500  | 1.3647          | 1.1835 |
| 1.1964        | 10.99 | 6000  | 1.2442          | 1.1528 |
| 1.1169        | 11.9  | 6500  | 1.5896          | 1.2059 |
| 1.0342        | 12.82 | 7000  | 1.3880          | 1.1766 |
| 0.989         | 13.74 | 7500  | 1.2111          | 1.1396 |
| 0.9109        | 14.65 | 8000  | 1.3362          | 1.1137 |
| 0.8875        | 15.57 | 8500  | 1.2594          | 1.1326 |
| 0.8053        | 16.48 | 9000  | 1.1858          | 1.1242 |
| 0.7566        | 17.4  | 9500  | 1.1987          | 1.1117 |
| 0.7284        | 18.32 | 10000 | 1.2963          | 1.0998 |
| 0.7345        | 19.23 | 10500 | 1.1835          | 1.0865 |
| 0.6424        | 20.15 | 11000 | 1.1564          | 1.0907 |
| 0.6323        | 21.06 | 11500 | 1.2123          | 1.0851 |
| 0.5871        | 21.98 | 12000 | 1.2736          | 1.0691 |
| 0.5788        | 22.89 | 12500 | 1.2094          | 1.0768 |
| 0.5368        | 23.81 | 13000 | 1.1626          | 1.0398 |
| 0.5357        | 24.73 | 13500 | 1.1960          | 1.0607 |
| 0.5407        | 25.64 | 14000 | 1.1724          | 1.0586 |
| 0.491         | 26.56 | 14500 | 1.1877          | 1.0426 |
| 0.4866        | 27.47 | 15000 | 1.2227          | 1.0593 |
| 0.5011        | 28.39 | 15500 | 1.2033          | 1.0440 |
| 0.4634        | 29.3  | 16000 | 1.2016          | 1.0412 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.13.2
