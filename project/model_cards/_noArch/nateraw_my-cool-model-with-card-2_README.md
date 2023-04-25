---
language: en
license: mit
tags:
- image-classification
datasets: beans
model-index:
- name: my-cool-model-with-card-2
  results:
  - task:
      type: image-classification
    dataset:
      type: beans
      name: Beans
    metrics:
    - type: acc
      value: 0.9
---

# MyModelName

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