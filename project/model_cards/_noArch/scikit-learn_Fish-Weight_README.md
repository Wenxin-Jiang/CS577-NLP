---
license: mit
library_name: sklearn
tags:
- sklearn
- skops
- tabular-regression
widget:
  structuredData:
    Height:
    - 11.52
    - 12.48
    - 12.3778
    Length1:
    - 23.2
    - 24.0
    - 23.9
    Length2:
    - 25.4
    - 26.3
    - 26.5
    Length3:
    - 30.0
    - 31.2
    - 31.1
    Species:
    - Bream
    - Bream
    - Bream
    Width:
    - 4.02
    - 4.3056
    - 4.6961
---

# Model description

This is a GradientBoostingRegressor on a fish dataset.

## Intended uses & limitations

This model is intended for educational purposes.


### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter                                      | Value                                                                                                                                                              |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| memory                                              |                                                                                                                                                                    |
| steps                                               | [('columntransformer', ColumnTransformer(remainder='passthrough',transformers=[('onehotencoder',OneHotEncoder(handle_unknown='ignore',sparse=False),<sklearn.compose._column_transformer.make_column_selector object at 0x000001E750BBC6A0>)])), ('gradientboostingregressor', GradientBoostingRegressor(random_state=42))]                                                                                                                                                                    |
| verbose                                             | False                                                                                                                                                              |
| columntransformer                                   | ColumnTransformer(remainder='passthrough',transformers=[('onehotencoder',OneHotEncoder(handle_unknown='ignore',sparse=False),<sklearn.compose._column_transformer.make_column_selector object at 0x000001E750BBC6A0>)])                                                                                                                                                                    |
| gradientboostingregressor                           | GradientBoostingRegressor(random_state=42)                                                                                                                         |
| columntransformer__n_jobs                           |                                                                                                                                                                    |
| columntransformer__remainder                        | passthrough                                                                                                                                                        |
| columntransformer__sparse_threshold                 | 0.3                                                                                                                                                                |
| columntransformer__transformer_weights              |                                                                                                                                                                    |
| columntransformer__transformers                     | [('onehotencoder', OneHotEncoder(handle_unknown='ignore', sparse=False), <sklearn.compose._column_transformer.make_column_selector object at 0x000001E750BBC6A0>)] |
| columntransformer__verbose                          | False                                                                                                                                                              |
| columntransformer__verbose_feature_names_out        | True                                                                                                                                                               |
| columntransformer__onehotencoder                    | OneHotEncoder(handle_unknown='ignore', sparse=False)                                                                                                               |
| columntransformer__onehotencoder__categories        | auto                                                                                                                                                               |
| columntransformer__onehotencoder__drop              |                                                                                                                                                                    |
| columntransformer__onehotencoder__dtype             | <class 'numpy.float64'>                                                                                                                                            |
| columntransformer__onehotencoder__handle_unknown    | ignore                                                                                                                                                             |
| columntransformer__onehotencoder__sparse            | False                                                                                                                                                              |
| gradientboostingregressor__alpha                    | 0.9                                                                                                                                                                |
| gradientboostingregressor__ccp_alpha                | 0.0                                                                                                                                                                |
| gradientboostingregressor__criterion                | friedman_mse                                                                                                                                                       |
| gradientboostingregressor__init                     |                                                                                                                                                                    |
| gradientboostingregressor__learning_rate            | 0.1                                                                                                                                                                |
| gradientboostingregressor__loss                     | squared_error                                                                                                                                                      |
| gradientboostingregressor__max_depth                | 3                                                                                                                                                                  |
| gradientboostingregressor__max_features             |                                                                                                                                                                    |
| gradientboostingregressor__max_leaf_nodes           |                                                                                                                                                                    |
| gradientboostingregressor__min_impurity_decrease    | 0.0                                                                                                                                                                |
| gradientboostingregressor__min_samples_leaf         | 1                                                                                                                                                                  |
| gradientboostingregressor__min_samples_split        | 2                                                                                                                                                                  |
| gradientboostingregressor__min_weight_fraction_leaf | 0.0                                                                                                                                                                |
| gradientboostingregressor__n_estimators             | 100                                                                                                                                                                |
| gradientboostingregressor__n_iter_no_change         |                                                                                                                                                                    |
| gradientboostingregressor__random_state             | 42                                                                                                                                                                 |
| gradientboostingregressor__subsample                | 1.0                                                                                                                                                                |
| gradientboostingregressor__tol                      | 0.0001                                                                                                                                                             |
| gradientboostingregressor__validation_fraction      | 0.1                                                                                                                                                                |
| gradientboostingregressor__verbose                  | 0                                                                                                                                                                  |
| gradientboostingregressor__warm_start               | False                                                                                                                                                              |

</details>

### Model Plot

The model plot is below.

<style>#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 {color: black;background-color: white;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 pre{padding: 0;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-toggleable {background-color: white;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-estimator:hover {background-color: #d4ebff;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-item {z-index: 1;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-parallel-item:only-child::after {width: 0;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794 div.sk-text-repr-fallback {display: none;}</style><div id="sk-ccf5150a-bed5-4d7b-a5a9-a1a6d13a1794" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>Pipeline(steps=[(&#x27;columntransformer&#x27;,ColumnTransformer(remainder=&#x27;passthrough&#x27;,transformers=[(&#x27;onehotencoder&#x27;,OneHotEncoder(handle_unknown=&#x27;ignore&#x27;,sparse=False),&lt;sklearn.compose._column_transformer.make_column_selector object at 0x000001E750BBC6A0&gt;)])),(&#x27;gradientboostingregressor&#x27;,GradientBoostingRegressor(random_state=42))])</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="f6612892-c085-4dd9-8dca-9cb8081c3777" type="checkbox" ><label for="f6612892-c085-4dd9-8dca-9cb8081c3777" class="sk-toggleable__label sk-toggleable__label-arrow">Pipeline</label><div class="sk-toggleable__content"><pre>Pipeline(steps=[(&#x27;columntransformer&#x27;,ColumnTransformer(remainder=&#x27;passthrough&#x27;,transformers=[(&#x27;onehotencoder&#x27;,OneHotEncoder(handle_unknown=&#x27;ignore&#x27;,sparse=False),&lt;sklearn.compose._column_transformer.make_column_selector object at 0x000001E750BBC6A0&gt;)])),(&#x27;gradientboostingregressor&#x27;,GradientBoostingRegressor(random_state=42))])</pre></div></div></div><div class="sk-serial"><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="3d74f98b-ae31-452d-af87-2c65b0323ba2" type="checkbox" ><label for="3d74f98b-ae31-452d-af87-2c65b0323ba2" class="sk-toggleable__label sk-toggleable__label-arrow">columntransformer: ColumnTransformer</label><div class="sk-toggleable__content"><pre>ColumnTransformer(remainder=&#x27;passthrough&#x27;,transformers=[(&#x27;onehotencoder&#x27;,OneHotEncoder(handle_unknown=&#x27;ignore&#x27;,sparse=False),&lt;sklearn.compose._column_transformer.make_column_selector object at 0x000001E750BBC6A0&gt;)])</pre></div></div></div><div class="sk-parallel"><div class="sk-parallel-item"><div class="sk-item"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="4af39992-03cf-4522-a288-2db0a787a63c" type="checkbox" ><label for="4af39992-03cf-4522-a288-2db0a787a63c" class="sk-toggleable__label sk-toggleable__label-arrow">onehotencoder</label><div class="sk-toggleable__content"><pre>&lt;sklearn.compose._column_transformer.make_column_selector object at 0x000001E750BBC6A0&gt;</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="519d5e51-5fa6-45d6-a3f7-59c11370402d" type="checkbox" ><label for="519d5e51-5fa6-45d6-a3f7-59c11370402d" class="sk-toggleable__label sk-toggleable__label-arrow">OneHotEncoder</label><div class="sk-toggleable__content"><pre>OneHotEncoder(handle_unknown=&#x27;ignore&#x27;, sparse=False)</pre></div></div></div></div></div></div><div class="sk-parallel-item"><div class="sk-item"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="7ede29a7-2614-4eed-a021-e85f1aaa5659" type="checkbox" ><label for="7ede29a7-2614-4eed-a021-e85f1aaa5659" class="sk-toggleable__label sk-toggleable__label-arrow">remainder</label><div class="sk-toggleable__content"><pre>[&#x27;Length1&#x27;, &#x27;Length2&#x27;, &#x27;Length3&#x27;, &#x27;Height&#x27;, &#x27;Width&#x27;]</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="69357535-0314-4987-a311-112335d2cb52" type="checkbox" ><label for="69357535-0314-4987-a311-112335d2cb52" class="sk-toggleable__label sk-toggleable__label-arrow">passthrough</label><div class="sk-toggleable__content"><pre>passthrough</pre></div></div></div></div></div></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="f247fbf2-2247-4e99-aaa2-f6fb89ce1b13" type="checkbox" ><label for="f247fbf2-2247-4e99-aaa2-f6fb89ce1b13" class="sk-toggleable__label sk-toggleable__label-arrow">GradientBoostingRegressor</label><div class="sk-toggleable__content"><pre>GradientBoostingRegressor(random_state=42)</pre></div></div></div></div></div></div></div>


# How to Get Started with the Model

Use the code below to get started with the model.

<details>
<summary> Click to expand </summary>

```python
from skops.hub_utils import download
from skops.io import load

download("brendenc/Fish-Weight", "path_to_folder")
# make sure model file is in skops format
# if model is a pickle file, make sure it's from a source you trust
model = load("path_to_folder/example.pkl")
```

</details>



# Model Card Authors

This model card is written by following authors:

Brenden Connors

