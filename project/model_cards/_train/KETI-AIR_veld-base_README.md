---
language:
- en
- ko
- multilingual
license: apache-2.0
tags:
- vision, language
- pretrained model
- image-to-text
eos_token: </s>
---

# veld base

Pretrained Vision Encoder Text Decoder Model in Korean and English. See [Github](https://github.com/AIRC-KETI/veld) for more details.

## How to use

```python
from transformers import AutoProcessor, AutoModel

processor = AutoProcessor.from_pretrained("KETI-AIR/veld-base", trust_remote_code=True)
model = AutoModel.from_pretrained("KETI-AIR/veld-base", trust_remote_code=True)
```

You can use AutoTokenizer and AutoFeatureExtractor instead AutoProcessor.
You don't need to pass `trust_remote_code=True` for AutoTokenizer and AutoFeatureExtractor

```python
from transformers import AutoFeatureExtractor, AutoTokenizer, AutoModel

feature_extractor = AutoFeatureExtractor.from_pretrained("KETI-AIR/veld-base")
tokenizer = AutoTokenizer.from_pretrained("KETI-AIR/veld-base")
model = AutoModel.from_pretrained("KETI-AIR/veld-base", trust_remote_code=True)
```
