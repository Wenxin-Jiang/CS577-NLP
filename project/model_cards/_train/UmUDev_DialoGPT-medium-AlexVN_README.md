---
tags:
- conversational
---

```python
from transformers import AutoTokenizer, AutoModelWithLMHead
  
tokenizer = AutoTokenizer.from_pretrained("UmUDev/DialoGPT-medium-Alex")

model = AutoModelWithLMHead.from_pretrained("UmUDev/DialoGPT-medium-Alex")


print("====chatting 5 times with nucleus & top-k sampling & tweaking temperature & multiple sentences====")
# chatting 5 times with nucleus & top-k sampling & tweaking temperature & multiple
# sentences
for step in range(20):
    # take user input
    text = input(">> You:")
    # encode the input and add end of string token
    input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors="pt")
    # concatenate new user input with chat history (if there is)
    bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1) if step > 0 else input_ids
    # generate a bot response
    chat_history_ids_list = model.generate(
        bot_input_ids,
        max_length=1000,
        do_sample=True,
        top_p=0.95,
        top_k=50,
        temperature=0.75,
        num_return_sequences=5,
        pad_token_id=tokenizer.eos_token_id
    )
    #print the outputs
    for i in range(len(chat_history_ids_list)):
      output = tokenizer.decode(chat_history_ids_list[i][bot_input_ids.shape[-1]:], skip_special_tokens=True)
      print(f"DialoGPT {i}: {output}")
    choice_index = int(input("Choose the response you want for the next input: "))
    chat_history_ids = torch.unsqueeze(chat_history_ids_list[choice_index], dim=0)
```