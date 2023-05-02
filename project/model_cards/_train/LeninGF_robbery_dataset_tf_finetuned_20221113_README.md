---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: robbery_dataset_tf_finetuned_20221113
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# robbery_dataset_tf_finetuned_20221113

This model is a fine-tuned version of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0506
- Train Sparse Categorical Accuracy: 0.9844
- Validation Loss: 0.4108
- Validation Sparse Categorical Accuracy: 0.9068
- Epoch: 9

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': 5e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Sparse Categorical Accuracy | Validation Loss | Validation Sparse Categorical Accuracy | Epoch |
|:----------:|:---------------------------------:|:---------------:|:--------------------------------------:|:-----:|
| 0.4908     | 0.8335                            | 0.2872          | 0.9060                                 | 0     |
| 0.2496     | 0.9180                            | 0.3137          | 0.8978                                 | 1     |
| 0.1947     | 0.9351                            | 0.3234          | 0.9062                                 | 2     |
| 0.1597     | 0.9483                            | 0.3092          | 0.9087                                 | 3     |
| 0.1304     | 0.9580                            | 0.2928          | 0.9140                                 | 4     |
| 0.1013     | 0.9684                            | 0.3450          | 0.9143                                 | 5     |
| 0.0785     | 0.9742                            | 0.3590          | 0.9080                                 | 6     |
| 0.0709     | 0.9778                            | 0.3711          | 0.9057                                 | 7     |
| 0.0541     | 0.9821                            | 0.4010          | 0.9128                                 | 8     |
| 0.0506     | 0.9844                            | 0.4108          | 0.9068                                 | 9     |


### Framework versions

- Transformers 4.24.0
- TensorFlow 2.9.2
- Datasets 2.6.1
- Tokenizers 0.13.2
