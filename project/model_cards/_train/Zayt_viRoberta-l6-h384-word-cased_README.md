More information: [github](https://github.com/TanHM-1211/viRoberta-l6-h384-cased)
```python
from underthesea import word_tokenize
from transformers import RobertaTokenizer, RobertaModel

model_name = 'Zayt/viRoberta-l6-h384-word-cased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForMaskedLM.from_pretrained(model_name)

text = word_tokenize("Xin chào, tôi không còn là sinh viên đại học Bách Khoa.", format='text')
output = model(**tokenizer(text, return_tensors='pt))
output
```