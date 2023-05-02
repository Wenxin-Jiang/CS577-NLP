---
datasets:
- squad_v2
---

# ALBERT-base for QA

## Overview
**Language model:** albert-base </br>
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
batch_size=32

n_epochs=3
base_LM_model = "albert-base-v2"
learning_rate=3e-5
adam_epsilon=1e-5
adam_beta1=0.95
adam_beta2=0.999
warmup_steps=300
weight_decay=0.01
optimizer=AdamW
lr_scheduler="polynomial"
```

## Performance
```
"exact": 78.253
"f1":    81.523
"total": 11873
"HasAns_exact": 73.616
"HasAns_f1":    80.165
"HasAns_total": 5928
"NoAns_exact":  82.876
"NoAns_f1":     82.876
"NoAns_total":  5945
```

## Usage
### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "PremalMatalia/albert-base-best-squad2"

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