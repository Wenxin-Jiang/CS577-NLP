---
tags:
- question-generation
- question-answering
language: 
- thai
- th
datasets:
- NSC2018
- iapp-wiki-qa-dataset
- XQuAD 
license: mit
---

[Google's mT5](https://github.com/google-research/multilingual-t5)

This is a model for generating questions from Thai texts. It was fine-tuned on NSC2018 corpus

```python
from transformers import MT5Tokenizer, MT5ForConditionalGeneration
  
tokenizer = MT5Tokenizer.from_pretrained("Pollawat/mt5-small-thai-qa-qg")
model = MT5ForConditionalGeneration.from_pretrained("Pollawat/mt5-small-thai-qa-qg")

text = "กรุงเทพมหานคร เป็นเมืองหลวงและนครที่มีประชากรมากที่สุดของประเทศไทย เป็นศูนย์กลางการปกครอง การศึกษา การคมนาคมขนส่ง การเงินการธนาคาร การพาณิชย์ การสื่อสาร และความเจริญของประเทศ เป็นเมืองที่มีชื่อยาวที่สุดในโลก ตั้งอยู่บนสามเหลี่ยมปากแม่น้ำเจ้าพระยา มีแม่น้ำเจ้าพระยาไหลผ่านและแบ่งเมืองออกเป็น 2 ฝั่ง คือ ฝั่งพระนครและฝั่งธนบุรี กรุงเทพมหานครมีพื้นที่ทั้งหมด 1,568.737 ตร.กม. มีประชากรตามทะเบียนราษฎรกว่า 5 ล้านคน"

input_ids = tokenizer.encode(text, return_tensors='pt')

beam_output = model.generate(
    input_ids, 
    max_length=50,
    num_beams=5,
    early_stopping=True
)

print(tokenizer.decode(beam_output[0]))
>> <pad> <extra_id_0> แม่น้ําเจ้าพระยาไหลผ่านและแบ่งเมืองออกเป็น 2 ฝั่ง คือ ฝั่งใด <ANS> ฝั่งพระนครและฝั่งธนบุรี</s>

print(tokenizer.decode(beam_output[0], skip_special_tokens=True))
>> <extra_id_0> แม่น้ําเจ้าพระยาไหลผ่านและแบ่งเมืองออกเป็น 2 ฝั่ง คือ ฝั่งใด ฝั่งพระนครและฝั่งธนบุรี
```