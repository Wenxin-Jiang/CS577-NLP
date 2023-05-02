# MedCPT

###### LingYi system pre training medical model

###### Prease load the model from [**CPT**](https://huggingface.co/fnlp/cpt-large)

## Usage

```python
>>> from modeling_cpt import CPTForConditionalGeneration
>>> from transformers import BertTokenizer
>>> tokenizer = BertTokenizer.from_pretrained("WENGSYX/MedCPT")
>>> model = CPTForConditionalGeneration.from_pretrained("WENGSYX/MedCPT")
>>> inputs = tokenizer.encode("医生你好，腹泻难受应该怎么办？", return_tensors='pt')
>>> pred_ids = model.generate(input_ids, num_beams=4, max_length=20)
>>> print(tokenizer.convert_ids_to_tokens(pred_ids[i]))
```