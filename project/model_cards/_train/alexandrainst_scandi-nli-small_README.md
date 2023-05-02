---
pipeline_tag: zero-shot-classification
language:
- da
- no
- nb
- sv
license: mit
datasets:
- strombergnlp/danfever
- KBLab/overlim
- MoritzLaurer/multilingual-NLI-26lang-2mil7
widget:
- example_title: Danish
  text: Mexicansk bokser advarer Messi - 'Du skal bede til gud, om at jeg ikke finder dig'
  candidate_labels: sundhed, politik, sport, religion
- example_title: Norwegian
  text: Regjeringen i Russland hevder Norge fører en politikk som vil føre til opptrapping i Arktis og «den endelige ødeleggelsen av russisk-norske relasjoner».
  candidate_labels: helse, politikk, sport, religion
- example_title: Swedish
  text: Så luras kroppens immunförsvar att bota cancer
  candidate_labels: hälsa, politik, sport, religion
inference:
  parameters:
    hypothesis_template: "Dette eksempel handler om {}"
---

# ScandiNLI - Natural Language Inference model for Scandinavian Languages

This model is a fine-tuned version of [jonfd/electra-small-nordic](https://huggingface.co/jonfd/electra-small-nordic) for Natural Language Inference in Danish, Norwegian Bokmål and Swedish.

We have released three models for Scandinavian NLI, of different sizes:

- [alexandrainst/scandi-nli-large](https://huggingface.co/alexandrainst/scandi-nli-large)
- [alexandrainst/scandi-nli-base](https://huggingface.co/alexandrainst/scandi-nli-base)
- alexandrainst/scandi-nli-small (this)

A demo of the large model can be found in [this Hugging Face Space](https://huggingface.co/spaces/alexandrainst/zero-shot-classification) - check it out!

The performance and model size of each of them can be found in the Performance section below.


## Quick start

You can use this model in your scripts as follows:

```python
>>> from transformers import pipeline
>>> classifier = pipeline(
...     "zero-shot-classification",
...     model="alexandrainst/scandi-nli-small",
... )
>>> classifier(
...     "Mexicansk bokser advarer Messi - 'Du skal bede til gud, om at jeg ikke finder dig'",
...     candidate_labels=['sundhed', 'politik', 'sport', 'religion'],
...     hypothesis_template="Dette eksempel handler om {}",
... )
{'sequence': "Mexicansk bokser advarer Messi - 'Du skal bede til gud, om at jeg ikke finder dig'",
 'labels': ['religion', 'sport', 'politik', 'sundhed'],
 'scores': [0.4504755437374115,
  0.20737220346927643,
  0.1976872682571411,
  0.14446501433849335]}
```

## Performance

We evaluate the models in Danish, Swedish and Norwegian Bokmål separately.

In all cases, we report Matthew's Correlation Coefficient (MCC), macro-average F1-score as well as accuracy.


### Scandinavian Evaluation

The Scandinavian scores are the average of the Danish, Swedish and Norwegian scores, which can be found in the sections below.

| **Model** | **MCC** | **Macro-F1** | **Accuracy** | **Number of Parameters** |
| :-------- | :------------ | :--------- | :----------- | :----------- |
| [`alexandrainst/scandi-nli-large`](https://huggingface.co/alexandrainst/scandi-nli-large) | **73.70%** | **74.44%** | **83.91%** | 354M |
| [`MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7`](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7) | 69.01% | 71.99% | 80.66% | 279M |
| [`alexandrainst/scandi-nli-base`](https://huggingface.co/alexandrainst/scandi-nli-base) | 67.42% | 71.54% | 80.09% | 178M |
| [`joeddav/xlm-roberta-large-xnli`](https://huggingface.co/joeddav/xlm-roberta-large-xnli) | 64.17% | 70.80% | 77.29% | 560M |
| [`MoritzLaurer/mDeBERTa-v3-base-mnli-xnli`](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) | 63.94% | 70.41% | 77.23% | 279M |
| [`NbAiLab/nb-bert-base-mnli`](https://huggingface.co/NbAiLab/nb-bert-base-mnli) | 61.71% | 68.36% | 76.08% | 178M |
| `alexandrainst/scandi-nli-small` (this) | 56.02% | 65.30% | 73.56% | **22M** |


### Danish Evaluation

We use a test split of the [DanFEVER dataset](https://aclanthology.org/2021.nodalida-main.pdf#page=439) to evaluate the Danish performance of the models.

The test split is generated using [this gist](https://gist.github.com/saattrupdan/1cb8379232fdec6e943dc84595a85e7c).

| **Model** | **MCC** | **Macro-F1** | **Accuracy** | **Number of Parameters** |
| :-------- | :------------ | :--------- | :----------- | :----------- |
| [`alexandrainst/scandi-nli-large`](https://huggingface.co/alexandrainst/scandi-nli-large) | **73.80%** | **58.41%** | **86.98%** | 354M |
| [`MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7`](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7) | 68.37% | 57.10% | 83.25% | 279M |
| [`alexandrainst/scandi-nli-base`](https://huggingface.co/alexandrainst/scandi-nli-base) | 62.44% | 55.00% | 80.42% | 178M |
| [`NbAiLab/nb-bert-base-mnli`](https://huggingface.co/NbAiLab/nb-bert-base-mnli) | 56.92% | 53.25% | 76.39% | 178M |
| [`MoritzLaurer/mDeBERTa-v3-base-mnli-xnli`](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) | 52.79% | 52.00% | 72.35% | 279M |
| [`joeddav/xlm-roberta-large-xnli`](https://huggingface.co/joeddav/xlm-roberta-large-xnli) | 49.18% | 50.31% | 69.73% | 560M |
| `alexandrainst/scandi-nli-small` (this) | 47.28% | 48.88% | 73.46% | **22M** |


### Swedish Evaluation

We use the test split of the machine translated version of the [MultiNLI](https://cims.nyu.edu/~sbowman/multinli/) dataset to evaluate the Swedish performance of the models.

We acknowledge that not evaluating on a gold standard dataset is not ideal, but unfortunately we are not aware of any NLI datasets in Swedish.

| **Model** | **MCC** | **Macro-F1** | **Accuracy** | **Number of Parameters** |
| :-------- | :------------ | :--------- | :----------- | :----------- |
| [`alexandrainst/scandi-nli-large`](https://huggingface.co/alexandrainst/scandi-nli-large) | **76.69%** | **84.47%** | **84.38%** | 354M |
| [`joeddav/xlm-roberta-large-xnli`](https://huggingface.co/joeddav/xlm-roberta-large-xnli) | 75.35% | 83.42% | 83.55% | 560M |
| [`MoritzLaurer/mDeBERTa-v3-base-mnli-xnli`](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) | 73.84% | 82.46% | 82.58% | 279M |
| [`MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7`](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7) | 73.32% | 82.15% | 82.08% | 279M |
| [`alexandrainst/scandi-nli-base`](https://huggingface.co/alexandrainst/scandi-nli-base) | 72.29% | 81.37% | 81.51% | 178M |
| [`NbAiLab/nb-bert-base-mnli`](https://huggingface.co/NbAiLab/nb-bert-base-mnli) | 64.69% | 76.40% | 76.47% | 178M |
| `alexandrainst/scandi-nli-small` (this) | 62.35% | 74.79% | 74.93% | **22M** |


### Norwegian Evaluation

We use the test split of the machine translated version of the [MultiNLI](https://cims.nyu.edu/~sbowman/multinli/) dataset to evaluate the Norwegian performance of the models.

We acknowledge that not evaluating on a gold standard dataset is not ideal, but unfortunately we are not aware of any NLI datasets in Norwegian.

| **Model** | **MCC** | **Macro-F1** | **Accuracy** | **Number of Parameters** |
| :-------- | :------------ | :--------- | :----------- | :----------- |
| [`alexandrainst/scandi-nli-large`](https://huggingface.co/alexandrainst/scandi-nli-large) | **70.61%** | **80.43%** | **80.36%** | 354M |
| [`joeddav/xlm-roberta-large-xnli`](https://huggingface.co/joeddav/xlm-roberta-large-xnli) | 67.99% | 78.68% | 78.60% | 560M |
| [`alexandrainst/scandi-nli-base`](https://huggingface.co/alexandrainst/scandi-nli-base) | 67.53% | 78.24% | 78.33% | 178M |
| [`MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7`](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7) | 65.33% | 76.73% | 76.65% | 279M |
| [`MoritzLaurer/mDeBERTa-v3-base-mnli-xnli`](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) | 65.18% | 76.76% | 76.77% | 279M |
| [`NbAiLab/nb-bert-base-mnli`](https://huggingface.co/NbAiLab/nb-bert-base-mnli) | 63.51% | 75.42% | 75.39% | 178M |
| `alexandrainst/scandi-nli-small` (this) | 58.42% | 72.22% | 72.30% | **22M** |


## Training procedure

It has been fine-tuned on a dataset composed of [DanFEVER](https://aclanthology.org/2021.nodalida-main.pdf#page=439) as well as machine translated versions of [MultiNLI](https://cims.nyu.edu/~sbowman/multinli/) and [CommitmentBank](https://doi.org/10.18148/sub/2019.v23i2.601) into all three languages, and machine translated versions of [FEVER](https://aclanthology.org/N18-1074/) and [Adversarial NLI](https://aclanthology.org/2020.acl-main.441/) into Swedish.

The training split of DanFEVER is generated using [this gist](https://gist.github.com/saattrupdan/1cb8379232fdec6e943dc84595a85e7c).

The three languages are sampled equally during training, and they're validated on validation splits of [DanFEVER](https://aclanthology.org/2021.nodalida-main.pdf#page=439) and machine translated versions of [MultiNLI](https://cims.nyu.edu/~sbowman/multinli/) for Swedish and Norwegian Bokmål, sampled equally.

Check out the [Github repository](https://github.com/alexandrainst/ScandiNLI) for the code used to train the ScandiNLI models, and the full training logs can be found in [this Weights and Biases report](https://wandb.ai/saattrupdan/huggingface/reports/ScandiNLI--VmlldzozMDQyOTk1?accessToken=r9crgxqvvigy2hatdjeobzwipz7f3id5vqg8ooksljhfw6wl0hv1b05asypsfj9v).

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 4242
- gradient_accumulation_steps: 1
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9, 0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- max_steps: 50,000