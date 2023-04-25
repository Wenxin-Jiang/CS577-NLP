---
library_name: sklearn
tags:
- sklearn
- skops
- tabular-classification
model_file: model.pkl
widget:
  structuredData:
    area_mean:
    - 407.4
    - 1335.0
    - 428.0
    area_se:
    - 26.99
    - 77.02
    - 17.12
    area_worst:
    - 508.9
    - 1946.0
    - 546.3
    compactness_mean:
    - 0.05991
    - 0.1076
    - 0.069
    compactness_se:
    - 0.01065
    - 0.01895
    - 0.01727
    compactness_worst:
    - 0.1049
    - 0.3055
    - 0.188
    concave points_mean:
    - 0.02069
    - 0.08941
    - 0.01393
    concave points_se:
    - 0.009175
    - 0.01232
    - 0.006747
    concave points_worst:
    - 0.06544
    - 0.2112
    - 0.06913
    concavity_mean:
    - 0.02638
    - 0.1527
    - 0.02669
    concavity_se:
    - 0.01245
    - 0.02681
    - 0.02045
    concavity_worst:
    - 0.08105
    - 0.4159
    - 0.1471
    fractal_dimension_mean:
    - 0.05934
    - 0.05478
    - 0.06057
    fractal_dimension_se:
    - 0.001461
    - 0.001711
    - 0.002922
    fractal_dimension_worst:
    - 0.06487
    - 0.07055
    - 0.07993
    perimeter_mean:
    - 73.28
    - 134.8
    - 75.51
    perimeter_se:
    - 2.684
    - 4.119
    - 1.444
    perimeter_worst:
    - 83.12
    - 166.8
    - 85.22
    radius_mean:
    - 11.5
    - 20.64
    - 11.84
    radius_se:
    - 0.3927
    - 0.6137
    - 0.2222
    radius_worst:
    - 12.97
    - 25.37
    - 13.3
    smoothness_mean:
    - 0.09345
    - 0.09446
    - 0.08871
    smoothness_se:
    - 0.00638
    - 0.006211
    - 0.005517
    smoothness_worst:
    - 0.1183
    - 0.1562
    - 0.128
    symmetry_mean:
    - 0.1834
    - 0.1571
    - 0.1533
    symmetry_se:
    - 0.02292
    - 0.01276
    - 0.01616
    symmetry_worst:
    - 0.274
    - 0.2689
    - 0.2535
    texture_mean:
    - 18.45
    - 17.35
    - 18.94
    texture_se:
    - 0.8429
    - 0.6575
    - 0.8652
    texture_worst:
    - 22.46
    - 23.17
    - 24.99
---

# Model description

This is a Logistic Regression trained on breast cancer dataset.

## Intended uses & limitations

This model is trained for educational purposes.

## Training Procedure

### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter           | Value                                                           |
|--------------------------|-----------------------------------------------------------------|
| memory                   |                                                                 |
| steps                    | [('scaler', StandardScaler()), ('model', LogisticRegression())] |
| verbose                  | False                                                           |
| scaler                   | StandardScaler()                                                |
| model                    | LogisticRegression()                                            |
| scaler__copy             | True                                                            |
| scaler__with_mean        | True                                                            |
| scaler__with_std         | True                                                            |
| model__C                 | 1.0                                                             |
| model__class_weight      |                                                                 |
| model__dual              | False                                                           |
| model__fit_intercept     | True                                                            |
| model__intercept_scaling | 1                                                               |
| model__l1_ratio          |                                                                 |
| model__max_iter          | 100                                                             |
| model__multi_class       | auto                                                            |
| model__n_jobs            |                                                                 |
| model__penalty           | l2                                                              |
| model__random_state      |                                                                 |
| model__solver            | lbfgs                                                           |
| model__tol               | 0.0001                                                          |
| model__verbose           | 0                                                               |
| model__warm_start        | False                                                           |

</details>

### Model Plot

The model plot is below.

<style>#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 {color: black;background-color: white;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 pre{padding: 0;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-toggleable {background-color: white;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-estimator:hover {background-color: #d4ebff;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-item {z-index: 1;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-parallel-item:only-child::after {width: 0;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152 div.sk-text-repr-fallback {display: none;}</style><div id="sk-5b6643ea-0cef-4d0c-8389-2cf071bf6152" class="sk-top-container" style="overflow: auto;"><div class="sk-text-repr-fallback"><pre>Pipeline(steps=[(&#x27;scaler&#x27;, StandardScaler()), (&#x27;model&#x27;, LogisticRegression())])</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="76a688ab-e260-4cf7-a9f2-bf77900be27c" type="checkbox" ><label for="76a688ab-e260-4cf7-a9f2-bf77900be27c" class="sk-toggleable__label sk-toggleable__label-arrow">Pipeline</label><div class="sk-toggleable__content"><pre>Pipeline(steps=[(&#x27;scaler&#x27;, StandardScaler()), (&#x27;model&#x27;, LogisticRegression())])</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="6a4fcd10-6b63-40a6-a848-13717b9f7c82" type="checkbox" ><label for="6a4fcd10-6b63-40a6-a848-13717b9f7c82" class="sk-toggleable__label sk-toggleable__label-arrow">StandardScaler</label><div class="sk-toggleable__content"><pre>StandardScaler()</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="974bd93d-19db-4a61-b7ff-66d07e5bbadb" type="checkbox" ><label for="974bd93d-19db-4a61-b7ff-66d07e5bbadb" class="sk-toggleable__label sk-toggleable__label-arrow">LogisticRegression</label><div class="sk-toggleable__content"><pre>LogisticRegression()</pre></div></div></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.



| Metric   |    Value |
|----------|----------|
| accuracy | 0.965035 |
| f1 score | 0.965035 |

# How to Get Started with the Model

Use the code below to get started with the model.

```python
import joblib
import json
import pandas as pd
clf = joblib.load(model.pkl)
with open("config.json") as f:
    config = json.load(f)
clf.predict(pd.DataFrame.from_dict(config["sklearn"]["example_input"]))
```


# Additional Content

## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)