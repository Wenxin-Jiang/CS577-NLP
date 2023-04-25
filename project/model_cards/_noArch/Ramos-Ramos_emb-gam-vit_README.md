---
license: mit
library_name: sklearn
tags:
- sklearn
- skops
- tabular-classification
- visual emb-gam
---

# Model description

This is a LogisticRegressionCV model trained on averages of patch embeddings from the Imagenette dataset. This forms the GAM of an [Emb-GAM](https://arxiv.org/abs/2209.11799) extended to images. Patch embeddings are meant to be extracted with the [`google/vit-base-patch16-224` ViT checkpoint](https://huggingface.co/google/vit-base-patch16-224).

## Intended uses & limitations

This model is not intended to be used in production.

## Training Procedure

### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter    | Value                                                     |
|-------------------|-----------------------------------------------------------|
| Cs                | 10                                                        |
| class_weight      |                                                           |
| cv                | StratifiedKFold(n_splits=5, random_state=1, shuffle=True) |
| dual              | False                                                     |
| fit_intercept     | True                                                      |
| intercept_scaling | 1.0                                                       |
| l1_ratios         |                                                           |
| max_iter          | 100                                                       |
| multi_class       | auto                                                      |
| n_jobs            |                                                           |
| penalty           | l2                                                        |
| random_state      | 1                                                         |
| refit             | False                                                     |
| scoring           |                                                           |
| solver            | lbfgs                                                     |
| tol               | 0.0001                                                    |
| verbose           | 0                                                         |

</details>

### Model Plot

The model plot is below.

<style>#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e {color: black;background-color: white;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e pre{padding: 0;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-toggleable {background-color: white;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-estimator:hover {background-color: #d4ebff;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-item {z-index: 1;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-parallel-item:only-child::after {width: 0;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-57980b4f-6828-4a54-ae50-b50e1f9f097e div.sk-text-repr-fallback {display: none;}</style><div id="sk-57980b4f-6828-4a54-ae50-b50e1f9f097e" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LogisticRegressionCV(cv=StratifiedKFold(n_splits=5, random_state=1, shuffle=True),random_state=1, refit=False)</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="51ec5e46-9aaa-4487-adda-6718142c9f85" type="checkbox" checked><label for="51ec5e46-9aaa-4487-adda-6718142c9f85" class="sk-toggleable__label sk-toggleable__label-arrow">LogisticRegressionCV</label><div class="sk-toggleable__content"><pre>LogisticRegressionCV(cv=StratifiedKFold(n_splits=5, random_state=1, shuffle=True),random_state=1, refit=False)</pre></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.



| Metric   |   Value |
|----------|---------|
| accuracy | 0.99465 |
| f1 score | 0.99465 |

# How to Get Started with the Model

Use the code below to get started with the model.

<details>
<summary> Click to expand </summary>

```python
from PIL import Image
from skops import hub_utils
import torch
from transformers import AutoFeatureExtractor, AutoModel
import pickle
import os

# load embedding model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
feature_extractor = AutoFeatureExtractor.from_pretrained("google/vit-base-patch16-224")
model = AutoModel.from_pretrained("google/vit-base-patch16-224").eval().to(device)

# load logistic regression
os.mkdir("emb-gam-vit")
hub_utils.download(repo_id="Ramos-Ramos/emb-gam-vit", dst="emb-gam-vit")

with open("emb-gam-vit/model.pkl", "rb") as file: 
  logistic_regression = pickle.load(file)
    
# load image
img = Image.open("examples/english_springer.png")

# preprocess image
inputs = {k: v.to(device) for k, v in feature_extractor(img, return_tensors='pt').items()}

# extract patch embeddings
with torch.no_grad():
  patch_embeddings = model(**inputs).last_hidden_state[0, 1:].cpu()

# classify
pred = logistic_regression.predict(patch_embeddings.sum(dim=0, keepdim=True))

# get patch contributions
patch_contributions = logistic_regression.coef_ @ patch_embeddings.T.numpy()
```

</details>




# Model Card Authors

This model card is written by following authors:

Patrick Ramos and Ryan Ramos

# Model Card Contact

You can contact the model card authors through following channels:
[More Information Needed]

# Citation

Below you can find information related to citation.

**BibTeX:**
```
@article{singh2022emb,
  title={Emb-GAM: an Interpretable and Efficient Predictor using Pre-trained Language Models},
  author={Singh, Chandan and Gao, Jianfeng},
  journal={arXiv preprint arXiv:2209.11799},
  year={2022}
}
```


# Additional Content

## confusion_matrix

![confusion_matrix](confusion_matrix.png)