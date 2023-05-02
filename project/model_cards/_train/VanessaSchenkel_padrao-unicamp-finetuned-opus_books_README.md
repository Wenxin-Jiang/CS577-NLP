---
tags:
- generated_from_keras_callback
model-index:
- name: VanessaSchenkel/padrao-unicamp-finetuned-opus_books
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# VanessaSchenkel/padrao-unicamp-finetuned-opus_books

This model is a fine-tuned version of [unicamp-dl/translation-en-pt-t5](https://huggingface.co/unicamp-dl/translation-en-pt-t5) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.2766
- Validation Loss: 2.0044
- Train Bleu: 20.1866
- Train Gen Len: 25.6491
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
| 2.2766     | 2.0044          | 20.1866    | 25.6491       | 0     |


### Framework versions

- Transformers 4.21.1
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1
