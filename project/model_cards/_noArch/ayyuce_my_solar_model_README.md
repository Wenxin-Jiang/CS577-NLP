---
license: mit
library_name: sklearn
tags:
- sklearn
- skops
- tabular-regression
widget:
  structuredData:
    AMBIENT_TEMPERATURE:
    - 21.4322062
    - 27.322759933333337
    - 25.56246340000001
    DAILY_YIELD:
    - 0.0
    - 996.4285714
    - 685.0
    DC_POWER:
    - 0.0
    - 8358.285714
    - 6741.285714
    IRRADIATION:
    - 0.0
    - 0.6465474886666664
    - 0.498367802
    MODULE_TEMPERATURE:
    - 19.826896066666663
    - 45.7407144
    - 38.252356133333336
    TOTAL_YIELD:
    - 7218223.0
    - 6366043.429
    - 6372656.0
---

# Model description

This is a LinearRegression model trained on Solar Power Generation Data.

## Intended uses & limitations

This model is not ready to be used in production.

## Training Procedure

### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter   | Value      |
|------------------|------------|
| alpha            | 1.0        |
| copy_X           | True       |
| fit_intercept    | True       |
| l1_ratio         | 0.5        |
| max_iter         | 1000       |
| normalize        | deprecated |
| positive         | False      |
| precompute       | False      |
| random_state     | 0          |
| selection        | cyclic     |
| tol              | 0.0001     |
| warm_start       | False      |

</details>

### Model Plot

The model plot is below.

<style>#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b {color: black;background-color: white;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b pre{padding: 0;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-toggleable {background-color: white;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-estimator:hover {background-color: #d4ebff;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-item {z-index: 1;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-parallel-item:only-child::after {width: 0;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b div.sk-container {display: inline-block;position: relative;}</style><div id="sk-a3a3b863-d5cf-4b57-9e19-e3d8f2db0a0b" class"sk-top-container"><div class="sk-container"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="d20384ee-8f34-4e73-b4a5-b15dfd56af7a" type="checkbox" checked><label class="sk-toggleable__label" for="d20384ee-8f34-4e73-b4a5-b15dfd56af7a">ElasticNet</label><div class="sk-toggleable__content"><pre>ElasticNet(random_state=0)</pre></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.



| Metric   |   Value |
|----------|---------|
| accuracy | 99.9994 |

# How to Get Started with the Model

Use the code below to get started with the model.

<details>
<summary> Click to expand </summary>

```python
import pickle 
with open(dtc_pkl_filename, 'rb') as file: 
    clf = pickle.load(file)
```

</details>




# Model Card Authors

This model card is written by following authors:

ayyuce demirbas

# Model Card Contact

You can contact the model card authors through following channels:
[More Information Needed]

# Citation

Below you can find information related to citation.

**BibTeX:**
```
bibtex
@inproceedings{...,year={2022}}
```