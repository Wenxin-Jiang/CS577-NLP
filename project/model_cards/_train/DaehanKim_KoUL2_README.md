# KoUL2 

- 모두의말뭉치 + AI hub에 공개된 기타 한국어 텍스트 데이터를 기반으로 학습된 UL2(Unifying Language Learning Paradigm)모델입니다.
- 파라미터 수는 279526656(280M)개로 encoder-decoder 구조를 가지고 있습니다.
- [lassl](https://github.com/lassl/lassl) 오픈소스 프로젝트를 활용하여 학습하였습니다.
- 사전학습만 진행된 모델이므로 아래와 같이 UL2의 denoising을 확인해보실 수 있습니다. 
```py
model = T5ForConditionalGeneration.from_pretrained("DaehanKim/KoUL2")                                                                                                 
tokenizer = AutoTokenizer.from_pretrained("DaehanKim/KoUL2")

for prefix_token in ("[NLU]","[NLG]","[S2S]"):
    input_string = f"{prefix_token}어떤 아파트는 호가가 [new_id_27]는등 경기 침체로 인한 [new_id_26]를 확인할 수 있었습니다.</s>"
    inputs = tokenizer(input_string, return_tensors="pt", add_special_tokens=False)
    decoder_inputs = tokenizer("<pad>[new_id_27]", return_tensors='pt', add_special_tokens=False)
    outputs = model.generate(input_ids = inputs.input_ids, decoder_input_ids=decoder_inputs.input_ids, num_beams=10, num_return_sequences=5)
    print(tokenizer.batch_decode(outputs))
``` 
```
# output
['<pad>[new_id_27] 고공행진을[new_id_26] 아파트의 호가가 고공행진을', '<pad>[new_id_27] 고공 행진을[new_id_26] 아파트 호가가 고공 행진', '<pad>[new_id_27] 고공 행진을[new_id_26] 아파트 값이 고공 행진', '<pad>[new_id_27] 고공 행진을[new_id_26] 아파트의 호가가 고공 행', '<pad>[new_id_27] 고공 행진을[new_id_26] 아파트 호가가 고공행진을']
['<pad>[new_id_27] 천만 원 이상 오르고 어떤 아파트는 호가가 천만 ', '<pad>[new_id_27] 천만 원 이상 오르고 어떤 아파트는 호가가 천만[new_id_26]', '<pad>[new_id_27] 천만 원 이상 오르고 어떤 아파트는 호가가 천 만', '<pad>[new_id_27] 천만 원에서 천만 원 까지 오르는[new_id_26] 아파트 가격 하락', '<pad>[new_id_27] 천만 원 이상 오르고 어떤 아파트는 호가가 천 원']
['<pad>[new_id_27] 천만 원 이상 오르는[new_id_26] 아파트 값이 천만 원', '<pad>[new_id_27] 천만 원 이상 오르는[new_id_26] 아파트 값이 천만 원을', '<pad>[new_id_27] 천만 원 이상 오르는[new_id_26] 아파트 값이 오르는 등 부동산', '<pad>[new_id_27] 고공 행진을 이어가고[new_id_26] 아파트 값이 하락하는 등', '<pad>[new_id_27] 고공 행진을 하고[new_id_26] 아파트 값이 하락하는 등']
```
- 사전학습 과정에서 sentinel token은 기존 T5와 호환되게 하기 위해 [new_id_27]...[new_id_1]<extra_token_0>...<extra_token_99> 순으로 들어가게 됩니다. 학습 방식에 대한 내용은 [이 포스트](https://daehankim.blogspot.com/2022/08/lassl-feat-t5-ul2.html)를 참조해주시면 감사하겠습니다.
- License는 MIT입니다.
- 학습 로그는 [여기](https://wandb.ai/lucas01/huggingface?workspace=user-lucas01)에서 확인하실 수 있습니다.
- 모델이나 데이터 셋에 대해 궁금하신 점이 있으시면 `kdh5852 [at] gmail [dot] com`으로 문의해주시면 답변 드리겠습니다. 

## acknowledgement

- 이 프로젝트는 TFRC 프로그램의 TPU 지원을 받아 수행되었습니다.