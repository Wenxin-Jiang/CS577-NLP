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

This is a LogisticRegressionCV model trained on averages of patch embeddings from the Imagenette dataset. This forms the GAM of an [Emb-GAM](https://arxiv.org/abs/2209.11799) extended to images. Patch embeddings are meant to be extracted with the [`facebook/dino-vitb16` DINO checkpoint](https://huggingface.co/facebook/dino-vitb16).

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

<style>#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d {color: black;background-color: white;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d pre{padding: 0;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-toggleable {background-color: white;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-estimator:hover {background-color: #d4ebff;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-item {z-index: 1;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-parallel-item:only-child::after {width: 0;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-58b9b78a-229c-4a6a-b67b-244945cdc29d div.sk-text-repr-fallback {display: none;}</style><div id="sk-58b9b78a-229c-4a6a-b67b-244945cdc29d" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LogisticRegressionCV(cv=StratifiedKFold(n_splits=5, random_state=1, shuffle=True),random_state=1, refit=False)</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="d612eebc-39a3-42fc-99e0-37e6f258ac21" type="checkbox" checked><label for="d612eebc-39a3-42fc-99e0-37e6f258ac21" class="sk-toggleable__label sk-toggleable__label-arrow">LogisticRegressionCV</label><div class="sk-toggleable__content"><pre>LogisticRegressionCV(cv=StratifiedKFold(n_splits=5, random_state=1, shuffle=True),random_state=1, refit=False)</pre></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.



| Metric   |   Value |
|----------|---------|
| accuracy | 0.97707 |
| f1 score | 0.97707 |

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
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
feature_extractor = AutoFeatureExtractor.from_pretrained('facebook/dino-vitb16')
model = AutoModel.from_pretrained('facebook/dino-vitb16').eval().to(device)

# load logistic regression
os.mkdir('emb-gam-dino')
hub_utils.download(repo_id='Ramos-Ramos/emb-gam-dino', dst='emb-gam-dino')

with open('emb-gam-dino/model.pkl', 'rb') as file: 
  logistic_regression = pickle.load(file)
    
# load image
img = Image.open('examples/english_springer.png')

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

Patrick Ramos

# Model Card Contact

You can contact the model card authors through following channels:
[More Information Needed]

# Citation

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

# Demo

Check out our HuggingFace Space [here](https://huggingface.co/spaces/Ramos-Ramos/emb-gam-dino)! It does Imagenette classification and visualizes patch contributions per label.