---
language: 
- en
tags:
- text-classification
- zero-shot-classification
metrics:
- accuracy
widget:
- text: "I liked the movie. [SEP] The movie was good."

---
# MiniLM-L6-mnli
## Model description
This model was trained on the [MultiNLI](https://huggingface.co/datasets/multi_nli) dataset. 
The base model is MiniLM-L6 from Microsoft, which is very fast, but a bit less accurate than other models.  

## Intended uses & limitations
#### How to use the model
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "MoritzLaurer/MiniLM-L6-mnli"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

premise = "I liked the movie"
hypothesis = "The movie was good."

input = tokenizer(premise, hypothesis, truncation=True, return_tensors="pt")
output = model(input["input_ids"].to(device))  # device = "cuda:0" or "cpu"
prediction = torch.softmax(output["logits"][0], -1).tolist()
label_names = ["entailment", "neutral", "contradiction"]
prediction = {name: round(float(pred) * 100, 1) for pred, name in zip(prediction, label_names)}
print(prediction)
```
### Training data
[MultiNLI](https://huggingface.co/datasets/multi_nli).

### Training procedure
MiniLM-L6-mnli-binary was trained using the Hugging Face trainer with the following hyperparameters.
```
training_args = TrainingArguments(
    num_train_epochs=5,              # total number of training epochs
    learning_rate=2e-05,
    per_device_train_batch_size=32,   # batch size per device during training
    per_device_eval_batch_size=32,    # batch size for evaluation
    warmup_ratio=0.1,                # number of warmup steps for learning rate scheduler
    weight_decay=0.06,               # strength of weight decay
    fp16=True                        # mixed precision training
)
```
### Eval results
The model was evaluated using the (matched) test set from MultiNLI. Accuracy: 0.814

## Limitations and bias
Please consult the original MiniLM paper and literature on different NLI datasets for potential biases. 

### BibTeX entry and citation info
If you want to cite this model, please cite the original MiniLM paper, the respective NLI datasets and include a link to this model on the Hugging Face hub. 