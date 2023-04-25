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

# MultiIndicParaphraseGeneration

This repository contains the [IndicBART](https://huggingface.co/ai4bharat/IndicBART) checkpoint finetuned on the 11 languages of [IndicParaphrase](https://huggingface.co/datasets/ai4bharat/IndicParaphrase) dataset. For finetuning details,
see the [paper](https://arxiv.org/abs/2203.05437). 
<ul>
<li >Supported languages: Assamese, Bengali, Gujarati, Hindi, Marathi, Odiya, Punjabi, Kannada, Malayalam, Tamil, and Telugu. Not all of these languages are supported by mBART50 and mT5. </li>
<li >The model is much smaller than the mBART and mT5(-base) models, so less computationally expensive for decoding. </li>
<li> Trained on large Indic language corpora (5.53 million sentences). </li>
<li> All languages, have been represented in Devanagari script to encourage transfer learning among the related languages. </li>
</ul>



## Using this model in `transformers`

```
from transformers import MBartForConditionalGeneration, AutoModelForSeq2SeqLM
from transformers import AlbertTokenizer, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/MultiIndicParaphraseGeneration", do_lower_case=False, use_fast=False, keep_accents=True)
# Or use tokenizer = AlbertTokenizer.from_pretrained("ai4bharat/MultiIndicParaphraseGeneration", do_lower_case=False, use_fast=False, keep_accents=True)
model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/MultiIndicParaphraseGeneration")
# Or use model = MBartForConditionalGeneration.from_pretrained("ai4bharat/MultiIndicParaphraseGeneration")

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
print(decoded_output) # दिल्ली विश्वविद्यालय देश की प्रमुख विश्वविद्यालयों में शामिल है।

# Note that if your output language is not Hindi or Marathi, you should convert its script from Devanagari to the desired language using the Indic NLP Library.

```
# Note:
If you wish to use any language written in a non-Devanagari script, then you should first convert it to Devanagari using the <a href="https://github.com/anoopkunchukuttan/indic_nlp_library">Indic NLP Library</a>. After you get the output, you should convert it back into the original script.

## Benchmarks

Scores on the `IndicParaphrase` test sets are as follows:

Language | BLEU / Self-BLEU / iBLEU
---------|----------------------------
as | 1.66 / 2.06 / 0.54
bn | 11.57 / 1.69 / 7.59
gu | 22.10 / 2.76 / 14.64
hi | 27.29 / 2.87 / 18.24
kn | 15.40 / 2.98 / 9.89
ml | 10.57 / 1.70 / 6.89
mr | 20.38 / 2.20 / 13.61
or | 19.26 / 2.10 / 12.85
pa | 14.87 / 1.35 / 10.00
ta | 18.52 / 2.88 / 12.10
te | 16.70 / 3.34 / 10.69



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
