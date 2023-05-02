---
language: "english"
license: "mit"
datasets:
- race
- ai2_arc
- openbookqa
metrics:
- accuracy
---

# Roberta Large Fine Tuned on RACE

## Model description

This model follows the implementation by Allen AI team about [Aristo Roberta V7 Model](https://leaderboard.allenai.org/arc/submission/blcotvl7rrltlue6bsv0) given in [ARC Challenge](https://leaderboard.allenai.org/arc/submissions/public)

#### How to use

```python

import datasets
from transformers import RobertaTokenizer
from transformers import  RobertaForMultipleChoice

tokenizer = RobertaTokenizer.from_pretrained(
"LIAMF-USP/aristo-roberta")
model = RobertaForMultipleChoice.from_pretrained(
"LIAMF-USP/aristo-roberta")
dataset = datasets.load_dataset(
    "arc",,
    split=["train", "validation", "test"],
)
training_examples = dataset[0]
evaluation_examples = dataset[1]
test_examples = dataset[2]

example=training_examples[0] 
example_id = example["example_id"]
question = example["question"]
label_example = example["answer"]
options = example["options"]
if label_example in ["A", "B", "C", "D", "E"]:
    label_map = {label: i for i, label in enumerate(
					["A", "B", "C", "D", "E"])}
elif label_example in ["1", "2", "3", "4", "5"]:
    label_map = {label: i for i, label in enumerate(
					["1", "2", "3", "4", "5"])}
else:
    print(f"{label_example} not found")
while len(options) < 5:
    empty_option = {}
    empty_option['option_context'] = ''
    empty_option['option_text'] = ''
    options.append(empty_option)
choices_inputs = []
for ending_idx, option in enumerate(options):
    ending = option["option_text"]
    context = option["option_context"]
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
    
    if "num_truncated_tokens" in inputs and inputs["num_truncated_tokens"] > 0:
        logging.warning(f"Question: {example_id} with option {ending_idx} was truncated")
    choices_inputs.append(inputs)
label = label_map[label_example]
input_ids = [x["input_ids"] for x in choices_inputs]
attention_mask = (
    [x["attention_mask"] for x in choices_inputs]
     # as the senteces follow the same structure, just one of them is
     # necessary to check
    if "attention_mask" in choices_inputs[0]
    else None
)
example_encoded = {
    "example_id": example_id,
    "input_ids": input_ids,
    "attention_mask": attention_mask,
    "token_type_ids": token_type_ids,
    "label": label

}
output = model(**example_encoded)
```


## Training data

the Training data was the same as proposed [here](https://leaderboard.allenai.org/arc/submission/blcotvl7rrltlue6bsv0) 

The only diferrence was the hypeparameters of RACE fine tuned model, which were reported [here](https://huggingface.co/LIAMF-USP/roberta-large-finetuned-race#eval-results)

## Training procedure

It was necessary to preprocess the data with a method that is exemplified for a single instance in the _How to use_ section. The used hyperparameters were the following:

| Hyperparameter | Value |
|:----:|:----:|
| adam_beta1                  | 0.9      |
| adam_beta2                  | 0.98     |
| adam_epsilon                | 1.000e-8 |
| eval_batch_size             | 16       |
| train_batch_size            | 4        |
| fp16                        | True     |
| gradient_accumulation_steps | 4       |
| learning_rate               | 0.00001  |
| warmup_steps                | 0.06     |
| max_length                  | 256      |
| epochs                  |   4      |

The other parameters were the default ones from [Trainer](https://huggingface.co/transformers/main_classes/trainer.html) and [Trainer Arguments](https://huggingface.co/transformers/main_classes/trainer.html#trainingarguments)

## Eval results:
| Dataset Acc | Challenge Test |
|:----:|:----:|
|      | 65.358 |

**The model was trained with a TITAN RTX** 
