---
datasets:
- squad_v2
---

# RoBERTa-base for QA

## Overview
**Language model:** 'roberta-base' </br>
**Language:** English </br>
**Downstream-task:** Extractive QA </br>
**Training data:** SQuAD 2.0 </br>
**Eval data:** SQuAD 2.0 </br>
**Code:** <TBD> </br>

## Env Information
`transformers` version: 4.9.1 </br>
Platform: Linux-5.4.104+-x86_64-with-Ubuntu-18.04-bionic </br>
Python version: 3.7.11 </br>
PyTorch version (GPU?): 1.9.0+cu102 (False)</br>
Tensorflow version (GPU?): 2.5.0 (False)</br>

## Hyperparameters
```
max_seq_len=386
doc_stride=128
n_best_size=20
max_answer_length=30
min_null_score=7.0
batch_size=8

n_epochs=6
base_LM_model = "roberta-base"
learning_rate=1.5e-5
adam_epsilon=1e-5
adam_beta1=0.95
adam_beta2=0.999
warmup_steps=100
weight_decay=0.01
optimizer=AdamW
lr_scheduler="polynomial"
```
##### There is a special threshold value CLS_threshold=-3 used to more accurately identify no answers [Logic will be available in GitHub Repo [TBD]

## Performance
```
"exact": 81.192622
"f1":    83.95408
"total": 11873
"HasAns_exact": 74.190283
"HasAns_f1":    79.721119
"HasAns_total": 5928
"NoAns_exact":  88.174937
"NoAns_f1":     88.174937
"NoAns_total":  5945
```

## Usage
### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "PremalMatalia/roberta-base-best-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'Which name is also used to describe the Amazon rainforest in English?',
    'context': 'The Amazon rainforest (Portuguese: Floresta Amazônica or Amazônia; Spanish: Selva Amazónica, Amazonía or usually Amazonia; French: Forêt amazonienne; Dutch: Amazoneregenwoud), also known in English as Amazonia or the Amazon Jungle, is a moist broadleaf forest that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 square kilometres (2,700,000 sq mi), of which 5,500,000 square kilometres (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations. The majority of the forest is contained within Brazil, with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, and with minor amounts in Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana. States or departments in four nations contain "Amazonas" in their names. The Amazon represents over half of the planet\'s remaining rainforests, and comprises the largest and most biodiverse tract of tropical rainforest in the world, with an estimated 390 billion individual trees divided into 16,000 species.'
}
res = nlp(QA_input)
print(res)

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```

## Authors
Premal Matalia