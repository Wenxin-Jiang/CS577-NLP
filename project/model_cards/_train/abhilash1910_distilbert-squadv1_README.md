# DistilBERT--SQuAD-v1

Training is done on the [SQuAD](https://huggingface.co/datasets/squad) dataset. The model can be accessed via [HuggingFace](https://huggingface.co/abhilash1910/distilbert-squadv1):


## Model Specifications

We have used the following parameters:

- Training Batch Size : 512
- Learning Rate : 3e-5
- Training Epochs : 0.75
- Sequence Length : 384
- Stride : 128


## Usage Specifications


```python

from transformers import AutoModelForQuestionAnswering,AutoTokenizer,pipeline
model=AutoModelForQuestionAnswering.from_pretrained('abhilash1910/distilbert-squadv1')
tokenizer=AutoTokenizer.from_pretrained('abhilash1910/distilbert-squadv1')
nlp_QA=pipeline('question-answering',model=model,tokenizer=tokenizer)
QA_inp={
    'question': 'What is the fund price of Huggingface in NYSE?',
    'context': 'Huggingface Co. has a total fund price of $19.6 million dollars'
}
result=nlp_QA(QA_inp)
result
```

The result is:

```bash

{'score': 0.38547369837760925,
 'start': 42,
 'end': 55,
 'answer': '$19.6 million'}
 ```

---
language:
- en
license: apache-2.0
datasets:
- squad_v1

---

