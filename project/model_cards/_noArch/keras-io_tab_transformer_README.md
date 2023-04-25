---
library_name: keras
tags:
- tabular-classification
- transformer
---


### Keras Implementation of Structured data learning with TabTransformer
This repo contains the trained model of [Structured data learning with TabTransformer](https://keras.io/examples/structured_data/tabtransformer/#define-dataset-metadata).
The full credit goes to: [Khalid Salama](https://www.linkedin.com/in/khalid-salama-24403144/)

Spaces Link: 

### Model summary:
- The trained model uses self-attention based Transformers structure following by multiple feed forward layers in order to serve supervised and semi-supervised learning.
- The model's inputs can contain both numerical and categorical features. 
- All the categorical features will be encoded into embedding vector with the same number of embedding dimensions, before adding (point-wise) with each other and feeding into a stack of Transformer blocks.
- The contextual embeddings of the categorical features after the final Transformer layer, are concatenated with the input numerical features, and fed into a final MLP block.
- A SoftMax function is applied at the end of the model.

## Intended uses & limitations:
- This model can be used for both supervised and semi-supervised tasks on tabular data.

## Training and evaluation data:
- This model was trained using the [United States Census Income Dataset](https://archive.ics.uci.edu/ml/datasets/census+income) provided by the UC Irvine Machine Learning Repository. The task of the dataset is to predict whether a person is likely to be making over USD 50,000 a year (binary classification).
- The dataset consists of 14 input features: 5 numerical features and 9 categorical features.

## Training procedure
### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: 'AdamW'
- learning_rate: 0.001
- weight decay: 1e-04
- loss: 'sparse_categorical_crossentropy'
- beta_1: 0.9
- beta_2: 0.999
- epsilon: 1e-07
- epochs: 50
- batch_size: 16
- training_precision: float32

 ## Training Metrics
Model history needed
 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>