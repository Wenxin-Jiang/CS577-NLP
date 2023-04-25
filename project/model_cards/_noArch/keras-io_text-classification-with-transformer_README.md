---
library_name: keras
tags:
- text-classification
---

## Model description

Implement a Transformer block as a Keras layer and use it for text classification.

For details on the implementation, please see the original link on [keras](https://keras.io/examples/nlp/text_classification_with_transformer/)

Full credits to: [Apoorv Nandan](https://twitter.com/NandanApoorv)

## Training and evaluation data

The model is trained and evaluated on the IMDB dataset for sentiment analysis.

Details on the dataset can be found on [keras](https://keras.io/api/datasets/imdb/)

Note that the keras dataset is already tokenized, so the model doesn't have an associated tokenizer. Since the hosted text classification pipeline only accepts text as input, it is currently broken.

For a live demo of the model using my own tokenizer, please use the [space](https://huggingface.co/spaces/keras-io/text-classification-with-transformer)

### Training hyperparameters

The following hyperparameters were used during training:

| name | learning_rate | decay | beta_1 | beta_2 | epsilon | amsgrad | training_precision |
|----|-------------|-----|------|------|-------|-------|------------------|
|Adam|0.0010000000474974513|0.0|0.8999999761581421|0.9990000128746033|1e-07|False|float32|

 ## Training Metrics

| Epochs | Train Loss | Train Accuracy | Validation Loss | Validation Accuracy |
 |--- |--- |--- |--- |--- |
| 1| 0.385|  0.819|  0.298|  0.868| 
| 2| 0.198|  0.925|  0.333|  0.863| 
 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>