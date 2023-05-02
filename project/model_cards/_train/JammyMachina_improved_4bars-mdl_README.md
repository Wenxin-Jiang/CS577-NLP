---
tags:
- generated_from_trainer
model-index:
- name: improved_4bars-mdl
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# improved_4bars-mdl

This model is a fine-tuned version of [JammyMachina/improved_4bars-mdl](https://huggingface.co/JammyMachina/improved_4bars-mdl) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8519

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 21
- eval_batch_size: 24
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.2574        | 0.1   | 1024  | 0.7889          |
| 0.2633        | 0.21  | 2048  | 0.7802          |
| 0.2635        | 0.31  | 3072  | 0.7877          |
| 0.2639        | 0.41  | 4096  | 0.7751          |
| 0.2625        | 0.52  | 5120  | 0.7836          |
| 0.2609        | 0.62  | 6144  | 0.7758          |
| 0.2597        | 0.73  | 7168  | 0.7923          |
| 0.2612        | 0.83  | 8192  | 0.8000          |
| 0.2612        | 0.93  | 9216  | 0.7935          |
| 0.2554        | 1.04  | 10240 | 0.7943          |
| 0.2524        | 1.14  | 11264 | 0.8015          |
| 0.2504        | 1.24  | 12288 | 0.7962          |
| 0.2524        | 1.35  | 13312 | 0.8086          |
| 0.2521        | 1.45  | 14336 | 0.8062          |
| 0.2503        | 1.55  | 15360 | 0.7998          |
| 0.2523        | 1.66  | 16384 | 0.8098          |
| 0.251         | 1.76  | 17408 | 0.8213          |
| 0.2509        | 1.86  | 18432 | 0.8138          |
| 0.2533        | 1.97  | 19456 | 0.8182          |
| 0.245         | 2.07  | 20480 | 0.8290          |
| 0.2432        | 2.18  | 21504 | 0.8328          |
| 0.2435        | 2.28  | 22528 | 0.8187          |
| 0.2423        | 2.38  | 23552 | 0.8238          |
| 0.2443        | 2.49  | 24576 | 0.8249          |
| 0.2431        | 2.59  | 25600 | 0.8253          |
| 0.2432        | 2.69  | 26624 | 0.8269          |
| 0.2421        | 2.8   | 27648 | 0.8282          |
| 0.2421        | 2.9   | 28672 | 0.8268          |
| 0.243         | 3.0   | 29696 | 0.8345          |
| 0.2367        | 3.11  | 30720 | 0.8424          |
| 0.237         | 3.21  | 31744 | 0.8374          |
| 0.2351        | 3.32  | 32768 | 0.8431          |
| 0.2374        | 3.42  | 33792 | 0.8425          |
| 0.2355        | 3.52  | 34816 | 0.8352          |
| 0.2373        | 3.63  | 35840 | 0.8452          |
| 0.2356        | 3.73  | 36864 | 0.8383          |
| 0.2343        | 3.83  | 37888 | 0.8444          |
| 0.2348        | 3.94  | 38912 | 0.8428          |
| 0.2349        | 4.04  | 39936 | 0.8480          |
| 0.2327        | 4.14  | 40960 | 0.8482          |
| 0.2337        | 4.25  | 41984 | 0.8510          |
| 0.2288        | 4.35  | 43008 | 0.8499          |
| 0.2299        | 4.45  | 44032 | 0.8522          |
| 0.2277        | 4.56  | 45056 | 0.8526          |
| 0.2301        | 4.66  | 46080 | 0.8518          |
| 0.2312        | 4.77  | 47104 | 0.8511          |
| 0.2284        | 4.87  | 48128 | 0.8507          |
| 0.2294        | 4.97  | 49152 | 0.8519          |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
