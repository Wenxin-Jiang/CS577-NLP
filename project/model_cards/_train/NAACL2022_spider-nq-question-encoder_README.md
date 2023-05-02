# Spider-NQ: Question Encoder

This is the question encoder of the model fine-tuned on Natural Questions (and initialized from Spider) discussed in our paper [Learning to Retrieve Passages without Supervision](https://arxiv.org/abs/2112.07708).

## Usage

We used weight sharing for the query encoder and passage encoder, so the same model should be applied for both.

**Note**! We format the passages similar to DPR, i.e. the title and the text are separated by a `[SEP]` token, but token 
type ids are all 0-s. 

An example usage:

```python
from transformers import AutoTokenizer, DPRQuestionEncoder

tokenizer = AutoTokenizer.from_pretrained("NAACL2022/spider-nq-question-encoder")
model = DPRQuestionEncoder.from_pretrained("NAACL2022/spider-nq-question-encoder")

question = "Who is the villain in lord of the rings"
input_dict = tokenizer(question, return_tensors="pt")
del input_dict["token_type_ids"]

outputs = model(**input_dict)
```
