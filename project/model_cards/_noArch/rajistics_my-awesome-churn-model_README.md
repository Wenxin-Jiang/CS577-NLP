---
license: mit
library_name: sklearn
tags:
- sklearn
- skops
- tabular-classification
widget:
  structuredData:
    Contract:
    - Two year
    - Month-to-month
    - One year
    Dependents:
    - 'Yes'
    - 'No'
    - 'No'
    DeviceProtection:
    - 'No'
    - 'No'
    - 'Yes'
    InternetService:
    - Fiber optic
    - Fiber optic
    - DSL
    MonthlyCharges:
    - 79.05
    - 84.95
    - 68.8
    MultipleLines:
    - 'Yes'
    - 'Yes'
    - 'Yes'
    OnlineBackup:
    - 'No'
    - 'No'
    - 'Yes'
    OnlineSecurity:
    - 'Yes'
    - 'No'
    - 'Yes'
    PaperlessBilling:
    - 'No'
    - 'Yes'
    - 'No'
    Partner:
    - 'Yes'
    - 'Yes'
    - 'No'
    PaymentMethod:
    - Bank transfer (automatic)
    - Electronic check
    - Bank transfer (automatic)
    PhoneService:
    - 'Yes'
    - 'Yes'
    - 'Yes'
    SeniorCitizen:
    - 0
    - 0
    - 0
    StreamingMovies:
    - 'No'
    - 'No'
    - 'No'
    StreamingTV:
    - 'No'
    - 'Yes'
    - 'No'
    TechSupport:
    - 'No'
    - 'No'
    - 'Yes'
    TotalCharges:
    - 5730.7
    - 1378.25
    - 4111.35
    gender:
    - Female
    - Female
    - Male
    tenure:
    - 72
    - 16
    - 63
---

# Model description

This is a Logistic Regression model trained on churn dataset.

## Intended uses & limitations

This model is not ready to be used in production.

## Training Procedure

### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter                             | Value                                                                             |
|--------------------------------------------|-----------------------------------------------------------------------------------|
| memory                                     |                                                                                   |
| steps                                      | [('preprocessor', ColumnTransformer(transformers=[('num',
                                 Pipeline(steps=[('imputer',
                                                  SimpleImputer(strategy='median')),
                                                 ('std_scaler',
                                                  StandardScaler())]),
                                 ['MonthlyCharges', 'TotalCharges', 'tenure']),
                                ('cat', OneHotEncoder(),
                                 ['SeniorCitizen', 'gender', 'Partner',
                                  'Dependents', 'PhoneService', 'MultipleLines',
                                  'InternetService', 'OnlineSecurity',
                                  'OnlineBackup', 'DeviceProtection',
                                  'TechSupport', 'StreamingTV',
                                  'StreamingMovies', 'Contract',
                                  'PaperlessBilling', 'PaymentMethod'])])), ('classifier', LogisticRegression(class_weight='balanced', max_iter=300))]                                                                                   |
| verbose                                    | False                                                                             |
| preprocessor                               | ColumnTransformer(transformers=[('num',
                                 Pipeline(steps=[('imputer',
                                                  SimpleImputer(strategy='median')),
                                                 ('std_scaler',
                                                  StandardScaler())]),
                                 ['MonthlyCharges', 'TotalCharges', 'tenure']),
                                ('cat', OneHotEncoder(),
                                 ['SeniorCitizen', 'gender', 'Partner',
                                  'Dependents', 'PhoneService', 'MultipleLines',
                                  'InternetService', 'OnlineSecurity',
                                  'OnlineBackup', 'DeviceProtection',
                                  'TechSupport', 'StreamingTV',
                                  'StreamingMovies', 'Contract',
                                  'PaperlessBilling', 'PaymentMethod'])])                                                                                   |
| classifier                                 | LogisticRegression(class_weight='balanced', max_iter=300)                         |
| preprocessor__n_jobs                       |                                                                                   |
| preprocessor__remainder                    | drop                                                                              |
| preprocessor__sparse_threshold             | 0.3                                                                               |
| preprocessor__transformer_weights          |                                                                                   |
| preprocessor__transformers                 | [('num', Pipeline(steps=[('imputer', SimpleImputer(strategy='median')),
                ('std_scaler', StandardScaler())]), ['MonthlyCharges', 'TotalCharges', 'tenure']), ('cat', OneHotEncoder(), ['SeniorCitizen', 'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'])]                                                                                   |
| preprocessor__verbose                      | False                                                                             |
| preprocessor__verbose_feature_names_out    | True                                                                              |
| preprocessor__num                          | Pipeline(steps=[('imputer', SimpleImputer(strategy='median')),
                ('std_scaler', StandardScaler())])                                                                                   |
| preprocessor__cat                          | OneHotEncoder()                                                                   |
| preprocessor__num__memory                  |                                                                                   |
| preprocessor__num__steps                   | [('imputer', SimpleImputer(strategy='median')), ('std_scaler', StandardScaler())] |
| preprocessor__num__verbose                 | False                                                                             |
| preprocessor__num__imputer                 | SimpleImputer(strategy='median')                                                  |
| preprocessor__num__std_scaler              | StandardScaler()                                                                  |
| preprocessor__num__imputer__add_indicator  | False                                                                             |
| preprocessor__num__imputer__copy           | True                                                                              |
| preprocessor__num__imputer__fill_value     |                                                                                   |
| preprocessor__num__imputer__missing_values | nan                                                                               |
| preprocessor__num__imputer__strategy       | median                                                                            |
| preprocessor__num__imputer__verbose        | deprecated                                                                        |
| preprocessor__num__std_scaler__copy        | True                                                                              |
| preprocessor__num__std_scaler__with_mean   | True                                                                              |
| preprocessor__num__std_scaler__with_std    | True                                                                              |
| preprocessor__cat__categories              | auto                                                                              |
| preprocessor__cat__drop                    |                                                                                   |
| preprocessor__cat__dtype                   | <class 'numpy.float64'>                                                           |
| preprocessor__cat__handle_unknown          | error                                                                             |
| preprocessor__cat__max_categories          |                                                                                   |
| preprocessor__cat__min_frequency           |                                                                                   |
| preprocessor__cat__sparse                  | True                                                                              |
| classifier__C                              | 1.0                                                                               |
| classifier__class_weight                   | balanced                                                                          |
| classifier__dual                           | False                                                                             |
| classifier__fit_intercept                  | True                                                                              |
| classifier__intercept_scaling              | 1                                                                                 |
| classifier__l1_ratio                       |                                                                                   |
| classifier__max_iter                       | 300                                                                               |
| classifier__multi_class                    | auto                                                                              |
| classifier__n_jobs                         |                                                                                   |
| classifier__penalty                        | l2                                                                                |
| classifier__random_state                   |                                                                                   |
| classifier__solver                         | lbfgs                                                                             |
| classifier__tol                            | 0.0001                                                                            |
| classifier__verbose                        | 0                                                                                 |
| classifier__warm_start                     | False                                                                             |

</details>

### Model Plot

The model plot is below.

<style>#sk-container-id-3 {color: black;background-color: white;}#sk-container-id-3 pre{padding: 0;}#sk-container-id-3 div.sk-toggleable {background-color: white;}#sk-container-id-3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-3 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-3 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-3 div.sk-item {position: relative;z-index: 1;}#sk-container-id-3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-3 div.sk-item::before, #sk-container-id-3 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-3 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-3 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-3 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-3 div.sk-label-container {text-align: center;}#sk-container-id-3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-3 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-3" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>Pipeline(steps=[(&#x27;preprocessor&#x27;,ColumnTransformer(transformers=[(&#x27;num&#x27;,Pipeline(steps=[(&#x27;imputer&#x27;,SimpleImputer(strategy=&#x27;median&#x27;)),(&#x27;std_scaler&#x27;,StandardScaler())]),[&#x27;MonthlyCharges&#x27;,&#x27;TotalCharges&#x27;, &#x27;tenure&#x27;]),(&#x27;cat&#x27;, OneHotEncoder(),[&#x27;SeniorCitizen&#x27;, &#x27;gender&#x27;,&#x27;Partner&#x27;, &#x27;Dependents&#x27;,&#x27;PhoneService&#x27;,&#x27;MultipleLines&#x27;,&#x27;InternetService&#x27;,&#x27;OnlineSecurity&#x27;,&#x27;OnlineBackup&#x27;,&#x27;DeviceProtection&#x27;,&#x27;TechSupport&#x27;, &#x27;StreamingTV&#x27;,&#x27;StreamingMovies&#x27;,&#x27;Contract&#x27;,&#x27;PaperlessBilling&#x27;,&#x27;PaymentMethod&#x27;])])),(&#x27;classifier&#x27;,LogisticRegression(class_weight=&#x27;balanced&#x27;, max_iter=300))])</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-10" type="checkbox" ><label for="sk-estimator-id-10" class="sk-toggleable__label sk-toggleable__label-arrow">Pipeline</label><div class="sk-toggleable__content"><pre>Pipeline(steps=[(&#x27;preprocessor&#x27;,ColumnTransformer(transformers=[(&#x27;num&#x27;,Pipeline(steps=[(&#x27;imputer&#x27;,SimpleImputer(strategy=&#x27;median&#x27;)),(&#x27;std_scaler&#x27;,StandardScaler())]),[&#x27;MonthlyCharges&#x27;,&#x27;TotalCharges&#x27;, &#x27;tenure&#x27;]),(&#x27;cat&#x27;, OneHotEncoder(),[&#x27;SeniorCitizen&#x27;, &#x27;gender&#x27;,&#x27;Partner&#x27;, &#x27;Dependents&#x27;,&#x27;PhoneService&#x27;,&#x27;MultipleLines&#x27;,&#x27;InternetService&#x27;,&#x27;OnlineSecurity&#x27;,&#x27;OnlineBackup&#x27;,&#x27;DeviceProtection&#x27;,&#x27;TechSupport&#x27;, &#x27;StreamingTV&#x27;,&#x27;StreamingMovies&#x27;,&#x27;Contract&#x27;,&#x27;PaperlessBilling&#x27;,&#x27;PaymentMethod&#x27;])])),(&#x27;classifier&#x27;,LogisticRegression(class_weight=&#x27;balanced&#x27;, max_iter=300))])</pre></div></div></div><div class="sk-serial"><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-11" type="checkbox" ><label for="sk-estimator-id-11" class="sk-toggleable__label sk-toggleable__label-arrow">preprocessor: ColumnTransformer</label><div class="sk-toggleable__content"><pre>ColumnTransformer(transformers=[(&#x27;num&#x27;,Pipeline(steps=[(&#x27;imputer&#x27;,SimpleImputer(strategy=&#x27;median&#x27;)),(&#x27;std_scaler&#x27;,StandardScaler())]),[&#x27;MonthlyCharges&#x27;, &#x27;TotalCharges&#x27;, &#x27;tenure&#x27;]),(&#x27;cat&#x27;, OneHotEncoder(),[&#x27;SeniorCitizen&#x27;, &#x27;gender&#x27;, &#x27;Partner&#x27;,&#x27;Dependents&#x27;, &#x27;PhoneService&#x27;, &#x27;MultipleLines&#x27;,&#x27;InternetService&#x27;, &#x27;OnlineSecurity&#x27;,&#x27;OnlineBackup&#x27;, &#x27;DeviceProtection&#x27;,&#x27;TechSupport&#x27;, &#x27;StreamingTV&#x27;,&#x27;StreamingMovies&#x27;, &#x27;Contract&#x27;,&#x27;PaperlessBilling&#x27;, &#x27;PaymentMethod&#x27;])])</pre></div></div></div><div class="sk-parallel"><div class="sk-parallel-item"><div class="sk-item"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-12" type="checkbox" ><label for="sk-estimator-id-12" class="sk-toggleable__label sk-toggleable__label-arrow">num</label><div class="sk-toggleable__content"><pre>[&#x27;MonthlyCharges&#x27;, &#x27;TotalCharges&#x27;, &#x27;tenure&#x27;]</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-13" type="checkbox" ><label for="sk-estimator-id-13" class="sk-toggleable__label sk-toggleable__label-arrow">SimpleImputer</label><div class="sk-toggleable__content"><pre>SimpleImputer(strategy=&#x27;median&#x27;)</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-14" type="checkbox" ><label for="sk-estimator-id-14" class="sk-toggleable__label sk-toggleable__label-arrow">StandardScaler</label><div class="sk-toggleable__content"><pre>StandardScaler()</pre></div></div></div></div></div></div></div></div><div class="sk-parallel-item"><div class="sk-item"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-15" type="checkbox" ><label for="sk-estimator-id-15" class="sk-toggleable__label sk-toggleable__label-arrow">cat</label><div class="sk-toggleable__content"><pre>[&#x27;SeniorCitizen&#x27;, &#x27;gender&#x27;, &#x27;Partner&#x27;, &#x27;Dependents&#x27;, &#x27;PhoneService&#x27;, &#x27;MultipleLines&#x27;, &#x27;InternetService&#x27;, &#x27;OnlineSecurity&#x27;, &#x27;OnlineBackup&#x27;, &#x27;DeviceProtection&#x27;, &#x27;TechSupport&#x27;, &#x27;StreamingTV&#x27;, &#x27;StreamingMovies&#x27;, &#x27;Contract&#x27;, &#x27;PaperlessBilling&#x27;, &#x27;PaymentMethod&#x27;]</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-16" type="checkbox" ><label for="sk-estimator-id-16" class="sk-toggleable__label sk-toggleable__label-arrow">OneHotEncoder</label><div class="sk-toggleable__content"><pre>OneHotEncoder()</pre></div></div></div></div></div></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-17" type="checkbox" ><label for="sk-estimator-id-17" class="sk-toggleable__label sk-toggleable__label-arrow">LogisticRegression</label><div class="sk-toggleable__content"><pre>LogisticRegression(class_weight=&#x27;balanced&#x27;, max_iter=300)</pre></div></div></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.



| Metric   |    Value |
|----------|----------|
| accuracy | 0.730305 |
| f1 score | 0.730305 |

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

skops_user

# Model Card Contact

You can contact the model card authors through following channels:
[More Information Needed]

# Citation

Below you can find information related to citation.

**BibTeX:**
```
bibtex
@inproceedings{...,year={2020}}
```


# Additional Content

## confusion_matrix

![confusion_matrix](confusion_matrix.png)