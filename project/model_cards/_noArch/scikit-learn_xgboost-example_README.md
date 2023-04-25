---
license: mit
library_name: sklearn
tags:
- sklearn
- skops
- tabular-regression
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

This is an XGBoost model trained to predict daily alcohol consumption of students.


## Training Procedure

### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter                        | Value                                                |
|---------------------------------------|------------------------------------------------------|
| memory                                |                                                      |
| steps                                 | [('onehotencoder', OneHotEncoder(handle_unknown='ignore', sparse=False)), ('xgbregressor', XGBRegressor(base_score=None, booster=None, callbacks=None,<br />             colsample_bylevel=None, colsample_bynode=None,<br />             colsample_bytree=None, early_stopping_rounds=None,<br />             enable_categorical=False, eval_metric=None, feature_types=None,<br />             gamma=None, gpu_id=None, grow_policy=None, importance_type=None,<br />             interaction_constraints=None, learning_rate=None, max_bin=None,<br />             max_cat_threshold=None, max_cat_to_onehot=None,<br />             max_delta_step=None, max_depth=5, max_leaves=None,<br />             min_child_weight=None, missing=nan, monotone_constraints=None,<br />             n_estimators=100, n_jobs=None, num_parallel_tree=None,<br />             predictor=None, random_state=None, ...))]                                                      |
| verbose                               | False                                                |
| onehotencoder                         | OneHotEncoder(handle_unknown='ignore', sparse=False) |
| xgbregressor                          | XGBRegressor(base_score=None, booster=None, callbacks=None,<br />             colsample_bylevel=None, colsample_bynode=None,<br />             colsample_bytree=None, early_stopping_rounds=None,<br />             enable_categorical=False, eval_metric=None, feature_types=None,<br />             gamma=None, gpu_id=None, grow_policy=None, importance_type=None,<br />             interaction_constraints=None, learning_rate=None, max_bin=None,<br />             max_cat_threshold=None, max_cat_to_onehot=None,<br />             max_delta_step=None, max_depth=5, max_leaves=None,<br />             min_child_weight=None, missing=nan, monotone_constraints=None,<br />             n_estimators=100, n_jobs=None, num_parallel_tree=None,<br />             predictor=None, random_state=None, ...)                                                      |
| onehotencoder__categories             | auto                                                 |
| onehotencoder__drop                   |                                                      |
| onehotencoder__dtype                  | <class 'numpy.float64'>                              |
| onehotencoder__handle_unknown         | ignore                                               |
| onehotencoder__sparse                 | False                                                |
| xgbregressor__objective               | reg:squarederror                                     |
| xgbregressor__base_score              |                                                      |
| xgbregressor__booster                 |                                                      |
| xgbregressor__callbacks               |                                                      |
| xgbregressor__colsample_bylevel       |                                                      |
| xgbregressor__colsample_bynode        |                                                      |
| xgbregressor__colsample_bytree        |                                                      |
| xgbregressor__early_stopping_rounds   |                                                      |
| xgbregressor__enable_categorical      | False                                                |
| xgbregressor__eval_metric             |                                                      |
| xgbregressor__feature_types           |                                                      |
| xgbregressor__gamma                   |                                                      |
| xgbregressor__gpu_id                  |                                                      |
| xgbregressor__grow_policy             |                                                      |
| xgbregressor__importance_type         |                                                      |
| xgbregressor__interaction_constraints |                                                      |
| xgbregressor__learning_rate           |                                                      |
| xgbregressor__max_bin                 |                                                      |
| xgbregressor__max_cat_threshold       |                                                      |
| xgbregressor__max_cat_to_onehot       |                                                      |
| xgbregressor__max_delta_step          |                                                      |
| xgbregressor__max_depth               | 5                                                    |
| xgbregressor__max_leaves              |                                                      |
| xgbregressor__min_child_weight        |                                                      |
| xgbregressor__missing                 | nan                                                  |
| xgbregressor__monotone_constraints    |                                                      |
| xgbregressor__n_estimators            | 100                                                  |
| xgbregressor__n_jobs                  |                                                      |
| xgbregressor__num_parallel_tree       |                                                      |
| xgbregressor__predictor               |                                                      |
| xgbregressor__random_state            |                                                      |
| xgbregressor__reg_alpha               |                                                      |
| xgbregressor__reg_lambda              |                                                      |
| xgbregressor__sampling_method         |                                                      |
| xgbregressor__scale_pos_weight        |                                                      |
| xgbregressor__subsample               |                                                      |
| xgbregressor__tree_method             |                                                      |
| xgbregressor__validate_parameters     |                                                      |
| xgbregressor__verbosity               |                                                      |

</details>

### Model Plot

The model plot is below.

<style>#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 {color: black;background-color: white;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 pre{padding: 0;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-toggleable {background-color: white;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-item {z-index: 1;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-parallel-item:only-child::after {width: 0;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3 div.sk-text-repr-fallback {display: none;}</style><div id="sk-d0e2e311-416b-4a48-aa9a-44adf04b1ee3" class="sk-top-container" style="overflow: auto;"><div class="sk-text-repr-fallback"><pre>Pipeline(steps=[(&#x27;onehotencoder&#x27;,OneHotEncoder(handle_unknown=&#x27;ignore&#x27;, sparse=False)),(&#x27;xgbregressor&#x27;,XGBRegressor(base_score=None, booster=None, callbacks=None,colsample_bylevel=None, colsample_bynode=None,colsample_bytree=None, early_stopping_rounds=None,enable_categorical=False, eval_metric=None,feature_types=None, gamma=None, gpu_id=None,grow_policy=None, importance_type=None,interaction_constraints=None, learning_rate=None,max_bin=None, max_cat_threshold=None,max_cat_to_onehot=None, max_delta_step=None,max_depth=5, max_leaves=None,min_child_weight=None, missing=nan,monotone_constraints=None, n_estimators=100,n_jobs=None, num_parallel_tree=None,predictor=None, random_state=None, ...))])</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="3e1fc9fd-9464-4cf2-a34f-716e1f03bb90" type="checkbox" ><label for="3e1fc9fd-9464-4cf2-a34f-716e1f03bb90" class="sk-toggleable__label sk-toggleable__label-arrow">Pipeline</label><div class="sk-toggleable__content"><pre>Pipeline(steps=[(&#x27;onehotencoder&#x27;,OneHotEncoder(handle_unknown=&#x27;ignore&#x27;, sparse=False)),(&#x27;xgbregressor&#x27;,XGBRegressor(base_score=None, booster=None, callbacks=None,colsample_bylevel=None, colsample_bynode=None,colsample_bytree=None, early_stopping_rounds=None,enable_categorical=False, eval_metric=None,feature_types=None, gamma=None, gpu_id=None,grow_policy=None, importance_type=None,interaction_constraints=None, learning_rate=None,max_bin=None, max_cat_threshold=None,max_cat_to_onehot=None, max_delta_step=None,max_depth=5, max_leaves=None,min_child_weight=None, missing=nan,monotone_constraints=None, n_estimators=100,n_jobs=None, num_parallel_tree=None,predictor=None, random_state=None, ...))])</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="064b4f21-1fc7-4646-9751-108c0cbbd266" type="checkbox" ><label for="064b4f21-1fc7-4646-9751-108c0cbbd266" class="sk-toggleable__label sk-toggleable__label-arrow">OneHotEncoder</label><div class="sk-toggleable__content"><pre>OneHotEncoder(handle_unknown=&#x27;ignore&#x27;, sparse=False)</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="8239516d-467c-4346-82ae-95b2c33e2b8a" type="checkbox" ><label for="8239516d-467c-4346-82ae-95b2c33e2b8a" class="sk-toggleable__label sk-toggleable__label-arrow">XGBRegressor</label><div class="sk-toggleable__content"><pre>XGBRegressor(base_score=None, booster=None, callbacks=None,colsample_bylevel=None, colsample_bynode=None,colsample_bytree=None, early_stopping_rounds=None,enable_categorical=False, eval_metric=None, feature_types=None,gamma=None, gpu_id=None, grow_policy=None, importance_type=None,interaction_constraints=None, learning_rate=None, max_bin=None,max_cat_threshold=None, max_cat_to_onehot=None,max_delta_step=None, max_depth=5, max_leaves=None,min_child_weight=None, missing=nan, monotone_constraints=None,n_estimators=100, n_jobs=None, num_parallel_tree=None,predictor=None, random_state=None, ...)</pre></div></div></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.

| Metric             |   Value |
|--------------------|---------|
| R squared          | 0.382   |
| Mean Squared Error | 0.43055 |


# Feature Importance Plot

<style>table.eli5-weights tr:hover {filter: brightness(85%);}</style><p>Explained as: feature importances</p><pre>XGBoost feature importances; values are numbers 0 <= x <= 1;all values sum to 1.</pre><table class="eli5-weights eli5-feature-importances" style="border-collapse: collapse; border: none; margin-top: 0em; table-layout: auto;"><thead><tr style="border: none;"><th style="padding: 0 1em 0 0.5em; text-align: right; border: none;">Weight</th><th style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">Feature</th></tr></thead><tbody><tr style="background-color: hsl(120, 100.00%, 80.00%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.3592</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x26_5</td></tr><tr style="background-color: hsl(120, 100.00%, 94.98%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0499</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x26_1</td></tr><tr style="background-color: hsl(120, 100.00%, 95.83%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0383</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x26_4</td></tr><tr style="background-color: hsl(120, 100.00%, 96.28%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0325</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x23_3</td></tr><tr style="background-color: hsl(120, 100.00%, 96.85%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0256</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x28_0</td></tr><tr style="background-color: hsl(120, 100.00%, 97.09%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0229</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x30_10</td></tr><tr style="background-color: hsl(120, 100.00%, 97.15%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0222</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x8_health</td></tr><tr style="background-color: hsl(120, 100.00%, 97.32%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0203</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x29_10</td></tr><tr style="background-color: hsl(120, 100.00%, 97.35%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0200</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x14_2</td></tr><tr style="background-color: hsl(120, 100.00%, 97.35%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0200</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x7_3</td></tr><tr style="background-color: hsl(120, 100.00%, 97.36%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0199</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x31_16</td></tr><tr style="background-color: hsl(120, 100.00%, 97.55%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0179</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x28_8</td></tr><tr style="background-color: hsl(120, 100.00%, 97.78%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0155</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x28_6</td></tr><tr style="background-color: hsl(120, 100.00%, 97.78%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0155</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x11_mother</td></tr><tr style="background-color: hsl(120, 100.00%, 97.85%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0149</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x29_12</td></tr><tr style="background-color: hsl(120, 100.00%, 97.89%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0145</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x26_2</td></tr><tr style="background-color: hsl(120, 100.00%, 97.96%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0138</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x21_no</td></tr><tr style="background-color: hsl(120, 100.00%, 98.24%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0112</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x6_2</td></tr><tr style="background-color: hsl(120, 100.00%, 98.39%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0098</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x14_0</td></tr><tr style="background-color: hsl(120, 100.00%, 98.47%); border: none;"><td style="padding: 0 1em 0 0.5em; text-align: right; border: none;">0.0092</td><td style="padding: 0 0.5em 0 0.5em; text-align: left; border: none;">x18_no</td></tr><tr style="background-color: hsl(120, 100.00%, 98.47%); border: none;"><td colspan="2" style="padding: 0 0.5em 0 0.5em; text-align: center; border: none; white-space: nowrap;"><i>&hellip; 161 more &hellip;</i></td></tr></tbody></table>
