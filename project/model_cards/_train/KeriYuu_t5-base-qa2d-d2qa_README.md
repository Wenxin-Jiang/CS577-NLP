---
language:
- en
license:
- afl-3.0

---

# Easy Conversion Between Boolean QA Pairs and Declarative Statements

## Convert declarations to QAs:

Add the prefix "D2QA:" to the declaration.

## Convert QAs to declarations:

Add the prefix "QA2D:" to the QA pair.

## Example

```python
from transformers import T5Tokenizer, AutoModelForSeq2SeqLM
tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("KeriYuu/bootstrapQA")
input_text1 = "D2QA: Apple orchards lack the requisite soil pH to make blue colors."
input_text2 = "QA2D: question: Is the chance of always winning a lotto consistently very low? answer: Yes."
input = tokenizer(input_text1, return_tensors='pt', padding=True, max_length=64, truncation=True)
output = model.generate(input_ids=input['input_ids'],attention_mask=input['attention_mask'],max_length=64,num_beams=5)
result = tokenizer.batch_decode(output, skip_special_tokens=True)
```