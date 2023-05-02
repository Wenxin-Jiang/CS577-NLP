---
language: fa
license: apache-2.0
tags: 
- Farsi
---
# Arnavāz (ارنواز)

**Model Description:** Arnavaz/gpt-arnavaz-beta is gpt2 language model that is fine-tuned using [bolbolzaban/gpt2-persian](https://huggingface.co/bolbolzaban/gpt2-persian) pretrained model.
[bolbolzaban/gpt2-persian](https://huggingface.co/bolbolzaban/gpt2-persian) has been trained similar to [gpt2-medium](https://huggingface.co/gpt2-medium) with differences in context size, tokenizer and language [(Read more)](https://medium.com/@khashei/a-not-so-dangerous-ai-in-the-persian-language-39172a641c84).
- **Developed by:** [Rezā Latifi](https://rezalatifi.ir)
- **Model Type:** Transformer-based language model
- **Language:** Persian (All characters other than the Persian alphabet are replaced with special tokens)
- **License:** [Modified MIT License](https://github.com/openai/gpt-2/blob/master/LICENSE)
- **Related Models:** [bolbolzaban/gpt2-persian](https://huggingface.co/bolbolzaban/gpt2-persian), [gpt2-medium](https://huggingface.co/gpt2-medium)
- **Resources for more information:**
  - [Arnavaz Website](https://openai.com/blog/better-language-models/)

## How to utilize
Using a pipeline for text generation, Arnavaz can be utilized like this:

```python
from transformers import pipeline, AutoTokenizer, GPT2LMHeadModel, AutoConfig
tokenizer = AutoTokenizer.from_pretrained('Arnavaz/gpt2-arnavaz-beta')
model = GPT2LMHeadModel.from_pretrained('Arnavaz/gpt2-arnavaz-beta')
config = AutoConfig.from_pretrained('Arnavaz/gpt2-arnavaz-beta', max_length=512)
generator = pipeline('text-generation', model, tokenizer=tokenizer, config=config)

def getEloquent(ineloquent):
  result = generator(f"[BOS]{ineloquent}[SEP]")[0]['generated_text']
  return result[result.find('[SEP]')+5:]
 
sample = getEloquent('استفاده از کاغذ پاپیروس برای نوشتن کتاب از حدود دو هزار سال قبل از میلاد در مصر رایج شد.')
```
