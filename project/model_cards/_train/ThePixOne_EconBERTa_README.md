EconBERTa - RoBERTa further trained for 25k steps (T=512, batch_size = 256) on text sourced from economics books.

Example usage for MLM: 

```python
from transformers import RobertaTokenizer, RobertaForMaskedLM
from transformers import pipeline

tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForMaskedLM.from_pretrained('models').cpu()
model.eval()
mlm = pipeline('fill-mask', model = model, tokenizer  = tokenizer)
test = "ECB - euro, FED - <mask>, BoJ - yen"
print(mlm(test)[:2])

[{'sequence': 'ECB - euro, FED - dollar, BoJ - yen',
  'score': 0.7342271208763123,
  'token': 1404,
  'token_str': ' dollar'},
 {'sequence': 'ECB - euro, FED - dollars, BoJ - yen',
  'score': 0.10828445851802826,
  'token': 1932,
  'token_str': ' dollars'}]
```

