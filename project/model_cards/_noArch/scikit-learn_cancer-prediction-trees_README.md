---
library_name: sklearn
tags:
- sklearn
- skops
- tabular-classification
model_file: model.pkl
widget:
  structuredData:
    x0:
    - 19.89
    - 12.89
    - 17.14
    x1:
    - 20.26
    - 13.12
    - 16.4
    x10:
    - 0.5079
    - 0.1532
    - 1.046
    x11:
    - 0.8737
    - 0.469
    - 0.976
    x12:
    - 3.654
    - 1.115
    - 7.276
    x13:
    - 59.7
    - 12.68
    - 111.4
    x14:
    - 0.005089
    - 0.004731
    - 0.008029
    x15:
    - 0.02303
    - 0.01345
    - 0.03799
    x16:
    - 0.03052
    - 0.01652
    - 0.03732
    x17:
    - 0.01178
    - 0.005905
    - 0.02397
    x18:
    - 0.01057
    - 0.01619
    - 0.02308
    x19:
    - 0.003391
    - 0.002081
    - 0.007444
    x2:
    - 130.5
    - 81.89
    - 116.0
    x20:
    - 23.73
    - 13.62
    - 22.25
    x21:
    - 25.23
    - 15.54
    - 21.4
    x22:
    - 160.5
    - 87.4
    - 152.4
    x23:
    - 1646.0
    - 577.0
    - 1461.0
    x24:
    - 0.1417
    - 0.09616
    - 0.1545
    x25:
    - 0.3309
    - 0.1147
    - 0.3949
    x26:
    - 0.4185
    - 0.1186
    - 0.3853
    x27:
    - 0.1613
    - 0.05366
    - 0.255
    x28:
    - 0.2549
    - 0.2309
    - 0.4066
    x29:
    - 0.09136
    - 0.06915
    - 0.1059
    x3:
    - 1214.0
    - 515.9
    - 912.7
    x4:
    - 0.1037
    - 0.06955
    - 0.1186
    x5:
    - 0.131
    - 0.03729
    - 0.2276
    x6:
    - 0.1411
    - 0.0226
    - 0.2229
    x7:
    - 0.09431
    - 0.01171
    - 0.1401
    x8:
    - 0.1802
    - 0.1337
    - 0.304
    x9:
    - 0.06188
    - 0.05581
    - 0.07413
---

# Model description

This is a Decision Tree Classifier trained on breast cancer dataset and pruned with CCP.

## Intended uses & limitations

This model is trained for educational purposes.

## Training Procedure

### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter           | Value   |
|--------------------------|---------|
| ccp_alpha                | 0.0     |
| class_weight             |         |
| criterion                | gini    |
| max_depth                |         |
| max_features             |         |
| max_leaf_nodes           |         |
| min_impurity_decrease    | 0.0     |
| min_impurity_split       |         |
| min_samples_leaf         | 1       |
| min_samples_split        | 2       |
| min_weight_fraction_leaf | 0.0     |
| random_state             | 0       |
| splitter                 | best    |

</details>

### Model Plot

The model plot is below.

<style>div.sk-top-container {color: black;background-color: white;}div.sk-toggleable {background-color: white;}label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.2em 0.3em;box-sizing: border-box;text-align: center;}div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}div.sk-estimator {font-family: monospace;background-color: #f0f8ff;margin: 0.25em 0.25em;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;}div.sk-estimator:hover {background-color: #d4ebff;}div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;}div.sk-item {z-index: 1;}div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}div.sk-parallel-item:only-child::after {width: 0;}div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0.2em;box-sizing: border-box;padding-bottom: 0.1em;background-color: white;position: relative;}div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}div.sk-label-container {position: relative;z-index: 2;text-align: center;}div.sk-container {display: inline-block;position: relative;}</style><div class="sk-top-container"><div class="sk-container"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="2f21b6bf-6c69-42c6-8cc3-1024ae9f4a92" type="checkbox" checked><label class="sk-toggleable__label" for="2f21b6bf-6c69-42c6-8cc3-1024ae9f4a92">DecisionTreeClassifier</label><div class="sk-toggleable__content"><pre>DecisionTreeClassifier(random_state=0)</pre></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.



| Metric   |    Value |
|----------|----------|
| accuracy | 0.937063 |
| f1 score | 0.937063 |

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

## Feature Importances

![Feature Importances](feature_importances.png)

## Tree Splits

![Tree Splits](tree.png)

## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)