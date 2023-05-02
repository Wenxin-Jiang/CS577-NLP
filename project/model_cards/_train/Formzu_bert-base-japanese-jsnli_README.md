---
language: 
- ja
license: cc-by-sa-4.0
tags:
- zero-shot-classification
- text-classification
- nli
- pytorch
metrics:
- accuracy
datasets:
- JSNLI
pipeline_tag: text-classification
widget:
- text: "あなたが好きです。 あなたを愛しています。"
model-index:
- name: bert-base-japanese-jsnli
  results:
  - task:
      type: text-classification
      name: Natural Language Inference
    dataset:
      type: snli
      name: JSNLI 
      split: dev
    metrics:
      - type: accuracy
        value: 0.9288
        verified: false
---
# bert-base-japanese-jsnli

This model is a fine-tuned version of [cl-tohoku/bert-base-japanese-v2](https://huggingface.co/cl-tohoku/bert-base-japanese-v2) on the [JSNLI](https://nlp.ist.i.kyoto-u.ac.jp/?%E6%97%A5%E6%9C%AC%E8%AA%9ESNLI%28JSNLI%29%E3%83%87%E3%83%BC%E3%82%BF%E3%82%BB%E3%83%83%E3%83%88) dataset.
It achieves the following results on the evaluation set:

- Loss: 0.2085
- Accuracy: 0.9288

### How to use the model
#### Simple zero-shot classification pipeline
```python
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="Formzu/bert-base-japanese-jsnli")

sequence_to_classify = "いつか世界を見る。"
candidate_labels = ['旅行', '料理', '踊り']
out = classifier(sequence_to_classify, candidate_labels, hypothesis_template="この例は{}です。")
print(out)
#{'sequence': 'いつか世界を見る。', 
# 'labels': ['旅行', '料理', '踊り'], 
# 'scores': [0.6758995652198792, 0.22110949456691742, 0.1029909998178482]}
```
#### NLI use-case
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

model_name = "Formzu/bert-base-japanese-jsnli"
model = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

premise = "いつか世界を見る。"
label = '旅行'
hypothesis = f'この例は{label}です。'

input = tokenizer.encode(premise, hypothesis, return_tensors='pt').to(device)
with torch.no_grad():
    logits = model(input)["logits"][0]
    probs = logits.softmax(dim=-1)
    print(probs.cpu().numpy(), logits.cpu().numpy())
#[0.68940836 0.29482093 0.01577068] [ 1.7791482   0.92968255 -1.998533  ]
```
## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
| :-----------: | :---: | :---: | :-------------: | :------: |
|    0.4054    |  1.0  | 16657 |     0.2141     |  0.9216  |
|    0.3297    |  2.0  | 33314 |     0.2145     |  0.9236  |
|    0.2645    |  3.0  | 49971 |     0.2085     |  0.9288  |

### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
