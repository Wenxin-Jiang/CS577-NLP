---
tags:
- generated_from_keras_callback
model-index:
- name: VanessaSchenkel/padrao-mbart-vanessa-finetuned-handscrafted-puro
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# VanessaSchenkel/padrao-mbart-vanessa-finetuned-handscrafted-puro

This model is a fine-tuned version of [Narrativa/mbart-large-50-finetuned-opus-en-pt-translation](https://huggingface.co/Narrativa/mbart-large-50-finetuned-opus-en-pt-translation) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.2001
- Validation Loss: 0.7276
- Train Bleu: 66.2393
- Train Gen Len: 11.75
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
| 2.2001     | 0.7276          | 66.2393    | 11.75         | 0     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.6.1
- Tokenizers 0.13.2
