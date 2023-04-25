---
tags:
- image-classification
- timm
library_tag: timm
license: mit
---
# Model card for Bingsu/4dblock-maxvit_rmlp_tiny_rw_256

데이콘 포디블록 구조 추출 AI 경진대회

<https://dacon.io/competitions/official/236046/overview/description>

public score: 0.86392

```python
from timm import create_model

model = create_model("hf_hub:Bingsu/dacon_4dblock-maxvit_rmlp_tiny_rw_256", pretrained=True)
```