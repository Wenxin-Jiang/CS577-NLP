---
library_name: sklearn
tags:
- sklearn
- skops
- tabular-regression
model_format: pickle
model_file: model.pkl
widget:
  structuredData:
    Fedu:
    - 3
    - 3
    - 3
    Fjob:
    - other
    - other
    - services
    G1:
    - 12
    - 13
    - 8
    G2:
    - 13
    - 14
    - 7
    G3:
    - 12
    - 14
    - 0
    Medu:
    - 3
    - 2
    - 1
    Mjob:
    - services
    - other
    - at_home
    Pstatus:
    - T
    - T
    - T
    Walc:
    - 2
    - 1
    - 1
    absences:
    - 2
    - 0
    - 0
    activities:
    - 'yes'
    - 'no'
    - 'yes'
    address:
    - U
    - U
    - U
    age:
    - 16
    - 16
    - 16
    failures:
    - 0
    - 0
    - 3
    famrel:
    - 4
    - 5
    - 4
    famsize:
    - GT3
    - GT3
    - GT3
    famsup:
    - 'no'
    - 'no'
    - 'no'
    freetime:
    - 2
    - 3
    - 3
    goout:
    - 3
    - 3
    - 5
    guardian:
    - mother
    - father
    - mother
    health:
    - 3
    - 3
    - 3
    higher:
    - 'yes'
    - 'yes'
    - 'yes'
    internet:
    - 'yes'
    - 'yes'
    - 'yes'
    nursery:
    - 'yes'
    - 'yes'
    - 'no'
    paid:
    - 'yes'
    - 'no'
    - 'no'
    reason:
    - home
    - home
    - home
    romantic:
    - 'yes'
    - 'no'
    - 'yes'
    school:
    - GP
    - GP
    - GP
    schoolsup:
    - 'no'
    - 'no'
    - 'no'
    sex:
    - M
    - M
    - F
    studytime:
    - 2
    - 1
    - 2
    traveltime:
    - 1
    - 2
    - 1
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

| Hyperparameter                        | Value                                                |
|---------------------------------------|------------------------------------------------------|
| memory                                |                                                      |
| steps                                 | [('onehotencoder', OneHotEncoder(handle_unknown='ignore', sparse=False)), ('xgbregressor', XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,<br />             colsample_bynode=1, colsample_bytree=1, enable_categorical=False,<br />             gamma=0, gpu_id=-1, importance_type=None,<br />             interaction_constraints='', learning_rate=0.300000012,<br />             max_delta_step=0, max_depth=5, min_child_weight=1, missing=nan,<br />             monotone_constraints='()', n_estimators=100, n_jobs=8,<br />             num_parallel_tree=1, predictor='auto', random_state=0, reg_alpha=0,<br />             reg_lambda=1, scale_pos_weight=1, subsample=1, tree_method='exact',<br />             validate_parameters=1, verbosity=None))]                                                      |
| verbose                               | False                                                |
| onehotencoder                         | OneHotEncoder(handle_unknown='ignore', sparse=False) |
| xgbregressor                          | XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,<br />             colsample_bynode=1, colsample_bytree=1, enable_categorical=False,<br />             gamma=0, gpu_id=-1, importance_type=None,<br />             interaction_constraints='', learning_rate=0.300000012,<br />             max_delta_step=0, max_depth=5, min_child_weight=1, missing=nan,<br />             monotone_constraints='()', n_estimators=100, n_jobs=8,<br />             num_parallel_tree=1, predictor='auto', random_state=0, reg_alpha=0,<br />             reg_lambda=1, scale_pos_weight=1, subsample=1, tree_method='exact',<br />             validate_parameters=1, verbosity=None)                                                      |
| onehotencoder__categories             | auto                                                 |
| onehotencoder__drop                   |                                                      |
| onehotencoder__dtype                  | <class 'numpy.float64'>                              |
| onehotencoder__handle_unknown         | ignore                                               |
| onehotencoder__max_categories         |                                                      |
| onehotencoder__min_frequency          |                                                      |
| onehotencoder__sparse                 | False                                                |
| xgbregressor__objective               | reg:squarederror                                     |
| xgbregressor__base_score              | 0.5                                                  |
| xgbregressor__booster                 | gbtree                                               |
| xgbregressor__colsample_bylevel       | 1                                                    |
| xgbregressor__colsample_bynode        | 1                                                    |
| xgbregressor__colsample_bytree        | 1                                                    |
| xgbregressor__enable_categorical      | False                                                |
| xgbregressor__gamma                   | 0                                                    |
| xgbregressor__gpu_id                  | -1                                                   |
| xgbregressor__importance_type         |                                                      |
| xgbregressor__interaction_constraints |                                                      |
| xgbregressor__learning_rate           | 0.300000012                                          |
| xgbregressor__max_delta_step          | 0                                                    |
| xgbregressor__max_depth               | 5                                                    |
| xgbregressor__min_child_weight        | 1                                                    |
| xgbregressor__missing                 | nan                                                  |
| xgbregressor__monotone_constraints    | ()                                                   |
| xgbregressor__n_estimators            | 100                                                  |
| xgbregressor__n_jobs                  | 8                                                    |
| xgbregressor__num_parallel_tree       | 1                                                    |
| xgbregressor__predictor               | auto                                                 |
| xgbregressor__random_state            | 0                                                    |
| xgbregressor__reg_alpha               | 0                                                    |
| xgbregressor__reg_lambda              | 1                                                    |
| xgbregressor__scale_pos_weight        | 1                                                    |
| xgbregressor__subsample               | 1                                                    |
| xgbregressor__tree_method             | exact                                                |
| xgbregressor__validate_parameters     | 1                                                    |
| xgbregressor__verbosity               |                                                      |

</details>

### Model Plot

The model plot is below.

<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container" style="overflow: auto;"><div class="sk-text-repr-fallback"><pre>Pipeline(steps=[(&#x27;onehotencoder&#x27;,OneHotEncoder(handle_unknown=&#x27;ignore&#x27;, sparse=False)),(&#x27;xgbregressor&#x27;,XGBRegressor(base_score=0.5, booster=&#x27;gbtree&#x27;,colsample_bylevel=1, colsample_bynode=1,colsample_bytree=1, enable_categorical=False,gamma=0, gpu_id=-1, importance_type=None,interaction_constraints=&#x27;&#x27;,learning_rate=0.300000012, max_delta_step=0,max_depth=5, min_child_weight=1, missing=nan,monotone_constraints=&#x27;()&#x27;, n_estimators=100,n_jobs=8, num_parallel_tree=1, predictor=&#x27;auto&#x27;,random_state=0, reg_alpha=0, reg_lambda=1,scale_pos_weight=1, subsample=1,tree_method=&#x27;exact&#x27;, validate_parameters=1,verbosity=None))])</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" ><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">Pipeline</label><div class="sk-toggleable__content"><pre>Pipeline(steps=[(&#x27;onehotencoder&#x27;,OneHotEncoder(handle_unknown=&#x27;ignore&#x27;, sparse=False)),(&#x27;xgbregressor&#x27;,XGBRegressor(base_score=0.5, booster=&#x27;gbtree&#x27;,colsample_bylevel=1, colsample_bynode=1,colsample_bytree=1, enable_categorical=False,gamma=0, gpu_id=-1, importance_type=None,interaction_constraints=&#x27;&#x27;,learning_rate=0.300000012, max_delta_step=0,max_depth=5, min_child_weight=1, missing=nan,monotone_constraints=&#x27;()&#x27;, n_estimators=100,n_jobs=8, num_parallel_tree=1, predictor=&#x27;auto&#x27;,random_state=0, reg_alpha=0, reg_lambda=1,scale_pos_weight=1, subsample=1,tree_method=&#x27;exact&#x27;, validate_parameters=1,verbosity=None))])</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-2" type="checkbox" ><label for="sk-estimator-id-2" class="sk-toggleable__label sk-toggleable__label-arrow">OneHotEncoder</label><div class="sk-toggleable__content"><pre>OneHotEncoder(handle_unknown=&#x27;ignore&#x27;, sparse=False)</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-3" type="checkbox" ><label for="sk-estimator-id-3" class="sk-toggleable__label sk-toggleable__label-arrow">XGBRegressor</label><div class="sk-toggleable__content"><pre>XGBRegressor(base_score=0.5, booster=&#x27;gbtree&#x27;, colsample_bylevel=1,colsample_bynode=1, colsample_bytree=1, enable_categorical=False,gamma=0, gpu_id=-1, importance_type=None,interaction_constraints=&#x27;&#x27;, learning_rate=0.300000012,max_delta_step=0, max_depth=5, min_child_weight=1, missing=nan,monotone_constraints=&#x27;()&#x27;, n_estimators=100, n_jobs=8,num_parallel_tree=1, predictor=&#x27;auto&#x27;, random_state=0, reg_alpha=0,reg_lambda=1, scale_pos_weight=1, subsample=1, tree_method=&#x27;exact&#x27;,validate_parameters=1, verbosity=None)</pre></div></div></div></div></div></div></div>

## Evaluation Results

[More Information Needed]

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
