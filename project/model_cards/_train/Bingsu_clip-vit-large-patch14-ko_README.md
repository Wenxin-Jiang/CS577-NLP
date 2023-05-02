---
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/cat-dog-music.png
  candidate_labels: 기타 치는 고양이, 피아노 치는 강아지
  example_title: Guitar, cat and dog
language: ko
license: mit
---

# clip-vit-large-patch14-ko

Korean CLIP model trained by [Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation](https://arxiv.org/abs/2004.09813)

[Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation](https://arxiv.org/abs/2004.09813)로 학습된 한국어 CLIP 모델입니다.

훈련 코드: <https://github.com/Bing-su/KoCLIP_training_code>

사용된 데이터: AIHUB에 있는 모든 한국어-영어 병렬 데이터

## How to Use

#### 1.

```python
import requests
import torch
from PIL import Image
from transformers import AutoModel, AutoProcessor

repo = "Bingsu/clip-vit-large-patch14-ko"
model = AutoModel.from_pretrained(repo)
processor = AutoProcessor.from_pretrained(repo)

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)
inputs = processor(text=["고양이 두 마리", "개 두 마리"], images=image, return_tensors="pt", padding=True)
with torch.inference_mode():
    outputs = model(**inputs)
logits_per_image = outputs.logits_per_image
probs = logits_per_image.softmax(dim=1)
```

```python
>>> probs
tensor([[0.9974, 0.0026]])
```

#### 2.

```python
from transformers import pipeline

repo = "Bingsu/clip-vit-large-patch14-ko"
pipe = pipeline("zero-shot-image-classification", model=repo)

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
result = pipe(images=url, candidate_labels=["고양이 한 마리", "고양이 두 마리", "분홍색 소파에 드러누운 고양이 친구들"], hypothesis_template="{}")
```

```python
>>> result
[{'score': 0.9907576441764832, 'label': '분홍색 소파에 드러누운 고양이 친구들'},
 {'score': 0.009206341579556465, 'label': '고양이 두 마리'},
 {'score': 3.606083555496298e-05, 'label': '고양이 한 마리'}]
```