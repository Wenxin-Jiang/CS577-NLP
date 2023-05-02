---
language: 
- multilingual
- ta
tags:
- question-answering
datasets:
- squad v2
- chaii
- mlqa
- xquad
metrics:
- Exact Match
- F1

widget:
- text: "சென்னையில் எத்தனை மக்கள் வாழ்கின்றனர்?"
  context: "சென்னை (Chennai) தமிழ்நாட்டின் தலைநகரமும் இந்தியாவின் நான்காவது பெரிய நகரமும் ஆகும். 1996 ஆம் ஆண்டுக்கு முன்னர் இந்நகரம் மெட்ராஸ் (Madras) என்று அழைக்கப்பட்டு வந்தது. சென்னை, வங்காள விரிகுடாவின் கரையில் அமைந்த துறைமுக நகரங்களுள் ஒன்று. சுமார் 10 மில்லியன் (ஒரு கோடி) மக்கள் வாழும் இந்நகரம், உலகின் 35 பெரிய மாநகரங்களுள் ஒன்று. 17ஆம் நூற்றாண்டில் ஆங்கிலேயர் சென்னையில் கால் பதித்தது முதல், சென்னை நகரம் ஒரு முக்கிய நகரமாக வளர்ந்து வந்திருக்கிறது. சென்னை தென்னிந்தியாவின் வாசலாகக் கருதப்படுகிறது. சென்னை நகரில் உள்ள மெரினா கடற்கரை உலகின் நீளமான கடற்கரைகளுள் ஒன்று. சென்னை கோலிவுட் (Kollywood) என அறியப்படும் தமிழ்த் திரைப்படத் துறையின் தாயகம். பல விளையாட்டு அரங்கங்கள் உள்ள சென்னையில் பல விளையாட்டுப் போட்டிகளும் நடைபெறுகின்றன."
  example_title: "Question Answering"
---

# XLM-RoBERTa Large trained on Dravidian Language QA

## Overview
**Language model:** XLM-RoBERTa-lg
**Language:** Multilingual, focussed on Tamil & Hindi 
**Downstream-task:** Extractive QA
**Eval data:** K-Fold on Training Data

## Hyperparameters
```
batch_size = 4
base_LM_model = "xlm-roberta-large"
learning_rate = 1e-5

optimizer = AdamW
weight_decay = 1e-2
epsilon = 1e-8
max_grad_norm = 1.0

lr_schedule = LinearWarmup
warmup_proportion = 0.2

max_seq_len = 256
doc_stride=128
max_query_length=64
``` 

## Performance
Evaluated on our human annotated dataset with 1000 tamil question-context pairs [link]
```
  "em": 77.536,
  "f1": 85.665
```

## Usage
### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
model_name = "Srini99/FYP_TamilQA"

model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'யாரால் பொங்கல் சிறப்பாகக் கொண்டாடப்படுகிறது?',
    'context': 'பொங்கல் என்பது தமிழர்களால் சிறப்பாகக் கொண்டாடப்படும் ஓர் அறுவடைப் பண்டிகை ஆகும்.'
}
res = nlp(QA_input)
```