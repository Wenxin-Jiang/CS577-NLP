---
library_name: keras
tags:
- tabular-regression
- time-series
- anomaly-detection
---

## Timeseries anomaly detection using an Autoencoder

This repo contains the model and the notebook to this [Keras example on Timeseries anomaly detection using an Autoencoder.](https://keras.io/examples/timeseries/timeseries_anomaly_detection/)

Full credits to: [Pavithra Vijay](https://github.com/pavithrasv)


## Background and Datasets

This script demonstrates how you can use a reconstruction convolutional autoencoder model to detect anomalies in timeseries data. We will use the [Numenta Anomaly Benchmark(NAB)](https://www.kaggle.com/datasets/boltzmannbrain/nab) dataset. It provides artifical timeseries data containing labeled anomalous periods of behavior. Data are ordered, timestamped, single-valued metrics.



### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': 0.001, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

 ## Training Metrics

| Epochs | Train Loss | Validation Loss |
 |--- |--- |--- |
| 1| 0.011|  0.014| 
| 2| 0.011|  0.015| 
| 3| 0.01|  0.012| 
| 4| 0.01|  0.013| 
| 5| 0.01|  0.012| 
| 6| 0.009|  0.014| 
| 7| 0.009|  0.013| 
| 8| 0.009|  0.012| 
| 9| 0.009|  0.012| 
| 10| 0.009|  0.011| 
| 11| 0.008|  0.01| 
| 12| 0.008|  0.011| 
| 13| 0.008|  0.009| 
| 14| 0.008|  0.011| 
| 15| 0.008|  0.009| 
| 16| 0.008|  0.009| 
| 17| 0.008|  0.009| 
| 18| 0.007|  0.01| 
| 19| 0.007|  0.009| 
| 20| 0.007|  0.008| 
| 21| 0.007|  0.009| 
| 22| 0.007|  0.008| 
| 23| 0.007|  0.008| 
| 24| 0.007|  0.007| 
| 25| 0.007|  0.008| 
| 26| 0.006|  0.009| 
| 27| 0.006|  0.008| 
| 28| 0.006|  0.009| 
| 29| 0.006|  0.008| 
 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>