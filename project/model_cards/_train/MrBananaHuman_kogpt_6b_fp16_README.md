kakao brain에서 공개한 kogpt 6b model('kakaobrain/kogpt')을 fp16으로 저장한 모델입니다.

### 카카오브레인 모델을 fp16으로 로드하는 방법

```python
import torch
from transformers import GPTJForCausalLM

model = GPTJForCausalLM.from_pretrained('kakaobrain/kogpt', cache_dir='./my_dir', revision='KoGPT6B-ryan1.5b', torch_dtype=torch.float16)
```

### fp16 모델 로드 후 문장 생성
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_rLDzhGohJPbOD5I_eTIOdx4aOTp43uK?usp=sharing)

```python
import torch
from transformers import GPTJForCausalLM, AutoTokenizer

model = GPTJForCausalLM.from_pretrained('MrBananaHuman/kogpt_6b_fp16', low_cpu_mem_usage=True))
model.to('cuda')
tokenizer = AutoTokenizer.from_pretrained('MrBananaHuman/kogpt_6b_fp16')

input_text = '이순신은'
input_ids = tokenizer(input_text, return_tensors='pt').input_ids.to('cuda')

output = model.generate(input_ids, max_length=64)
print(tokenizer.decode(output[0]))

>>> 이순신은 우리에게 무엇인가? 1. 머리말 이글은 임진왜란 당시 이순인이 보여준

```

### 참고 링크
https://github.com/kakaobrain/kogpt/issues/6?fbclid=IwAR1KpWhuHnevQvEWV18o16k2z9TLgrXkbWTkKqzL-NDXHfDnWcIq7I4SJXM