---
tags:
- generated_from_trainer
model-index:
- name: elec-gmusic-familized-model-13-12__17-35-53
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# elec-gmusic-familized-model-13-12__17-35-53

This model is a fine-tuned version of [JammyMachina/elec-gmusic-familized-model-13-12__17-35-53](https://huggingface.co/JammyMachina/elec-gmusic-familized-model-13-12__17-35-53) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4303

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
- train_batch_size: 36
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.2509        | 0.1   | 1024  | 0.4268          |
| 0.2521        | 0.2   | 2048  | 0.4284          |
| 0.2533        | 0.3   | 3072  | 0.4219          |
| 0.2517        | 0.4   | 4096  | 0.4245          |
| 0.2512        | 0.5   | 5120  | 0.4229          |
| 0.2506        | 0.6   | 6144  | 0.4191          |
| 0.2512        | 0.71  | 7168  | 0.4247          |
| 0.2483        | 0.81  | 8192  | 0.4239          |
| 0.2479        | 0.91  | 9216  | 0.4259          |
| 0.2498        | 1.01  | 10240 | 0.4262          |
| 0.2467        | 1.11  | 11264 | 0.4267          |
| 0.2466        | 1.21  | 12288 | 0.4263          |
| 0.2449        | 1.31  | 13312 | 0.4251          |
| 0.2452        | 1.41  | 14336 | 0.4274          |
| 0.2449        | 1.51  | 15360 | 0.4263          |
| 0.2444        | 1.61  | 16384 | 0.4240          |
| 0.2428        | 1.71  | 17408 | 0.4289          |
| 0.2425        | 1.81  | 18432 | 0.4229          |
| 0.2424        | 1.91  | 19456 | 0.4291          |
| 0.2422        | 2.01  | 20480 | 0.4247          |
| 0.2397        | 2.12  | 21504 | 0.4271          |
| 0.2397        | 2.22  | 22528 | 0.4226          |
| 0.2411        | 2.32  | 23552 | 0.4269          |
| 0.2408        | 2.42  | 24576 | 0.4288          |
| 0.2392        | 2.52  | 25600 | 0.4223          |
| 0.2391        | 2.62  | 26624 | 0.4297          |
| 0.2385        | 2.72  | 27648 | 0.4253          |
| 0.2371        | 2.82  | 28672 | 0.4297          |
| 0.2373        | 2.92  | 29696 | 0.4232          |
| 0.2368        | 3.02  | 30720 | 0.4296          |
| 0.2355        | 3.12  | 31744 | 0.4327          |
| 0.2354        | 3.22  | 32768 | 0.4305          |
| 0.2345        | 3.32  | 33792 | 0.4286          |
| 0.2355        | 3.42  | 34816 | 0.4350          |
| 0.2353        | 3.53  | 35840 | 0.4269          |
| 0.2351        | 3.63  | 36864 | 0.4301          |
| 0.2336        | 3.73  | 37888 | 0.4301          |
| 0.2344        | 3.83  | 38912 | 0.4319          |
| 0.2339        | 3.93  | 39936 | 0.4305          |
| 0.2326        | 4.03  | 40960 | 0.4298          |
| 0.2316        | 4.13  | 41984 | 0.4308          |
| 0.2311        | 4.23  | 43008 | 0.4330          |
| 0.2315        | 4.33  | 44032 | 0.4313          |
| 0.2305        | 4.43  | 45056 | 0.4319          |
| 0.2328        | 4.53  | 46080 | 0.4292          |
| 0.232         | 4.63  | 47104 | 0.4289          |
| 0.2309        | 4.73  | 48128 | 0.4303          |
| 0.23          | 4.83  | 49152 | 0.4317          |
| 0.2315        | 4.94  | 50176 | 0.4303          |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
