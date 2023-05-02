---
language: en
datasets:
- squad
tags:
- Question Generation
widget:
 - text: "<answer> T5v1.1 <context> Cheng fine-tuned T5v1.1 on SQuAD for question generation."
   example_title: "Example 1"
 - text: "<answer> SQuAD <context> Cheng fine-tuned T5v1.1 on SQuAD dataset for question generation."
   example_title: "Example 2"
 - text: "<answer> thousands <context> Transformers provides thousands of pre-trained models to perform tasks on different modalities such as text, vision, and audio."
   example_title: "Example 3"
---

# T5v1.1-Base Fine-Tuned on SQuAD for Question Generation

### Model in Action:

```python
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

trained_model_path = 'ZhangCheng/T5v1.1-Base-Fine-Tuned-for-Question-Generation'
trained_tokenizer_path = 'ZhangCheng/T5v1.1-Base-Fine-Tuned-for-Question-Generation'

class QuestionGeneration:

    def __init__(self):
        self.model = T5ForConditionalGeneration.from_pretrained(trained_model_path)
        self.tokenizer = T5Tokenizer.from_pretrained(trained_tokenizer_path)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = self.model.to(self.device)
        self.model.eval()

    def generate(self, answer:str, context:str):
        input_text = '<answer> %s <context> %s ' % (answer, context)
        encoding = self.tokenizer.encode_plus(
            input_text,
            return_tensors='pt'
        )
        input_ids = encoding['input_ids'].to(self.device)
        attention_mask = encoding['attention_mask'].to(self.device)
        outputs = self.model.generate(
            input_ids = input_ids,
            attention_mask = attention_mask
        )
        question = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens = True,
            clean_up_tokenization_spaces = True
        )
        return {'question': question, 'answer': answer}

if __name__ == "__main__":
    context = 'ZhangCheng fine-tuned T5v1.1 on SQuAD dataset for question generation.'
    answer = 'ZhangCheng'
    QG = QuestionGeneration()
    qa = QG.generate(answer, context)
    print(qa['question'])
    # Output: 
    # Who fine-tuned T5v1.1 on SQuAD?
```
