---
library_name: sklearn
tags:
- sklearn
- skops
- tabular-regression
model_file: pipeline.skops
widget:
  structuredData:
    acceleration:
    - 20.7
    - 17.0
    - 18.6
    cylinders:
    - 4
    - 4
    - 4
    displacement:
    - 98.0
    - 120.0
    - 120.0
    horsepower:
    - '65'
    - '88'
    - '79'
    model year:
    - 81
    - 75
    - 82
    origin:
    - 1
    - 2
    - 1
    weight:
    - 2380
    - 2957
    - 2625
---

# Model description

This is a regression model on MPG dataset trained for this [kaggle tutorial](https://www.kaggle.com/unofficialmerve/persisting-your-scikit-learn-model-using-skops/).

## Intended uses & limitations

This model is not ready to be used in production.

## Training Procedure

### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter           | Value         |
|--------------------------|---------------|
| ccp_alpha                | 0.0           |
| criterion                | squared_error |
| max_depth                |               |
| max_features             |               |
| max_leaf_nodes           |               |
| min_impurity_decrease    | 0.0           |
| min_samples_leaf         | 1             |
| min_samples_split        | 2             |
| min_weight_fraction_leaf | 0.0           |
| random_state             |               |
| splitter                 | best          |

</details>

### Model Plot

The model plot is below.

<style>#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 {color: black;background-color: white;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 pre{padding: 0;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-toggleable {background-color: white;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-item {z-index: 1;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-parallel-item:only-child::after {width: 0;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3 div.sk-text-repr-fallback {display: none;}</style><div id="sk-3ea712fc-223a-4e18-9d66-e9fdc5d944b3" class="sk-top-container" style="overflow: auto;"><div class="sk-text-repr-fallback"><pre>DecisionTreeRegressor()</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="37ade0f5-01f0-4181-acab-e7150c3b5fa2" type="checkbox" checked><label for="37ade0f5-01f0-4181-acab-e7150c3b5fa2" class="sk-toggleable__label sk-toggleable__label-arrow">DecisionTreeRegressor</label><div class="sk-toggleable__content"><pre>DecisionTreeRegressor()</pre></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.



| Metric             | Value                                 |
|--------------------|---------------------------------------|
| Mean Squared Error | 10.86399394359616                     |
| R-Squared          | <function r2_score at 0x7f743fc54b00> |

# How to Get Started with the Model

Use the code below to get started with the model.

```python
from skops.io import load
import json
import pandas as pd
clf = load("pipeline.skops")
with open("config.json") as f:
    config = json.load(f)
clf.predict(pd.DataFrame.from_dict(config["sklearn"]["example_input"]))
```


# Model Card Authors

This model card is written by following authors:

[More Information Needed]

# Model Card Contact

You can contact the model card authors through following channels:
[More Information Needed]

# Citation

Below you can find information related to citation.

**BibTeX:**
```
[More Information Needed]
```