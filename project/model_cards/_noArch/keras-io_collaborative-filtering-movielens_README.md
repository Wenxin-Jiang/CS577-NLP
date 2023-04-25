---
library_name: keras
tags:
- collaborative-filtering
- recommender
- tabular-classification
license:
- cc0-1.0
---

## Model description

This repo contains the model and the notebook on [how to build and train a Keras model for Collaborative Filtering for Movie Recommendations](https://keras.io/examples/structured_data/collaborative_filtering_movielens/). 

Full credits to [Siddhartha Banerjee](https://twitter.com/sidd2006).

## Intended uses & limitations

Based on a user and movies they have rated highly in the past, this model outputs the predicted rating a user would give to a movie they haven't seen yet (between 0-1). This information can be used to find out the top recommended movies for this user.

## Training and evaluation data

The dataset consists of user's ratings on specific movies. It also consists of the movie's specific genres.

## Training procedure

The model was trained for 5 epochs with a batch size of 64.

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': 0.001, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

 ## Training Metrics

| Epochs | Train Loss | Validation Loss |
 |--- |--- |--- |
| 1| 0.637|  0.619| 
| 2| 0.614|  0.616| 
| 3| 0.609|  0.611| 
| 4| 0.608|  0.61| 
| 5| 0.608|  0.609| 
 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>