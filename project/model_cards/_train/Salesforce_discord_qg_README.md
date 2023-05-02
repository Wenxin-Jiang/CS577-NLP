---
license: apache-2.0
language:
- en
tags:
- question_generation
- qg
- qgen
widget:
- text: "The International Monetary Fund warned on Tuesday that colliding pressures from inflation, war-driven energy and food crises and sharply higher interest rates were pushing the world to the brink of recession and threatening financial market stability."
  example_title: "Example 1"

---

Model card for the Question Generation component of the Discord Questions paper (EMNLP 2022 - Findings). The model is a finetuned BART-large, and can be used with the following command:
```py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

dqg_tokenizer = AutoTokenizer.from_pretrained("Salesforce/discord_qg")
discord_qg = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/discord_qg")

paragraph = "The International Monetary Fund warned on Tuesday that colliding pressures from inflation, war-driven energy and food crises and sharply higher interest rates were pushing the world to the brink of recession and threatening financial market stability."

encoder_ids = dqg_tokenizer.batch_encode_plus([paragraph], add_special_tokens=True, return_tensors="pt")
model_output = discord_qg.generate(**encoder_ids)

generated_texts = dqg_tokenizer.batch_decode(model_output, skip_special_tokens=True)
print(generated_texts) #  ['When was the last time the IMF warned of a global recession?']
```

The model has a tendency to generate "When " questions. If you would rather generate other questions you can do the following:

```py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

qg_tokenizer = AutoTokenizer.from_pretrained("Salesforce/discord_qg")
qg_model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/discord_qg")

paragraph = "The International Monetary Fund warned on Tuesday that colliding pressures from inflation, war-driven energy and food crises and sharply higher interest rates were pushing the world to the brink of recession and threatening financial market stability."

for start_word in ["How", "Why"]:
    encoder_ids = qg_tokenizer.batch_encode_plus([paragraph], add_special_tokens=True, padding=True, truncation=True, return_tensors="pt")
    decoder_input_ids = qg_tokenizer.batch_encode_plus([start_word], add_special_tokens=True, return_tensors="pt")["input_ids"][:, :-1]
    model_output = qg_model.generate(**encoder_ids, decoder_input_ids=decoder_input_ids, max_length=20)
    generated_questions = qg_tokenizer.batch_decode(model_output, skip_special_tokens=True)

    print(generated_questions)
 ```
 Prints:
 ```
['How will the global economy be affected?']
['Why was the IMF warning?']
 ```