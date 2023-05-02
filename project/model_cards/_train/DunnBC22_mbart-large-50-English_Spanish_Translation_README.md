---
license: mit
tags:
- translation
- generated_from_trainer
metrics:
- bleu
- rouge
model-index:
- name: mbart-large-50-English_Spanish_Translation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart-large-50-English_Spanish_Translation

This model is a fine-tuned version of [facebook/mbart-large-50](https://huggingface.co/facebook/mbart-large-50) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0290
- Bleu: 41.4437
- Rouge: {'rouge1': 0.6751402780531002, 'rouge2': 0.49769602014143044, 'rougeL': 0.6371513427059108, 'rougeLsum': 0.6376403149816605}
- Meteor: {'meteor': 0.6479226630466496}

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Rouge                                                                                                                        | Meteor                         |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:----------------------------------------------------------------------------------------------------------------------------:|:------------------------------:|
| 1.5608        | 1.0   | 900  | 1.0899          | 39.9184 | {'rouge1': 0.6645461901016299, 'rouge2': 0.48457734138815345, 'rougeL': 0.6254335531454508, 'rougeLsum': 0.6258737583448748} | {'meteor': 0.6376166612731494} |
| 0.9734        | 2.0   | 1800 | 1.0290          | 41.4436 | {'rouge1': 0.6751348620702116, 'rouge2': 0.4976855704059807, 'rougeL': 0.6371345376462452, 'rougeLsum': 0.6376186633843448}  | {'meteor': 0.6479188510808377} |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1
- Datasets 2.5.2
- Tokenizers 0.12.1
