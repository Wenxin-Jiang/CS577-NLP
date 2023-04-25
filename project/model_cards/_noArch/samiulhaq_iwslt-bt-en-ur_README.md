---
language:
- en
- ur
license: apache-2.0
datasets:
- iwslt14
metrics:
- bleu
library_name: fairseq
pipeline_tag: translation
---

### English to Urdu Translation
English to Urdu translation model is a Transformer model trained on IWSLT back-translated data using Faireq. 
This model is produced during the experimentation related to building Context-Aware NMT models for low-resourced languages such as Urdu, Hindi, Sindhi, Pashtu and Punjabi. This particular model does not contains any contextual information and it is baseline sentence-level transformer model.
The evaluation is done on WMT2017 standard test set. 

* source group: English 
* target group: Urdu 

* model: transformer
* Contextual 
* Test Set: WMT2017
* pre-processing: Moses + Indic Tokenizer
* Dataset + Libray Details:  [DLNMT](https://github.com/sami-haq99/nrpu-dlnmt)

## Benchmarks

| testset               | BLEU  |
|-----------------------|-------|
| Wmt2017  	| 57.95 	|

## How to use model?
* This model can be accessed via git clone:
  ```
  git clone https://huggingface.co/samiulhaq/iwslt-bt-en-ur
  ```
* You can use Fairseq library to access the model for translations:
  ```
  from fairseq.models.transformer import TransformerModel
  ```

### Load the model
```
model = TransformerModel.from_pretrained('path/to/model')

```

#### Set the model to evaluation mode
```
model.eval()
```

#### Perform inference
```
input_text = 'Hello, how are you?'

output_text = model.translate(input_text)

print(output_text)
```
