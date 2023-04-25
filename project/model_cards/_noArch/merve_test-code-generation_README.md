---
library_name: sklearn
tags:
- sklearn
- skops
- tabular-classification
model_file: example.pkl
widget:
  structuredData:
    area error:
    - 30.29
    - 96.05
    - 48.31
    compactness error:
    - 0.01911
    - 0.01652
    - 0.01484
    concave points error:
    - 0.01037
    - 0.0137
    - 0.01093
    concavity error:
    - 0.02701
    - 0.02269
    - 0.02813
    fractal dimension error:
    - 0.003586
    - 0.001698
    - 0.002461
    mean area:
    - 481.9
    - 1130.0
    - 748.9
    mean compactness:
    - 0.1058
    - 0.1029
    - 0.1223
    mean concave points:
    - 0.03821
    - 0.07951
    - 0.08087
    mean concavity:
    - 0.08005
    - 0.108
    - 0.1466
    mean fractal dimension:
    - 0.06373
    - 0.05461
    - 0.05796
    mean perimeter:
    - 81.09
    - 123.6
    - 101.7
    mean radius:
    - 12.47
    - 18.94
    - 15.46
    mean smoothness:
    - 0.09965
    - 0.09009
    - 0.1092
    mean symmetry:
    - 0.1925
    - 0.1582
    - 0.1931
    mean texture:
    - 18.6
    - 21.31
    - 19.48
    perimeter error:
    - 2.497
    - 5.486
    - 3.094
    radius error:
    - 0.3961
    - 0.7888
    - 0.4743
    smoothness error:
    - 0.006953
    - 0.004444
    - 0.00624
    symmetry error:
    - 0.01782
    - 0.01386
    - 0.01397
    texture error:
    - 1.044
    - 0.7975
    - 0.7859
    worst area:
    - 677.9
    - 1866.0
    - 1156.0
    worst compactness:
    - 0.2378
    - 0.2336
    - 0.2394
    worst concave points:
    - 0.1015
    - 0.1789
    - 0.1514
    worst concavity:
    - 0.2671
    - 0.2687
    - 0.3791
    worst fractal dimension:
    - 0.0875
    - 0.06589
    - 0.08019
    worst perimeter:
    - 96.05
    - 165.9
    - 124.9
    worst radius:
    - 14.97
    - 24.86
    - 19.26
    worst smoothness:
    - 0.1426
    - 0.1193
    - 0.1546
    worst symmetry:
    - 0.3014
    - 0.2551
    - 0.2837
    worst texture:
    - 24.64
    - 26.58
    - 26.0
---

# Model description

[More Information Needed]

## Intended uses & limitations

[More Information Needed]

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
| min_samples_leaf         | 1       |
| min_samples_split        | 2       |
| min_weight_fraction_leaf | 0.0     |
| random_state             |         |
| splitter                 | best    |

</details>

### Model Plot

The model plot is below.

<style>#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe {color: black;background-color: white;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe pre{padding: 0;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-toggleable {background-color: white;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-estimator:hover {background-color: #d4ebff;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-item {z-index: 1;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-parallel-item:only-child::after {width: 0;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe div.sk-text-repr-fallback {display: none;}</style><div id="sk-e8a885f1-cbc4-4c9a-b46b-c755fe7af8fe" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>DecisionTreeClassifier()</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="baa9fb41-2382-4981-824f-a69815f63fd3" type="checkbox" checked><label for="baa9fb41-2382-4981-824f-a69815f63fd3" class="sk-toggleable__label sk-toggleable__label-arrow">DecisionTreeClassifier</label><div class="sk-toggleable__content"><pre>DecisionTreeClassifier()</pre></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.



| Metric   | Value   |
|----------|---------|

# How to Get Started with the Model

Use the code below to get started with the model.

```python
import joblib
import json
import pandas as pd
clf = joblib.load(example.pkl)
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