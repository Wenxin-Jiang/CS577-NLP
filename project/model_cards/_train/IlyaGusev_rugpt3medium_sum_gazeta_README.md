---
language:
- ru
tags:
- causal-lm
- summarization
datasets:
- IlyaGusev/gazeta
license:
- apache-2.0
inference: false
widget:
- text: "Высота башни составляет 324 метра (1063 фута), примерно такая же высота, как у 81-этажного здания, и самое высокое сооружение в Париже. Его основание квадратно, размером 125 метров (410 футов) с любой стороны. Во время строительства Эйфелева башня превзошла монумент Вашингтона, став самым высоким искусственным сооружением в мире, и этот титул она удерживала в течение 41 года до завершения строительство здания Крайслер в Нью-Йорке в 1930 году. Это первое сооружение которое достигло высоты 300 метров. Из-за добавления вещательной антенны на вершине башни в 1957 году она сейчас выше здания Крайслер на 5,2 метра (17 футов). За исключением передатчиков, Эйфелева башня является второй самой высокой отдельно стоящей структурой во Франции после виадука Мийо.<s>"
  example_title: "Википедия"
---

# RuGPT3MediumSumGazeta

## Model description

This is the model for abstractive summarization for Russian based on [rugpt3medium_based_on_gpt2](https://huggingface.co/sberbank-ai/rugpt3medium_based_on_gpt2).


## Intended uses & limitations

#### How to use

Colab: [link](https://colab.research.google.com/drive/1eR-ev0Y5ISWIwGnzYYoHyGMaSIUz8GTN)

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "IlyaGusev/rugpt3medium_sum_gazeta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

article_text = "..."

text_tokens = tokenizer(
    article_text,
    max_length=600,
    add_special_tokens=False, 
    padding=False,
    truncation=True
)["input_ids"]
input_ids = text_tokens + [tokenizer.sep_token_id]
input_ids = torch.LongTensor([input_ids])

output_ids = model.generate(
    input_ids=input_ids,
    no_repeat_ngram_size=4
)

summary = tokenizer.decode(output_ids[0], skip_special_tokens=False)
summary = summary.split(tokenizer.sep_token)[1]
summary = summary.split(tokenizer.eos_token)[0]
print(summary)
```

## Training data

- Dataset: [Gazeta](https://huggingface.co/datasets/IlyaGusev/gazeta)

## Training procedure

- Training script: [train.py](https://github.com/IlyaGusev/summarus/blob/master/external/hf_scripts/train.py)
- Config: [gpt_training_config.json](https://github.com/IlyaGusev/summarus/blob/master/external/hf_scripts/configs/gpt_training_config.json)

## Eval results

* Train dataset: **Gazeta v1 train**
* Test dataset: **Gazeta v1 test**
* Source max_length: **600**
* Target max_length: **200**
* no_repeat_ngram_size: **4**
* num_beams: **5**

| Model                     | R-1-f | R-2-f | R-L-f | chrF | METEOR | BLEU | Avg char length |
|:--------------------------|:------|:------|:------|:-------|:-------|:-----|:-----|
| [mbart_ru_sum_gazeta](https://huggingface.co/IlyaGusev/mbart_ru_sum_gazeta)       | **32.4**  | 14.3  | 28.0  | 39.7 | **26.4** | 12.1 | 371 |
| [rut5_base_sum_gazeta](https://huggingface.co/IlyaGusev/rut5_base_sum_gazeta)      | 32.2  | **14.4**  | **28.1** | **39.8** | 25.7 | **12.3** | 330 |
| [rugpt3medium_sum_gazeta](https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta) | 26.2 | 7.7 | 21.7 | 33.8 | 18.2 | 4.3 | 244 |

* Train dataset: **Gazeta v1 train**
* Test dataset: **Gazeta v2 test**
* Source max_length: **600**
* Target max_length: **200**
* no_repeat_ngram_size: **4**
* num_beams: **5**

| Model                     | R-1-f | R-2-f | R-L-f | chrF | METEOR | BLEU | Avg char length |
|:--------------------------|:------|:------|:------|:-------|:-------|:-----|:-----|
| [mbart_ru_sum_gazeta](https://huggingface.co/IlyaGusev/mbart_ru_sum_gazeta)        | **28.7**  | **11.1**  | 24.4  | **37.3** | **22.7**  | **9.4** | 373 |
| [rut5_base_sum_gazeta](https://huggingface.co/IlyaGusev/rut5_base_sum_gazeta)      | 28.6 | **11.1** | **24.5** | 37.2 | 22.0 | **9.4** | 331 |
| [rugpt3medium_sum_gazeta](https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta) | 24.1 | 6.5 | 19.8 | 32.1 | 16.3 | 3.6 | 242 |

Evaluation script: [evaluate.py](https://github.com/IlyaGusev/summarus/blob/master/evaluate.py)

Flags: --language ru --tokenize-after --lower
