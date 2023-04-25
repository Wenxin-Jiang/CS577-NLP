---
license: mit
library_name: sklearn
tags:
- sklearn
- skops
- tabular-classification
model_file: example.pkl
widget:
  structuredData:
    'Unnamed: 32':
    - .nan
    - .nan
    - .nan
    area_mean:
    - 481.9
    - 1130.0
    - 748.9
    area_se:
    - 30.29
    - 96.05
    - 48.31
    area_worst:
    - 677.9
    - 1866.0
    - 1156.0
    compactness_mean:
    - 0.1058
    - 0.1029
    - 0.1223
    compactness_se:
    - 0.01911
    - 0.01652
    - 0.01484
    compactness_worst:
    - 0.2378
    - 0.2336
    - 0.2394
    concave points_mean:
    - 0.03821
    - 0.07951
    - 0.08087
    concave points_se:
    - 0.01037
    - 0.0137
    - 0.01093
    concave points_worst:
    - 0.1015
    - 0.1789
    - 0.1514
    concavity_mean:
    - 0.08005
    - 0.108
    - 0.1466
    concavity_se:
    - 0.02701
    - 0.02269
    - 0.02813
    concavity_worst:
    - 0.2671
    - 0.2687
    - 0.3791
    fractal_dimension_mean:
    - 0.06373
    - 0.05461
    - 0.05796
    fractal_dimension_se:
    - 0.003586
    - 0.001698
    - 0.002461
    fractal_dimension_worst:
    - 0.0875
    - 0.06589
    - 0.08019
    id:
    - 87930
    - 859575
    - 8670
    perimeter_mean:
    - 81.09
    - 123.6
    - 101.7
    perimeter_se:
    - 2.497
    - 5.486
    - 3.094
    perimeter_worst:
    - 96.05
    - 165.9
    - 124.9
    radius_mean:
    - 12.47
    - 18.94
    - 15.46
    radius_se:
    - 0.3961
    - 0.7888
    - 0.4743
    radius_worst:
    - 14.97
    - 24.86
    - 19.26
    smoothness_mean:
    - 0.09965
    - 0.09009
    - 0.1092
    smoothness_se:
    - 0.006953
    - 0.004444
    - 0.00624
    smoothness_worst:
    - 0.1426
    - 0.1193
    - 0.1546
    symmetry_mean:
    - 0.1925
    - 0.1582
    - 0.1931
    symmetry_se:
    - 0.01782
    - 0.01386
    - 0.01397
    symmetry_worst:
    - 0.3014
    - 0.2551
    - 0.2837
    texture_mean:
    - 18.6
    - 21.31
    - 19.48
    texture_se:
    - 1.044
    - 0.7975
    - 0.7859
    texture_worst:
    - 24.64
    - 26.58
    - 26.0
---

# Model description

[More Information Needed]

## Intended uses & limitations

This model is not ready to be used in production.

## Training Procedure

### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter           | Value                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------|
| memory                   |                                                                                               |
| steps                    | [('imputer', SimpleImputer()), ('scaler', StandardScaler()), ('model', LogisticRegression())] |
| verbose                  | False                                                                                         |
| imputer                  | SimpleImputer()                                                                               |
| scaler                   | StandardScaler()                                                                              |
| model                    | LogisticRegression()                                                                          |
| imputer__add_indicator   | False                                                                                         |
| imputer__copy            | True                                                                                          |
| imputer__fill_value      |                                                                                               |
| imputer__missing_values  | nan                                                                                           |
| imputer__strategy        | mean                                                                                          |
| imputer__verbose         | 0                                                                                             |
| scaler__copy             | True                                                                                          |
| scaler__with_mean        | True                                                                                          |
| scaler__with_std         | True                                                                                          |
| model__C                 | 1.0                                                                                           |
| model__class_weight      |                                                                                               |
| model__dual              | False                                                                                         |
| model__fit_intercept     | True                                                                                          |
| model__intercept_scaling | 1                                                                                             |
| model__l1_ratio          |                                                                                               |
| model__max_iter          | 100                                                                                           |
| model__multi_class       | auto                                                                                          |
| model__n_jobs            |                                                                                               |
| model__penalty           | l2                                                                                            |
| model__random_state      |                                                                                               |
| model__solver            | lbfgs                                                                                         |
| model__tol               | 0.0001                                                                                        |
| model__verbose           | 0                                                                                             |
| model__warm_start        | False                                                                                         |

</details>

### Model Plot

The model plot is below.

<style>#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b {color: black;background-color: white;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b pre{padding: 0;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-toggleable {background-color: white;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-estimator:hover {background-color: #d4ebff;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-item {z-index: 1;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-parallel-item:only-child::after {width: 0;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b div.sk-text-repr-fallback {display: none;}</style><div id="sk-e60317e1-ee5c-4f4d-98a6-92332ba1474b" class="sk-top-container" style="overflow: auto;"><div class="sk-text-repr-fallback"><pre>Pipeline(steps=[(&#x27;imputer&#x27;, SimpleImputer()), (&#x27;scaler&#x27;, StandardScaler()),(&#x27;model&#x27;, LogisticRegression())])</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="6aee50d2-d0d7-437e-8e9b-bd1121de94e7" type="checkbox" ><label for="6aee50d2-d0d7-437e-8e9b-bd1121de94e7" class="sk-toggleable__label sk-toggleable__label-arrow">Pipeline</label><div class="sk-toggleable__content"><pre>Pipeline(steps=[(&#x27;imputer&#x27;, SimpleImputer()), (&#x27;scaler&#x27;, StandardScaler()),(&#x27;model&#x27;, LogisticRegression())])</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="ac5b7f88-9a16-4c90-8fcb-2a4f833cadf1" type="checkbox" ><label for="ac5b7f88-9a16-4c90-8fcb-2a4f833cadf1" class="sk-toggleable__label sk-toggleable__label-arrow">SimpleImputer</label><div class="sk-toggleable__content"><pre>SimpleImputer()</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="65ce6721-e323-4189-a9bd-e373e248f0f7" type="checkbox" ><label for="65ce6721-e323-4189-a9bd-e373e248f0f7" class="sk-toggleable__label sk-toggleable__label-arrow">StandardScaler</label><div class="sk-toggleable__content"><pre>StandardScaler()</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="2328c6c4-413e-46ed-b597-1b88227e45a5" type="checkbox" ><label for="2328c6c4-413e-46ed-b597-1b88227e45a5" class="sk-toggleable__label sk-toggleable__label-arrow">LogisticRegression</label><div class="sk-toggleable__content"><pre>LogisticRegression()</pre></div></div></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.

| Metric   |    Value |
|----------|----------|
| accuracy | 0.982456 |
| f1 score | 0.982456 |

# How to Get Started with the Model

[More Information Needed]

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

# Confusion Matrix

![Confusion Matrix](path-to-confusion-matrix.png)
