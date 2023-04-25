---
language: en
license: mit
library_name: timm
tags:
- image-classification
- resnet
datasets: beans
metrics:
- accuracy
- f1
model-index:
- name: my-cool-model-with-eval-results
  results:
  - task:
      type: image-classification
    dataset:
      type: beans
      name: Beans
    metrics:
    - type: accuracy
      value: 0.85
    - type: f1
      value: 0.75
---

# my-cool-model-with-eval-results

## Model description

This isn't really a model, it's just a test repo to see if the [modelcards](https://github.com/nateraw/modelcards) package works!

## Intended uses & limitations

#### How to use

```python
# You can include sample code which will be formatted
```

#### Limitations and bias

Provide examples of latent issues and potential remediations.

## Training data

Describe the data you used to train the model.
If you initialized it with pre-trained weights, add a link to the pre-trained model card or repository with description of the pre-training data.

## Training procedure

Preprocessing, hardware used, hyperparameters...

## Eval results

Provide some evaluation results.

### BibTeX entry and citation info

```bibtex
@inproceedings{...,
  year={2020}
}
```