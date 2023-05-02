---
language:
- rus
tags:
- mbart
inference:
  parameters:
    no_repeat_ngram_size: 4,
    num_beams : 5
datasets:
- IlyaGusev/gazeta
- samsum
- samsum_(translated_into_Russian)
widget:
- text: | 
    Джефф: Могу ли я обучить модель 🤗 Transformers на Amazon SageMaker? 
    Филипп: Конечно, вы можете использовать новый контейнер для глубокого обучения HuggingFace. 
    Джефф: Хорошо.
    Джефф: и как я могу начать? 
    Джефф: где я могу найти документацию? 
    Филипп: ок, ок, здесь можно найти все: https://huggingface.co/blog/the-partnership-amazon-sagemaker-and-hugging-face

model-index:
- name: "mbart_ruDialogSum"
  results:
  - task: 
      name: Abstractive Dialogue Summarization
      type: abstractive-text-summarization 
    dataset:
      name: "SAMSum Corpus (translated to Russian)" 
      type: samsum
    metrics:
       - name: Validation ROGUE-1
         type: rogue-1
         value: 34.5
       - name: Validation ROGUE-L
         type: rogue-l
         value: 33
       - name: Test ROGUE-1
         type: rogue-1
         value: 31
       - name: Test ROGUE-L
         type: rogue-l
         value: 28
---
### 📝 Description

MBart for Russian summarization fine-tuned for **dialogues** summarization.


This model was firstly fine-tuned by [Ilya Gusev](https://hf.co/IlyaGusev) on [Gazeta dataset](https://huggingface.co/datasets/IlyaGusev/gazeta). We have **fine tuned** that model on [SamSum dataset]() **translated to Russian** using GoogleTranslateAPI

🤗 Moreover! We have implemented a **! telegram bot [@summarization_bot](https://t.me/summarization_bot) !** with the inference of this model. Add it to the chat and get summaries instead of dozens spam messages!  🤗


### ❓ How to use with code
```python
from transformers import MBartTokenizer, MBartForConditionalGeneration

# Download model and tokenizer
model_name = "Kirili4ik/mbart_ruDialogSum"   
tokenizer =  AutoTokenizer.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)
model.eval()

article_text = "..."

input_ids = tokenizer(
    [article_text],
    max_length=600,
    padding="max_length",
    truncation=True,
    return_tensors="pt",
)["input_ids"]

output_ids = model.generate(
    input_ids=input_ids,
    top_k=0,
    num_beams=3,
    no_repeat_ngram_size=3
)[0]


summary = tokenizer.decode(output_ids, skip_special_tokens=True)
print(summary)
```
