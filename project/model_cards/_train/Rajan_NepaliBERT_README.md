
# NepaliBERT(Phase 1) 
NEPALIBERT is a state-of-the-art language model for Nepali based on the BERT model. The model is trained using a masked language modeling (MLM). 

# Loading the model and tokenizer 
1. clone the model repo 
```
git lfs install
git clone https://huggingface.co/Rajan/NepaliBERT
```
2. Loading the Tokenizer 
```
from transformers import BertTokenizer
vocab_file_dir = './NepaliBERT/' 
tokenizer = BertTokenizer.from_pretrained(vocab_file_dir,
                                        strip_accents=False,
                                         clean_text=False )
```
3. Loading the model:
```
from transformers import BertForMaskedLM
model = BertForMaskedLM.from_pretrained('./NepaliBERT')
```

The easiest way to check whether our language model is learning anything interesting is via the ```FillMaskPipeline```.

Pipelines are simple wrappers around tokenizers and models, and the 'fill-mask' one will let you input a sequence containing a masked token (here, [mask]) and return a list of the most probable filled sequences, with their probabilities.

```
from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model=model,
    tokenizer=tokenizer
)
```
For more info visit the [GITHUB🤗](https://github.com/R4j4n/NepaliBERT)