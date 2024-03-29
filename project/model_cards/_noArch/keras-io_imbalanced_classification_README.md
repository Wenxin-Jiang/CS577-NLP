---
library_name: keras
tags:
- tabular-classification
- imbalanced-classification
---

## Model Description
### Keras Implementation of Imbalanced classification: credit card fraud detection
This repo contains the trained model of [Imbalanced classification: credit card fraud detection](https://keras.io/examples/structured_data/imbalanced_classification/).
The full credit goes to: [fchollet](https://twitter.com/fchollet)

## Intended uses & limitations
- The trained model is used to detect of a specific transaction is fraudulent or not.

## Training dataset
- [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Due to the high imbalance of the target feature (417 frauds or 0.18% of total 284,807 samples), training weight was applied to reduce the False Negatives to the lowest level as possible.

## Training procedure
### Training hyperparameter 
The following hyperparameters were used during training:
- optimizer: 'Adam'
- learning_rate: 0.01
- loss: 'binary_crossentropy'
- epochs: 30
- batch_size: 2048
- beta_1: 0.9
- beta_2: 0.999
- epsilon: 1e-07
- training_precision: float32

 ## Training Metrics

| Epochs | Train Loss | Train Fn | Train Fp | Train Tn | Train Tp | Train Precision | Train Recall | Validation Loss | Validation Fn | Validation Fp | Validation Tn | Validation Tp | Validation Precision | Validation Recall |
 |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 1| 0.0|  14.0|  6202.0|  221227.0|  403.0|  0.061|  0.966|  0.043|  9.0|  622.0|  56264.0|  66.0|  0.096|  0.88| 
| 2| 0.0|  3.0|  3514.0|  223915.0|  414.0|  0.105|  0.993|  0.025|  10.0|  528.0|  56358.0|  65.0|  0.11|  0.867| 
| 3| 0.0|  2.0|  2419.0|  225010.0|  415.0|  0.146|  0.995|  0.014|  11.0|  283.0|  56603.0|  64.0|  0.184|  0.853| 
| 4| 0.0|  3.0|  2482.0|  224947.0|  414.0|  0.143|  0.993|  0.027|  11.0|  340.0|  56546.0|  64.0|  0.158|  0.853| 
| 5| 0.0|  2.0|  2295.0|  225134.0|  415.0|  0.153|  0.995|  0.034|  11.0|  245.0|  56641.0|  64.0|  0.207|  0.853| 
| 6| 0.0|  3.0|  2239.0|  225190.0|  414.0|  0.156|  0.993|  0.037|  10.0|  495.0|  56391.0|  65.0|  0.116|  0.867| 
| 7| 0.0|  2.0|  3095.0|  224334.0|  415.0|  0.118|  0.995|  0.011|  11.0|  194.0|  56692.0|  64.0|  0.248|  0.853| 
| 8| 0.0|  4.0|  1844.0|  225585.0|  413.0|  0.183|  0.99|  0.035|  9.0|  429.0|  56457.0|  66.0|  0.133|  0.88| 
| 9| 0.0|  1.0|  2119.0|  225310.0|  416.0|  0.164|  0.998|  0.012|  11.0|  167.0|  56719.0|  64.0|  0.277|  0.853| 
| 10| 0.0|  3.0|  1539.0|  225890.0|  414.0|  0.212|  0.993|  0.013|  13.0|  144.0|  56742.0|  62.0|  0.301|  0.827| 
| 11| 0.0|  6.0|  3444.0|  223985.0|  411.0|  0.107|  0.986|  0.039|  11.0|  394.0|  56492.0|  64.0|  0.14|  0.853| 
| 12| 0.0|  4.0|  3818.0|  223611.0|  413.0|  0.098|  0.99|  0.03|  9.0|  523.0|  56363.0|  66.0|  0.112|  0.88| 
| 13| 0.0|  7.0|  4482.0|  222947.0|  410.0|  0.084|  0.983|  0.059|  6.0|  1364.0|  55522.0|  69.0|  0.048|  0.92| 
| 14| 0.0|  2.0|  3064.0|  224365.0|  415.0|  0.119|  0.995|  0.033|  9.0|  699.0|  56187.0|  66.0|  0.086|  0.88| 
| 15| 0.0|  4.0|  3563.0|  223866.0|  413.0|  0.104|  0.99|  0.066|  8.0|  956.0|  55930.0|  67.0|  0.065|  0.893| 
| 16| 0.0|  4.0|  2536.0|  224893.0|  413.0|  0.14|  0.99|  0.016|  9.0|  339.0|  56547.0|  66.0|  0.163|  0.88| 
| 17| 0.0|  6.0|  2594.0|  224835.0|  411.0|  0.137|  0.986|  0.049|  8.0|  821.0|  56065.0|  67.0|  0.075|  0.893| 
| 18| 0.0|  1.0|  1911.0|  225518.0|  416.0|  0.179|  0.998|  0.013|  8.0|  215.0|  56671.0|  67.0|  0.238|  0.893| 
| 19| 0.0|  2.0|  1457.0|  225972.0|  415.0|  0.222|  0.995|  0.018|  7.0|  342.0|  56544.0|  68.0|  0.166|  0.907| 
| 20| 0.0|  0.0|  1132.0|  226297.0|  417.0|  0.269|  1.0|  0.011|  10.0|  172.0|  56714.0|  65.0|  0.274|  0.867| 
| 21| 0.0|  1.0|  840.0|  226589.0|  416.0|  0.331|  0.998|  0.008|  11.0|  100.0|  56786.0|  64.0|  0.39|  0.853| 
| 22| 0.0|  1.0|  2124.0|  225305.0|  416.0|  0.164|  0.998|  0.075|  10.0|  350.0|  56536.0|  65.0|  0.157|  0.867| 
| 23| 0.0|  2.0|  1457.0|  225972.0|  415.0|  0.222|  0.995|  0.03|  11.0|  242.0|  56644.0|  64.0|  0.209|  0.853| 
| 24| 0.0|  5.0|  2761.0|  224668.0|  412.0|  0.13|  0.988|  0.297|  6.0|  2741.0|  54145.0|  69.0|  0.025|  0.92| 
| 25| 0.0|  3.0|  2484.0|  224945.0|  414.0|  0.143|  0.993|  0.025|  10.0|  199.0|  56687.0|  65.0|  0.246|  0.867| 
| 26| 0.0|  4.0|  4867.0|  222562.0|  413.0|  0.078|  0.99|  0.021|  18.0|  33.0|  56853.0|  57.0|  0.633|  0.76| 
| 27| 0.0|  8.0|  4230.0|  223199.0|  409.0|  0.088|  0.981|  0.053|  9.0|  1541.0|  55345.0|  66.0|  0.041|  0.88| 
| 28| 0.0|  9.0|  5305.0|  222124.0|  408.0|  0.071|  0.978|  0.026|  9.0|  398.0|  56488.0|  66.0|  0.142|  0.88| 
| 29| 0.0|  5.0|  4846.0|  222583.0|  412.0|  0.078|  0.988|  0.242|  6.0|  7883.0|  49003.0|  69.0|  0.009|  0.92| 
| 30| 0.0|  5.0|  5193.0|  222236.0|  412.0|  0.074|  0.988|  0.026|  7.0|  449.0|  56437.0|  68.0|  0.132|  0.907| 

 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>