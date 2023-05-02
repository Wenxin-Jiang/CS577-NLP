---
language:
- zh
license:
- apache-2.0
---
```python
import jieba_fast
from transformers import BertTokenizer
from transformers import BigBirdModel
class JiebaTokenizer(BertTokenizer):
    def __init__(
        self, pre_tokenizer=lambda x: jieba_fast.cut(x, HMM=False), *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.pre_tokenizer = pre_tokenizer
    def _tokenize(self, text, *arg, **kwargs):
        split_tokens = []
        for text in self.pre_tokenizer(text):
            if text in self.vocab:
                split_tokens.append(text)
            else:
                split_tokens.extend(super()._tokenize(text))
        return split_tokens
model = BigBirdModel.from_pretrained('Lowin/chinese-bigbird-mini-1024')
tokenizer = JiebaTokenizer.from_pretrained('Lowin/chinese-bigbird-mini-1024')
```
https://github.com/LowinLi/chinese-bigbird