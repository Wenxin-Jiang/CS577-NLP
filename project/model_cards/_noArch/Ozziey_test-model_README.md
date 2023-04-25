---
license: mit
library_name: sklearn
tags:
- sklearn
- skops
- tabular-classification
model_file: HME_pickle
widget:
  structuredData:
    anger:
    - 0.13340177
    - 0.26429585
    - 0.75805366
    disgust:
    - 0.07661828
    - 0.14570697
    - 0.21044387
    fear:
    - 0.094705686
    - 0.057977196
    - 0.003689876
    joy:
    - 0.006762238
    - 0.2627153
    - 0.001755206
    neutral:
    - 0.03295978
    - 0.019884355
    - 0.013996695
    sadness:
    - 0.6507381
    - 0.24445744
    - 0.011482558
    surprise:
    - 0.004814104
    - 0.00496282
    - 0.000578273
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

| Hyperparameter   |   Value |
|------------------|---------|
| alpha            |       1 |
| class_prior      |         |
| fit_prior        |       1 |
| norm             |       0 |

</details>

### Model Plot

The model plot is below.

<style>#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 {color: black;background-color: white;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 pre{padding: 0;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-toggleable {background-color: white;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-estimator:hover {background-color: #d4ebff;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-item {z-index: 1;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-parallel-item:only-child::after {width: 0;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0 div.sk-text-repr-fallback {display: none;}</style><div id="sk-b53d2f4f-2533-401b-9a2a-da04c1fbfce0" class="sk-top-container" style="overflow: auto;"><div class="sk-text-repr-fallback"><pre>ComplementNB()</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="8d305fec-9b3e-4d4c-960e-2d386ab08acc" type="checkbox" checked><label for="8d305fec-9b3e-4d4c-960e-2d386ab08acc" class="sk-toggleable__label sk-toggleable__label-arrow">ComplementNB</label><div class="sk-toggleable__content"><pre>ComplementNB()</pre></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.

| Metric   |    Value |
|----------|----------|
| accuracy | 0.536424 |
| f1 score | 0.536424 |

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

# citation_bibtex

bibtex
@inproceedings{...,year={2022}}

# model_card_authors

skops_user

# limitations

This model is purely for academic purposes.

# model_description

This is a Complement NB model trained on a poetry dataset.

# eval_method

The model is evaluated using test split, on accuracy and F1 score with macro average.
