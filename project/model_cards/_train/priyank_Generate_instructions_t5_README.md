
```
import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer


def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    
    set_seed(42)


model = T5ForConditionalGeneration.from_pretrained("priyank/Generate_instructions_t5")
tokenizer = T5Tokenizer.from_pretrained("priyank/Generate_instructions_t5")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)


sentence = "ask user to provide his date of birth"
text =  "paraphrase: " + sentence + " </s>"


max_len = 256

encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)


# set top_k = 50 and set top_p = 0.95 and num_return_sequences = 3
beam_outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    do_sample=True,
    max_length=256,
    top_k=120,
    top_p=0.98,
    early_stopping=True,
    num_return_sequences=10
)


print ("\\
Apprentice Query ::")
print (sentence)
print ("\\
Auto Generated Instruction ::")
final_outputs =[]
for beam_output in beam_outputs:
    sent = tokenizer.decode(beam_output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
    if sent.lower() != sentence.lower() and sent not in final_outputs:
        final_outputs.append(sent)

for i, final_output in enumerate(final_outputs):
    print("{}: {}".format(i, final_output))


Apprentice Query ::
if balance is greater than $100, then tell the user he needs more balance

Auto Generated Instruction ::
0: IF (assert(user.balance > $100)) THEN (say you need more balance)

```

Reference: https://github.com/ramsrigouthamg/Paraphrase-any-question-with-T5-Text-To-Text-Transfer-Transformer-