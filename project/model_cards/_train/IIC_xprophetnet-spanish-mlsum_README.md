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
        value: 25.1158  
        name: rouge1    
      - type: rouge2
        value: 8.4847
        name: rouge2
      - type: rougeL
        value: 20.6184
        name: rougeL
      - type: rougeLsum
        value: 20.8948
        name: rougeLsum
---

This is a model for text summarization in Spanish. It has been trained on the spanish portion of [mlsum](https://huggingface.co/datasets/mlsum). For that, [XLM-ProphetNet (a multilingual version of Prophetnet)](https://huggingface.co/microsoft/xprophetnet-large-wiki100-cased) was used. 

For tuning the hyperparameters  of the model we used [Optuna](https://optuna.org/), with only 10 different trials and 7 initial random trials, as the dataset chosen for training the model was huge. The set of hyperparameters used was the following:

```python

    def hp_space(trial):
        return {
            "learning_rate": trial.suggest_float(
                "learning_rate", 1e-5, 7e-5, log=True
            ),
            "num_train_epochs": trial.suggest_categorical(
                "num_train_epochs", [3, 5, 7, 10]
            ),
            "per_device_train_batch_size": trial.suggest_categorical(
                "per_device_train_batch_size", [16]),
            "per_device_eval_batch_size": trial.suggest_categorical(
                "per_device_eval_batch_size", [32]),
            "gradient_accumulation_steps": trial.suggest_categorical(
                "gradient_accumulation_steps", [2, 4, 8]),
            "warmup_steps": trial.suggest_categorical(
                "warmup_steps", [50, 100, 500, 1000]
            ),
            "weight_decay": trial.suggest_float(
                 "weight_decay", 0.0, 0.1
            ),
```

The reported results are on the test split of mlsum. Complete metrics are:

```json
{"rouge1": 25.1158, "rouge2": 8.4847, "rougeL": 20.6184, "rougeLsum": 20.8948, "gen_len": 19.6496}
```

This model is really easy to use, and with the following lines of code you can just start summarizing your documents in Spanish:

```python
from transformers import ProphetNetForConditionalGeneration, AutoTokenizer

text = "Hola esto es un ejemplo de texto a resumir. Poco hay que resumir aquí, pero es sólo de muestra."
model_str = "avacaondata/xprophetnet-spanish-mlsum"

tokenizer = AutoTokenizer.from_pretrained(model_str)
model = ProphetNetForConditionalGeneration.from_pretrained(model_str)

input_ids = tokenizer(text, return_tensors="pt").input_ids

output_ids = model.generate(input_ids)[0]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
```

### Contributions
Thanks to [@avacaondata](https://huggingface.co/avacaondata), [@alborotis](https://huggingface.co/alborotis), [@albarji](https://huggingface.co/albarji), [@Dabs](https://huggingface.co/Dabs), [@GuillemGSubies](https://huggingface.co/GuillemGSubies) for adding this model.