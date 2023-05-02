---
tags:
- question-generation
language: 
- thai
- th
datasets:
- NSC2018
- wiki-documents-nsc
- ThaiQACorpus-DevelopmentDataset
widget:
- text: "โรงเรียนบ้านขุนด่าน ตั้งอยู่ที่ขุนด่าน จ.นครนายก </s>"
  example_title: "Example 01"
- text: "พลเอก ประยุทธ์ จันทร์โอชา (เกิด 21 มีนาคม พ.ศ. 2497) ชื่อเล่น ตู่ เป็นนักการเมืองและอดีตนายทหารบกชาวไทย  </s>"
  example_title: "Example 02"
- text: "วันที่ 1 กันยายน 2550 12:00 น. ตำรวจภูธรจ.บุรีรัมย์บุกตรวจยึดไม้แปรรูปหวงห้ามกว่า 80 แผ่น  </s>"
  example_title: "Example 03"
- text: "กรุงเทพมหานคร  เป็นศูนย์กลางการปกครอง การศึกษา การคมนาคมขนส่ง การเงินการธนาคาร การพาณิชย์ การสื่อสาร และความเจริญของประเทศ ตั้งอยู่บนสามเหลี่ยมปากแม่น้ำเจ้าพระยา มีแม่น้ำเจ้าพระยาไหลผ่านและแบ่งเมืองออกเป็น 2 ฝั่ง คือ ฝั่งพระนครและฝั่งธนบุรี กรุงเทพมหานครมีพื้นที่ทั้งหมด 1,568.737 ตร.กม. </s>"
  example_title: "Example 04"

license: mit
---
[SuperAI Engineer Season 2](https://superai.aiat.or.th/) , [Machima](https://machchima.superai.me/)

[Google's mT5](https://github.com/google-research/multilingual-t5) , [Pollawat](https://huggingface.co/Pollawat/mt5-small-thai-qg)

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

model = T5ForConditionalGeneration.from_pretrained('SuperAI2-Machima/mt5-small-thai-qg-v2')
tokenizer = T5Tokenizer.from_pretrained('SuperAI2-Machima/mt5-small-thai-qg-v2')

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