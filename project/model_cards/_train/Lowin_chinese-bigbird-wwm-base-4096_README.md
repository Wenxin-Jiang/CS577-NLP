---
language:
- zh
license:
- apache-2.0
---
```python
from transformers import BertTokenizer
from transformers import BigBirdModel

model = BigBirdModel.from_pretrained('Lowin/chinese-bigbird-wwm-base-4096')
tokenizer = BertTokenizer.from_pretrained('Lowin/chinese-bigbird-wwm-base-4096')
```
https://github.com/LowinLi/chinese-bigbird