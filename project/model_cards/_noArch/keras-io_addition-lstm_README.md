---
library_name: keras
tags:
- text-generation
---

## Model description

This repo contains the model which showcases the learning capabilities of LSTM using a simple example. A single-layer LSTM is made to learn to add two numbers, provided as strings. The model has been trained for adding two numbers where each number can have maximum of 5 digits.   

*Example:*
Input: "535+61"
Output: "596"

Full credits to [Smerity](https://twitter.com/Smerity) and others for this work.

## Intended uses & limitations

More information needed

## Training and evaluation data

The data consists of generation of two random 5 digit numbers as input and their sum as output. These numbers (_and their sum)_ are encoded and fed as input to LSTM. The full data creation code is available within the [example](https://keras.io/examples/nlp/addition_rnn/).

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 32
- optimizer: {'name': 'Adam', 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32
- num_epochs: 30

 ## Training Metrics

| Epochs | Train Loss | Train Accuracy | Validation Loss | Validation Accuracy |
 |--- |--- |--- |--- |--- |
| 1| 0.071|  0.977|  0.12|  0.957| 
| 2| 0.063|  0.98|  0.102|  0.963| 
| 3| 0.061|  0.98|  0.094|  0.967| 
| 4| 0.051|  0.983|  0.091|  0.969| 
| 5| 0.052|  0.983|  0.093|  0.964| 
| 6| 0.05|  0.983|  0.073|  0.975| 
| 7| 0.039|  0.988|  0.069|  0.976| 
| 8| 0.054|  0.983|  0.103|  0.965| 
| 9| 0.04|  0.987|  0.063|  0.977| 
| 10| 0.033|  0.99|  0.141|  0.953| 
| 11| 0.037|  0.989|  0.083|  0.971| 
| 12| 0.04|  0.987|  0.069|  0.976| 
| 13| 0.027|  0.992|  0.053|  0.98| 
| 14| 0.03|  0.991|  0.071|  0.974| 
| 15| 0.03|  0.991|  0.061|  0.979| 
| 16| 0.029|  0.991|  0.048|  0.982| 
| 17| 0.037|  0.989|  0.091|  0.97| 
| 18| 0.023|  0.993|  0.039|  0.987| 
| 19| 0.028|  0.991|  0.058|  0.981| 
| 20| 0.022|  0.994|  0.057|  0.98| 
| 21| 0.023|  0.993|  0.038|  0.987| 
| 22| 0.034|  0.99|  0.054|  0.982| 
| 23| 0.026|  0.993|  0.12|  0.959| 
| 24| 0.027|  0.992|  0.034|  0.989| 
| 25| 0.022|  0.993|  0.047|  0.984| 
| 26| 0.02|  0.994|  0.062|  0.978| 
| 27| 0.024|  0.993|  0.043|  0.985| 
| 28| 0.019|  0.994|  0.057|  0.979| 
| 29| 0.017|  0.995|  0.054|  0.982| 
| 30| 0.021|  0.994|  0.033|  0.989| 
 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>