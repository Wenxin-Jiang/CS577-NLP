---
license: bigscience-bloom-rail-1.0
language:
- zh
pipeline_tag: text-generation
widget:
- text: "中国的首都是"

---

This model is based on [bigscience/bloom-7b1](https://huggingface.co/bigscience/bloom-7b1). 

We pruned its vocabulary from 250880 to 46145 with Chinese corpus to reduce GPU memory usage. So the total parameter is 6b4 now.

# How to use
```python
from transformers import BloomTokenizerFast, BloomForCausalLM

tokenizer = BloomTokenizerFast.from_pretrained('Langboat/bloom-6b4-zh')
model = BloomForCausalLM.from_pretrained('Langboat/bloom-6b4-zh')

print(tokenizer.batch_decode(model.generate(tokenizer.encode('中国的首都是', return_tensors='pt'))))
```
