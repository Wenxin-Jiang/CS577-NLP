---
language: 
- en
license: mit
tags:
- text-classification
- zero-shot-classification
metrics:
- accuracy
datasets:
- multi_nli
- anli
- fever
- lingnli
pipeline_tag: zero-shot-classification

---
# DeBERTa-v3-xsmall-mnli-fever-anli-ling-binary
## Model description
This model was trained on 782 357 hypothesis-premise pairs from 4 NLI datasets: [MultiNLI](https://huggingface.co/datasets/multi_nli), [Fever-NLI](https://github.com/easonnie/combine-FEVER-NSMN/blob/master/other_resources/nli_fever.md), [LingNLI](https://arxiv.org/abs/2104.07179) and [ANLI](https://github.com/facebookresearch/anli). 

Note that the model was trained on binary NLI to predict either "entailment" or "not-entailment". This is specifically designed for zero-shot classification, where the difference between "neutral" and "contradiction" is irrelevant. 

The base model is [DeBERTa-v3-xsmall from Microsoft](https://huggingface.co/microsoft/deberta-v3-xsmall). The v3 variant of DeBERTa substantially outperforms previous versions of the model by including a different pre-training objective, see the [DeBERTa-V3 paper](https://arxiv.org/abs/2111.09543). 

For highest performance (but less speed), I recommend using https://huggingface.co/MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli.

## Intended uses & limitations
#### How to use the model
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

model_name = "MoritzLaurer/DeBERTa-v3-xsmall-mnli-fever-anli-ling-binary"
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
This model was trained on 782 357 hypothesis-premise pairs from 4 NLI datasets: [MultiNLI](https://huggingface.co/datasets/multi_nli), [Fever-NLI](https://github.com/easonnie/combine-FEVER-NSMN/blob/master/other_resources/nli_fever.md), [LingNLI](https://arxiv.org/abs/2104.07179) and [ANLI](https://github.com/facebookresearch/anli). 

### Training procedure
DeBERTa-v3-xsmall-mnli-fever-anli-ling-binary was trained using the Hugging Face trainer with the following hyperparameters.
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
The model was evaluated using the binary test sets for MultiNLI, ANLI, LingNLI and the binary dev set for Fever-NLI (two classes instead of three). The metric used is accuracy.

dataset | mnli-m-2c | mnli-mm-2c | fever-nli-2c | anli-all-2c | anli-r3-2c | lingnli-2c
--------|---------|----------|---------|----------|----------|------
accuracy | 0.925 | 0.922 | 0.892 | 0.676 | 0.665 | 0.888
speed (text/sec, CPU, 128 batch) | 6.0 | 6.3 | 3.0 | 5.8 | 5.0 | 7.6
speed (text/sec, GPU Tesla P100, 128 batch) | 473 | 487 | 230 | 390 | 340 | 586


## Limitations and bias
Please consult the original DeBERTa paper and literature on different NLI datasets for potential biases. 

## Citation
If you use this model, please cite: Laurer, Moritz, Wouter van Atteveldt, Andreu Salleras Casas, and Kasper Welbers. 2022. ‘Less Annotating, More Classifying – Addressing the Data Scarcity Issue of Supervised Machine Learning with Deep Transfer Learning and BERT - NLI’. Preprint, June. Open Science Framework. https://osf.io/74b8k.

### Ideas for cooperation or questions?
If you have questions or ideas for cooperation, contact me at m{dot}laurer{at}vu{dot}nl or [LinkedIn](https://www.linkedin.com/in/moritz-laurer/)

### Debugging and issues
Note that DeBERTa-v3 was released on 06.12.21 and older versions of HF Transformers seem to have issues running the model (e.g. resulting in an issue with the tokenizer). Using Transformers>=4.13 might solve some issues. 