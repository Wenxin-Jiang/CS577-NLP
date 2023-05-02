---
license: mit
tags:
- generated_from_trainer
model-index:
- name: ds9_all
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ds9_all

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.4079

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.372e-07
- train_batch_size: 1
- eval_batch_size: 1
- seed: 3138344630
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10
- num_epochs: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.1261        | 13.0  | 8619  | 3.4600          |
| 1.141         | 14.0  | 9282  | 3.4634          |
| 1.1278        | 15.0  | 9945  | 3.4665          |
| 1.1183        | 16.0  | 10608 | 3.4697          |
| 1.1048        | 17.0  | 11271 | 3.4714          |
| 1.1061        | 18.0  | 11934 | 3.4752          |
| 1.1471        | 19.0  | 12597 | 3.4773          |
| 1.1402        | 20.0  | 13260 | 3.4798          |
| 1.0847        | 21.0  | 13923 | 3.4811          |
| 1.1462        | 22.0  | 14586 | 3.4841          |
| 1.1107        | 23.0  | 15249 | 3.4852          |
| 1.1192        | 24.0  | 15912 | 3.4873          |
| 1.0868        | 25.0  | 16575 | 3.4879          |
| 1.1313        | 26.0  | 17238 | 3.4898          |
| 1.1033        | 27.0  | 17901 | 3.4915          |
| 1.1578        | 28.0  | 18564 | 3.4939          |
| 1.0987        | 29.0  | 19227 | 3.4947          |
| 1.0779        | 30.0  | 19890 | 3.4972          |
| 1.3567        | 61.0  | 20191 | 3.4576          |
| 1.3278        | 62.0  | 20522 | 3.4528          |
| 1.3292        | 63.0  | 20853 | 3.4468          |
| 1.3285        | 64.0  | 21184 | 3.4431          |
| 1.3032        | 65.0  | 21515 | 3.4370          |
| 1.318         | 66.0  | 21846 | 3.4345          |
| 1.3003        | 67.0  | 22177 | 3.4289          |
| 1.3202        | 68.0  | 22508 | 3.4274          |
| 1.2643        | 69.0  | 22839 | 3.4232          |
| 1.2862        | 70.0  | 23170 | 3.4223          |
| 1.2597        | 71.0  | 23501 | 3.4186          |
| 1.2426        | 72.0  | 23832 | 3.4176          |
| 1.2539        | 73.0  | 24163 | 3.4152          |
| 1.2604        | 74.0  | 24494 | 3.4147          |
| 1.263         | 75.0  | 24825 | 3.4128          |
| 1.2642        | 76.0  | 25156 | 3.4127          |
| 1.2694        | 77.0  | 25487 | 3.4109          |
| 1.2251        | 78.0  | 25818 | 3.4106          |
| 1.2673        | 79.0  | 26149 | 3.4097          |
| 1.233         | 80.0  | 26480 | 3.4096          |
| 1.2408        | 81.0  | 26811 | 3.4087          |
| 1.2579        | 82.0  | 27142 | 3.4088          |
| 1.2346        | 83.0  | 27473 | 3.4081          |
| 1.2298        | 84.0  | 27804 | 3.4082          |
| 1.219         | 85.0  | 28135 | 3.4079          |
| 1.2515        | 86.0  | 28466 | 3.4080          |
| 1.2316        | 87.0  | 28797 | 3.4084          |
| 1.2085        | 88.0  | 29128 | 3.4085          |
| 1.2334        | 89.0  | 29459 | 3.4085          |
| 1.2263        | 90.0  | 29790 | 3.4084          |
| 1.2312        | 91.0  | 30121 | 3.4084          |
| 1.2584        | 92.0  | 30452 | 3.4086          |
| 1.2106        | 93.0  | 30783 | 3.4089          |
| 1.2078        | 94.0  | 31114 | 3.4091          |
| 1.2329        | 95.0  | 31445 | 3.4090          |
| 1.1836        | 96.0  | 31776 | 3.4097          |
| 1.2135        | 97.0  | 32107 | 3.4097          |
| 1.2372        | 98.0  | 32438 | 3.4099          |
| 1.2163        | 99.0  | 32769 | 3.4107          |
| 1.1937        | 100.0 | 33100 | 3.4110          |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0+cu113
- Datasets 1.15.1
- Tokenizers 0.10.3
