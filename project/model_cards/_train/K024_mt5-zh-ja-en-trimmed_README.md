---
language:
- zh
- ja
- en

tags:
- translation

widget:
- text: "ja2zh: 吾輩は猫である。名前はまだ無い。"

license: cc-by-nc-sa-4.0
---

This model is finetuned from [mt5-base](https://huggingface.co/google/mt5-base).

The model vocabulary is trimmed to ~1/3 by selecting top 85000 tokens in the training data. The code to trim the vocabulary can be found [here](https://gist.github.com/K024/4a100a0f4f4b07208958e0f3244da6ad).

Usage:
```python
from transformers import (
  T5Tokenizer,
  MT5ForConditionalGeneration,
  Text2TextGenerationPipeline,
)

path = "K024/mt5-zh-ja-en-trimmed"
pipe = Text2TextGenerationPipeline(
  model=MT5ForConditionalGeneration.from_pretrained(path),
  tokenizer=T5Tokenizer.from_pretrained(path),
)

sentence = "ja2zh: 吾輩は猫である。名前はまだ無い。"
res = pipe(sentence, max_length=100, num_beams=4)
res[0]['generated_text']
```

Training data:
```
wikimedia-en-ja
wikimedia-en-zh
wikimedia-ja-zh
wikititles-ja-en
wikititles-zh-en
wikimatrix-ja-zh
news-commentary-en-ja
news-commentary-en-zh
news-commentary-ja-zh
ted2020-en-ja
ted2020-en-zh
ted2020-ja-zh
```

License: [![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
