---
language: 
  - fa
tags:
  - Wikipedia
  - Summarizer
  - bert2bert
  - Summarization
task_categories:
  - Summarization
  - text generation
task_ids:
- news-articles-summarization
license:
- apache-2.0
multilinguality:
- monolingual
datasets:
- pn-summary
- XL-Sum
metrics:
- rouge-1
- rouge-2
- rouge-l
---


# WikiBert2WikiBert
Bert language models can be employed for Summarization tasks. WikiBert2WikiBert is an encoder-decoder transformer model that is initialized using the Persian WikiBert Model weights. The WikiBert Model is a Bert language model which is fine-tuned on Persian Wikipedia. After using the WikiBert weights for initialization, the model is trained for five epochs on PN-summary and Persian BBC datasets.

## How to Use:
You can use the code below to get the model's outputs, or you can simply use the demo on the right.
```
from transformers import (
    BertTokenizerFast,
    EncoderDecoderConfig,
    EncoderDecoderModel,
    BertConfig
)

model_name = 'Arashasg/WikiBert2WikiBert'
tokenizer = BertTokenizerFast.from_pretrained(model_name)
config = EncoderDecoderConfig.from_pretrained(model_name)
model = EncoderDecoderModel.from_pretrained(model_name, config=config)


def generate_summary(text):
    inputs = tokenizer(text, padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to("cuda")
    attention_mask = inputs.attention_mask.to("cuda")

    outputs = model.generate(input_ids, attention_mask=attention_mask)

    output_str = tokenizer.batch_decode(outputs, skip_special_tokens=True)


    return output_str

input = 'your input comes here'
summary = generate_summary(input)
```

## Evaluation
I separated 5 percent of the pn-summary for evaluation of the model. The rouge scores of the model are as follows:

| Rouge-1  | Rouge-2  | Rouge-l |
| ------------- | ------------- | ------------- |
| 38.97%  | 18.42%  | 34.50%  |

