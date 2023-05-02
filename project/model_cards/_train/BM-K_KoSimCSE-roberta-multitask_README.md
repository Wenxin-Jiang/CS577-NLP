---
language: ko
tags:
  - korean
---

https://github.com/BM-K/Sentence-Embedding-is-all-you-need

# Korean-Sentence-Embedding
🍭 Korean sentence embedding repository. You can download the pre-trained models and inference right away, also it provides environments where individuals can train models.

## Quick tour
```python
import torch
from transformers import AutoModel, AutoTokenizer

def cal_score(a, b):
    if len(a.shape) == 1: a = a.unsqueeze(0)
    if len(b.shape) == 1: b = b.unsqueeze(0)

    a_norm = a / a.norm(dim=1)[:, None]
    b_norm = b / b.norm(dim=1)[:, None]
    return torch.mm(a_norm, b_norm.transpose(0, 1)) * 100

model = AutoModel.from_pretrained('BM-K/KoSimCSE-roberta-multitask') 
AutoTokenizer.from_pretrained('BM-K/KoSimCSE-roberta-multitask')

sentences = ['치타가 들판을 가로 질러 먹이를 쫓는다.',
             '치타 한 마리가 먹이 뒤에서 달리고 있다.',
             '원숭이 한 마리가 드럼을 연주한다.']

inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")
embeddings, _ = model(**inputs, return_dict=False)

score01 = cal_score(embeddings[0][0], embeddings[1][0])
score02 = cal_score(embeddings[0][0], embeddings[2][0])
```

## Performance
- Semantic Textual Similarity test set results <br>

| Model                  | AVG | Cosine Pearson | Cosine Spearman | Euclidean Pearson | Euclidean Spearman | Manhattan Pearson | Manhattan Spearman | Dot Pearson | Dot Spearman |
|------------------------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| KoSBERT<sup>†</sup><sub>SKT</sub>    | 77.40 | 78.81 | 78.47 | 77.68 | 77.78 | 77.71 | 77.83 | 75.75 | 75.22 |
| KoSBERT              | 80.39 | 82.13 | 82.25 | 80.67 | 80.75 | 80.69 | 80.78 | 77.96 | 77.90 |
| KoSRoBERTa           | 81.64 | 81.20 | 82.20 | 81.79 | 82.34 | 81.59 | 82.20 | 80.62 | 81.25 |
| | | | | | | | | |
| KoSentenceBART         | 77.14 | 79.71 | 78.74 | 78.42 | 78.02 | 78.40 | 78.00 | 74.24 | 72.15 |
| KoSentenceT5          | 77.83 | 80.87 | 79.74 | 80.24 | 79.36 | 80.19 | 79.27 | 72.81 | 70.17 |
| | | | | | | | | |
| KoSimCSE-BERT<sup>†</sup><sub>SKT</sub>   | 81.32 | 82.12 | 82.56 | 81.84 | 81.63 | 81.99 | 81.74 | 79.55 | 79.19 |
| KoSimCSE-BERT              | 83.37 | 83.22 | 83.58 | 83.24 | 83.60 | 83.15 | 83.54 | 83.13 | 83.49 |
| KoSimCSE-RoBERTa          | 83.65 | 83.60 | 83.77 | 83.54 | 83.76 | 83.55 | 83.77 | 83.55 | 83.64 |
| | | | | | | | | | |
| KoSimCSE-BERT-multitask              | 85.71 | 85.29 | 86.02 | 85.63 | 86.01 | 85.57 | 85.97 | 85.26 | 85.93 |
| KoSimCSE-RoBERTa-multitask          | 85.77 | 85.08 | 86.12 | 85.84 | 86.12 | 85.83 | 86.12 | 85.03 | 85.99 |