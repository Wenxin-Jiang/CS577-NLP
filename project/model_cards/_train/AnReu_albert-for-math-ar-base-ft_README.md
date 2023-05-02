# ALBERT for Math AR

This model is further pre-trained on the Mathematics StackExchange questions and answers. It is based on Albert base v2 and uses the same tokenizer. In addition to pre-training the model was finetuned on Math Question Answer Retrieval. The sequence classification head is trained to output a relevance score if you input the question as the first segment and the answer as the second segment. You can use the relevance score to rank different answers for retrieval.

## Usage
```python
# based on https://huggingface.co/docs/transformers/main/en/task_summary#sequence-classification
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("albert-base-v2")
model = AutoModelForSequenceClassification.from_pretrained("AnReu/albert-for-math-ar-base-ft")

classes = ["non relevant", "relevant"]

sequence_0 = "How can I calculate x in $3x = 5$"
sequence_1 = "Just divide by 3: $x = \\frac{5}{3}$"
sequence_2 = "The general rule for squaring a sum is $(a+b)^2=a^2+2ab+b^2$"

# The tokenizer will automatically add any model specific separators (i.e. <CLS> and <SEP>) and tokens to
# the sequence, as well as compute the attention masks.
irrelevant = tokenizer(sequence_0, sequence_2, return_tensors="pt")
relevant = tokenizer(sequence_0, sequence_1, return_tensors="pt")

irrelevant_classification_logits = model(**irrelevant).logits
relevant_classification_logits = model(**relevant).logits

irrelevant_results = torch.softmax(irrelevant_classification_logits, dim=1).tolist()[0]
relevant_results = torch.softmax(relevant_classification_logits, dim=1).tolist()[0]

# Should be irrelevant
for i in range(len(classes)):
    print(f"{classes[i]}: {int(round(irrelevant_results[i] * 100))}%")

# Should be relevant
for i in range(len(classes)):
    print(f"{classes[i]}: {int(round(relevant_results[i] * 100))}%")
```

## Reference
If you use this model, please consider referencing our paper:

```bibtex
@inproceedings{reusch2021tu_dbs,
  title={TU\_DBS in the ARQMath Lab 2021, CLEF},
  author={Reusch, Anja and Thiele, Maik and Lehner, Wolfgang},
  year={2021},
  organization={CLEF}
}
```
