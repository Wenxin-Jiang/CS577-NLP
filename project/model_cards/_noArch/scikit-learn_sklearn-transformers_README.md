---
license: apache-2.0
tags:
- text-classification
- generic
- notebook-favorites
library_name: generic
---
## Hugging Face Transformers with Scikit-learn Classifiers 🤩🌟

This repository contains a small proof-of-concept pipeline that leverages longformer embeddings with scikit-learn Logistic Regression that does sentiment analysis. 
The training leverages the language module of [whatlies](https://github.com/koaning/whatlies).
See the tutorial notebook [here](https://www.kaggle.com/code/unofficialmerve/scikit-learn-with-transformers/notebook).

# Classification Report 📈
Below is the classification report 👇🏻
```
              precision    recall  f1-score   support

           0       0.85      0.89      0.87       522
           1       0.89      0.85      0.87       550

    accuracy                           0.87      1072
   macro avg       0.87      0.87      0.87      1072
weighted avg       0.87      0.87      0.87      1072
```
# Pipeline 🌟
Below you can see the pipeline 👇🏻 (it's interactive! 🪄)
<style>#sk-40148507-8fa3-419e-8462-0cd31028ba20 {color: black;background-color: white;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 pre{padding: 0;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-toggleable {background-color: white;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-estimator:hover {background-color: #d4ebff;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-item {z-index: 1;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-parallel-item:only-child::after {width: 0;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-container {/* jupyter\'s `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-40148507-8fa3-419e-8462-0cd31028ba20 div.sk-text-repr-fallback {display: none;}</style><div id="sk-40148507-8fa3-419e-8462-0cd31028ba20" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>Pipeline(steps=[(&#x27;embedding&#x27;,\n                 HFTransformersLanguage(model_name_or_path=&#x27;facebook/bart-base&#x27;)),\n                (&#x27;model&#x27;, LogisticRegression())])</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="9042928c-84ce-45ec-a5c0-181ce820f2c7" type="checkbox" ><label for="9042928c-84ce-45ec-a5c0-181ce820f2c7" class="sk-toggleable__label sk-toggleable__label-arrow">Pipeline</label><div class="sk-toggleable__content"><pre>Pipeline(steps=[(&#x27;embedding&#x27;,\n                 HFTransformersLanguage(model_name_or_path=&#x27;facebook/bart-base&#x27;)),\n                (&#x27;model&#x27;, LogisticRegression())])</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="55bb4869-7378-430d-a174-0c343e24018c" type="checkbox" ><label for="55bb4869-7378-430d-a174-0c343e24018c" class="sk-toggleable__label sk-toggleable__label-arrow">HFTransformersLanguage</label><div class="sk-toggleable__content"><pre>HFTransformersLanguage(model_name_or_path=&#x27;facebook/bart-base&#x27;)</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="c6377f91-830e-4547-9bf8-9d4f0aa2fb8c" type="checkbox" ><label for="c6377f91-830e-4547-9bf8-9d4f0aa2fb8c" class="sk-toggleable__label sk-toggleable__label-arrow">LogisticRegression</label><div class="sk-toggleable__content"><pre>LogisticRegression()</pre></div></div></div></div></div></div></div>

# Hyperparameters ❤️
You can find hyperparameters below 👇🏻✨
```
{'memory': None,
 'steps': [('embedding',
   HFTransformersLanguage(model_name_or_path='facebook/bart-base')),
  ('model', LogisticRegression())],
 'verbose': False,
 'embedding': HFTransformersLanguage(model_name_or_path='facebook/bart-base'),
 'model': LogisticRegression(),
 'embedding__model_name_or_path': 'facebook/bart-base',
 'model__C': 1.0,
 'model__class_weight': None,
 'model__dual': False,
 'model__fit_intercept': True,
 'model__intercept_scaling': 1,
 'model__l1_ratio': None,
 'model__max_iter': 100,
 'model__multi_class': 'auto',
 'model__n_jobs': None,
 'model__penalty': 'l2',
 'model__random_state': None,
 'model__solver': 'lbfgs',
 'model__tol': 0.0001,
 'model__verbose': 0,
 'model__warm_start': False}
 ```