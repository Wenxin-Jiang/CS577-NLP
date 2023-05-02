---
language:
- yue
tags:
- bart
- cantonese
- fill-mask
license: other
library_name: bart-base-jax
co2_eq_emissions:
  emissions: 6.29
  source: estimated by using ML CO2 Calculator
  training_type: second-stage pre-training
  hardware_used: Google Cloud TPU v4-16
---

# bart-base-cantonese

This is the Cantonese model of BART base. It is obtained by a second-stage pre-training on the [LIHKG dataset](https://github.com/ayaka14732/lihkg-scraper) based on the [fnlp/bart-base-chinese](https://huggingface.co/fnlp/bart-base-chinese) model.

This project is supported by Cloud TPUs from Google's [TPU Research Cloud](https://sites.research.google/trc/about/) (TRC).

**Note**: To avoid any copyright issues, please do not use this model for any purpose.

## GitHub Links

- Dataset: [ayaka14732/lihkg-scraper](https://github.com/ayaka14732/lihkg-scraper)
- Tokeniser: [ayaka14732/bert-tokenizer-cantonese](https://github.com/ayaka14732/bert-tokenizer-cantonese)
- Base model: [ayaka14732/bart-base-jax](https://github.com/ayaka14732/bart-base-jax)
- Pre-training: [ayaka14732/bart-base-cantonese](https://github.com/ayaka14732/bart-base-cantonese)

## Usage

```python
from transformers import BertTokenizer, BartForConditionalGeneration, Text2TextGenerationPipeline
tokenizer = BertTokenizer.from_pretrained('Ayaka/bart-base-cantonese')
model = BartForConditionalGeneration.from_pretrained('Ayaka/bart-base-cantonese')
text2text_generator = Text2TextGenerationPipeline(model, tokenizer)  
output = text2text_generator('聽日就要返香港，我激動到[MASK]唔着', max_length=50, do_sample=False)
print(output[0]['generated_text'].replace(' ', ''))
# output: 聽日就要返香港，我激動到瞓唔着
```

**Note**: Please use the `BertTokenizer` for the model vocabulary. DO NOT use the original `BartTokenizer`.

## Training Details

- Optimiser: SGD 0.03 + Adaptive Gradient Clipping 0.1
- Dataset: 172937863 sentences, pad or truncate to 64 tokens
- Batch size: 640
- Number of epochs: 7 epochs + 61440 steps
- Time: 44.0 hours on Google Cloud TPU v4-16

WandB link: [`1j7zs802`](https://wandb.ai/ayaka/bart-base-cantonese/runs/1j7zs802)
