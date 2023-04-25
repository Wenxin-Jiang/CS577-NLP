---
library_name: keras
tags:
- image-classification
- keras

---

## Model description

It's pretty simple, the model tries to differentiate between dogs/cats. 

## Intended uses & limitations

Only JPGs can be used and they are auto resized. **Meant for dogs and cats only.**

## Training and evaluation data

Combined training data from multiple sources. Downloaded around 3000 cat and dog photos from r/dogs and r/cats. Curated kaggle datasets into one large dataset. 

## Training procedure
Trained using an early stopping for overfitting

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': 0.001, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32
