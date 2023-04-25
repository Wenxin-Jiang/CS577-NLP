---
library_name: sklearn
tags:
- sklearn
- skops
- text-classification
model_file: middle_dutch_text-classification.pkl
widget:
- text: "Wje mayelin onghereit pieter van der beyke andries jnghel jehan de bleyer en jacob de bere Sceipenen mire vrauwen der Abbedessen van meessine jn nortscoten ende jn zuutscoten jn dien tyden doen te weitene tolle den gonen die deisen chaertre sullen zien of horen leisen Dat ledenaerd van den cole portre jn ypre heift ghecocht en ghecreighe ervelike te sine bouf en te sijns hoyrs bouf jeghen jacob cruken poortre jn ypre .vijf. vierendeel ymeits lants ligghende jn de proghye van zuutscote namelike binder vierscare mire vrauwen vors dat es te weitene oostwaert over dypre jeghe de woninghe marie sbuerechgrauen oostwaert over de strate streckende oost wart toter steenstrate moelne tussche martins broukers lande en johan covents lande an de zuutside ende clais onghereiden lande an de noortzide belast dit vors lant met twalef scellinghe en achte peninghe siaers erveliker rente."



---

# Model description

Middle Dutch NER with PassiveAgressiveClassifier

## Intended uses & limitations

This model is not ready to be used in production.

## Training Procedure

TESTING

### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter                  | Value                                                                                                                                                                            |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| memory                          |                                                                                                                                                                                  |
| steps                           | [('trans', FunctionTransformer(func=<function revert_data at 0x7f3fb95883a0>)), ('vectorizer', CountVectorizer()), ('classifier', PassiveAggressiveClassifier(random_state=42))] |
| verbose                         | False                                                                                                                                                                            |
| trans                           | FunctionTransformer(func=<function revert_data at 0x7f3fb95883a0>)                                                                                                               |
| vectorizer                      | CountVectorizer()                                                                                                                                                                |
| classifier                      | PassiveAggressiveClassifier(random_state=42)                                                                                                                                     |
| trans__accept_sparse            | False                                                                                                                                                                            |
| trans__check_inverse            | True                                                                                                                                                                             |
| trans__feature_names_out        |                                                                                                                                                                                  |
| trans__func                     | <function revert_data at 0x7f3fb95883a0>                                                                                                                                         |
| trans__inv_kw_args              |                                                                                                                                                                                  |
| trans__inverse_func             |                                                                                                                                                                                  |
| trans__kw_args                  |                                                                                                                                                                                  |
| trans__validate                 | False                                                                                                                                                                            |
| vectorizer__analyzer            | word                                                                                                                                                                             |
| vectorizer__binary              | False                                                                                                                                                                            |
| vectorizer__decode_error        | strict                                                                                                                                                                           |
| vectorizer__dtype               | <class 'numpy.int64'>                                                                                                                                                            |
| vectorizer__encoding            | utf-8                                                                                                                                                                            |
| vectorizer__input               | content                                                                                                                                                                          |
| vectorizer__lowercase           | True                                                                                                                                                                             |
| vectorizer__max_df              | 1.0                                                                                                                                                                              |
| vectorizer__max_features        |                                                                                                                                                                                  |
| vectorizer__min_df              | 1                                                                                                                                                                                |
| vectorizer__ngram_range         | (1, 1)                                                                                                                                                                           |
| vectorizer__preprocessor        |                                                                                                                                                                                  |
| vectorizer__stop_words          |                                                                                                                                                                                  |
| vectorizer__strip_accents       |                                                                                                                                                                                  |
| vectorizer__token_pattern       | (?u)\b\w\w+\b                                                                                                                                                                    |
| vectorizer__tokenizer           |                                                                                                                                                                                  |
| vectorizer__vocabulary          |                                                                                                                                                                                  |
| classifier__C                   | 1.0                                                                                                                                                                              |
| classifier__average             | False                                                                                                                                                                            |
| classifier__class_weight        |                                                                                                                                                                                  |
| classifier__early_stopping      | False                                                                                                                                                                            |
| classifier__fit_intercept       | True                                                                                                                                                                             |
| classifier__loss                | hinge                                                                                                                                                                            |
| classifier__max_iter            | 1000                                                                                                                                                                             |
| classifier__n_iter_no_change    | 5                                                                                                                                                                                |
| classifier__n_jobs              |                                                                                                                                                                                  |
| classifier__random_state        | 42                                                                                                                                                                               |
| classifier__shuffle             | True                                                                                                                                                                             |
| classifier__tol                 | 0.001                                                                                                                                                                            |
| classifier__validation_fraction | 0.1                                                                                                                                                                              |
| classifier__verbose             | 0                                                                                                                                                                                |
| classifier__warm_start          | False                                                                                                                                                                            |

</details>

### Model Plot

The model plot is below.

<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container" style="overflow: auto;"><div class="sk-text-repr-fallback"><pre>Pipeline(steps=[(&#x27;trans&#x27;,FunctionTransformer(func=&lt;function revert_data at 0x7f3fb95883a0&gt;)),(&#x27;vectorizer&#x27;, CountVectorizer()),(&#x27;classifier&#x27;, PassiveAggressiveClassifier(random_state=42))])</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" ><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">Pipeline</label><div class="sk-toggleable__content"><pre>Pipeline(steps=[(&#x27;trans&#x27;,FunctionTransformer(func=&lt;function revert_data at 0x7f3fb95883a0&gt;)),(&#x27;vectorizer&#x27;, CountVectorizer()),(&#x27;classifier&#x27;, PassiveAggressiveClassifier(random_state=42))])</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-2" type="checkbox" ><label for="sk-estimator-id-2" class="sk-toggleable__label sk-toggleable__label-arrow">FunctionTransformer</label><div class="sk-toggleable__content"><pre>FunctionTransformer(func=&lt;function revert_data at 0x7f3fb95883a0&gt;)</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-3" type="checkbox" ><label for="sk-estimator-id-3" class="sk-toggleable__label sk-toggleable__label-arrow">CountVectorizer</label><div class="sk-toggleable__content"><pre>CountVectorizer()</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-4" type="checkbox" ><label for="sk-estimator-id-4" class="sk-toggleable__label sk-toggleable__label-arrow">PassiveAggressiveClassifier</label><div class="sk-toggleable__content"><pre>PassiveAggressiveClassifier(random_state=42)</pre></div></div></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.

| Metric                  |    Value |
|-------------------------|----------|
| accuracy including 'O'  | 0.903724 |
| f1 score including 'O   | 0.903724 |
| precision excluding 'O' | 0.803184 |
| recall excluding 'O'    | 0.525071 |
| f1 excluding 'O'        | 0.635011 |

### Confusion Matrix

![Confusion Matrix](confusion_matrix.png)

# How to Get Started with the Model

[More Information Needed]

# Model Card Authors

Alassea TEST

# Model Card Contact

You can contact the model card authors through following channels:
[More Information Needed]

# Citation

**BibTeX**

```
@inproceedings{...,year={2022}}
```
