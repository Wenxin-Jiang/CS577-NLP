---
license: mit
language:
- en
tags:
- summarization
- headline-generation
- text-generation
datasets:
- JulesBelveze/tldr_news
metrics:
- rouge1
- rouge2
- rougeL
- rougeLsum

---

# t5-small for headline generation

This model is a [t5-small](https://huggingface.co/t5-small) fine-tuned for headline generation using
the [JulesBelveze/tldr_news](https://huggingface.co/datasets/JulesBelveze/tldr_news) dataset.

## Using this model
```python
import re
from transformers import AutoTokenizer, T5ForConditionalGeneration

WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

article_text = """US FCC commissioner Brendan Carr has asked Apple and Google to remove TikTok from their app stores. The video app is owned by Chinese company ByteDance. Carr claims that TikTok functions as a surveillance tool that harvests extensive amounts of personal and sensitive data from US citizens. TikTok says its data access approval process is overseen by a US-based security team and that data is only accessed on an as-needed basis under strict controls."""
model_name = "JulesBelveze/t5-small-headline-generator"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

input_ids = tokenizer(
    [WHITESPACE_HANDLER(article_text)],
    return_tensors="pt",
    padding="max_length",
    truncation=True,
    max_length=384
)["input_ids"]

output_ids = model.generate(
    input_ids=input_ids,
    max_length=84,
    no_repeat_ngram_size=2,
    num_beams=4
)[0]

summary = tokenizer.decode(
    output_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)
print(summary)
```

## Evaluation

| Metric     | Score   |
|------------|---------|
| ROUGE 1    | 44.2379 |
| ROUGE 2    | 17.4961 |
| ROUGE L    | 41.1119 |
| ROUGE Lsum | 41.1256 |