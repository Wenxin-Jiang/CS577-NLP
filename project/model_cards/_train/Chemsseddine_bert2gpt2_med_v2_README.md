---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bert2gpt2_med_v2 
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

<img src="https://huggingface.co/Chemsseddine/bert2gpt2_med_ml_orange_summ-finetuned_med_sum_new-finetuned_med_sum_new/resolve/main/logobert2gpt2.png" alt="Map of positive probabilities per country." width="200"/>

# bert2gpt2_med_v2 

This model is a fine-tuned version of [Chemsseddine/bert2gpt2SUMM-finetuned-mlsum-finetuned-mlorange_sum](https://huggingface.co/Chemsseddine/bert2gpt2SUMM-finetuned-mlsum-finetuned-mlorange_sum) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0684
- Rouge1: 34.1248
- Rouge2: 17.7006
- Rougel: 33.4661
- Rougelsum: 33.4419
- Gen Len: 22.6429

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.9107        | 1.0   | 1000  | 2.0877          | 30.4547 | 14.4024 | 30.3642 | 30.3788   | 21.9714 |
| 1.8782        | 2.0   | 2000  | 1.8151          | 32.6607 | 16.8089 | 32.3844 | 32.4762   | 21.7714 |
| 1.291         | 3.0   | 3000  | 1.7523          | 33.6391 | 16.7866 | 32.4256 | 32.3306   | 22.7429 |
| 0.819         | 4.0   | 4000  | 1.7650          | 35.0633 | 19.1222 | 34.4902 | 34.6796   | 22.4714 |
| 0.4857        | 5.0   | 5000  | 1.8129          | 33.8763 | 16.9303 | 32.8845 | 32.9225   | 22.3857 |
| 0.3232        | 6.0   | 6000  | 1.9339          | 33.9272 | 17.1784 | 32.9301 | 33.0253   | 22.4286 |
| 0.2022        | 7.0   | 7000  | 1.9634          | 33.9869 | 16.4238 | 33.7336 | 33.65     | 22.6429 |
| 0.1452        | 8.0   | 8000  | 2.0090          | 33.8892 | 18.2723 | 33.7514 | 33.6531   | 22.5714 |
| 0.0845        | 9.0   | 9000  | 2.0337          | 33.9649 | 17.1339 | 33.5061 | 33.4157   | 22.7857 |
| 0.0531        | 10.0  | 10000 | 2.0684          | 34.1248 | 17.7006 | 33.4661 | 33.4419   | 22.6429 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
