---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: gpt2-ner-invoiceSenderRecipient_all_inv_03_01
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-ner-invoiceSenderRecipient_all_inv_03_01

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0307
- Precision: 0.7932
- Recall: 0.8488
- F1: 0.8201
- Accuracy: 0.9895

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0363        | 0.01  | 500   | 0.0338          | 0.7846    | 0.7969 | 0.7907 | 0.9884   |
| 0.0392        | 0.02  | 1000  | 0.0346          | 0.7665    | 0.8211 | 0.7929 | 0.9881   |
| 0.0363        | 0.04  | 1500  | 0.0347          | 0.7701    | 0.8075 | 0.7884 | 0.9880   |
| 0.0396        | 0.05  | 2000  | 0.0347          | 0.7454    | 0.8375 | 0.7888 | 0.9879   |
| 0.0366        | 0.06  | 2500  | 0.0350          | 0.7519    | 0.8345 | 0.7911 | 0.9879   |
| 0.0382        | 0.07  | 3000  | 0.0356          | 0.7500    | 0.8434 | 0.7939 | 0.9877   |
| 0.0424        | 0.09  | 3500  | 0.0358          | 0.7517    | 0.8287 | 0.7883 | 0.9877   |
| 0.0385        | 0.1   | 4000  | 0.0352          | 0.7605    | 0.8225 | 0.7903 | 0.9880   |
| 0.0382        | 0.11  | 4500  | 0.0361          | 0.7494    | 0.8159 | 0.7813 | 0.9874   |
| 0.0372        | 0.12  | 5000  | 0.0345          | 0.7817    | 0.8044 | 0.7929 | 0.9885   |
| 0.0377        | 0.14  | 5500  | 0.0346          | 0.7749    | 0.8238 | 0.7986 | 0.9884   |
| 0.0383        | 0.15  | 6000  | 0.0359          | 0.7568    | 0.8341 | 0.7936 | 0.9879   |
| 0.0372        | 0.16  | 6500  | 0.0356          | 0.7548    | 0.8356 | 0.7932 | 0.9879   |
| 0.0371        | 0.17  | 7000  | 0.0352          | 0.7540    | 0.8477 | 0.7981 | 0.9880   |
| 0.0368        | 0.19  | 7500  | 0.0349          | 0.7662    | 0.8310 | 0.7973 | 0.9881   |
| 0.0388        | 0.2   | 8000  | 0.0339          | 0.7648    | 0.8336 | 0.7977 | 0.9883   |
| 0.0368        | 0.21  | 8500  | 0.0336          | 0.7729    | 0.8305 | 0.8006 | 0.9886   |
| 0.0389        | 0.22  | 9000  | 0.0340          | 0.7750    | 0.8208 | 0.7972 | 0.9884   |
| 0.0384        | 0.24  | 9500  | 0.0349          | 0.7549    | 0.8499 | 0.7996 | 0.9880   |
| 0.0376        | 0.25  | 10000 | 0.0358          | 0.7531    | 0.8390 | 0.7938 | 0.9875   |
| 0.0354        | 0.26  | 10500 | 0.0346          | 0.7650    | 0.8318 | 0.7970 | 0.9882   |
| 0.0358        | 0.27  | 11000 | 0.0338          | 0.7694    | 0.8397 | 0.8030 | 0.9886   |
| 0.0389        | 0.28  | 11500 | 0.0341          | 0.7586    | 0.8502 | 0.8018 | 0.9882   |
| 0.0383        | 0.3   | 12000 | 0.0342          | 0.7688    | 0.8275 | 0.7971 | 0.9881   |
| 0.0355        | 0.31  | 12500 | 0.0337          | 0.7783    | 0.8281 | 0.8024 | 0.9885   |
| 0.0372        | 0.32  | 13000 | 0.0338          | 0.7703    | 0.8399 | 0.8036 | 0.9884   |
| 0.0369        | 0.33  | 13500 | 0.0331          | 0.7683    | 0.8427 | 0.8038 | 0.9886   |
| 0.0361        | 0.35  | 14000 | 0.0336          | 0.7699    | 0.8322 | 0.7999 | 0.9885   |
| 0.0361        | 0.36  | 14500 | 0.0336          | 0.7735    | 0.8390 | 0.8049 | 0.9885   |
| 0.0372        | 0.37  | 15000 | 0.0333          | 0.7747    | 0.8343 | 0.8034 | 0.9887   |
| 0.0366        | 0.38  | 15500 | 0.0343          | 0.7646    | 0.8468 | 0.8036 | 0.9883   |
| 0.0345        | 0.4   | 16000 | 0.0333          | 0.7790    | 0.8334 | 0.8053 | 0.9887   |
| 0.0363        | 0.41  | 16500 | 0.0329          | 0.7783    | 0.8301 | 0.8034 | 0.9887   |
| 0.0348        | 0.42  | 17000 | 0.0341          | 0.7626    | 0.8533 | 0.8054 | 0.9884   |
| 0.0391        | 0.43  | 17500 | 0.0324          | 0.7873    | 0.8295 | 0.8079 | 0.9889   |
| 0.0344        | 0.45  | 18000 | 0.0334          | 0.7769    | 0.8369 | 0.8058 | 0.9887   |
| 0.0378        | 0.46  | 18500 | 0.0337          | 0.7741    | 0.8394 | 0.8054 | 0.9886   |
| 0.035         | 0.47  | 19000 | 0.0328          | 0.7827    | 0.8323 | 0.8067 | 0.9888   |
| 0.0351        | 0.48  | 19500 | 0.0327          | 0.7815    | 0.8371 | 0.8083 | 0.9889   |
| 0.037         | 0.5   | 20000 | 0.0328          | 0.7793    | 0.8388 | 0.8079 | 0.9888   |
| 0.0346        | 0.51  | 20500 | 0.0325          | 0.7804    | 0.8416 | 0.8099 | 0.9890   |
| 0.0364        | 0.52  | 21000 | 0.0323          | 0.7861    | 0.8339 | 0.8093 | 0.9889   |
| 0.0356        | 0.53  | 21500 | 0.0327          | 0.7729    | 0.8510 | 0.8101 | 0.9889   |
| 0.0346        | 0.54  | 22000 | 0.0325          | 0.7791    | 0.8407 | 0.8087 | 0.9889   |
| 0.0342        | 0.56  | 22500 | 0.0334          | 0.7790    | 0.8443 | 0.8104 | 0.9889   |
| 0.0368        | 0.57  | 23000 | 0.0322          | 0.7869    | 0.8323 | 0.8089 | 0.9890   |
| 0.0371        | 0.58  | 23500 | 0.0320          | 0.7890    | 0.8356 | 0.8116 | 0.9891   |
| 0.0344        | 0.59  | 24000 | 0.0321          | 0.7910    | 0.8321 | 0.8110 | 0.9892   |
| 0.0342        | 0.61  | 24500 | 0.0319          | 0.7881    | 0.8356 | 0.8111 | 0.9892   |
| 0.0339        | 0.62  | 25000 | 0.0320          | 0.7889    | 0.8317 | 0.8097 | 0.9892   |
| 0.0347        | 0.63  | 25500 | 0.0316          | 0.7909    | 0.8347 | 0.8122 | 0.9892   |
| 0.034         | 0.64  | 26000 | 0.0318          | 0.7887    | 0.8324 | 0.8100 | 0.9891   |
| 0.0347        | 0.66  | 26500 | 0.0317          | 0.7791    | 0.8525 | 0.8141 | 0.9891   |
| 0.0345        | 0.67  | 27000 | 0.0318          | 0.7870    | 0.8384 | 0.8119 | 0.9892   |
| 0.0347        | 0.68  | 27500 | 0.0317          | 0.7903    | 0.8426 | 0.8157 | 0.9893   |
| 0.0371        | 0.69  | 28000 | 0.0311          | 0.7965    | 0.8332 | 0.8144 | 0.9894   |
| 0.0338        | 0.71  | 28500 | 0.0316          | 0.7863    | 0.8442 | 0.8142 | 0.9892   |
| 0.0352        | 0.72  | 29000 | 0.0315          | 0.7810    | 0.8537 | 0.8157 | 0.9892   |
| 0.0344        | 0.73  | 29500 | 0.0314          | 0.7953    | 0.8353 | 0.8148 | 0.9894   |
| 0.0322        | 0.74  | 30000 | 0.0320          | 0.7836    | 0.8449 | 0.8131 | 0.9891   |
| 0.0355        | 0.76  | 30500 | 0.0312          | 0.7877    | 0.8480 | 0.8167 | 0.9894   |
| 0.035         | 0.77  | 31000 | 0.0313          | 0.7864    | 0.8504 | 0.8171 | 0.9893   |
| 0.0346        | 0.78  | 31500 | 0.0310          | 0.7931    | 0.8424 | 0.8170 | 0.9895   |
| 0.0339        | 0.79  | 32000 | 0.0316          | 0.7857    | 0.8501 | 0.8166 | 0.9893   |
| 0.033         | 0.8   | 32500 | 0.0311          | 0.7975    | 0.8406 | 0.8185 | 0.9895   |
| 0.0337        | 0.82  | 33000 | 0.0314          | 0.7886    | 0.8457 | 0.8162 | 0.9894   |
| 0.0357        | 0.83  | 33500 | 0.0311          | 0.7923    | 0.8437 | 0.8172 | 0.9894   |
| 0.0348        | 0.84  | 34000 | 0.0312          | 0.7909    | 0.8490 | 0.8189 | 0.9894   |
| 0.0343        | 0.85  | 34500 | 0.0311          | 0.7856    | 0.8528 | 0.8179 | 0.9893   |
| 0.0323        | 0.87  | 35000 | 0.0311          | 0.7884    | 0.8505 | 0.8183 | 0.9894   |
| 0.0329        | 0.88  | 35500 | 0.0307          | 0.7981    | 0.8399 | 0.8185 | 0.9896   |
| 0.0324        | 0.89  | 36000 | 0.0313          | 0.7830    | 0.8576 | 0.8186 | 0.9893   |
| 0.0336        | 0.9   | 36500 | 0.0312          | 0.7836    | 0.8566 | 0.8185 | 0.9893   |
| 0.0327        | 0.92  | 37000 | 0.0309          | 0.7887    | 0.8501 | 0.8182 | 0.9895   |
| 0.0338        | 0.93  | 37500 | 0.0312          | 0.7887    | 0.8514 | 0.8188 | 0.9894   |
| 0.0327        | 0.94  | 38000 | 0.0311          | 0.7873    | 0.8534 | 0.8190 | 0.9894   |
| 0.0326        | 0.95  | 38500 | 0.0308          | 0.7953    | 0.8459 | 0.8198 | 0.9895   |
| 0.0338        | 0.97  | 39000 | 0.0307          | 0.7932    | 0.8488 | 0.8201 | 0.9895   |
| 0.0354        | 0.98  | 39500 | 0.0308          | 0.7916    | 0.8502 | 0.8198 | 0.9895   |
| 0.0313        | 0.99  | 40000 | 0.0309          | 0.7897    | 0.8523 | 0.8198 | 0.9895   |


### Framework versions

- Transformers 4.22.0
- Pytorch 1.10.0
- Tokenizers 0.12.1
