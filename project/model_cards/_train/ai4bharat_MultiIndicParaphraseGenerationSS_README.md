---
tags:
- paraphrase-generation
- multilingual
- nlp
- indicnlp
datasets:
- ai4bharat/IndicParaphrase
language:
- as
- bn
- gu
- hi
- kn
- ml
- mr
- or
- pa
- ta
- te
license:
- mit


---

# MultiIndicParaphraseGenerationSS

This repository contains the [IndicBARTSS](https://huggingface.co/ai4bharat/IndicBARTSS) checkpoint finetuned on the 11 languages of [IndicParaphrase](https://huggingface.co/datasets/ai4bharat/IndicParaphrase) dataset. For finetuning details,
see the [paper](https://arxiv.org/abs/2203.05437). 
<ul>
<li >Supported languages: Assamese, Bengali, Gujarati, Hindi, Marathi, Odiya, Punjabi, Kannada, Malayalam, Tamil, and Telugu. Not all of these languages are supported by mBART50 and mT5. </li>
<li >The model is much smaller than the mBART and mT5(-base) models, so less computationally expensive for decoding. </li>
<li> Trained on large Indic language corpora (5.53 million sentences). </li>
<li> Unlike <a href="https://huggingface.co/ai4bharat/MultiIndicParaphraseGeneration">MultiIndicParaphraseGeneration</a> each language is written in its own script, so you do not need to perform any script mapping to/from Devanagari. </li>
</ul>



## Using this model in `transformers`

```
from transformers import MBartForConditionalGeneration, AutoModelForSeq2SeqLM
from transformers import AlbertTokenizer, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/MultiIndicParaphraseGenerationSS", do_lower_case=False, use_fast=False, keep_accents=True)
# Or use tokenizer = AlbertTokenizer.from_pretrained("ai4bharat/MultiIndicParaphraseGenerationSS", do_lower_case=False, use_fast=False, keep_accents=True)
model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/MultiIndicParaphraseGenerationSS")
# Or use model = MBartForConditionalGeneration.from_pretrained("ai4bharat/MultiIndicParaphraseGenerationSS")

# Some initial mapping
bos_id = tokenizer._convert_token_to_id_with_added_voc("<s>")
eos_id = tokenizer._convert_token_to_id_with_added_voc("</s>")
pad_id = tokenizer._convert_token_to_id_with_added_voc("<pad>")

# To get lang_id use any of ['<2as>', '<2bn>', '<2en>', '<2gu>', '<2hi>', '<2kn>', '<2ml>', '<2mr>', '<2or>', '<2pa>', '<2ta>', '<2te>']
# First tokenize the input. The format below is how IndicBART was trained so the input should be "Sentence </s> <2xx>" where xx is the language code. Similarly, the output should be "<2yy> Sentence </s>".
inp = tokenizer("दिल्ली यूनिवर्सिटी देश की प्रसिद्ध यूनिवर्सिटी में से एक है. </s> <2hi>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids 

# For generation. Pardon the messiness. Note the decoder_start_token_id.

model_output=model.generate(inp, use_cache=True,no_repeat_ngram_size=3,encoder_no_repeat_ngram_size=3, num_beams=4, max_length=20, min_length=1, early_stopping=True, pad_token_id=pad_id, bos_token_id=bos_id, eos_token_id=eos_id, decoder_start_token_id=tokenizer._convert_token_to_id_with_added_voc("<2hi>"))

# Decode to get output strings
decoded_output=tokenizer.decode(model_output[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
print(decoded_output) #दिल्ली यूनिवर्सिटी भारत की सबसे बड़ी यूनिवर्सिटी है।
```

## Benchmarks

Scores on the `IndicParaphrase` test sets are as follows:

Language | BLEU / Self-BLEU / iBLEU
---------|----------------------------
as | 1.19 / 1.64 / 0.34
bn | 10.04 / 1.08 / 6.70
gu | 18.69 / 1.62 / 12.60
hi | 25.05 / 1.75 / 17.01
kn | 13.14 / 1.89 / 8.63
ml | 8.71 / 1.36 / 5.69
mr | 18.50 / 1.49 / 12.50
or | 23.02 / 2.68 / 15.31
pa | 17.61 / 1.37 / 11.92
ta | 16.25 / 2.13 / 10.74
te | 14.16 / 2.29 / 9.23



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
