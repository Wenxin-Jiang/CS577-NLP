---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Manirathinam21/DistilBert_SMSSpam_classifier
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Manirathinam21/DistilBert_SMSSpam_classifier

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an SMSSpam Detection dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0114
- Train Accuracy: 0.9962
- Epoch: 2

## Target Labels

label: a classification label, with possible values including 
- Ham : 0 
- Spam : 1 

## Model description

Tokenizer used is DistilBertTokenizerFast  with return_tensors='tf' parameter in tokenizer because building model in a tensorflow framework

Model: TFDistilBertForSequenceClassification 
 
Optimizer: Adam with learning rate=5e-5

Loss: SparseCategoricalCrossentropy

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

After Tokenized, Encoded datasets are converted to Dataset Objects by using tf.data.Dataset.from_tensor_slices((dict(train_encoding),  train_y))

This step is done to inject a dataset into TFModel in a specific TF format

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': 5e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Epoch |
|:----------:|:--------------:|:-----:|
| 0.0754     | 0.9803         | 0     |
| 0.0252     | 0.9935         | 1     |
| 0.0114     | 0.9962         | 2     |


### Framework versions

- Transformers 4.21.1
- TensorFlow 2.8.2
- Tokenizers 0.12.1
