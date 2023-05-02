---
tags:
- wikibio
- multilingual
- nlp
- indicnlp
datasets:
- ai4bharat/IndicWikiBio
language:
- as
- bn
- hi
- kn
- ml
- or
- pa
- ta
- te
licenses:
- cc-by-nc-4.0
widget:
- text: <TAG> name </TAG> राम नरेश पांडेय <TAG> office </TAG> विधायक - 205 - कुशीनगर विधान सभा निर्वाचन क्षेत्र , उत्तर प्रदेश <TAG> term </TAG> 1967 से 1968 <TAG> nationality </TAG> भारतीय </s> <2hi>
---

# MultiIndicWikiBioSS

MultiIndicWikiBioSS is a multilingual, sequence-to-sequence pre-trained model, a [IndicBARTSS](https://huggingface.co/ai4bharat/IndicBARTSS) checkpoint fine-tuned on the 9 languages of [IndicWikiBio](https://huggingface.co/datasets/ai4bharat/IndicWikiBio) dataset. For fine-tuning details,
see the [paper](https://arxiv.org/abs/2203.05437). You can use MultiIndicWikiBioSS to build biography generation applications for Indian languages by fine-tuning the model with supervised training data. Some salient features of the MultiIndicWikiBioSS are:

<ul>
<li >Supported languages: Assamese, Bengali, Hindi, Oriya, Punjabi, Kannada, Malayalam, Tamil, and Telugu. Not all of these languages are supported by mBART50 and mT5. </li>
<li >The model is much smaller than the mBART and mT5(-base) models, so less computationally expensive for finetuning and decoding. </li>
<li> Fine-tuned on an Indic language corpora (34,653 examples). </li>
<li> Unlike ai4bharat/MultiIndicWikiBioUnified, each language is written in its own script, so you do not need to perform any script mapping to/from Devanagari. </li>
</ul>

You can read more about MultiIndicWikiBioSS in this <a href="https://arxiv.org/abs/2203.05437">paper</a>.


## Using this model in `transformers`

```
from transformers import MBartForConditionalGeneration, AutoModelForSeq2SeqLM
from transformers import AlbertTokenizer, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("ai4bharat/MultiIndicWikiBioSS", do_lower_case=False, use_fast=False, keep_accents=True)
# Or use tokenizer = AlbertTokenizer.from_pretrained("ai4bharat/MultiIndicWikiBioSS", do_lower_case=False, use_fast=False, keep_accents=True)

model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/MultiIndicWikiBioSS")
# Or use model = MBartForConditionalGeneration.from_pretrained("ai4bharat/MultiIndicWikiBioSS")

# Some initial mapping
bos_id = tokenizer._convert_token_to_id_with_added_voc("<s>")
eos_id = tokenizer._convert_token_to_id_with_added_voc("</s>")
pad_id = tokenizer._convert_token_to_id_with_added_voc("<pad>")
# To get lang_id use any of ['<2as>', '<2bn>', '<2hi>', '<2kn>', '<2ml>', '<2or>', '<2pa>', '<2ta>', '<2te>']

# First tokenize the input and outputs. The format below is how IndicBART was trained so the input should be "Sentence </s> <2xx>" where xx is the language code. Similarly, the output should be "<2yy> Sentence </s>". 
inp = tokenizer("<TAG> name </TAG> भीखा लाल <TAG> office </TAG> विधायक - 318 - हसनगंज विधान सभा निर्वाचन क्षेत्र , उत्तर प्रदेश <TAG> term </TAG> 1957 से 1962 <TAG> nationality </TAG> भारतीय</s><2hi>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids 

out = tokenizer("<2hi> भीखा लाल ,भारत के उत्तर प्रदेश की दूसरी विधानसभा सभा में विधायक रहे। </s>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids 

model_outputs=model(input_ids=inp, decoder_input_ids=out[:,0:-1], labels=out[:,1:])

# For loss
model_outputs.loss ## This is not label smoothed.

# For logits
model_outputs.logits

# For generation. Pardon the messiness. Note the decoder_start_token_id.
model.eval() # Set dropouts to zero

model_output=model.generate(inp, use_cache=True,no_repeat_ngram_size=3,encoder_no_repeat_ngram_size=3, num_beams=4, max_length=20, min_length=1, early_stopping=True, pad_token_id=pad_id, bos_token_id=bos_id, eos_token_id=eos_id, decoder_start_token_id=tokenizer._convert_token_to_id_with_added_voc("<2hi>"))

# Decode to get output strings
decoded_output=tokenizer.decode(model_output[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
print(decoded_output) # __भीखा लाल ,भारत के उत्तर प्रदेश की दूसरी विधानसभा सभा में विधायक रहे।

```

## Benchmarks

Scores on the `IndicWikiBio` test sets are as follows:

Language | RougeL
---------|----------------------------
as | 56.50
bn | 56.58
hi | 67.34
kn | 39.37
ml | 38.42
or | 70.71
pa | 52.78
ta | 51.11
te | 51.72



## Citation

If you use this model, please cite the following paper:
```
@inproceedings{Kumar2022IndicNLGSM,
  title={IndicNLG Suite: Multilingual Datasets for Diverse NLG Tasks in Indic Languages},
  author={Aman Kumar and Himani Shrotriya and Prachi Sahu and Raj Dabre and Ratish Puduppully and Anoop Kunchukuttan and Amogh Mishra and Mitesh M. Khapra and Pratyush Kumar},
  year={2022},
  url = "https://arxiv.org/abs/2203.05437"
  }
```
# License
The model is available under the MIT License.