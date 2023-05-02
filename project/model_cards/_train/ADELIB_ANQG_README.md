Hugging Face's logo
Hugging Face
Search models, datasets, users...
Models
Datasets
Spaces
Docs
Solutions
Pricing




Mihakram
/
Arabic_Question_Generation Copied
like
0
Text2Text Generation
PyTorch
Transformers
Arabic

arxiv:2109.12068
t5
AutoTrain Compatible
Model card
Files and versions
Community
Arabic_Question_Generation
/
README.md
Mihakram's picture
Mihakram
Update README.md
9920e0d
14 minutes ago
raw
history
blame
contribute
delete
Safe
3.41 kB
---
language: 
- ar
widget:
- text: "context: الثورة الجزائرية أو ثورة المليون شهيد، اندلعت في 1 نوفمبر 1954 ضد المستعمر الفرنسي ودامت 7 سنوات ونصف. استشهد فيها أكثر من مليون ونصف مليون جزائري answer:  7 سنوات ونصف </s>
"
- text: "context: اسكتلندا دولة في شمال غرب أوروبا، تعتبر جزء من الدول الأربع المكونة المملكة المتحدة. تحتل الثلث الشمالي من جزيرة بريطانيا العظمى وتحدها جنوبا إنجلترا ويحدها شرقا بحر الشمال وغربا المحيط الأطلسي. عاصمتها أدنبرة، وأهم مدنها وأكبرها مدينة غلاسكو. كانت اسكتلندا مملكة مستقلة حتى 1 مايو 1707  answer:  أدنبرة  </s>"

- text: "context: مات المستشار الألماني أدولف هتلر في 30 أبريل 1945 منتحرا عن طريق تناول مادة السيانيد السامة وإطلاق النار على نفسه وهي الرواية العامة المقبولة لطريقة موت الزعيم النازي answer: منتحرا </s>
"

---
# Arabic Question generation Model


This model is ready to use for **Question generation**, simply input the text and answer and the model will generate a question,  This model is a fine-tuned version of [AraT5-Base Model](https://huggingface.co/UBC-NLP/AraT5-base)
 

## Requirements
```
!pip install transformers
```


## Model in Action 🚀
```python
from transformers import AutoTokenizer,AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("Mihakram/Arabic_Question_Generation")
tokenizer = AutoTokenizer.from_pretrained("Mihakram/Arabic_Question_Generation")
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

## Expriments
We report score with `NQG Scorer`.

If not special explanation, the size of the model defaults to "base".

### Metrics resaults
 Bleu 1|Bleu 2|Bleu 3|Bleu 4|METEOR|ROUGE-L|
------|------|------|------|------|-------|
54.67 |39.26 |30.34 |24.15 |25.43 |52.64  |

## References

The **Ara-T5** model was presented in [AraT5: Text-to-Text Transformers for Arabic Language Generation](https://arxiv.org/abs/2109.12068) by *El Moatez Billah Nagoudi, AbdelRahim Elmadany, Muhammad Abdul-Mageed* 

## Citation
If you want to cite this model you can use this:

```bibtex
@misc{Mihakram/,
  title={},
  author={Mihoubi, Ibrir},
  publisher={Hugging Face},
  journal={Hugging Face Hub},
  howpublished={\url{https://huggingface.co/}},
  year={2022}
}
```