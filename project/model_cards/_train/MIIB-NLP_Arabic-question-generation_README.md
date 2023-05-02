---
language: 
- ar
tags:
- answer-aware-question-generation 
- question-generation
- QG
widget:
- text: "context: الثورة الجزائرية أو ثورة المليون شهيد، اندلعت في 1 نوفمبر 1954 ضد المستعمر الفرنسي ودامت 7 سنوات ونصف. استشهد فيها أكثر من مليون ونصف مليون جزائري answer:  7 سنوات ونصف </s>
"
- text: "context: اسكتلندا دولة في شمال غرب أوروبا، تعتبر جزء من الدول الأربع المكونة المملكة المتحدة. تحتل الثلث الشمالي من جزيرة بريطانيا العظمى وتحدها جنوبا إنجلترا ويحدها شرقا بحر الشمال وغربا المحيط الأطلسي. عاصمتها أدنبرة، وأهم مدنها وأكبرها مدينة غلاسكو. كانت اسكتلندا مملكة مستقلة حتى 1 مايو 1707  answer:  أدنبرة  </s>"

- text: "context: تم تفكيك الإمبراطورية النمساوية المجرية في عام 1918 بعد نهاية الحرب العالمية الأولى. وكان اباطرتها: الإمبراطور فرانس جوزيف الأول هابسبورغ لورين (في الفترة من 1867 إلى 1916) والإمبراطورة إليزابيث (من 1867 إلى 1898)، تبعها الإمبراطور تشارلز الأول إمبراطور النمسا (من 1916 إلى 1918). answer: 1918 </s>
"
metrics:
- bleu
model-index:
- name: Arabic-Question-Generation
  results:
  - task:
      name: Question-Generation
      type: automatic-question-generation
    metrics:
    - name: Bleu1
      type: bleu
      value: 37.62
    - name: Bleu2
      type: bleu
      value: 27.80
    - name: Bleu3
      type: bleu
      value: 20.89
    - name: Bleu4
      type: bleu
      value: 15.87
    - name: meteor
      type: meteor
      value: 33.19
    - name: rougel
      type: rouge
      value: 43.37
      

---
# Arabic Question Generation Model

This model is ready to use for **Question Generation** task, simply input the text and answer, the model will generate a question, This model is a fine-tuned version of [AraT5-Base](https://huggingface.co/UBC-NLP/AraT5-base) Model 

## Live Demo 
Get the Question from given Context and a Answer : [Arabic QG Model](https://huggingface.co/spaces/MIIB-NLP/Arabic-Question-Generation)

## Model in Action 🚀
```python
#Requirements: !pip install transformers
from transformers import AutoTokenizer,AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained("MIIB-NLP/Arabic-question-generation")
tokenizer = AutoTokenizer.from_pretrained("MIIB-NLP/Arabic-question-generation")

def get_question(context,answer):
  text="context: " +context + " " + "answer: " + answer + " </s>"
  text_encoding = tokenizer.encode_plus(
      text,return_tensors="pt"
  )
  model.eval()
  generated_ids =  model.generate(
    input_ids=text_encoding['input_ids'],
    attention_mask=text_encoding['attention_mask'],
    max_length=64,
    num_beams=5,
    num_return_sequences=1
  )
  return tokenizer.decode(generated_ids[0],skip_special_tokens=True,clean_up_tokenization_spaces=True).replace('question: ',' ')

context="الثورة الجزائرية أو ثورة المليون شهيد، اندلعت في 1 نوفمبر 1954 ضد المستعمر الفرنسي ودامت 7 سنوات ونصف. استشهد فيها أكثر من مليون ونصف مليون جزائري"
answer =" 7 سنوات ونصف"

get_question(context,answer)

#output : question="كم استمرت الثورة الجزائرية؟ " 

```

## Details of Ara-T5

The **Ara-T5** model was presented in [AraT5: Text-to-Text Transformers for Arabic Language Generation](https://arxiv.org/abs/2109.12068) by *El Moatez Billah Nagoudi, AbdelRahim Elmadany, Muhammad Abdul-Mageed* 


## Contacts

**Mihoubi Akram Fawzi**: [Linkedin](https://www.linkedin.com/in/mihoubi-akram/) | [Github](https://github.com/mihoubi-akram) | <mihhakram@gmail.com>

**Ibrir Adel**: [Linkedin](https://www.linkedin.com/in/adel-ibrir/) | [Github]() | <adelibrir2015@gmail.com>

