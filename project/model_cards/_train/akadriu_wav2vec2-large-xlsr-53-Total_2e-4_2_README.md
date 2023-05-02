---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-53-Total_2e-4_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-53-Total_2e-4_2

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2733
- Wer: 0.2116

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 5.2741        | 0.1   | 200   | 2.9070          | 0.9707 |
| 2.034         | 0.2   | 400   | 0.7240          | 0.6798 |
| 1.0037        | 0.3   | 600   | 0.5651          | 0.5368 |
| 0.8834        | 0.4   | 800   | 0.4709          | 0.4669 |
| 0.7973        | 0.5   | 1000  | 0.4305          | 0.4261 |
| 0.7489        | 0.6   | 1200  | 0.4017          | 0.3763 |
| 0.7507        | 0.7   | 1400  | 0.3662          | 0.3481 |
| 0.7108        | 0.8   | 1600  | 0.3604          | 0.3513 |
| 0.7151        | 0.9   | 1800  | 0.3563          | 0.3406 |
| 0.6755        | 1.0   | 2000  | 0.3365          | 0.3210 |
| 0.6038        | 1.1   | 2200  | 0.3394          | 0.3053 |
| 0.6109        | 1.2   | 2400  | 0.3179          | 0.2844 |
| 0.5999        | 1.3   | 2600  | 0.3166          | 0.2773 |
| 0.6291        | 1.4   | 2800  | 0.3134          | 0.2733 |
| 0.626         | 1.5   | 3000  | 0.3060          | 0.2690 |
| 0.6188        | 1.6   | 3200  | 0.3038          | 0.2644 |
| 0.5757        | 1.7   | 3400  | 0.3015          | 0.2566 |
| 0.5943        | 1.8   | 3600  | 0.2925          | 0.2494 |
| 0.6043        | 1.9   | 3800  | 0.2858          | 0.2491 |
| 0.5874        | 2.0   | 4000  | 0.2874          | 0.2452 |
| 0.5263        | 2.1   | 4200  | 0.2800          | 0.2364 |
| 0.5282        | 2.2   | 4400  | 0.2848          | 0.2387 |
| 0.4953        | 2.3   | 4600  | 0.2793          | 0.2360 |
| 0.5428        | 2.4   | 4800  | 0.2863          | 0.2414 |
| 0.5618        | 2.5   | 5000  | 0.2788          | 0.2350 |
| 0.5395        | 2.6   | 5200  | 0.2765          | 0.2325 |
| 0.5178        | 2.7   | 5400  | 0.2787          | 0.2351 |
| 0.5264        | 2.8   | 5600  | 0.2755          | 0.2312 |
| 0.5222        | 2.9   | 5800  | 0.2692          | 0.2258 |
| 0.5184        | 3.0   | 6000  | 0.2681          | 0.2242 |
| 0.4826        | 3.1   | 6200  | 0.2736          | 0.2224 |
| 0.479         | 3.2   | 6400  | 0.2896          | 0.2353 |
| 0.4938        | 3.3   | 6600  | 0.2744          | 0.2252 |
| 0.4772        | 3.4   | 6800  | 0.2735          | 0.2242 |
| 0.4831        | 3.5   | 7000  | 0.2721          | 0.2225 |
| 0.4869        | 3.6   | 7200  | 0.2710          | 0.2194 |
| 0.4515        | 3.7   | 7400  | 0.2692          | 0.2196 |
| 0.4732        | 3.8   | 7600  | 0.2729          | 0.2269 |
| 0.4683        | 3.9   | 7800  | 0.2713          | 0.2211 |
| 0.4674        | 4.0   | 8000  | 0.2642          | 0.2116 |
| 0.4239        | 4.1   | 8200  | 0.2773          | 0.2176 |
| 0.4306        | 4.2   | 8400  | 0.2779          | 0.2191 |
| 0.441         | 4.3   | 8600  | 0.2758          | 0.2136 |
| 0.4343        | 4.4   | 8800  | 0.2797          | 0.2203 |
| 0.4059        | 4.5   | 9000  | 0.2763          | 0.2159 |
| 0.4399        | 4.6   | 9200  | 0.2755          | 0.2123 |
| 0.4131        | 4.7   | 9400  | 0.2741          | 0.2124 |
| 0.4331        | 4.8   | 9600  | 0.2728          | 0.2101 |
| 0.4288        | 4.9   | 9800  | 0.2730          | 0.2110 |
| 0.4341        | 5.0   | 10000 | 0.2733          | 0.2116 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3
