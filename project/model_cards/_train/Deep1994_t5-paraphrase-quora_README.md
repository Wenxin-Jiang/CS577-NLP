---
license: afl-3.0
---
## Model description
​T5 Model for generating paraphrases of english sentences. Trained on the [Quora Paraphrase dataset](https://www.kaggle.com/c/quora-question-pairs).

## Online demo website
Click [https://huggingface.co/spaces/Deep1994/t5-paraphrase](https://huggingface.co/spaces/Deep1994/t5-paraphrase) to have a try online.

## How to use
```python
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

set_seed(1234)

model = T5ForConditionalGeneration.from_pretrained('Deep1994/t5-paraphrase-quora')
tokenizer = T5Tokenizer.from_pretrained('Deep1994/t5-paraphrase-quora')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

sentence = "What is the best comedy TV serial/series?"

text =  "paraphrase: " + sentence

encoding = tokenizer.encode_plus(text, pad_to_max_length=True, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)

# top k/ top p sampling
beam_outputs = model.generate(
    input_ids=input_ids, 
    attention_mask=attention_masks,
    do_sample=True,
    max_length=20,
    top_k=50,
    top_p=0.95,
    early_stopping=True,
    num_return_sequences=5
)

# beam search
# beam_outputs = model.generate(
#     input_ids=input_ids, 
#     attention_mask=attention_masks, 
#     max_length=20, 
#     num_beams=5, 
#     no_repeat_ngram_size=2, 
#     num_return_sequences=5, 
#     early_stopping=True
# )

print ("\nOriginal Question: ")
print (sentence)
print ("\n")
print ("Paraphrased Questions: ")
final_outputs = []
for beam_output in beam_outputs:
    sent = tokenizer.decode(beam_output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    if sent.lower() != sentence.lower() and sent not in final_outputs:
        final_outputs.append(sent)

for i, final_output in enumerate(final_outputs):
    print("{}: {}".format(i, final_output))

```
```
Original Question:
What is the best comedy TV serial/series?

Beam search: 
0: What is the best comedy TV series?
1: What are some of the best comedy TV series?
2: Which is the best comedy TV series?
3: What are the best comedy TV series?
4: What are some of the best comedy TV shows?

Top k/ Top p sampling:
0: What are some of the best comedy TV dramas?
1: What are the best comedy TV series or series?
2: What are the best comedy television serials?
3: What is the best comedy series?
4: Which are some best comedy TV series series?
```

For more reference on training your own T5 model, do check out [t5-paraphrase-generation](https://github.com/Deep1994/t5-paraphrase-generation).