### Description:
BART Model has been finetuned on CNN/DailyMail Dataset with Sample Size 10000.

### How To Use:

```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


src_text = [" PG&E stated it scheduled the blackouts in response to forecasts for high winds amid dry conditions. The aim is to reduce the risk of wildfires. Nearly 800 thousand customers were scheduled to be affected by the shutoffs which were expected to last through at least midday tomorrow.", "In the end, it played out like a movie. A tense, heartbreaking story, and then a surprise twist at the end. As eight of Mary Jane Veloso's fellow death row inmates -- mostly foreigners, like her -- were put to death by firing squad early Wednesday in a wooded grove on the Indonesian island of Nusa Kambangan, the Filipina maid and mother of two was spared, at least for now. Her family was returning from what they thought was their final visit to the prison on so-called \"execution island\" when a Philippine TV crew flagged their bus down to tell them of the decision to postpone her execution. Her ecstatic mother, Celia Veloso, told CNN: \"We are so happy, so happy. I thought I had lost my daughter already but God is so good. Thank you to everyone who helped us."]

torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'

tokenizer = AutoTokenizer.from_pretrained("Mousumi/finetuned_bart")

model = AutoModelForSeq2SeqLM.from_pretrained("Mousumi/finetuned_bart").to(torch_device)

no_samples = len(src_text)
result = []

for i in range(no_samples):
    with tokenizer.as_target_tokenizer():
        tokenized_text = tokenizer([src_text[i]], return_tensors='pt', padding=True, truncation=True)
    batch = tokenized_text.to(torch_device)
    translated = model.generate(**batch)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    result.append(tgt_text[0])

print(result)

```