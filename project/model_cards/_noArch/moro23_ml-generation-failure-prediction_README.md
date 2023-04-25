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
    - -0.09914599897912607
    - 0.1924502175495108
    - -0.17512599701971115
    x1:
    - -1.3527180038544737
    - -0.30254418369353936
    - -0.3432808784971574
    x10:
    - -1.033043867154581
    - 1.181705677961924
    - -0.9707375350979036
    x11:
    - -0.20058976250553548
    - -0.4075697886243593
    - 0.6689385877105022
    x12:
    - 1.1264447260202237
    - -0.3277542910601845
    - -0.7061243553947382
    x13:
    - 2.3578550805452707
    - -0.2452873082756669
    - 0.16449778472088433
    x14:
    - -0.16970349843770105
    - 0.15845033365719116
    - 0.6702026662867782
    x15:
    - 1.02155174900202
    - -0.4957105400056871
    - 0.3067590970166067
    x16:
    - 0.6475392302343093
    - -1.1039038751689478
    - 0.7252174341663654
    x17:
    - -0.6561708760276103
    - 0.4740018109547748
    - 0.465681500410126
    x18:
    - -0.6490963010371028
    - 0.17088731040051813
    - -0.17090270391075216
    x19:
    - 1.993556271321547
    - -0.8900413826773769
    - 0.4823497456924965
    x2:
    - -0.08333069468143207
    - -0.5776679970917816
    - 0.4719859556084112
    x20:
    - 0.38373337482281333
    - 0.11724727885071742
    - 0.41793176854856023
    x21:
    - -0.48219399953359454
    - 0.5483595851446571
    - -0.2845084323579843
    x22:
    - 0.6002099386032473
    - -0.3328169335193628
    - -0.1177130496330338
    x23:
    - -0.9986427796510361
    - -0.12805445675530894
    - 0.16764132064699072
    x24:
    - 0.9191079842956807
    - -0.2904321748144559
    - 0.9305255321835336
    x25:
    - -1.0662088112874974
    - -0.5211282845791263
    - -0.4395435923307972
    x26:
    - 0.07671124580480018
    - 0.830067710593458
    - 0.10148248620612801
    x27:
    - -0.19394704099684984
    - 0.3655010965468254
    - 0.2082667800019003
    x28:
    - -1.06070986806479
    - 0.45059914693412395
    - -0.42221731060136036
    x29:
    - -0.49547996576705416
    - 0.293080871191101
    - -0.7124529042788277
    x3:
    - 0.40319634268672655
    - -0.7266844038748933
    - -0.4392535240984599
    x30:
    - 0.3177776541070613
    - -0.6555347490121567
    - 0.6992894776600148
    x31:
    - 0.36132913089368796
    - -0.5052005518828991
    - -0.29502005278945825
    x32:
    - -1.5275287471841141
    - 0.6835310518117088
    - -0.852342002620441
    x33:
    - 0.41861643726463144
    - 0.24432341138030303
    - 0.28970967818031484
    x34:
    - -0.5635425334957935
    - -0.057994651130336465
    - -0.5481205839673382
    x35:
    - 0.6952237303944357
    - -0.2186268698466881
    - 1.083122777048039
    x36:
    - 0.7923281272792859
    - -0.27781559530809646
    - 0.7338411152759391
    x37:
    - -2.5752767636847587
    - 1.386096372652616
    - -0.3566644498671143
    x38:
    - -0.24870867574122876
    - 0.47352314520838223
    - 0.5234704003548943
    x39:
    - -0.1901453323468956
    - -0.20338282797456578
    - 0.8470486651132534
    x4:
    - -0.5374409606451687
    - -0.45754391548594736
    - 0.27538071985784895
    x5:
    - -1.7151691480844589
    - 1.5828928158435347
    - -0.47142929432970415
    x6:
    - -0.5429735469430116
    - 0.24865361490379212
    - 0.10442729092365317
    x7:
    - 1.5994259033001812
    - -1.1704887195126548
    - 0.5751493156703039
    x8:
    - 0.5660448068869487
    - -0.14629006117952106
    - -0.7940429338085028
    x9:
    - -0.14997228968462223
    - 0.9027177003558653
    - 0.21863455413984226
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

| Hyperparameter          | Value           |
|-------------------------|-----------------|
| objective               | binary:logistic |
| use_label_encoder       |                 |
| base_score              | 0.5             |
| booster                 | gbtree          |
| callbacks               |                 |
| colsample_bylevel       | 1               |
| colsample_bynode        | 1               |
| colsample_bytree        | 1               |
| early_stopping_rounds   |                 |
| enable_categorical      | False           |
| eval_metric             | logloss         |
| feature_types           |                 |
| gamma                   | 3               |
| gpu_id                  | -1              |
| grow_policy             | depthwise       |
| importance_type         |                 |
| interaction_constraints |                 |
| learning_rate           | 0.1             |
| max_bin                 | 256             |
| max_cat_threshold       | 64              |
| max_cat_to_onehot       | 4               |
| max_delta_step          | 0               |
| max_depth               | 6               |
| max_leaves              | 0               |
| min_child_weight        | 1               |
| missing                 | nan             |
| monotone_constraints    | ()              |
| n_estimators            | 250             |
| n_jobs                  | 0               |
| num_parallel_tree       | 1               |
| predictor               | auto            |
| random_state            | 1               |
| reg_alpha               | 0               |
| reg_lambda              | 1               |
| sampling_method         | uniform         |
| scale_pos_weight        | 10              |
| subsample               | 0.8             |
| tree_method             | exact           |
| validate_parameters     | 1               |
| verbosity               |                 |

</details>

### Model Plot

The model plot is below.

<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-2" class="sk-top-container" style="overflow: auto;"><div class="sk-text-repr-fallback"><pre>XGBClassifier(base_score=0.5, booster=&#x27;gbtree&#x27;, callbacks=None,colsample_bylevel=1, colsample_bynode=1, colsample_bytree=1,early_stopping_rounds=None, enable_categorical=False,eval_metric=&#x27;logloss&#x27;, feature_types=None, gamma=3, gpu_id=-1,grow_policy=&#x27;depthwise&#x27;, importance_type=None,interaction_constraints=&#x27;&#x27;, learning_rate=0.1, max_bin=256,max_cat_threshold=64, max_cat_to_onehot=4, max_delta_step=0,max_depth=6, max_leaves=0, min_child_weight=1, missing=nan,monotone_constraints=&#x27;()&#x27;, n_estimators=250, n_jobs=0,num_parallel_tree=1, predictor=&#x27;auto&#x27;, random_state=1, ...)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-2" type="checkbox" checked><label for="sk-estimator-id-2" class="sk-toggleable__label sk-toggleable__label-arrow">XGBClassifier</label><div class="sk-toggleable__content"><pre>XGBClassifier(base_score=0.5, booster=&#x27;gbtree&#x27;, callbacks=None,colsample_bylevel=1, colsample_bynode=1, colsample_bytree=1,early_stopping_rounds=None, enable_categorical=False,eval_metric=&#x27;logloss&#x27;, feature_types=None, gamma=3, gpu_id=-1,grow_policy=&#x27;depthwise&#x27;, importance_type=None,interaction_constraints=&#x27;&#x27;, learning_rate=0.1, max_bin=256,max_cat_threshold=64, max_cat_to_onehot=4, max_delta_step=0,max_depth=6, max_leaves=0, min_child_weight=1, missing=nan,monotone_constraints=&#x27;()&#x27;, n_estimators=250, n_jobs=0,num_parallel_tree=1, predictor=&#x27;auto&#x27;, random_state=1, ...)</pre></div></div></div></div></div>

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

# model_card_authors

Moro abdul Wahab

# model_description

ML classification model to predict or identify failures in a generator
