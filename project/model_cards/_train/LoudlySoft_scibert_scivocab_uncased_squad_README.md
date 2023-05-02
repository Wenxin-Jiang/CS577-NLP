## AllenAI's <i>scibert_scivocab_uncased</i> fine-tuned on SQuAD 2.0 evaluated with F1 = 86.85

#### To load the model:

```
from transformers import BertTokenizerFast
from transformers import BertForQuestionAnswering
 
tokenizer = BertTokenizerFast.from_pretrained("LoudlySoft/scibert_scivocab_uncased_squad")
model = BertForQuestionAnswering.from_pretrained("LoudlySoft/scibert_scivocab_uncased_squad")
```