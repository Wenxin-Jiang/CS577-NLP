---
language: 
- ru
- ru-RU 
tags:
- conversational
---
### 📝 Description

DialoGPT trained on Russian language and fine tuned on my telegram chat.


This model was created by [sberbank-ai](https://hf.co/sberbank-ai) and trained on Russian forums (see [Grossmend's model](https://hf.co/Grossmend/rudialogpt3_medium_based_on_gpt2)). You can find info about how it has been trained on [habr](https://habr.com/ru/company/icl_services/blog/548244/) (in Russian). I have created a **simple pipeline** and **fine tuned** that model on my own **exported telegram chat** (~30mb json). It is in fact very easy to get the data from telegram and fine tune a model. Therefore, I made a **colab tutorial** for it: https://colab.research.google.com/drive/1fnAVURjyZRK9VQg1Co_-SKUQnRES8l9R?usp=sharing

⚠️ Due to specifics of the data Hosted inference API may not work properly ⚠️

🤗To try it use my [Spaces demo](https://huggingface.co/spaces/Kirili4ik/chat-with-Kirill)🤗


### ❓ How to use with code

```python

# Download model and tokenizer
checkpoint = "Kirili4ik/ruDialoGpt3-medium-finetuned-telegram"   
tokenizer =  AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)
model.eval()


# util function to get expected len after tokenizing
def get_length_param(text: str, tokenizer) -> str:
    tokens_count = len(tokenizer.encode(text))
    if tokens_count <= 15:
        len_param = '1'
    elif tokens_count <= 50:
        len_param = '2'
    elif tokens_count <= 256:
        len_param = '3'
    else:
        len_param = '-'
    return len_param


# util function to get next person number (1/0) for Machine or Human in the dialogue
def get_user_param(text: dict, machine_name_in_chat: str) -> str:
    if text['from'] == machine_name_in_chat:
        return '1'  # machine
    else:
        return '0'  # human


chat_history_ids = torch.zeros((1, 0), dtype=torch.int)

while True:
    
    next_who = input("Who's phrase?\t")  #input("H / G?")     # Human or GPT

    # In case Human
    if next_who == "H" or next_who == "Human":
        input_user = input("===> Human: ")
        
        # encode the new user input, add parameters and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(f"|0|{get_length_param(input_user, tokenizer)}|" \
                                              + input_user + tokenizer.eos_token, return_tensors="pt")
        # append the new user input tokens to the chat history
        chat_history_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)

    if next_who == "G" or next_who == "GPT":

        next_len = input("Phrase len? 1/2/3/-\t")  #input("Exp. len?(-/1/2/3): ")
        # encode the new user input, add parameters and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(f"|1|{next_len}|", return_tensors="pt")
        # append the new user input tokens to the chat history
        chat_history_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
        
        # print(tokenizer.decode(chat_history_ids[-1])) # uncomment to see full gpt input
        
        # save previous len
        input_len = chat_history_ids.shape[-1]
        # generated a response; PS you can read about the parameters at hf.co/blog/how-to-generate
        chat_history_ids = model.generate(
            chat_history_ids,
            num_return_sequences=1,                     # use for more variants, but have to print [i]
            max_length=512,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=50,
            top_p=0.9,
            temperature = 0.6,                          # 0 for greedy
            mask_token_id=tokenizer.mask_token_id,
            eos_token_id=tokenizer.eos_token_id,
            unk_token_id=tokenizer.unk_token_id,
            pad_token_id=tokenizer.pad_token_id,
            device='cpu'
        )
        
        
        # pretty print last ouput tokens from bot
        print(f"===> GPT-3:  {tokenizer.decode(chat_history_ids[:, input_len:][0], skip_special_tokens=True)}")
```