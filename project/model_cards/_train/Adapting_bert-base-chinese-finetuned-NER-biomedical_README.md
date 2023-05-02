Fine-tuned [Bert-Base-Chinese](https://huggingface.co/bert-base-chinese) for NER task on [Adapting/chinese_biomedical_NER_dataset](https://huggingface.co/datasets/Adapting/chinese_biomedical_NER_dataset)

# Usage
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
tokenizer = AutoTokenizer.from_pretrained("Adapting/bert-base-chinese-finetuned-NER-biomedical")
model = AutoModelForTokenClassification.from_pretrained("Adapting/bert-base-chinese-finetuned-NER-biomedical",revision='7f63e3d18b1dc3cc23041a89e77be21860704d2e')

from transformers import pipeline
nlp = pipeline('ner',model=model,tokenizer = tokenizer)

tag_set = [
 'B_手术',
 'I_疾病和诊断',
 'B_症状',
 'I_解剖部位',
 'I_药物',
 'B_影像检查',
 'B_药物',
 'B_疾病和诊断',
 'I_影像检查',
 'I_手术',
 'B_解剖部位',
 'O',
 'B_实验室检验',
 'I_症状',
 'I_实验室检验'
 ]
 
tag2id = lambda tag: tag_set.index(tag)
id2tag = lambda id: tag_set[id]

def readable_result(result):

    results_in_word = []
    j = 0
    while j < len(result):   
        i = result[j]
        entity = id2tag(int(i['entity'][i['entity'].index('_')+1:]))
        token = i['word']
        if entity.startswith('B'):
            entity_name = entity[entity.index('_')+1:]

            word = token
            j = j+1
            while j<len(result):
                next = result[j]
                next_ent = id2tag(int(next['entity'][next['entity'].index('_')+1:]))
                next_token = next['word']

                if next_ent.startswith('I') and next_ent[next_ent.index('_')+1:] == entity_name:
                    word += next_token
                    j += 1

                    if j >= len(result):
                        results_in_word.append((entity_name,word))
                else:
                    results_in_word.append((entity_name,word))
                    break

        else:
            j += 1
    
    return results_in_word


        
print(readable_result(nlp('淋球菌性尿道炎会引起头痛')))

'''
[('疾病和诊断', '淋球菌性尿道炎'), ('症状', '头痛')]
'''
```