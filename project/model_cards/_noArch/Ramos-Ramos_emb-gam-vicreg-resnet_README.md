---
license: mit
library_name: sklearn
tags:
- sklearn
- skops
- tabular-classification
model_file: model.pkl
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

<style>#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 {color: black;background-color: white;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 pre{padding: 0;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-toggleable {background-color: white;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-estimator:hover {background-color: #d4ebff;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-item {z-index: 1;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-parallel-item:only-child::after {width: 0;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-3244a8f9-b723-4dac-a610-2fbd0449e147 div.sk-text-repr-fallback {display: none;}</style><div id="sk-3244a8f9-b723-4dac-a610-2fbd0449e147" class="sk-top-container" style="overflow: auto;"><div class="sk-text-repr-fallback"><pre>LogisticRegressionCV(cv=StratifiedKFold(n_splits=5, random_state=1, shuffle=True),random_state=1, refit=False)</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="3fe57819-ef08-46de-a235-f0f501b88302" type="checkbox" checked><label for="3fe57819-ef08-46de-a235-f0f501b88302" class="sk-toggleable__label sk-toggleable__label-arrow">LogisticRegressionCV</label><div class="sk-toggleable__content"><pre>LogisticRegressionCV(cv=StratifiedKFold(n_splits=5, random_state=1, shuffle=True),random_state=1, refit=False)</pre></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.

| Metric   |    Value |
|----------|----------|
| accuracy | 0.982166 |
| f1 score | 0.982166 |

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

@article{singh2022emb,
  title={Emb-GAM: an Interpretable and Efficient Predictor using Pre-trained Language Models},
  author={Singh, Chandan and Gao, Jianfeng},
  journal={arXiv preprint arXiv:2209.11799},
  year={2022}
}

# get_started_code

from PIL import Image
from skops import hub_utils
import torch
from transformers import AutoFeatureExtractor, AutoModel
import pickle
import os

# load embedding model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
feature_extractor = AutoFeatureExtractor.from_pretrained('Ramos-Ramos/vicreg-resnet-50')
model = AutoModel.from_pretrained('Ramos-Ramos/vicreg-resnet-50').eval().to(device)

# load logistic regression
os.mkdir('emb-gam-vicreg-resnet')
hub_utils.download(repo_id='Ramos-Ramos/emb-gam-vicreg-resnet', dst='emb-gam-vicreg-resnet')

with open('emb-gam-vicreg-resnet/model.pkl', 'rb') as file: 
  logistic_regression = pickle.load(file)
    
# load image
img = Image.open('examples/english_springer.png')

# preprocess image
inputs = {k: v.to(device) for k, v in feature_extractor(img, return_tensors='pt').items()}

# extract patch embeddings
with torch.no_grad():
  patch_embeddings = model(**inputs).last_hidden_state[0].permute(1, 2, 0).view(7*7, 2048).cpu()

# classify
pred = logistic_regression.predict(patch_embeddings.sum(dim=0, keepdim=True))

# get patch contributions
patch_contributions = logistic_regression.coef_ @ patch_embeddings.T.numpy()

# model_card_authors

Patrick Ramos and Ryan Ramos

# limitations

This model is not intended to be used in production.

# model_description

This is a LogisticRegressionCV model trained on averages of patch embeddings from the Imagenette dataset. This forms the GAM of an [Emb-GAM](https://arxiv.org/abs/2209.11799) extended to images. Patch embeddings are meant to be extracted with the [`Ramos-Ramos/vicreg-resnet-50` ResNet checkpoint](https://huggingface.co/Ramos-Ramos/vicreg-resnet-50).

# eval_method

The model is evaluated using test split, on accuracy and F1 score with macro average.

# confusion_matrix

![confusion_matrix](confusion_matrix.png)
