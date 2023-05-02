---
language: fr
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bert2gpt2_med_ml_orange_summ-finetuned_med_sum_new-finetuned_med_sum_new
  results: []
---
<img src="https://huggingface.co/Chemsseddine/bert2gpt2_med_ml_orange_summ-finetuned_med_sum_new-finetuned_med_sum_new/resolve/main/logobert2gpt2.png" alt="Map of positive probabilities per country." width="200"/>

# bert2gpt2SUMM-finetuned-mlsum

---
## This model is used for french summarization
- Problem type: Summarization
- Model ID: 980832493
- CO2 Emissions (in grams): 0.10685501288084795

This model is a fine-tuned version of [Chemsseddine/bert2gpt2SUMM](https://huggingface.co/Chemsseddine/bert2gpt2SUMM) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.03749418258667
- Rouge1: 28.8384
- Rouge2: 10.7511
- RougeL: 27.0842
- RougeLsum: 27.5118
- Gen Len: 22.0625


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 33199  | 4.03749       | 28.8384 | 10.7511 | 27.0842 | 27.5118   | 22.0625 |

