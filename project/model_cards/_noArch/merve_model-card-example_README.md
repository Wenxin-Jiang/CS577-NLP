---
tags:
- object-detection
library_name: keras
---

## Model description

This model has couple of Dense layers.

## Intended uses & limitations

It's intended to demonstrate capabilities of Hub for Keras on my blog post!

## Training and evaluation data

It's trained on dummy data. 

Above information is filled manually.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': 0.001, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

 ## Training Metrics
| Epochs | Train Loss | Validation Loss |
 |--- |--- |--- |
| 1| 0.102|  0.094| 
| 2| 0.094|  0.092| 
| 3| 0.092|  0.091| 
| 4| 0.091|  0.09| 
| 5| 0.09|  0.089| 
 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>