---
license: afl-3.0
language: "he"
tags:
- Text Classification
widget:
- text: "היער השחור והגדול"
- text: "ואז הוא הלך לטייל בתוך היער השחור והגדול"
datasets:
- orisuchy/Descriptive_Sentences_He
metrics:
- accuracy
- f1

---
# **Descriptive Sentences Classifier**

Based on [AlephBERT](https://huggingface.co/onlplab/alephbert-base) model.

# **Metrics**
[accuracy](https://huggingface.co/metrics/accuracy): 0.813953488372093
</br>
[f1](https://huggingface.co/metrics/f1): 0.8181818181818182
## How to Use the model:
```python
from transformers import pipeline
classifier = pipeline("text-classification",model='orisuchy/Descriptive_Classifier', return_all_scores=True)
outputs = classifier("מסווג חתיך במיוחד")
print(outputs)

"""
Output:
[[
{'label': 'Descriptive', 'score': 0.999764621257782},
{'label': 'Not Descriptive', 'score': 0.00023541577684227377}]]
"""
```
#### Or, if you want only the final class:
```python
from transformers import pipeline
classifier = pipeline("text-classification",model='orisuchy/Descriptive_Classifier')
output = classifier("הלכתי אליו הביתה וחיכיתי")
print(output)

"""
Output:
[{'label': 'Not Descriptive', 'score': 0.999901533126831}]
"""
```
Created by Daniel Smotritsky & Ori Suchy
<br>
[GitHub](https://github.com/orisuchy/miniProject_DHU)
<iframe src="https://wandb.ai/orisuchy/huggingface/reports/Shared-panel-22-03-01-15-03-08--VmlldzoxNjI5MjM0?highlightShare" style="border:none;height:1024px;width:100%">


