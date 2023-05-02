---
language: de
tags:
- grammar
- text2text-generation
license: cc-by-nc-sa-4.0
widget:
- text: "grammar: hier ein kleines beispiel was haltet ihr von der korrektur"
---

# T5 Grammar Correction 

This model restores upper and lower case as well as punctuation. It was trained with [Happy Transformer](https://github.com/EricFillion/happy-transformer) on the German Wikipedia dump.

## Usage 

`pip install happytransformer `

```python
from happytransformer import HappyTextToText, TTSettings
happy_tt = HappyTextToText("T5", "aiassociates/t5-small-grammar-correction-german")
args = TTSettings(num_beams=5, min_length=1)
# Add the prefix "grammar: " before each input 
result = happy_tt.generate_text("grammar: hier ein kleines beispiel was haltet ihr von der korrektur", args=args)
print(result.text) # Hier ein kleines Beispiel: Was haltet ihr von der Korrektur?
```

## Authors
**David Hustadt:** dh@ai.associates

## About us
[AI.Associates](https://www.ai.associates/)

[LinkedIn](https://www.linkedin.com/company/ai-associates)

We're always looking for developers to join us. Feel free to contact us careers@ai.associates