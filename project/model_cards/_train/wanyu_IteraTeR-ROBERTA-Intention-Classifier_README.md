---
datasets:
- IteraTeR_full_sent
---

# IteraTeR RoBERTa model
This model was obtained by fine-tuning [roberta-large](https://huggingface.co/roberta-large) on [IteraTeR-human-sent](https://huggingface.co/datasets/wanyu/IteraTeR_human_sent) dataset.

Paper: [Understanding Iterative Revision from Human-Written Text](https://arxiv.org/abs/2203.03802) <br>
Authors: Wanyu Du, Vipul Raheja, Dhruv Kumar, Zae Myung Kim, Melissa Lopez, Dongyeop Kang

## Edit Intention Prediction Task
Given a pair of original sentence and revised sentence, our model can predict the edit intention for this revision pair.<br>
More specifically, the model will predict the probability of the following edit intentions:
<table>
  <tr>
    <th>Edit Intention</th>
    <th>Definition</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>clarity</td>
    <td>Make the text more formal, concise, readable and understandable.</td>
    <td>
    Original: It's like a house which anyone can enter in it. <br>
    Revised: It's like a house which anyone can enter.
    </td>
  </tr>
  <tr>
    <td>fluency</td>
    <td>Fix grammatical errors in the text.</td>
    <td>
    Original: In the same year he became the Fellow of the Royal Society. <br>
    Revised: In the same year, he became the Fellow of the Royal Society.
    </td>
  </tr>
  <tr>
    <td>coherence</td>
    <td>Make the text more cohesive, logically linked and consistent as a whole.</td>
    <td>
    Original: Achievements and awards Among his other activities, he founded the Karachi Film Guild and Pakistan Film and TV Academy. <br>
    Revised: Among his other activities, he founded the Karachi Film Guild and Pakistan Film and TV Academy.
    </td>
  </tr>
  <tr>
    <td>style</td>
    <td>Convey the writer’s writing preferences, including emotions, tone, voice, etc..</td>
    <td>
    Original: She was last seen on 2005-10-22. <br>
    Revised: She was last seen on October 22, 2005.
    </td>
  </tr>
  <tr>
    <td>meaning-changed</td>
    <td>Update or add new information to the text.</td>
    <td>
    Original: This method improves the model accuracy from 64% to 78%. <br>
    Revised: This method improves the model accuracy from 64% to 83%.
    </td>
  </tr>
</table>



## Usage
```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("wanyu/IteraTeR-ROBERTA-Intention-Classifier")
model = AutoModelForSequenceClassification.from_pretrained("wanyu/IteraTeR-ROBERTA-Intention-Classifier")

id2label = {0: "clarity", 1: "fluency", 2: "coherence", 3: "style", 4: "meaning-changed"}

before_text = 'I likes coffee.'
after_text = 'I like coffee.'
model_input = tokenizer(before_text, after_text, return_tensors='pt')
model_output = model(**model_input)
softmax_scores = torch.softmax(model_output.logits, dim=-1)
pred_id = torch.argmax(softmax_scores)
pred_label = id2label[pred_id.int()]
```