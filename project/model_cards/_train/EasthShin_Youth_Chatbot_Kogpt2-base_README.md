## Youth_Chatbot_KoGPT2-base

**Demo Web**: [Ainize Endpoint](https://main-youth-chatbot-ko-gpt2-base-east-h-shin.endpoint.ainize.ai/)
<br>
**Demo Web Code**: [Github](https://github.com/EastHShin/Youth_Chatbot_KoGPT2-base)
<br>
**Youth-Chatbot API**: [Ainize API](https://ainize.ai/EastHShin/Youth_Chatbot_KoGPT2-base_API?branch=main)
<br>
<br>

## Overview
**Language model**: KoGPT2
<br>
**Language**: Korean
<br>
**Training data**: [Aihub](https://aihub.or.kr/aidata/7978)

## Usage
```
from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel
U_TKN = '<usr>'
S_TKN = '<sys>'
MASK = '<unused0>'
SENT = '<unused1>'
tokenizer = PreTrainedTokenizerFast.from_pretrained("EasthShin/Youth_Chatbot_Kogpt2-base",
  bos_token='</s>', eos_token='</s>', unk_token='<unk>',
  pad_token='<pad>', mask_token=MASK)

model = GPT2LMHeadModel.from_pretrained('EasthShin/Youth_Chatbot_Kogpt2-base')
input_ids = tokenizer.encode(U_TKN + {your text} + sent + S_TKN)
gen_ids = model.generate(torch.tensor([input_ids]),
                                 max_length=128,
                                 repetition_penalty= 2.0,
                                 pad_token_id=tokenizer.pad_token_id,
                                 eos_token_id=tokenizer.eos_token_id,
                                 bos_token_id=tokenizer.bos_token_id,
                                 use_cache=True)

generated = tokenizer.decode(gen_ids[0, :].tolist())

print(generated)
```