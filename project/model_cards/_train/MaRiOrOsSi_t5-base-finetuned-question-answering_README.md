---
language: en
datasets:
- duorc
widget:
 - text: "question: Is Giacomo Italian? context: Giacomo is 25 years old and he was born in Tuscany"
 - text: "question: Where does Christian come from? context: Christian is a student of UNISI but he come from Caserta"
 - text: "question: Is the dog coat grey? context: You have a beautiful dog with a brown coat"
tags:
- Generative Question Answering
---

# T5 for Generative Question Answering

This model is the result produced by Christian Di Maio and Giacomo Nunziati for the Language Processing Technologies exam.
Reference for [Google's T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) fine-tuned on [DuoRC](https://huggingface.co/datasets/duorc) for **Generative Question Answering** by just prepending the *question* to the *context*.

## Code
The code used for T5 training is available at this [repository](https://github.com/nunziati/bert-vs-t5-for-question-answering/blob/main/train_t5_selfrc.py).

## Results
The results are evaluated on:

 - DuoRC/SelfRC -> Test Subset
- DuoRC/ParaphraseRC -> Test Subset
- SQUADv1 -> Validation Subset

Removing all tokens not related to dictionary words from the evaluation metrics.
The model used as reference is BERT finetuned on SQUAD v1.

| Model | SelfRC | ParaphraseRC | SQUAD
|--|--|--|--|
| T5-BASE-FINETUNED | **F1**: 49.00 **EM**: 31.38 | **F1**: 28.75 **EM**: 15.18 | **F1**: 63.28 **EM**: 37.24 |
| BERT-BASE-FINETUNED | **F1**: 47.18 **EM**: 30.76 | **F1**: 21.20 **EM**: 12.62 | **F1**: 77.19 **EM**: 57.81 |

## How to use it 🚀

```python
from  transformers  import  AutoTokenizer, AutoModelWithLMHead, pipeline

model_name = "MaRiOrOsSi/t5-base-finetuned-question-answering"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelWithLMHead.from_pretrained(model_name)
question = "What is 42?"
context = "42 is the answer to life, the universe and everything"
input = f"question: {question} context: {context}"
encoded_input = tokenizer([input],
							 return_tensors='pt',
							 max_length=512,
							 truncation=True)
output = model.generate(input_ids = encoded_input.input_ids,
							attention_mask = encoded_input.attention_mask)
output = tokenizer.decode(output[0], skip_special_tokens=True)
print(output)
```

## Citation

Created by [Christian Di Maio](https://it.linkedin.com/in/christiandimaio) and [Giacomo Nunziati](https://it.linkedin.com/in/giacomo-nunziati-b19572185) 

> Made with <span style="color: #e25555;">&hearts;</span> in Italy
