---
tags:
- clip
language: ko
license: mit
---

# vitB32_bert_ko_small_clip

[openai/clip-vit-base-patch32](https://huggingface.co/openai/clip-vit-base-patch32) + [lassl/bert-ko-small](https://huggingface.co/lassl/bert-ko-small) CLIP Model

[training code(github)](https://github.com/Bing-su/KoCLIP_training_code)

## Train

SBERT의 [Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation](https://arxiv.org/abs/2004.09813)를 참고하여, `openai/clip-vit-base-patch32` 텍스트 모델의 가중치를 `lassl/bert-ko-small`로 복제하였습니다. 논문과는 달리 mean pooling을 사용하지 않고, huggingface모델의 기본 pooling을 그대로 사용하였습니다.

사용한 데이터: [Aihub 한국어-영어 번역(병렬) 말뭉치](https://aihub.or.kr/aidata/87)


## How to Use

#### 1.

```python
import requests
from PIL import Image
from transformers import VisionTextDualEncoderProcessor, VisionTextDualEncoderModel  # or Auto...

model = VisionTextDualEncoderModel.from_pretrained("Bingsu/vitB32_bert_ko_small_clip")
processor = VisionTextDualEncoderProcessor.from_pretrained("Bingsu/vitB32_bert_ko_small_clip")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(text=["고양이 두 마리", "개 두 마리"], images=image, return_tensors="pt", padding=True)

outputs = model(**inputs)
logits_per_image = outputs.logits_per_image
probs = logits_per_image.softmax(dim=1)
```

```pycon
>>> probs
tensor([[0.9756, 0.0244]], grad_fn=<SoftmaxBackward0>)
```

#### 2.

```python
from transformers import AutoModel, AutoProcessor, pipeline

model = AutoModel.from_pretrained("Bingsu/vitB32_bert_ko_small_clip")
processor = AutoProcessor.from_pretrained("Bingsu/vitB32_bert_ko_small_clip")
pipe = pipeline("zero-shot-image-classification", model=model, feature_extractor=processor.feature_extractor, tokenizer=processor.tokenizer)

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
result = pipe(images=url, candidate_labels=["고양이 한 마리", "고양이 두 마리", "고양이 두 마리와 리모컨 두 개"], hypothesis_template="{}")
```

```pycon
>>> result
[{'score': 0.871887743473053, 'label': '고양이 두 마리와 리모컨 두 개'},
 {'score': 0.12316706776618958, 'label': '고양이 두 마리'},
 {'score': 0.004945191089063883, 'label': '고양이 한 마리'}]
```
