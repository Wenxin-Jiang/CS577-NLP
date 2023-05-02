---
language: ms
tags:
- melayu-bert
license: mit
datasets:
- oscar
widget:
- text: "Saya [MASK] makan nasi hari ini."
---

## Melayu BERT

Melayu BERT is a masked language model based on [BERT](https://arxiv.org/abs/1810.04805). It was trained on the [OSCAR](https://huggingface.co/datasets/oscar) dataset, specifically the `unshuffled_original_ms` subset. The model used was [English BERT model](https://huggingface.co/bert-base-uncased) and fine-tuned on the Malaysian dataset. The model achieved a perplexity of 9.46 on a 20% validation dataset. Many of the techniques used are based on a Hugging Face tutorial [notebook](https://github.com/huggingface/notebooks/blob/master/examples/language_modeling.ipynb) written by [Sylvain Gugger](https://github.com/sgugger), and [fine-tuning tutorial notebook](https://github.com/piegu/fastai-projects/blob/master/finetuning-English-GPT2-any-language-Portuguese-HuggingFace-fastaiv2.ipynb) written by [Pierre Guillou](https://huggingface.co/pierreguillou). The model is available both for PyTorch and TensorFlow use.

## Model

The model was trained on 3 epochs with a learning rate of 2e-3 and achieved a training loss per steps as shown below.

|  Step  |Training loss|
|--------|-------------|
|500	 |  5.051300   |
|1000	 |  3.701700   |
|1500	 |  3.288600   |
|2000	 |  3.024000   |
|2500	 |  2.833500   |
|3000	 |  2.741600   |
|3500	 |  2.637900   |
|4000	 |  2.547900   |
|4500	 |  2.451500   |
|5000	 |  2.409600   |
|5500	 |  2.388300   |
|6000	 |  2.351600   |

## How to Use
### As Masked Language Model
```python
from transformers import pipeline
pretrained_name = "StevenLimcorn/MelayuBERT"
fill_mask = pipeline(
    "fill-mask",
    model=pretrained_name,
    tokenizer=pretrained_name
)
fill_mask("Saya [MASK] makan nasi hari ini.")
```

### Import Tokenizer and Model
```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
  
tokenizer = AutoTokenizer.from_pretrained("StevenLimcorn/MelayuBERT")

model = AutoModelForMaskedLM.from_pretrained("StevenLimcorn/MelayuBERT")
```
## Author
Melayu BERT was trained by [Steven Limcorn](https://github.com/stevenlimcorn) and [Wilson Wongso](https://hf.co/w11wo).