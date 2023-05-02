---
thumbnail: https://huggingface.co/front/thumbnails/dialogpt.png
tags:
- conversational
license: mit
---

### Large-Scale Pre-Training for Goal-Directed Dialog (GODEL)

GODEL is a large-scale pre-trained model for goal-directed dialogs. It is parameterized with a Transformer-based encoder-decoder model and trained for response generation grounded in external text, which allows more effective fine-tuning on dialog tasks that require conditioning the response on information that is external to the current conversation (e.g., a retrieved document). The pre-trained model can be efficiently fine-tuned and adapted to accomplish a new dialog task with a handful of task-specific dialogs. The v1.1 model is trained on 551M multi-turn dialogs from Reddit discussion thread, and 5M instruction and knowledge grounded dialogs.

##### Multi-turn generation examples from an interactive environment:
Chitchat example:
> Instruction: given a dialog context, you need to response empathically.  <br>
> User: Does money buy happiness? <br>
> Agent: It is a question. Money buys you a lot of things, but not enough to buy happiness. <br>
> User: What is the best way to buy happiness ? <br>
> Agent: Happiness is bought through your experience and not money. <br>

Grounded response generation example:
> Instruction: given a dialog context and related knowledge, you need to response safely based on the knowledge. <br>
> Knowledge: The best Stardew Valley mods PCGamesN_0 / About SMAPI <br>
> User: My favorite game is stardew valley. stardew valley is very fun. <br>
> Agent: I love Stardew Valley mods, like PCGamesN_0 / About SMAPI. <br>

Please find the information about preprocessing, training and full details of the GODEL in the [project webpage](https://aka.ms/GODEL).

ArXiv paper: [https://arxiv.org/abs/2206.11309](https://arxiv.org/abs/2206.11309)

### How to use

Now we are ready to try out how the model works as a chatting partner!

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")
model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")
def generate(instruction, knowledge, dialog):
    if knowledge != '':
        knowledge = '[KNOWLEDGE] ' + knowledge
    dialog = ' EOS '.join(dialog)
    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=128, min_length=8, top_p=0.9, do_sample=True)
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output
# Instruction for a chitchat task
instruction = f'Instruction: given a dialog context, you need to response empathically.'
# Leave the knowldge empty
knowledge = ''
dialog = [
    'Does money buy happiness?',
    'It is a question. Money buys you a lot of things, but not enough to buy happiness.',
    'What is the best way to buy happiness ?'
]
response = generate(instruction, knowledge, dialog)
print(response)
```

### Citation
if you use this code and data in your research, please cite our arxiv paper:
```
@misc{peng2022godel,
author = {Peng, Baolin and Galley, Michel and He, Pengcheng and Brockett, Chris and Liden, Lars and Nouri, Elnaz and Yu, Zhou and Dolan, Bill and Gao, Jianfeng},
title = {GODEL: Large-Scale Pre-training for Goal-Directed Dialog},
howpublished = {arXiv},
year = {2022},
month = {June},
url = {https://www.microsoft.com/en-us/research/publication/godel-large-scale-pre-training-for-goal-directed-dialog/},
}
```