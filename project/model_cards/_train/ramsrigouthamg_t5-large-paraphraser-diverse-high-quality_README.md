Blog post with more details as well as easy to use Google Colab link: https://towardsdatascience.com/high-quality-sentence-paraphraser-using-transformers-in-nlp-c33f4482856f

!pip install transformers==4.10.2

!pip install sentencepiece==0.1.96

```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained("ramsrigouthamg/t5-large-paraphraser-diverse-high-quality")
tokenizer = AutoTokenizer.from_pretrained("ramsrigouthamg/t5-large-paraphraser-diverse-high-quality")

import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print ("device ",device)
model = model.to(device)

# Beam Search

context = "Once, a group of frogs were roaming around the forest in search of water."
text = "paraphrase: "+context + " </s>"

encoding = tokenizer.encode_plus(text,max_length =128, padding=True, return_tensors="pt")
input_ids,attention_mask  = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)

model.eval()
beam_outputs = model.generate(
    input_ids=input_ids,attention_mask=attention_mask,
    max_length=128,
    early_stopping=True,
    num_beams=15,
    num_return_sequences=3

)

print ("\n\n")
print ("Original: ",context)
for beam_output in beam_outputs:
    sent = tokenizer.decode(beam_output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
    print (sent)
```
    
**Output from the above code**
    
```
Original:  Once, a group of frogs were roaming around the forest in search of water.
paraphrasedoutput: A herd of frogs were wandering around the woods in search of water.
paraphrasedoutput: A herd of frogs was wandering around the woods in search of water.
paraphrasedoutput: A herd of frogs were wandering around the forest in search of water at one time.
```