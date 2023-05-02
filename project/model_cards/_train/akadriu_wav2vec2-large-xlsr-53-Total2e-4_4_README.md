---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-53-Total2e-4_4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-53-Total2e-4_4

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2474
- Wer: 0.1951

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
| 5.5015        | 0.1   | 200   | 2.9261          | 0.9707 |
| 2.9197        | 0.2   | 400   | 2.7757          | 0.9707 |
| 1.7594        | 0.3   | 600   | 0.6117          | 0.5746 |
| 1.0908        | 0.4   | 800   | 0.4673          | 0.4530 |
| 0.9441        | 0.5   | 1000  | 0.4142          | 0.4010 |
| 0.8688        | 0.6   | 1200  | 0.3909          | 0.3675 |
| 0.849         | 0.7   | 1400  | 0.3649          | 0.3360 |
| 0.8223        | 0.8   | 1600  | 0.3532          | 0.3334 |
| 0.821         | 0.9   | 1800  | 0.3513          | 0.3185 |
| 0.7839        | 1.0   | 2000  | 0.3373          | 0.3039 |
| 0.714         | 1.1   | 2200  | 0.3210          | 0.2922 |
| 0.7129        | 1.2   | 2400  | 0.3216          | 0.2860 |
| 0.7076        | 1.3   | 2600  | 0.3279          | 0.2843 |
| 0.73          | 1.4   | 2800  | 0.3111          | 0.2662 |
| 0.7256        | 1.5   | 3000  | 0.3032          | 0.2625 |
| 0.72          | 1.6   | 3200  | 0.3066          | 0.2571 |
| 0.6754        | 1.7   | 3400  | 0.2999          | 0.2581 |
| 0.6859        | 1.8   | 3600  | 0.2935          | 0.2562 |
| 0.6966        | 1.9   | 3800  | 0.2858          | 0.2469 |
| 0.6791        | 2.0   | 4000  | 0.2857          | 0.2393 |
| 0.6412        | 2.1   | 4200  | 0.2815          | 0.2392 |
| 0.6356        | 2.2   | 4400  | 0.2836          | 0.2343 |
| 0.6048        | 2.3   | 4600  | 0.2824          | 0.2422 |
| 0.6473        | 2.4   | 4800  | 0.2805          | 0.2316 |
| 0.659         | 2.5   | 5000  | 0.2775          | 0.2262 |
| 0.6412        | 2.6   | 5200  | 0.2729          | 0.2249 |
| 0.6167        | 2.7   | 5400  | 0.2719          | 0.2227 |
| 0.6226        | 2.8   | 5600  | 0.2661          | 0.2193 |
| 0.6168        | 2.9   | 5800  | 0.2615          | 0.2172 |
| 0.6145        | 3.0   | 6000  | 0.2608          | 0.2148 |
| 0.593         | 3.1   | 6200  | 0.2643          | 0.2123 |
| 0.5919        | 3.2   | 6400  | 0.2617          | 0.2131 |
| 0.6115        | 3.3   | 6600  | 0.2589          | 0.2114 |
| 0.5859        | 3.4   | 6800  | 0.2591          | 0.2100 |
| 0.5919        | 3.5   | 7000  | 0.2564          | 0.2103 |
| 0.5873        | 3.6   | 7200  | 0.2572          | 0.2074 |
| 0.561         | 3.7   | 7400  | 0.2561          | 0.2056 |
| 0.5808        | 3.8   | 7600  | 0.2538          | 0.2062 |
| 0.5701        | 3.9   | 7800  | 0.2517          | 0.2029 |
| 0.5722        | 4.0   | 8000  | 0.2523          | 0.2007 |
| 0.5508        | 4.1   | 8200  | 0.2570          | 0.2023 |
| 0.5591        | 4.2   | 8400  | 0.2502          | 0.2029 |
| 0.5697        | 4.3   | 8600  | 0.2478          | 0.1991 |
| 0.5689        | 4.4   | 8800  | 0.2492          | 0.2021 |
| 0.5345        | 4.5   | 9000  | 0.2498          | 0.2005 |
| 0.5726        | 4.6   | 9200  | 0.2492          | 0.1983 |
| 0.5382        | 4.7   | 9400  | 0.2487          | 0.1974 |
| 0.5614        | 4.8   | 9600  | 0.2481          | 0.1957 |
| 0.5568        | 4.9   | 9800  | 0.2477          | 0.1955 |
| 0.5631        | 5.0   | 10000 | 0.2474          | 0.1951 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3
