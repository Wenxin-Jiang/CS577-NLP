---
language:
- es
tags:
- summarization  # Example: audio
- seq2seq  # Example: automatic-speech-recognition
datasets:
- mlsum
metrics:
- rouge2
- rouge1
- rougel
- rougelsum

# Optional. Add this if you want to encode your eval results in a structured way.
model-index:
- name: marimari-r2r-mlsum
  results:
  - task: 
      type: summarization  # Required. Example: automatic-speech-recognition
      name: abstractive summarization  # Optional. Example: Speech Recognition
    dataset:
      type: mlsum  # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: mlsum-es  # Required. Example: Common Voice zh-CN
      args: es         # Optional. Example: zh-CN
    metrics:
      - type: rouge1    # Required. Example: wer
        value: 28.7802  # Required. Example: 20.90
        name: rouge1    # Optional. Example: Test WER
      - type: rouge2
        value: 10.6748
        name: rouge2
      - type: rougeL
        value: 23.0447
        name: rougeL
      - type: rougeLsum
        value: 23.4055
        name: rougeLsum
---

<img src="https://huggingface.co/IIC/marimari-r2r-mlsum/resolve/main/marimariLogo.png"/>

This is a model for text summarization in Spanish. It has been trained on the spanish portion of [mlsum](https://huggingface.co/datasets/mlsum). For that, MariMari was created. It is called like that because it is an EncoderDecoder model built from Maria model, specifically, the [roberta model from the Maria Project](https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne). For building the Encoder Decoder model, [this paper was followed](https://arxiv.org/abs/1907.12461), which has a [direct implementation in transformers](https://huggingface.co/docs/transformers/master/model_doc/encoder-decoder). As there are no natural encoder decoder models in Spanish, such as BART or T5, we decided to leverage the capacity of the Roberta model of the MarIA project, as it has shown great results on several NLU tasks, therefore it was natural to think it could perform well on NLG tasks when trained properly.

For tuning the hyperparameters  of the model we used [Optuna](https://optuna.org/), with only 10 different trials and 7 initial random trials, as [the dataset chosen for training the model, mlsum](https://huggingface.co/datasets/mlsum) was huge. The set of hyperparameters used was the following:

```python

    def hp_space(trial):
        return {
            "learning_rate": trial.suggest_float(
                "learning_rate", 3e-5, 7e-5, log=True
            ),
            "num_train_epochs": trial.suggest_categorical(
                "num_train_epochs", [7]
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

The reported results are on the test split of mlsum. As you can see, MariMari-r2r-mlsum works better for summarization on mlsum than the previous best model in this regard, [beto2beto](https://huggingface.co/LeoCordoba/beto2beto-mlsum). The complete metrics on test are:

```json
{"rouge1": 28.7802, "rouge2": 10.6748, "rougeL": 23.0447, "rougeLsum": 23.4055, "gen_len": 25.7803}
```

This model is really easy to use, and with the following lines of code you can just start summarizing your documents in Spanish:

```python
from transformers import EncoderDecoderModel, AutoTokenizer

text = "Hola esto es un ejemplo de texto a resumir. Poco hay que resumir aquí, pero es sólo de muestra."

tokenizer = AutoTokenizer.from_pretrained("IIC/marimari-r2r-mlsum")
model = EncoderDecoderModel.from_pretrained("IIC/marimari-r2r-mlsum")

input_ids = tokenizer(text, return_tensors="pt").input_ids

output_ids = model.generate(input_ids)[0]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
```

### Contributions
Thanks to [@avacaondata](https://huggingface.co/avacaondata), [@alborotis](https://huggingface.co/alborotis), [@albarji](https://huggingface.co/albarji), [@Dabs](https://huggingface.co/Dabs), [@GuillemGSubies](https://huggingface.co/GuillemGSubies) for adding this model.