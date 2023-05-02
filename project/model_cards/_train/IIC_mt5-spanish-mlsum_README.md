---
language:
- es
tags:
- summarization
license: apache-2.0
datasets:
- mlsum
metrics:
- rouge1
- rouge2
- rougeL
- rougeLsum

model-index:
- name: xprophetnet-spanish-mlsum
  results:
  - task: 
      type: summarization 
      name: abstractive summarization  
    dataset:
      type: mlsum
      name: mlsum-es
      args: es         
    metrics:
      - type: rouge1    
        value: 21.9788 
        name: rouge1    
      - type: rouge2
        value: 6.5249
        name: rouge2
      - type: rougeL
        value: 17.7444
        name: rougeL
      - type: rougeLsum
        value: 18.9783
        name: rougeLsum
---

This is a model for text summarization in Spanish. It has been trained on the Spanish portion of [mlsum](https://huggingface.co/datasets/mlsum), finetuning the [mt5-base model](https://huggingface.co/google/mt5-base).

We used the following set of hyperparameters:

```python

    {
      "learning_rate": 2e-5,
      "num_train_epochs": 8,
      "per_device_train_batch_size": 1,
      "per_device_eval_batch_size": 1,
      "gradient_accumulation_steps": 256,
      "fp16": False,
      "weight_decay": 0.01,
    }
```

The model was finetuned to predict the concatenation of the title and the summary of each item in the dataset. The results that we show below correspond to the set split of mlsum. The metrics for the **concatenation of titles and summaries** are:

```json
{'rouge1': 26.946, 'rouge2': 10.7271, 'rougeL': 21.4591, 'rougeLsum': 24.5001, 'gen_len': 18.9628}
```
On the other hand, the metrics for **just the summaries** are:

```json
{'rouge1': 21.9788, 'rouge2': 6.5249, 'rougeL': 17.7444, 'rougeLsum': 18.9783, 'gen_len': 18.9628}
```

This model is really easy to use, and with the following lines of code you can just start summarizing your documents in Spanish:

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

text = "Hola esto es un ejemplo de texto a resumir. Poco hay que resumir aquí, pero es sólo de muestra."
model_str = "IIC/mt5-spanish-mlsum"
tokenizer = AutoTokenizer.from_pretrained(model_str)
model = AutoModelForSeq2SeqLM.from_pretrained(model_str)

input_ids = tokenizer(text, return_tensors="pt").input_ids

output_ids = model.generate(input_ids)[0]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
```

### Contributions
Thanks to [@avacaondata](https://huggingface.co/avacaondata), [@alborotis](https://huggingface.co/alborotis), [@albarji](https://huggingface.co/albarji), [@Dabs](https://huggingface.co/Dabs), [@GuillemGSubies](https://huggingface.co/GuillemGSubies) for adding this model.