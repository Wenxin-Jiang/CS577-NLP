# NepNewsBERT
## Masked Language Model for nepali language trained on nepali news scrapped from different nepali news website. The data set contained about 10 million of nepali sentences mainly related to nepali news. 

## Usage 

from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("Shushant/NepNewsBERT")

model = AutoModelForMaskedLM.from_pretrained("Shushant/NepNewsBERT")

from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model=model,
    tokenizer=tokenizer,
)
from pprint import pprint
pprint(fill_mask(f"तिमीलाई कस्तो {tokenizer.mask_token}."))