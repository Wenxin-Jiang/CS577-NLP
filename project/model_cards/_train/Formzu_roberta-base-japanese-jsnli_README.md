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
- text: "あなた が 好きです 。 　 あなた を 愛して い ます 。"
model-index:
- name: roberta-base-japanese-jsnli
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
        value: 0.9328
        verified: false
---
# roberta-base-japanese-jsnli

This model is a fine-tuned version of [nlp-waseda/roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) on the [JSNLI](https://nlp.ist.i.kyoto-u.ac.jp/?%E6%97%A5%E6%9C%AC%E8%AA%9ESNLI%28JSNLI%29%E3%83%87%E3%83%BC%E3%82%BF%E3%82%BB%E3%83%83%E3%83%88) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2039
- Accuracy: 0.9328

### How to use the model

The input text should be segmented into words by [Juman++](https://github.com/ku-nlp/jumanpp) in advance.

#### Simple zero-shot classification pipeline
```python
from transformers import pipeline
from pyknp import Juman

juman = Juman()

classifier = pipeline("zero-shot-classification", model="Formzu/roberta-base-japanese-jsnli")

sequence_to_classify = " ".join([tok.midasi for tok in juman.analysis("いつか世界を見る。").mrph_list()])

candidate_labels = ['旅行', '料理', '踊り']
out = classifier(sequence_to_classify, candidate_labels, hypothesis_template="この 例 は {} です 。")
print(out)
#{'sequence': 'いつか 世界 を 見る 。', 
# 'labels': ['旅行', '踊り', '料理'], 
# 'scores': [0.8998081684112549, 0.06059670448303223, 0.03959512338042259]}
```
#### NLI use-case
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from pyknp import Juman

juman = Juman()

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

model_name = "Formzu/roberta-base-japanese-jsnli"
model = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

premise = " ".join([tok.midasi for tok in juman.analysis("いつか世界を見る。").mrph_list()])
label = '旅行'
hypothesis = f'この 例 は {label} です 。'

input = tokenizer.encode(premise, hypothesis, return_tensors='pt').to(device)
with torch.no_grad():
    logits = model(input)["logits"][0]
    probs = logits.softmax(dim=-1)
    print(probs.cpu().numpy(), logits.cpu().numpy())
#[0.82168734 0.1744363  0.00387629] [ 2.3362164   0.78641605 -3.0202653 ]
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

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.4067        | 1.0   | 16657 | 0.2224          | 0.9201   |
| 0.3397        | 2.0   | 33314 | 0.2152          | 0.9208   |
| 0.2775        | 3.0   | 49971 | 0.2039          | 0.9328   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
