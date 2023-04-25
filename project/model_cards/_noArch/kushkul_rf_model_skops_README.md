---
license: mit
library_name: sklearn
tags:
- sklearn
- skops
- tabular-classification
widget:
  structuredData:
    x0:
    - 0.6666666666666667
    - 1.0
    - 1.0
    x1:
    - 0.0
    - 0.0
    - 0.0
    x10:
    - 0.0
    - 0.0
    - 0.0
    x11:
    - 0.0
    - 1.0
    - 0.0
    x12:
    - 1.0
    - 0.0
    - 1.0
    x13:
    - 0.0
    - 0.0
    - 0.0
    x14:
    - 0.0
    - 0.0
    - 0.0
    x15:
    - 1.0
    - 0.0
    - 0.0
    x16:
    - 0.0
    - 0.0
    - 0.0
    x17:
    - 0.0
    - 0.0
    - 1.0
    x18:
    - 0.0
    - 0.0
    - 0.0
    x19:
    - 0.0
    - 1.0
    - 0.0
    x2:
    - 1.0
    - 1.0
    - 1.0
    x20:
    - 1.0
    - 0.0
    - 0.0
    x21:
    - 0.0
    - 1.0
    - 1.0
    x22:
    - 0.0
    - 0.0
    - 0.0
    x23:
    - 1.0
    - 0.0
    - 1.0
    x24:
    - 0.0
    - 0.0
    - 0.0
    x25:
    - 0.0
    - 0.0
    - 0.0
    x26:
    - 0.0
    - 0.0
    - 0.0
    x27:
    - 0.0
    - 1.0
    - 0.0
    x3:
    - 0.0
    - 1.0
    - 0.0
    x4:
    - 0.0
    - 0.0
    - 1.0
    x5:
    - 1.0
    - 0.0
    - 0.0
    x6:
    - 0.0
    - 0.0
    - 0.0
    x7:
    - 0.24999999999999997
    - 0.14285714285714285
    - 0.3571428571428571
    x8:
    - 0.4772654358070523
    - 0.47033921746222385
    - 0.32320252247170167
    x9:
    - 0.0
    - 0.0
    - 0.0
---

# Model description

This is a Random Forest model trained on entire set of features from data provided by Reunion.

## Intended uses & limitations

This model is not fine-tuned for production.

## Training Procedure

### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter                      | Value                                                                                                                                                                                                                                                                       |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cv                                  | 3                                                                                                                                                                                                                                                                           |
| error_score                         | nan                                                                                                                                                                                                                                                                         |
| estimator__bootstrap                | True                                                                                                                                                                                                                                                                        |
| estimator__ccp_alpha                | 0.0                                                                                                                                                                                                                                                                         |
| estimator__class_weight             | balanced                                                                                                                                                                                                                                                                    |
| estimator__criterion                | gini                                                                                                                                                                                                                                                                        |
| estimator__max_depth                |                                                                                                                                                                                                                                                                             |
| estimator__max_features             | auto                                                                                                                                                                                                                                                                        |
| estimator__max_leaf_nodes           |                                                                                                                                                                                                                                                                             |
| estimator__max_samples              |                                                                                                                                                                                                                                                                             |
| estimator__min_impurity_decrease    | 0.0                                                                                                                                                                                                                                                                         |
| estimator__min_impurity_split       |                                                                                                                                                                                                                                                                             |
| estimator__min_samples_leaf         | 1                                                                                                                                                                                                                                                                           |
| estimator__min_samples_split        | 2                                                                                                                                                                                                                                                                           |
| estimator__min_weight_fraction_leaf | 0.0                                                                                                                                                                                                                                                                         |
| estimator__n_estimators             | 100                                                                                                                                                                                                                                                                         |
| estimator__n_jobs                   | -1                                                                                                                                                                                                                                                                          |
| estimator__oob_score                | False                                                                                                                                                                                                                                                                       |
| estimator__random_state             | 42                                                                                                                                                                                                                                                                          |
| estimator__verbose                  | 1                                                                                                                                                                                                                                                                           |
| estimator__warm_start               | False                                                                                                                                                                                                                                                                       |
| estimator                           | RandomForestClassifier(class_weight='balanced', n_jobs=-1, random_state=42,
                       verbose=1)                                                                                                                                                                                                                                                                             |
| n_iter                              | 100                                                                                                                                                                                                                                                                         |
| n_jobs                              | -1                                                                                                                                                                                                                                                                          |
| param_distributions                 | {'n_estimators': [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000], 'max_features': ['auto', 'sqrt'], 'max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, None], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 2, 4], 'bootstrap': [True, False]} |
| pre_dispatch                        | 2*n_jobs                                                                                                                                                                                                                                                                    |
| random_state                        | 42                                                                                                                                                                                                                                                                          |
| refit                               | True                                                                                                                                                                                                                                                                        |
| return_train_score                  | False                                                                                                                                                                                                                                                                       |
| scoring                             |                                                                                                                                                                                                                                                                             |
| verbose                             | 2                                                                                                                                                                                                                                                                           |

</details>

### Model Plot

The model plot is below.

<style>#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 {color: black;background-color: white;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 pre{padding: 0;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-toggleable {background-color: white;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.2em 0.3em;box-sizing: border-box;text-align: center;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;margin: 0.25em 0.25em;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-estimator:hover {background-color: #d4ebff;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-item {z-index: 1;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-parallel-item:only-child::after {width: 0;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0.2em;box-sizing: border-box;padding-bottom: 0.1em;background-color: white;position: relative;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-612ecc16-5410-4287-9cca-3bb6bb70aa61 div.sk-container {display: inline-block;position: relative;}</style><div id="sk-612ecc16-5410-4287-9cca-3bb6bb70aa61" class"sk-top-container"><div class="sk-container"><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="e81b924e-93ea-42c0-84fd-af8e0ec97962" type="checkbox" ><label class="sk-toggleable__label" for="e81b924e-93ea-42c0-84fd-af8e0ec97962">RandomizedSearchCV</label><div class="sk-toggleable__content"><pre>RandomizedSearchCV(cv=3,estimator=RandomForestClassifier(class_weight='balanced',n_jobs=-1, random_state=42,verbose=1),n_iter=100, n_jobs=-1,param_distributions={'bootstrap': [True, False],'max_depth': [10, 20, 30, 40, 50, 60,70, 80, 90, 100, 110,None],'max_features': ['auto', 'sqrt'],'min_samples_leaf': [1, 2, 4],'min_samples_split': [2, 5, 10],'n_estimators': [200, 400, 600, 800,1000, 1200, 1400, 1600,1800, 2000]},random_state=42, verbose=2)</pre></div></div></div><div class="sk-parallel"><div class="sk-parallel-item"><div class="sk-item"><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="4a4e6c45-5264-4a41-8fbe-d7cb73b658bb" type="checkbox" ><label class="sk-toggleable__label" for="4a4e6c45-5264-4a41-8fbe-d7cb73b658bb">RandomForestClassifier</label><div class="sk-toggleable__content"><pre>RandomForestClassifier(class_weight='balanced', n_jobs=-1, random_state=42,verbose=1)</pre></div></div></div></div></div></div></div></div></div></div>

##Â Evaluation Results

You can find the details about evaluation process and the evaluation results.



| Metric   |   Value |
|----------|---------|
| accuracy |   0.705 |
| recall   |   0.05  |

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

kushkul

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


# Additional Content

## confusion_matrix

![confusion_matrix](confusion_matrix.png)