---
tags:
- generated_from_trainer
model-index:
- name: DNADebertaSentencepiece10k_continuation_continuation_continuation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DNADebertaSentencepiece10k_continuation_continuation_continuation

This model is a fine-tuned version of [Vlasta/DNADebertaSentencepiece10k_continuation_continuation](https://huggingface.co/Vlasta/DNADebertaSentencepiece10k_continuation_continuation) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 5.2605

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 5.4076        | 0.36  | 5000   | 5.3702          |
| 5.4146        | 0.72  | 10000  | 5.3677          |
| 5.4119        | 1.08  | 15000  | 5.3661          |
| 5.4093        | 1.45  | 20000  | 5.3577          |
| 5.4055        | 1.81  | 25000  | 5.3574          |
| 5.3987        | 2.17  | 30000  | 5.3539          |
| 5.3974        | 2.53  | 35000  | 5.3509          |
| 5.3931        | 2.89  | 40000  | 5.3431          |
| 5.387         | 3.25  | 45000  | 5.3447          |
| 5.3868        | 3.61  | 50000  | 5.3404          |
| 5.3874        | 3.97  | 55000  | 5.3362          |
| 5.3797        | 4.34  | 60000  | 5.3275          |
| 5.3775        | 4.7   | 65000  | 5.3316          |
| 5.3737        | 5.06  | 70000  | 5.3245          |
| 5.367         | 5.42  | 75000  | 5.3228          |
| 5.3679        | 5.78  | 80000  | 5.3193          |
| 5.3648        | 6.14  | 85000  | 5.3185          |
| 5.3586        | 6.5   | 90000  | 5.3149          |
| 5.361         | 6.86  | 95000  | 5.3086          |
| 5.3572        | 7.23  | 100000 | 5.3080          |
| 5.3521        | 7.59  | 105000 | 5.3057          |
| 5.3516        | 7.95  | 110000 | 5.3020          |
| 5.3481        | 8.31  | 115000 | 5.2997          |
| 5.3453        | 8.67  | 120000 | 5.2990          |
| 5.3446        | 9.03  | 125000 | 5.2951          |
| 5.3418        | 9.39  | 130000 | 5.2888          |
| 5.3341        | 9.75  | 135000 | 5.2860          |
| 5.3371        | 10.12 | 140000 | 5.2879          |
| 5.3319        | 10.48 | 145000 | 5.2845          |
| 5.3316        | 10.84 | 150000 | 5.2822          |
| 5.3306        | 11.2  | 155000 | 5.2803          |
| 5.3272        | 11.56 | 160000 | 5.2743          |
| 5.3224        | 11.92 | 165000 | 5.2724          |
| 5.3224        | 12.28 | 170000 | 5.2726          |
| 5.3217        | 12.64 | 175000 | 5.2712          |
| 5.3167        | 13.01 | 180000 | 5.2663          |
| 5.3148        | 13.37 | 185000 | 5.2659          |
| 5.3154        | 13.73 | 190000 | 5.2624          |
| 5.3119        | 14.09 | 195000 | 5.2627          |
| 5.3122        | 14.45 | 200000 | 5.2599          |
| 5.3091        | 14.81 | 205000 | 5.2586          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0
- Datasets 2.2.2
- Tokenizers 0.12.1
