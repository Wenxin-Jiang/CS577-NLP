---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: convnext-tiny-224_finetuned_on_unlabelled_IA_with_snorkel_labels
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# convnext-tiny-224_finetuned_on_unlabelled_IA_with_snorkel_labels

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4381
- Precision: 0.8239
- Recall: 0.7919
- F1: 0.8058
- Accuracy: 0.8629

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 256
- eval_batch_size: 256
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 112  | 0.5589          | 0.7547    | 0.5380 | 0.5097 | 0.7679   |
| No log        | 2.0   | 224  | 0.5578          | 0.7691    | 0.5387 | 0.5103 | 0.7690   |
| No log        | 3.0   | 336  | 0.4812          | 0.8513    | 0.7371 | 0.7709 | 0.8555   |
| No log        | 4.0   | 448  | 0.4387          | 0.8734    | 0.6539 | 0.6835 | 0.8259   |
| 0.482         | 5.0   | 560  | 0.4427          | 0.8322    | 0.6250 | 0.6449 | 0.8085   |
| 0.482         | 6.0   | 672  | 0.6234          | 0.8219    | 0.5702 | 0.5635 | 0.7848   |
| 0.482         | 7.0   | 784  | 0.6187          | 0.8791    | 0.6070 | 0.6196 | 0.8054   |
| 0.482         | 8.0   | 896  | 0.3953          | 0.8683    | 0.7134 | 0.7507 | 0.8502   |
| 0.3656        | 9.0   | 1008 | 0.4381          | 0.8239    | 0.7919 | 0.8058 | 0.8629   |
| 0.3656        | 10.0  | 1120 | 0.5346          | 0.7794    | 0.7900 | 0.7844 | 0.8370   |
| 0.3656        | 11.0  | 1232 | 0.3685          | 0.8678    | 0.7600 | 0.7943 | 0.8681   |
| 0.3656        | 12.0  | 1344 | 0.6900          | 0.6244    | 0.6667 | 0.6099 | 0.6435   |
| 0.3656        | 13.0  | 1456 | 0.6097          | 0.6832    | 0.7149 | 0.6931 | 0.7511   |
| 0.2987        | 14.0  | 1568 | 0.5435          | 0.8746    | 0.6754 | 0.7096 | 0.8354   |
| 0.2987        | 15.0  | 1680 | 0.5525          | 0.7277    | 0.7690 | 0.7411 | 0.7890   |
| 0.2987        | 16.0  | 1792 | 0.5003          | 0.8086    | 0.7694 | 0.7856 | 0.8507   |
| 0.2987        | 17.0  | 1904 | 0.8172          | 0.6183    | 0.6576 | 0.6074 | 0.6450   |
| 0.2598        | 18.0  | 2016 | 0.6102          | 0.6977    | 0.7489 | 0.7070 | 0.75     |
| 0.2598        | 19.0  | 2128 | 0.4260          | 0.8523    | 0.7497 | 0.7822 | 0.8602   |
| 0.2598        | 20.0  | 2240 | 0.5503          | 0.8276    | 0.6770 | 0.7079 | 0.8281   |
| 0.2598        | 21.0  | 2352 | 0.4574          | 0.7994    | 0.7785 | 0.7879 | 0.8481   |
| 0.2598        | 22.0  | 2464 | 0.6307          | 0.8620    | 0.6353 | 0.6592 | 0.8165   |
| 0.2111        | 23.0  | 2576 | 0.4605          | 0.8196    | 0.7697 | 0.7894 | 0.8555   |
| 0.2111        | 24.0  | 2688 | 0.5290          | 0.8152    | 0.7320 | 0.7592 | 0.8434   |
| 0.2111        | 25.0  | 2800 | 0.4754          | 0.8755    | 0.7216 | 0.7599 | 0.8550   |
| 0.2111        | 26.0  | 2912 | 0.5161          | 0.8428    | 0.7436 | 0.7750 | 0.8555   |
| 0.1638        | 27.0  | 3024 | 0.5753          | 0.7358    | 0.7278 | 0.7316 | 0.8043   |
| 0.1638        | 28.0  | 3136 | 0.6403          | 0.8468    | 0.7016 | 0.7360 | 0.8412   |
| 0.1638        | 29.0  | 3248 | 0.5418          | 0.7912    | 0.7473 | 0.7647 | 0.8381   |
| 0.1638        | 30.0  | 3360 | 0.5651          | 0.8240    | 0.7315 | 0.7607 | 0.8460   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.0
- Tokenizers 0.13.1
