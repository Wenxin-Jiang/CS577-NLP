
#### Klue-bert base for Common Sense QA

#### Klue-CommonSense-model DEMO: [Ainize DEMO](https://main-klue-common-sense-qa-east-h-shin.endpoint.ainize.ai/)

#### Klue-CommonSense-model API: [Ainize API](https://ainize.ai/EastHShin/Klue-CommonSense_QA?branch=main)

### Overview

**Language model**: klue/bert-base
<br>
**Language**: Korean
<br>
**Downstream-task**: Extractive QA
<br>
**Training data**: Common sense Data from [Mindslab](https://mindslab.ai:8080/kr/company)
<br>
**Eval data**: Common sense Data from [Mindslab](https://mindslab.ai:8080/kr/company)
<br>
**Code**: See [Ainize Workspace](https://ainize.ai/workspace/create?imageId=hnj95592adzr02xPTqss&git=https://github.com/EastHShin/Klue-CommonSense-workspace)
<br>

### Usage

### In Transformers
```
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("EasthShin/Klue-CommonSense-model")
model = AutoModelForQuestionAnswering.from_pretrained("EasthShin/Klue-CommonSense-model")

context = "your context"
question = "your question"

encodings = tokenizer(context, question, max_length=512, truncation=True,
                      padding="max_length", return_token_type_ids=False)
encodings = {key: torch.tensor([val]) for key, val in encodings.items()}             

input_ids = encodings["input_ids"]
attention_mask = encodings["attention_mask"]

pred = model(input_ids, attention_mask=attention_mask)

start_logits, end_logits = pred.start_logits, pred.end_logits

token_start_index, token_end_index = start_logits.argmax(dim=-1), end_logits.argmax(dim=-1)

pred_ids = input_ids[0][token_start_index: token_end_index + 1]

prediction = tokenizer.decode(pred_ids)
```