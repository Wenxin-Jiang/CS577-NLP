---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1638
- Accuracy: 0.975

## Model description
The model Urdu audio and classify in following categories 
* Angry  
* Happy  
* Neutral  
* Sad  

## Training and evaluation data
The dataset is available at
https://www.kaggle.com/datasets/kingabzpro/urdu-emotion-dataset

## Training procedure
Training code is available at
https://www.kaggle.com/code/chtalhaanwar/urdu-emotions-hf

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.3838        | 1.0   | 10   | 1.3907          | 0.225    |
| 1.3732        | 2.0   | 20   | 1.3872          | 0.2125   |
| 1.3354        | 3.0   | 30   | 1.3116          | 0.6625   |
| 1.2689        | 4.0   | 40   | 1.1820          | 0.6375   |
| 1.1179        | 5.0   | 50   | 1.0075          | 0.7      |
| 0.9962        | 6.0   | 60   | 0.8707          | 0.7125   |
| 0.8842        | 7.0   | 70   | 0.7485          | 0.7625   |
| 0.786         | 8.0   | 80   | 0.6326          | 0.8      |
| 0.6757        | 9.0   | 90   | 0.5995          | 0.8      |
| 0.6104        | 10.0  | 100  | 0.4835          | 0.825    |
| 0.5821        | 11.0  | 110  | 0.3886          | 0.9      |
| 0.4721        | 12.0  | 120  | 0.3935          | 0.8625   |
| 0.3976        | 13.0  | 130  | 0.3020          | 0.925    |
| 0.4483        | 14.0  | 140  | 0.3171          | 0.9      |
| 0.2665        | 15.0  | 150  | 0.3016          | 0.9125   |
| 0.2119        | 16.0  | 160  | 0.2722          | 0.925    |
| 0.3376        | 17.0  | 170  | 0.3163          | 0.8875   |
| 0.1518        | 18.0  | 180  | 0.2681          | 0.9125   |
| 0.1559        | 19.0  | 190  | 0.3074          | 0.925    |
| 0.1031        | 20.0  | 200  | 0.3526          | 0.8875   |
| 0.1557        | 21.0  | 210  | 0.2254          | 0.9375   |
| 0.0846        | 22.0  | 220  | 0.2410          | 0.9375   |
| 0.0733        | 23.0  | 230  | 0.2369          | 0.925    |
| 0.0964        | 24.0  | 240  | 0.2273          | 0.9375   |
| 0.0574        | 25.0  | 250  | 0.2066          | 0.95     |
| 0.1113        | 26.0  | 260  | 0.2941          | 0.9125   |
| 0.1313        | 27.0  | 270  | 0.2715          | 0.925    |
| 0.0851        | 28.0  | 280  | 0.1725          | 0.9625   |
| 0.0402        | 29.0  | 290  | 0.2221          | 0.95     |
| 0.1075        | 30.0  | 300  | 0.2199          | 0.9625   |
| 0.0418        | 31.0  | 310  | 0.1699          | 0.95     |
| 0.1869        | 32.0  | 320  | 0.2287          | 0.9625   |
| 0.0637        | 33.0  | 330  | 0.3230          | 0.9125   |
| 0.0483        | 34.0  | 340  | 0.1602          | 0.975    |
| 0.0891        | 35.0  | 350  | 0.1615          | 0.975    |
| 0.0359        | 36.0  | 360  | 0.1571          | 0.975    |
| 0.1006        | 37.0  | 370  | 0.1809          | 0.9625   |
| 0.0417        | 38.0  | 380  | 0.1923          | 0.9625   |
| 0.0346        | 39.0  | 390  | 0.2035          | 0.9625   |
| 0.0417        | 40.0  | 400  | 0.1737          | 0.9625   |
| 0.0396        | 41.0  | 410  | 0.1833          | 0.9625   |
| 0.0202        | 42.0  | 420  | 0.1946          | 0.9625   |
| 0.0137        | 43.0  | 430  | 0.1785          | 0.9625   |
| 0.0214        | 44.0  | 440  | 0.1841          | 0.9625   |
| 0.0304        | 45.0  | 450  | 0.1690          | 0.9625   |
| 0.0199        | 46.0  | 460  | 0.1646          | 0.975    |
| 0.0122        | 47.0  | 470  | 0.1622          | 0.975    |
| 0.0324        | 48.0  | 480  | 0.1615          | 0.975    |
| 0.0269        | 49.0  | 490  | 0.1625          | 0.975    |
| 0.0245        | 50.0  | 500  | 0.1638          | 0.975    |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
