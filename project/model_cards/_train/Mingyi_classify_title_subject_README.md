---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: tmp6tsjsfbf
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# tmp6tsjsfbf

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0178
- Train Sparse Categorical Accuracy: 0.9962
- Epoch: 49

## Model description

This model classifies the title of a content (e.g., YouTube video, article, or podcast episode) into 1 of 8 subjects

0. art
1. personal development
2. world
3. health
4. science
5. business
6. humanities
7. technology.

This model is used to support [Sanderling](https://sanderling.app)

## Intended uses & limitations

More information needed

## Training and evaluation data

We used 1.5k labeled titles to train the model. Majority of the training dataset are English titles. The rest are Chinese titles.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': 5e-06, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Sparse Categorical Accuracy | Epoch |
|:----------:|:---------------------------------:|:-----:|
| 1.8005     | 0.3956                            | 0     |
| 1.3302     | 0.5916                            | 1     |
| 0.8998     | 0.7575                            | 2     |
| 0.6268     | 0.8468                            | 3     |
| 0.4239     | 0.9062                            | 4     |
| 0.2982     | 0.9414                            | 5     |
| 0.2245     | 0.9625                            | 6     |
| 0.1678     | 0.9730                            | 7     |
| 0.1399     | 0.9745                            | 8     |
| 0.1059     | 0.9827                            | 9     |
| 0.0822     | 0.9850                            | 10    |
| 0.0601     | 0.9902                            | 11    |
| 0.0481     | 0.9932                            | 12    |
| 0.0386     | 0.9955                            | 13    |
| 0.0292     | 0.9977                            | 14    |
| 0.0353     | 0.9940                            | 15    |
| 0.0336     | 0.9932                            | 16    |
| 0.0345     | 0.9910                            | 17    |
| 0.0179     | 0.9985                            | 18    |
| 0.0150     | 0.9985                            | 19    |
| 0.0365     | 0.9895                            | 20    |
| 0.0431     | 0.9895                            | 21    |
| 0.0243     | 0.9955                            | 22    |
| 0.0317     | 0.9925                            | 23    |
| 0.0375     | 0.9902                            | 24    |
| 0.0138     | 0.9970                            | 25    |
| 0.0159     | 0.9977                            | 26    |
| 0.0160     | 0.9962                            | 27    |
| 0.0151     | 0.9977                            | 28    |
| 0.0337     | 0.9902                            | 29    |
| 0.0119     | 0.9977                            | 30    |
| 0.0165     | 0.9955                            | 31    |
| 0.0133     | 0.9977                            | 32    |
| 0.0047     | 1.0                               | 33    |
| 0.0037     | 1.0                               | 34    |
| 0.0033     | 1.0                               | 35    |
| 0.0031     | 1.0                               | 36    |
| 0.0036     | 1.0                               | 37    |
| 0.0343     | 0.9887                            | 38    |
| 0.0234     | 0.9962                            | 39    |
| 0.0034     | 1.0                               | 40    |
| 0.0036     | 1.0                               | 41    |
| 0.0261     | 0.9917                            | 42    |
| 0.0111     | 0.9970                            | 43    |
| 0.0039     | 1.0                               | 44    |
| 0.0214     | 0.9932                            | 45    |
| 0.0044     | 0.9985                            | 46    |
| 0.0122     | 0.9985                            | 47    |
| 0.0119     | 0.9962                            | 48    |
| 0.0178     | 0.9962                            | 49    |


### Framework versions

- Transformers 4.15.0
- TensorFlow 2.7.0
- Tokenizers 0.10.3
