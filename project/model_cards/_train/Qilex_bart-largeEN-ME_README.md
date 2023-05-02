---
language:
- 'en'  
- 'me' 
license: afl-3.0  
tags:
- 'translation'
datasets:
- 'Qilex/EN-ME' 
metrics:
- bleu  

model-index:
- name: 'en-me'
  results:
  - task:
      type: 'translation'          
      name: 'translation en-me'           
    dataset:
      type: 'translation'
      name: 'Qilex/EN-ME'      
    
    metrics:
      - type: 'bleu'         
        value: 17.2    
---

This is a BART-large model finetuned on roughly 58000 aligned sentence pairs in English and Middle English, collected from the works of Geoffrey Chaucer, John Wycliffe, and the Gawain Poet.
<br>
It includes special characters such as þ. 
<br>
This model reflects the spelling inconsistencies characteristic of Middle English.
<br>
Because the model is trained largely on poetry and some prose, it is best at translating those sorts of tasks.
<br>
Performance can be improved by sentence tokenizing input data and translating sentence-by-sentence.
<br>
Removing contractions (hadn't -> had not) also boosts performance.

