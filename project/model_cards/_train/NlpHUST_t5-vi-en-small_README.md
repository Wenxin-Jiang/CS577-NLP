---
language:
- vi

tags:
- t5
- seq2seq

# Machine translation for vietnamese
## Model Description
T5-vi-en-small is a transformer model for vietnamese machine translation designed using T5 architecture.
## Training data
T5-vi-en-small was trained on 4M sentence pairs (english,vietnamese)
### How to use

```py
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
if torch.cuda.is_available():       
    device = torch.device("cuda")

    print('There are %d GPU(s) available.' % torch.cuda.device_count())

    print('We will use the GPU:', torch.cuda.get_device_name(0))
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")

model = T5ForConditionalGeneration.from_pretrained("NlpHUST/t5-vi-en-small")
tokenizer = T5Tokenizer.from_pretrained("NlpHUST/t5-vi-en-small")
model.to(device)

src = "Indonesia phỏng đoán nguyên nhân tàu ngầm chở 53 người mất tích bí ẩn"
tokenized_text = tokenizer.encode(src, return_tensors="pt").to(device)
model.eval()
summary_ids = model.generate(
                    tokenized_text,
                    max_length=256, 
                    num_beams=5,
                    repetition_penalty=2.5, 
                    length_penalty=1.0, 
                    early_stopping=True
                )
output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(output)

Indonesia anticipates the cause of the submarine transporting 53 mysterious missing persons

```