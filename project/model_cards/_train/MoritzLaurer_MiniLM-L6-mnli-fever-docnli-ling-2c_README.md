---
language: 
- en
tags:
- text-classification
- zero-shot-classification
metrics:
- accuracy
widget:
- text: "I first thought that I liked the movie, but upon second thought the movie was actually disappointing. [SEP] The movie was good."

---
# MiniLM-L6-mnli-fever-docnli-ling-2c
## Model description
This model was trained on 1.279.665 hypothesis-premise pairs from 8 NLI datasets: [MultiNLI](https://huggingface.co/datasets/multi_nli), [Fever-NLI](https://github.com/easonnie/combine-FEVER-NSMN/blob/master/other_resources/nli_fever.md), [LingNLI](https://arxiv.org/abs/2104.07179) and [DocNLI](https://arxiv.org/pdf/2106.09449.pdf) (which includes [ANLI](https://github.com/facebookresearch/anli), QNLI, DUC, CNN/DailyMail, Curation). 

It is the only model in the model hub trained on 8 NLI datasets, including DocNLI with very long texts to learn long range reasoning. Note that the model was trained on binary NLI to predict either "entailment" or "not-entailment". The DocNLI merges the classes "neural" and "contradiction" into "not-entailment" to create more training data. 

The base model is MiniLM-L6 from Microsoft. Which is very fast, but a bit less accurate than other models.  

## Intended uses & limitations
#### How to use the model
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "MoritzLaurer/MiniLM-L6-mnli-fever-docnli-ling-2c"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

premise = "I first thought that I liked the movie, but upon second thought it was actually disappointing."
hypothesis = "The movie was good."

input = tokenizer(premise, hypothesis, truncation=True, return_tensors="pt")
output = model(input["input_ids"].to(device))  # device = "cuda:0" or "cpu"
prediction = torch.softmax(output["logits"][0], -1).tolist()
label_names = ["entailment", "not_entailment"]
prediction = {name: round(float(pred) * 100, 1) for pred, name in zip(prediction, label_names)}
print(prediction)
```
### Training data
This model was trained on 1.279.665 hypothesis-premise pairs from 8 NLI datasets: [MultiNLI](https://huggingface.co/datasets/multi_nli), [Fever-NLI](https://github.com/easonnie/combine-FEVER-NSMN/blob/master/other_resources/nli_fever.md), [LingNLI](https://arxiv.org/abs/2104.07179) and [DocNLI](https://arxiv.org/pdf/2106.09449.pdf) (which includes [ANLI](https://github.com/facebookresearch/anli), QNLI, DUC, CNN/DailyMail, Curation).

### Training procedure
MiniLM-L6-mnli-fever-docnli-ling-2c was trained using the Hugging Face trainer with the following hyperparameters.
```
training_args = TrainingArguments(
    num_train_epochs=3,              # total number of training epochs
    learning_rate=2e-05,
    per_device_train_batch_size=32,   # batch size per device during training
    per_device_eval_batch_size=32,    # batch size for evaluation
    warmup_ratio=0.1,                # number of warmup steps for learning rate scheduler
    weight_decay=0.06,               # strength of weight decay
    fp16=True                        # mixed precision training
)
```
### Eval results
The model was evaluated using the binary test sets for MultiNLI and ANLI and the binary dev set for Fever-NLI (two classes instead of three). The metric used is accuracy.

mnli-m-2c | mnli-mm-2c | fever-nli-2c | anli-all-2c | anli-r3-2c
---------|----------|---------|----------|----------
(to upload)


## Limitations and bias
Please consult the original MiniLM paper and literature on different NLI datasets for potential biases. 

### BibTeX entry and citation info
If you want to cite this model, please cite the original MiniLM paper, the respective NLI datasets and include a link to this model on the Hugging Face hub. 

### Ideas for cooperation or questions?
If you have questions or ideas for cooperation, contact me at m.laurer{at}vu.nl or [LinkedIn](https://www.linkedin.com/in/moritz-laurer/)