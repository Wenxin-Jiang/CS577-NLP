---
tags:
- Yes No question-generation
language: 
- thai
- th
datasets:
- NSC2018
- wiki-documents-nsc
- ThaiQACorpus-DevelopmentDataset
widget:
- text: "วันที่ 1 กันยายน 2550 12:00 น. ตำรวจภูธรจ.บุรีรัมย์บุกตรวจยึดไม้แปรรูปหวงห้ามกว่า 80 แผ่น"
  example_title: "Example 01"
- text: "พลเอก ประยุทธ์ จันทร์โอชา (เกิด 21 มีนาคม พ.ศ. 2497) ชื่อเล่น ตู่ เป็นนักการเมืองและอดีตนายทหารบกชาวไทย"
  example_title: "Example 02"

license: mit
---
[SuperAI Engineer Season 2](https://superai.aiat.or.th/) , [Machima](https://machchima.superai.me/)

[Google's mT5](https://github.com/google-research/multilingual-t5) , [Pollawat](https://huggingface.co/Pollawat/mt5-small-thai-qg)

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

model = T5ForConditionalGeneration.from_pretrained('SuperAI2-Machima/mt5-small-thai-yes-no-qg')
tokenizer = T5Tokenizer.from_pretrained('SuperAI2-Machima/mt5-small-thai-yes-no-qg')

source_text = 'บุกยึดไม้เถื่อน อดีต ส.ส.บุรีรัมย์ เตรียมสร้างคฤหาสน์ทรงไทย 1 กันยายน 2550 12:00 น. ตำรวจภูธรจ.บุรีรัมย์บุกตรวจยึดไม้แปรรูปหวงห้ามกว่า 80 แผ่น'

print('Predicted Summary Text : ')
tokenized_text = tokenizer.encode(source_text, return_tensors="pt").to(device)
summary_ids = model.generate(tokenized_text,
                                        num_beams=4,
                                        no_repeat_ngram_size=2,
                                        max_length=50,
                                        early_stopping=True)
output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(output)
#Predicted Summary Text : 
#answer: 80 แผ่น question: ตํารวจภูธรจ.บุรีรัมย์บุกตรวจยึดไม้แปรรูปหวงห้ามกว่ากี่แผ่น
```