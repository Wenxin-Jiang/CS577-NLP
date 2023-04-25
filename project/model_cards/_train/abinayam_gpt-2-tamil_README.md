---

language: ta
datasets:
- oscar
- IndicNLP
widget:
- text: 'ஒரு ஊரிலே ஒரு காக்கைக்கு'

---
# GPT2-Tamil

This repository is created as part of the Flax/Jax community week by Huggingface. The aim of this project is to pretrain a language model using GPT-2 specifically for Tamil language. 

## Setup:
To setup the project, run the following command,
```python
pip install -r requirements.txt
```

## Model:
Pretrained model on Tamil language using a causal language modeling (CLM) objective.
 
## Dataset Used:
The GTP-2 model is trained on [oscar dataset - ta](https://huggingface.co/datasets/oscar) and [IndicNLP dataset - ta](https://indicnlp.ai4bharat.org/corpora/)

## Intended uses & limitations:
You can use the raw model for next sentence prediction, but it's mostly intended to be fine-tuned on a downstream task. See the [model hub](https://huggingface.co/models?filter=gpt2) to look for fine-tuned versions on a task that interests you.

## How to pretrain the model:
To perform training, do the following steps,

- Export the model directory (where you want to store the model artifacts like config, tokenizer, etc.)
```python
>>> export MODEL_DIR=<model_dir>
```
- Create the config.json by running the following command,
```python
>>> python src/create_config.py
```
- Create the tokenizer by running the following command,
```python
>>> python src/train_tokenizer.py
```
- Once the config and tokenizer is created, run the following script to start training the flax model
```python
>>> python scripts/train_gpt2-oscar-tamil.sh
```

## How to use:
To perform language generation using the model, pipeline can be used directly.

- First convert the flax model to pytorch using the following command,
```python
python src/convert_flax_to_pytorch.py
```
- Use the following snippet to perform language generation,
```python
 >>> from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline
 >>> model_name = 'abinayam/gpt-2-tamil'
 >>> model = AutoModelWithLMHead.from_pretrained(model_name)
 >>> tokenizer = AutoTokenizer.from_pretrained(model_name)
 >>> set_seed(42)
 >>> input_text = "ஒரு ஊரிலே ஒரு காக்கைக்கு"
 >>> max_len = 300
 >>> no_seq = 5
 >>> generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
 >>> sequence = generator(input_text, max_length=max_len, num_return_sequences=no_seq)
```
