---
language:
- ru
- en
pipeline_tag: text2text-generation
tags:
- PyTorch
- Transformers
- gpt2
- squad
- lm-head
- casual-lm
thumbnail: "https://github.com/RussianNLP/RusEnQA"

---

## RusEnQA

QA for Russian and English based on the [rugpt3xl](https://huggingface.co/sberbank-ai/rugpt3xl) model

### Fine-tuning format:

```
 "<s>paragraph: "+eng_context+"\nlang: rus\nquestion: "+rus_question+' answer: '+ rus_answer+"</s>"
```

### About ruGPT-3 XL model
Model was trained with 512 sequence length using [Deepspeed](https://github.com/microsoft/DeepSpeed) and [Megatron](https://github.com/NVIDIA/Megatron-LM) code by [SberDevices](https://sberdevices.ru/) team, on 80B tokens dataset for 4 epochs. After that model was finetuned 1 epoch with sequence length 2048.  
*Note! Model has sparse attention blocks.*

Total training time was around 10 days on 256 GPUs.
Final perplexity on test set is 12.05. Model parameters: 1.3B.