---
license: mit
library_name: sklearn
tags:
- sklearn
- skops
- text-classification
---

# Model description

This is a multinomial naive Bayes model trained on 20 new groups dataset. Count vectorizer and TFIDF vectorizer are used on top of the model.

## Intended uses & limitations

This model is not ready to be used in production.

## Training Procedure

### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter      | Value                                                                                  |
|---------------------|----------------------------------------------------------------------------------------|
| memory              |                                                                                        |
| steps               | [('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())] |
| verbose             | False                                                                                  |
| vect                | CountVectorizer()                                                                      |
| tfidf               | TfidfTransformer()                                                                     |
| clf                 | MultinomialNB()                                                                        |
| vect__analyzer      | word                                                                                   |
| vect__binary        | False                                                                                  |
| vect__decode_error  | strict                                                                                 |
| vect__dtype         | <class 'numpy.int64'>                                                                  |
| vect__encoding      | utf-8                                                                                  |
| vect__input         | content                                                                                |
| vect__lowercase     | True                                                                                   |
| vect__max_df        | 1.0                                                                                    |
| vect__max_features  |                                                                                        |
| vect__min_df        | 1                                                                                      |
| vect__ngram_range   | (1, 1)                                                                                 |
| vect__preprocessor  |                                                                                        |
| vect__stop_words    |                                                                                        |
| vect__strip_accents |                                                                                        |
| vect__token_pattern | (?u)\b\w\w+\b                                                                          |
| vect__tokenizer     |                                                                                        |
| vect__vocabulary    |                                                                                        |
| tfidf__norm         | l2                                                                                     |
| tfidf__smooth_idf   | True                                                                                   |
| tfidf__sublinear_tf | False                                                                                  |
| tfidf__use_idf      | True                                                                                   |
| clf__alpha          | 1.0                                                                                    |
| clf__class_prior    |                                                                                        |
| clf__fit_prior      | True                                                                                   |

</details>

### Model Plot

The model plot is below.

<style>#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 {color: black;background-color: white;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 pre{padding: 0;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-toggleable {background-color: white;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-estimator:hover {background-color: #d4ebff;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-item {z-index: 1;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-parallel-item:only-child::after {width: 0;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6 div.sk-text-repr-fallback {display: none;}</style><div id="sk-8f9616f3-01a7-4784-b5f5-5c31d2b0f7a6" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>Pipeline(steps=[(&#x27;vect&#x27;, CountVectorizer()), (&#x27;tfidf&#x27;, TfidfTransformer()),(&#x27;clf&#x27;, MultinomialNB())])</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="9caae382-ba9c-4e50-b4e0-017fa1bca4b4" type="checkbox" ><label for="9caae382-ba9c-4e50-b4e0-017fa1bca4b4" class="sk-toggleable__label sk-toggleable__label-arrow">Pipeline</label><div class="sk-toggleable__content"><pre>Pipeline(steps=[(&#x27;vect&#x27;, CountVectorizer()), (&#x27;tfidf&#x27;, TfidfTransformer()),(&#x27;clf&#x27;, MultinomialNB())])</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="6bf44786-d8ef-4af0-be6a-2ac8b82cf581" type="checkbox" ><label for="6bf44786-d8ef-4af0-be6a-2ac8b82cf581" class="sk-toggleable__label sk-toggleable__label-arrow">CountVectorizer</label><div class="sk-toggleable__content"><pre>CountVectorizer()</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="69b80eb1-41d4-421a-9875-a9e95faa6d45" type="checkbox" ><label for="69b80eb1-41d4-421a-9875-a9e95faa6d45" class="sk-toggleable__label sk-toggleable__label-arrow">TfidfTransformer</label><div class="sk-toggleable__content"><pre>TfidfTransformer()</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="63c8c7e2-7443-4092-a86b-32b1cbef1a1b" type="checkbox" ><label for="63c8c7e2-7443-4092-a86b-32b1cbef1a1b" class="sk-toggleable__label sk-toggleable__label-arrow">MultinomialNB</label><div class="sk-toggleable__content"><pre>MultinomialNB()</pre></div></div></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.



| Metric   | Value   |
|----------|---------|

# How to Get Started with the Model

Use the code below to get started with the model.

<details>
<summary> Click to expand </summary>

```python
import pickle
with open(pkl_filename, 'rb') as file:
    clf = pickle.load(file)
```

</details>




# Model Card Authors

This model card is written by following authors:

merve

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