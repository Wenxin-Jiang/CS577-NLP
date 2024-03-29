---
tags:
- generated_from_keras_callback
model-index:
- name: VanessaSchenkel/padrao-unicamp-vanessa-finetuned-handscrafted
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# VanessaSchenkel/padrao-unicamp-vanessa-finetuned-handscrafted

This model is a fine-tuned version of [VanessaSchenkel/padrao-unicamp-finetuned-news_commentary](https://huggingface.co/VanessaSchenkel/padrao-unicamp-finetuned-news_commentary) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.8875
- Validation Loss: 0.5701
- Train Bleu: 70.9943
- Train Gen Len: 8.8125
- Epoch: 0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Bleu | Train Gen Len | Epoch |
|:----------:|:---------------:|:----------:|:-------------:|:-----:|
| 0.8875     | 0.5701          | 70.9943    | 8.8125        | 0     |


### Framework versions

- Transformers 4.21.3
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
