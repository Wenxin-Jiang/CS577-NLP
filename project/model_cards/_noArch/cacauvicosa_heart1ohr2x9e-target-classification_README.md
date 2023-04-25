---
license: apache-2.0
library_name: sklearn
tags:
- tabular-classification
- baseline-trainer
---

## Baseline Model trained on heart1ohr2x9e to apply classification on target

**Metrics of the best model:**

accuracy             0.885854

average_precision    0.949471

roc_auc              0.050633

recall_macro         0.885324

f1_macro             0.885610

Name: LogisticRegression(class_weight='balanced', max_iter=1000), dtype: float64



**See model plot below:**

<style>#sk-container-id-8 {color: black;background-color: white;}#sk-container-id-8 pre{padding: 0;}#sk-container-id-8 div.sk-toggleable {background-color: white;}#sk-container-id-8 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-8 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-8 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-8 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-8 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-8 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-8 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-8 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-8 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-8 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-8 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-8 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-8 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-8 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-8 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-8 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-8 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-8 div.sk-item {position: relative;z-index: 1;}#sk-container-id-8 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-8 div.sk-item::before, #sk-container-id-8 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-8 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-8 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-8 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-8 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-8 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-8 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-8 div.sk-label-container {text-align: center;}#sk-container-id-8 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-8 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-8" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>Pipeline(steps=[(&#x27;easypreprocessor&#x27;,EasyPreprocessor(types=          continuous  dirty_float  low_card_int  ...   date  free_string  useless
age            False        False         False  ...  False        False    False
sex            False        False         False  ...  False        False    False
cp             False        False         False  ...  False        False    False
trestbps        True        False         False  ...  False        False    False
chol            True        False         False  ...  False        False    False
fbs            False        False         False  ...  False        False    False
restecg        False        Fa......  False        False    False
thalach         True        False         False  ...  False        False    False
exang          False        False         False  ...  False        False    False
oldpeak         True        False         False  ...  False        False    False
slope          False        False         False  ...  False        False    False
ca             False        False         False  ...  False        False    False
thal           False        False         False  ...  False        False    False[13 rows x 7 columns])),(&#x27;logisticregression&#x27;,LogisticRegression(C=1, class_weight=&#x27;balanced&#x27;,max_iter=1000))])</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-24" type="checkbox" ><label for="sk-estimator-id-24" class="sk-toggleable__label sk-toggleable__label-arrow">Pipeline</label><div class="sk-toggleable__content"><pre>Pipeline(steps=[(&#x27;easypreprocessor&#x27;,EasyPreprocessor(types=          continuous  dirty_float  low_card_int  ...   date  free_string  useless
age            False        False         False  ...  False        False    False
sex            False        False         False  ...  False        False    False
cp             False        False         False  ...  False        False    False
trestbps        True        False         False  ...  False        False    False
chol            True        False         False  ...  False        False    False
fbs            False        False         False  ...  False        False    False
restecg        False        Fa......  False        False    False
thalach         True        False         False  ...  False        False    False
exang          False        False         False  ...  False        False    False
oldpeak         True        False         False  ...  False        False    False
slope          False        False         False  ...  False        False    False
ca             False        False         False  ...  False        False    False
thal           False        False         False  ...  False        False    False[13 rows x 7 columns])),(&#x27;logisticregression&#x27;,LogisticRegression(C=1, class_weight=&#x27;balanced&#x27;,max_iter=1000))])</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-25" type="checkbox" ><label for="sk-estimator-id-25" class="sk-toggleable__label sk-toggleable__label-arrow">EasyPreprocessor</label><div class="sk-toggleable__content"><pre>EasyPreprocessor(types=          continuous  dirty_float  low_card_int  ...   date  free_string  useless
age            False        False         False  ...  False        False    False
sex            False        False         False  ...  False        False    False
cp             False        False         False  ...  False        False    False
trestbps        True        False         False  ...  False        False    False
chol            True        False         False  ...  False        False    False
fbs            False        False         False  ...  False        False    False
restecg        False        False         False  ...  False        False    False
thalach         True        False         False  ...  False        False    False
exang          False        False         False  ...  False        False    False
oldpeak         True        False         False  ...  False        False    False
slope          False        False         False  ...  False        False    False
ca             False        False         False  ...  False        False    False
thal           False        False         False  ...  False        False    False[13 rows x 7 columns])</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-26" type="checkbox" ><label for="sk-estimator-id-26" class="sk-toggleable__label sk-toggleable__label-arrow">LogisticRegression</label><div class="sk-toggleable__content"><pre>LogisticRegression(C=1, class_weight=&#x27;balanced&#x27;, max_iter=1000)</pre></div></div></div></div></div></div></div>

**Disclaimer:** This model is trained with dabl library as a baseline, for better results, use [AutoTrain](https://huggingface.co/autotrain).

**Logs of training** including the models tried in the process can be found in logs.txt