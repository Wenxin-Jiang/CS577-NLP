---
license: mit
---

Base model: [gpt2-large](https://huggingface.co/gpt2-large)

Fine-tuned to generate responses on a dataset of [COVID-19 public health tweets](https://github.com/TheRensselaerIDEA/generative-response-modeling). For more information about the dataset, task and training, see [our paper](https://arxiv.org/abs/2204.04353). This checkpoint corresponds to the lowest validation perplexity (3.36 at 2 epochs) seen during training. See Training metrics for Tensorboard logs.

Also see: our [Vaccine public health tweet response model](https://huggingface.co/TheRensselaerIDEA/gpt2-large-vaccine-tweet-response).

**Data input format:** <span style="color:red"><|message|></span>public health message<span style="color:red"><|author|></span>public health Twitter handle<span style="color:red"><|response|></span>

Example:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers.trainer_utils import set_seed
import torch

tokenizer = AutoTokenizer.from_pretrained("TheRensselaerIDEA/gpt2-large-covid-tweet-response")
model = AutoModelForCausalLM.from_pretrained("TheRensselaerIDEA/gpt2-large-covid-tweet-response")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
set_seed(33)

message = "Is your child worried about #COVID19? Learn the facts so you can answer your children’s questions."
author = "CDCgov"
num_responses = 2

author_token, message_token, response_token = tokenizer.additional_special_tokens
input_str = f"{message_token}{message}{author_token}{author}{response_token}"
inputs = tokenizer(input_str, return_tensors="pt").to(device)

responses_ids = model.generate(**inputs,
                               max_new_tokens=100,
                               pad_token_id=tokenizer.pad_token_id,
                               do_sample=True,
                               top_p=0.95,
                               temperature=1.5,
                               num_beams=3,
                               early_stopping=True,
                               num_return_sequences=num_responses)

responses = [tokenizer.decode(r[inputs.input_ids.shape[-1]:], skip_special_tokens=True) for r in responses_ids]
for i, resp in enumerate(responses):
    print(f"Response {i}: {resp}\n")
```

Output:
```
Response 0: @CDCgov I'm not worried. I don't know who needs to hear this, but I have a feeling I know who will be listening. 
It is not the virus. It is the media. I know you and CDC have been lying for months now, but the media will keep pushing this lie.

Response 1: #WashYourHands to help #StopTheSpread of #COVID19 and other diseases. Learn more about hand washing: #HandWashing
```

