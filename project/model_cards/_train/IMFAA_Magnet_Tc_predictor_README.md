---
library_name: sklearn
tags:
- tabular-regression
- materials property prediction
- baseline-trainer
---

**Model Description**

The magnet Curie temperature (Tc [K]) predictor model has been trained using a supervised learning approach on a specific set of magnet classes having 14:2:1 phases.
The dataset to train the Tc prediction model is a distinct literature source.
Further, the Tc values for various 14:2:1 magnet phases at room temperature are considered for dataset creation.

It predicts the Tc value using the chemical composition as a feature.

E.g: To predict the Tc value Nd2Fe14B1 magnet composition, the features are Nd=2, Fe=14, and B=1.

**Application & Limitations**

Input feature as the chemical composition of the test sample should match the sequence of the features described in the config file.

The trained model is valid for 14:2:1 phases only, which are stoichiometric compositions and the predicted Tc value is in Kelvin and at room temperature.

**Model pipeline**

The voting regressor to predict the Tc combines the following four base models and equal weight is assigned to each base model.

1. Extra tree regressor (ET)
2. Extreme gradient boosting (XGB)
3. Random forest regressor (RF)
4. Adaptive boosted RF regressor (AB)

                                               
# How to use the trained model for inference

```python
import json
import joblib
import pandas as pd

Tc_predictor = load('Magnet_Tc_predictor.joblib') # trained model
config = json.load(open('config.json'))
features = config['features'] # feature vector

#data = pd.read_excel("data.xlsx") # read test file with new compositions
data = data[features]

Predicted_value = Tc_predictor.predict(data) # predict Tc values
print("Predicted Tc value is: {0:.2f}'.format(Predicted_value)")

```
