---
language: "english"
license: "mit"
datasets:
- race
metrics:
- accuracy
---

# Roberta Large Fine Tuned on RACE

## Model description

This model is a fine-tuned model of Roberta-large applied on RACE

#### How to use

```python

import datasets
from transformers import RobertaTokenizer
from transformers import  RobertaForMultipleChoice

tokenizer = RobertaTokenizer.from_pretrained(
"LIAMF-USP/roberta-large-finetuned-race")
model = RobertaForMultipleChoice.from_pretrained(
"LIAMF-USP/roberta-large-finetuned-race")
dataset = datasets.load_dataset(
    "race",
    "all",
    split=["train", "validation", "test"],
)training_examples = dataset[0]
evaluation_examples = dataset[1]
test_examples = dataset[2]

example=training_examples[0] 
example_id = example["example_id"]
question = example["question"]
context = example["article"]
options = example["options"]
label_example = example["answer"]
label_map = {label: i 
    for i, label in enumerate(["A", "B", "C", "D"])}
choices_inputs = []
for ending_idx, (_, ending) in enumerate(
                                zip(context, options)):
    if question.find("_") != -1:
        # fill in the banks questions
        question_option = question.replace("_", ending)
    else:
        question_option = question + " " + ending
    inputs = tokenizer(
        context,
        question_option,
        add_special_tokens=True,
        max_length=MAX_SEQ_LENGTH,
        padding="max_length",
        truncation=True,
        return_overflowing_tokens=False,
    )    
label = label_map[label_example]
input_ids = [x["input_ids"] for x in choices_inputs]
attention_mask = (
    [x["attention_mask"] for x in choices_inputs]
     # as the senteces follow the same structure, 
     #just one of them is necessary to check
    if "attention_mask" in choices_inputs[0]
    else None
)
example_encoded = {
    "example_id": example_id,
    "input_ids": input_ids,
    "attention_mask": attention_mask,
    "label": label,
}
output = model(**example_encoded)
```


## Training data

The initial model was [roberta large model](https://huggingface.co/roberta-large) which was then fine-tuned on [RACE dataset](https://www.cs.cmu.edu/~glai1/data/race/)

## Training procedure

It was necessary to preprocess the data with a method that is exemplified for a single instance in the _How to use_ section. The used hyperparameters were the following:

| Hyperparameter | Value |
|:----:|:----:|
| adam_beta1                  | 0.9      |
| adam_beta2                  | 0.98     |
| adam_epsilon                | 1.000e-8 |
| eval_batch_size             | 32       |
| train_batch_size            | 1        |
| fp16                        | True     |
| gradient_accumulation_steps | 16       |
| learning_rate               | 0.00001  |
| warmup_steps                | 1000     |
| max_length                  | 512      |
| epochs                      | 4        |

## Eval results:
| Dataset Acc | Eval | All Test |High School Test |Middle School Test |
|:----:|:----:|:----:|:----:|:----:|
|      | 85.2 | 84.9|83.5|88.0|

**The model was trained with a Tesla V100-PCIE-16GB** 