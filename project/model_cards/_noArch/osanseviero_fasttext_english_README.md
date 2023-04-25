---
tags:
- feature-extraction
library_name: generic
---

# Pretrained FastText word vector for English

https://github.com/facebookresearch/fastText

Usage

```
import fasttext.util
ft = fasttext.load_model('cc.en.300.bin')
ft.get_word_vector('hello')
```