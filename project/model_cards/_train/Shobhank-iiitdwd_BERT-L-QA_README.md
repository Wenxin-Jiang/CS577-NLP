---
language: en
license: cc-by-4.0
datasets:
- squad_v2
model-index:
- name: deepset/bert-large-uncased-whole-word-masking-squad2
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
      value: 80.8846
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2E5ZGNkY2ExZWViZGEwNWE3OGRmMWM2ZmE4ZDU4ZDQ1OGM3ZWE0NTVmZjFmYmZjZmJmNjJmYTc3NTM3OTk3OSIsInZlcnNpb24iOjF9.aSblF4ywh1fnHHrN6UGL392R5KLaH3FCKQlpiXo_EdQ4XXEAENUCjYm9HWDiFsgfSENL35GkbSyz_GAhnefsAQ
    - type: f1
      value: 83.8765
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGFlNmEzMTk2NjRkNTI3ZTk3ZTU1NWNlYzIyN2E0ZDFlNDA2ZjYwZWJlNThkMmRmMmE0YzcwYjIyZDM5NmRiMCIsInZlcnNpb24iOjF9.-rc2_Bsp_B26-o12MFYuAU0Ad2Hg9PDx7Preuk27WlhYJDeKeEr32CW8LLANQABR3Mhw2x8uTYkEUrSDMxxLBw
---

# bert-large-uncased-whole-word-masking-squad2

This is a berta-large model, fine-tuned using the SQuAD2.0 dataset for the task of question answering.

## Overview
**Language model:** bert-large  
**Language:** English  
**Downstream-task:** Extractive QA  
**Training data:** SQuAD 2.0  
**Eval data:** SQuAD 2.0  
**Code:**  See [an example QA pipeline on Haystack](https://haystack.deepset.ai/tutorials/first-qa-system)  

## Usage

### In Haystack
Haystack is an NLP framework by deepset. You can use this model in a Haystack pipeline to do question answering at scale (over many documents). To load the model in [Haystack](https://github.com/deepset-ai/haystack/):
```python
reader = FARMReader(model_name_or_path="deepset/bert-large-uncased-whole-word-masking-squad2")
# or 
reader = TransformersReader(model_name_or_path="FILL",tokenizer="deepset/bert-large-uncased-whole-word-masking-squad2")
```

### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/bert-large-uncased-whole-word-masking-squad2"

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

## About us
<div class="grid lg:grid-cols-2 gap-x-4 gap-y-3">
    <div class="w-full h-40 object-cover mb-2 rounded-lg flex items-center justify-center">
         <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/deepset-logo-colored.png" class="w-40"/>
     </div>
     <div class="w-full h-40 object-cover mb-2 rounded-lg flex items-center justify-center">
         <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/haystack-logo-colored.png" class="w-40"/>
     </div>
</div>

[deepset](http://deepset.ai/) is the company behind the open-source NLP framework [Haystack](https://haystack.deepset.ai/) which is designed to help you build production ready NLP systems that use: Question answering, summarization, ranking etc.


Some of our other work: 
- [Distilled roberta-base-squad2 (aka "tinyroberta-squad2")]([https://huggingface.co/deepset/tinyroberta-squad2)
- [German BERT (aka "bert-base-german-cased")](https://deepset.ai/german-bert)
- [GermanQuAD and GermanDPR datasets and models (aka "gelectra-base-germanquad", "gbert-base-germandpr")](https://deepset.ai/germanquad)

## Get in touch and join the Haystack community

<p>For more info on Haystack, visit our <strong><a href="https://github.com/deepset-ai/haystack">GitHub</a></strong> repo and <strong><a href="https://docs.haystack.deepset.ai">Documentation</a></strong>. 

We also have a <strong><a class="h-7" href="https://haystack.deepset.ai/community">Discord community open to everyone!</a></strong></p>

[Twitter](https://twitter.com/deepset_ai) | [LinkedIn](https://www.linkedin.com/company/deepset-ai/) | [Discord](https://haystack.deepset.ai/community/join) | [GitHub Discussions](https://github.com/deepset-ai/haystack/discussions) | [Website](https://deepset.ai)

By the way: [we're hiring!](http://www.deepset.ai/jobs)