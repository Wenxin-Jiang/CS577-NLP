---
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/cat-dog-music.png
  candidate_labels: 기타치는 고양이, 피아노 치는 강아지
  example_title: Guitar, cat and dog
language: ko
license: mit
---

# clip-vit-base-patch32-ko

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

repo = "Bingsu/clip-vit-base-patch32-ko"
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
tensor([[0.9926, 0.0074]])
```

#### 2.

```python
from transformers import pipeline

repo = "Bingsu/clip-vit-base-patch32-ko"
pipe = pipeline("zero-shot-image-classification", model=repo)

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
result = pipe(images=url, candidate_labels=["고양이 한 마리", "고양이 두 마리", "분홍색 소파에 드러누운 고양이 친구들"], hypothesis_template="{}")
```

```python
>>> result
[{'score': 0.9456236958503723, 'label': '분홍색 소파에 드러누운 고양이 친구들'},
 {'score': 0.05315302312374115, 'label': '고양이 두 마리'},
 {'score': 0.0012233294546604156, 'label': '고양이 한 마리'}]
```

## Tokenizer

토크나이저는 한국어 데이터와 영어 데이터를 7:3 비율로 섞어, 원본 CLIP 토크나이저에서 `.train_new_from_iterator`를 통해 학습되었습니다.

https://github.com/huggingface/transformers/blob/bc21aaca789f1a366c05e8b5e111632944886393/src/transformers/models/clip/modeling_clip.py#L661-L666
```python
        # text_embeds.shape = [batch_size, sequence_length, transformer.width]
        # take features from the eot embedding (eot_token is the highest number in each sequence)
        # casting to torch.int for onnx compatibility: argmax doesn't support int64 inputs with opset 14
        pooled_output = last_hidden_state[
            torch.arange(last_hidden_state.shape[0]), input_ids.to(torch.int).argmax(dim=-1)
        ]
```

CLIP 모델은 `pooled_output`을 구할때 id가 가장 큰 토큰을 사용하기 때문에, eos 토큰은 가장 마지막 토큰이 되어야 합니다.
