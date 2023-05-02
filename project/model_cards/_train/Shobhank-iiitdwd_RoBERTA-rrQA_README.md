---
language: en
license: cc-by-4.0
datasets:
- squad_v2
model-index:
- name: Shobhank-iiitdwd/RoBERTA-rrQA
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad_v2
      type: squad_v2
      config: squad_v2
      split: validation
    metrics:
    - type: exact_match
      value: 79.9309
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDhhNjg5YzNiZGQ1YTIyYTAwZGUwOWEzZTRiYzdjM2QzYjA3ZTUxNDM1NjE1MTUyMjE1MGY1YzEzMjRjYzVjYiIsInZlcnNpb24iOjF9.EH5JJo8EEFwU7osPz3s7qanw_tigeCFhCXjSfyN0Y1nWVnSfulSxIk_DbAEI5iE80V4EKLyp5-mYFodWvL2KDA
    - type: f1
      value: 82.9501
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjk5ZDYwOGQyNjNkMWI0OTE4YzRmOTlkY2JjNjQ0YTZkNTMzMzNkYTA0MDFmNmI3NjA3NjNlMjhiMDQ2ZjJjNSIsInZlcnNpb24iOjF9.DDm0LNTkdLbGsue58bg1aH_s67KfbcmkvL-6ZiI2s8IoxhHJMSf29H_uV2YLyevwx900t-MwTVOW3qfFnMMEAQ
    - type: total
      value: 11869
      name: total
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMGFkMmI2ODM0NmY5NGNkNmUxYWViOWYxZDNkY2EzYWFmOWI4N2VhYzY5MGEzMTVhOTU4Zjc4YWViOGNjOWJjMCIsInZlcnNpb24iOjF9.fexrU1icJK5_MiifBtZWkeUvpmFISqBLDXSQJ8E6UnrRof-7cU0s4tX_dIsauHWtUpIHMPZCf5dlMWQKXZuAAA
---

# roberta-base for QA 

This is the [roberta-base](https://huggingface.co/roberta-base) model, fine-tuned using the [SQuAD2.0](https://huggingface.co/datasets/squad_v2) dataset. It's been trained on question-answer pairs, including unanswerable questions, for the task of Question Answering. 


## Overview
**Language model:** roberta-base  
**Language:** English  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0  
**Eval data:** SQuAD 2.0  

## Hyperparameters

```
batch_size = 96
n_epochs = 2
base_LM_model = "roberta-base"
max_seq_len = 386
learning_rate = 3e-5
lr_schedule = LinearWarmup
warmup_proportion = 0.2
doc_stride=128
max_query_length=64
```  The distilled model has a comparable prediction quality and runs at twice the speed of the base model.

## Usage

### In Haystack
Haystack is an NLP framework by deepset. You can use this model in a Haystack pipeline to do question answering at scale (over many documents). To load the model in [Haystack](https://github.com/deepset-ai/haystack/):
```python
reader = FARMReader(model_name_or_path="Shobhank-iiitdwd/RoBERTA-rrQA")
# or 
reader = TransformersReader(model_name_or_path="Shobhank-iiitdwd/RoBERTA-rrQA",tokenizer="Shobhank-iiitdwd/RoBERTA-rrQA")
```
### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "Shobhank-iiitdwd/RoBERTA-rrQA"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'Why is model conversion important?',
    'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
}
res = nlp(QA_input)

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```

## Performance
Evaluated on the SQuAD 2.0 dev set with the [official eval script](https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/).

```
"exact": 79.87029394424324,
"f1": 82.91251169582613,

"total": 11873,
"HasAns_exact": 77.93522267206478,
"HasAns_f1": 84.02838248389763,
"HasAns_total": 5928,
"NoAns_exact": 81.79983179142137,
"NoAns_f1": 81.79983179142137,
"NoAns_total": 5945
```