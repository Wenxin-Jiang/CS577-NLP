---
tags:
- summarization
datasets:
- gigaword
license: mit
thumbnail: https://en.wikipedia.org/wiki/Bart_Simpson#/media/File:Bart_Simpson_200px.png
---
# BART for Gigaword
 - This model was created by fine-tuning the `facebook/bart-large-cnn` weights (also on HuggingFace) for the Gigaword dataset. The model was fine-tuned on the Gigaword training set for 3 epochs, and the model with the highest ROUGE-1 score on the training set batches was kept.
 - The BART Tokenizer for CNN-Dailymail was used in the fine-tuning process and that is the tokenizer that will be loaded automatically when doing:
```
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("a1noack/bart-large-gigaword")
```
# Summary generation
 - This model achieves ROUGE-1 / ROUGE-2 / ROUGE-L of 37.28 / 18.58 / 34.53 on the Gigaword test set; this is pretty good when compared to PEGASUS, `google/pegasus-gigaword`, which achieves 39.12 / 19.86 / 36.24.
 - To achieve these results, generate text using the code below. `text_list` is a list of input text string.
 ```
input_ids_list = tokenizer(text_list, truncation=True, max_length=128, 
        return_tensors='pt', padding=True)['input_ids']
output_ids_list = model.generate(input_ids_list, min_length=0)
outputs_list = tokenizer.batch_decode(output_ids_list, skip_special_tokens=True, 
        clean_up_tokenization_spaces=False)
```