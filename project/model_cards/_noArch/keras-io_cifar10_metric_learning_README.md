---
library_name: keras
tags:
- image-classification
---

## Model description

Metric learning aims to measure the similarity among data samples and to learn embedding models. The motivation is to embed inputs in an embedding space such that similar images are close together in that space while dissimilar ones are far away.  

The model in this repo is an example which demonstrates the capabilities of metric learning to create embeddings. These embeddings are then used to perform Image Similarity Search. 

Full credits to [Mat Kelcey](https://twitter.com/mat_kelcey) for this work.

## Intended uses & limitations

More information needed

## Training and evaluation data

Trained and evaluated on [CIFAR-10](https://keras.io/api/datasets/cifar10/) dataset.

## Training procedure

### Training hyperparameters  
| name | learning_rate | decay | beta_1 | beta_2 | epsilon | amsgrad | training_precision |
|----|-------------|-----|------|------|-------|-------|------------------|
|Adam|0.0010000000474974513|0.0|0.8999999761581421|0.9990000128746033|1e-07|False|float32|

 ## Training Metrics

| Epochs | Train Loss |
 |--- |--- |
| 1| 2.248| 
| 2| 2.11| 
| 3| 2.042| 
| 4| 1.998| 
| 5| 1.957| 
| 6| 1.929| 
| 7| 1.897| 
| 8| 1.879| 
| 9| 1.844| 
| 10| 1.807| 
| 11| 1.799| 
| 12| 1.761| 
| 13| 1.762| 
| 14| 1.735| 
| 15| 1.713| 
| 16| 1.687| 
| 17| 1.669| 
| 18| 1.646| 
| 19| 1.633| 
| 20| 1.619| 
 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>