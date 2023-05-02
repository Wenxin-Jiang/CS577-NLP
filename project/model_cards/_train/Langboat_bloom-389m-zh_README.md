---
license: bigscience-bloom-rail-1.0
language:
- zh
pipeline_tag: text-generation
widget:
- text: "中国的首都是"

---

This model is based on [bigscience/bloom-560m](https://huggingface.co/bigscience/bloom-560m). 

We pruned its vocabulary from 250880 to 42437 with Chinese corpus to reduce GPU memory usage. So the total parameter is 389m now.

# How to use
```python
from transformers import BloomTokenizerFast, BloomForCausalLM

tokenizer = BloomTokenizerFast.from_pretrained('Langboat/bloom-389m-zh')
model = BloomForCausalLM.from_pretrained('Langboat/bloom-389m-zh')

print(tokenizer.batch_decode(model.generate(tokenizer.encode('中国的首都是', return_tensors='pt'))))
```