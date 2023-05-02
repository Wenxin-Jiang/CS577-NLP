---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: MariaZafar/gpt2-finetuned-wikitext2
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# MariaZafar/gpt2-finetuned-wikitext2

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.7785
- Validation Loss: 3.7004
- Epoch: 49

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

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 5.8858     | 7.5655          | 0     |
| 4.0619     | 5.8193          | 1     |
| 3.3766     | 4.9585          | 2     |
| 3.0686     | 4.5764          | 3     |
| 2.9022     | 4.3847          | 4     |
| 2.7838     | 4.2249          | 5     |
| 2.6997     | 4.1060          | 6     |
| 2.6154     | 4.0100          | 7     |
| 2.5575     | 3.9412          | 8     |
| 2.4933     | 3.8447          | 9     |
| 2.4397     | 3.7619          | 10    |
| 2.3835     | 3.7510          | 11    |
| 2.3403     | 3.6810          | 12    |
| 2.2924     | 3.6716          | 13    |
| 2.2513     | 3.6335          | 14    |
| 2.2031     | 3.6208          | 15    |
| 2.1619     | 3.5915          | 16    |
| 2.1234     | 3.5497          | 17    |
| 2.0792     | 3.5540          | 18    |
| 2.0398     | 3.5461          | 19    |
| 1.9976     | 3.5282          | 20    |
| 1.9577     | 3.5260          | 21    |
| 1.9176     | 3.5041          | 22    |
| 1.8745     | 3.4994          | 23    |
| 1.8304     | 3.5250          | 24    |
| 1.7881     | 3.4864          | 25    |
| 1.7423     | 3.4718          | 26    |
| 1.6993     | 3.5194          | 27    |
| 1.6503     | 3.5019          | 28    |
| 1.6025     | 3.5055          | 29    |
| 1.5500     | 3.5109          | 30    |
| 1.4964     | 3.5389          | 31    |
| 1.4448     | 3.5393          | 32    |
| 1.3954     | 3.5363          | 33    |
| 1.3464     | 3.5446          | 34    |
| 1.2978     | 3.5117          | 35    |
| 1.2494     | 3.5225          | 36    |
| 1.2004     | 3.5443          | 37    |
| 1.1534     | 3.5909          | 38    |
| 1.1124     | 3.5380          | 39    |
| 1.0709     | 3.6162          | 40    |
| 1.0265     | 3.6758          | 41    |
| 0.9936     | 3.6168          | 42    |
| 0.9590     | 3.6243          | 43    |
| 0.9238     | 3.6308          | 44    |
| 0.8886     | 3.6429          | 45    |
| 0.8635     | 3.7137          | 46    |
| 0.8352     | 3.6512          | 47    |
| 0.8050     | 3.7033          | 48    |
| 0.7785     | 3.7004          | 49    |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.8.0
- Datasets 2.2.1
- Tokenizers 0.12.1
