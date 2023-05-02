---
tags:
- sentence-summarization
- multilingual
- nlp
- indicnlp
datasets:
- ai4bharat/IndicSentenceSummarization
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
widget:
- जम्मू एवं कश्मीर के अनंतनाग जिले में शनिवार को सुरक्षाबलों के साथ मुठभेड़ में दो आतंकवादियों को मार गिराया गया। <s> <2hi>


---

# MultiIndicSentenceSummarizationSS

This repository contains the [IndicBARTSS](https://huggingface.co/ai4bharat/IndicBARTSS) checkpoint finetuned on the 11 languages of [IndicSentenceSummarization](https://huggingface.co/datasets/ai4bharat/IndicSentenceSummarization) dataset. For finetuning details,
see the [paper](https://arxiv.org/abs/2203.05437). 
<ul>
<li >Supported languages: Assamese, Bengali, Gujarati, Hindi, Marathi, Odiya, Punjabi, Kannada, Malayalam, Tamil, and Telugu. Not all of these languages are supported by mBART50 and mT5. </li>
<li >The model is much smaller than the mBART and mT5(-base) models, so less computationally expensive for decoding. </li>
<li> Trained on large Indic language corpora (5.53 million sentences). </li>
<li> Unlike <a href="https://huggingface.co/ai4bharat/MultiIndicSentenceSummarization">MultiIndicSentenceSummarization</a> each language is written in its own script, so you do not need to perform any script mapping to/from Devanagari. </li>
</ul>



## Using this model in `transformers`

```
from transformers import MBartForConditionalGeneration, AutoModelForSeq2SeqLM
from transformers import AlbertTokenizer, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/MultiIndicSentenceSummarizationSS", do_lower_case=False, use_fast=False, keep_accents=True)
# Or use tokenizer = AlbertTokenizer.from_pretrained("ai4bharat/MultiIndicSentenceSummarizationSS", do_lower_case=False, use_fast=False, keep_accents=True)
model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/MultiIndicSentenceSummarizationSS")
# Or use model = MBartForConditionalGeneration.from_pretrained("ai4bharat/MultiIndicSentenceSummarizationSS")

# Some initial mapping
bos_id = tokenizer._convert_token_to_id_with_added_voc("<s>")
eos_id = tokenizer._convert_token_to_id_with_added_voc("</s>")
pad_id = tokenizer._convert_token_to_id_with_added_voc("<pad>")

# To get lang_id use any of ['<2as>', '<2bn>', '<2en>', '<2gu>', '<2hi>', '<2kn>', '<2ml>', '<2mr>', '<2or>', '<2pa>', '<2ta>', '<2te>']
# First tokenize the input. The format below is how IndicBART was trained so the input should be "Sentence </s> <2xx>" where xx is the language code. Similarly, the output should be "<2yy> Sentence </s>".
inp = tokenizer("जम्मू एवं कश्मीर के अनंतनाग जिले में शनिवार को सुरक्षाबलों के साथ मुठभेड़ में दो आतंकवादियों को मार गिराया गया। </s> <2hi>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids 

# For generation. Pardon the messiness. Note the decoder_start_token_id.

model_output=model.generate(inp, use_cache=True,no_repeat_ngram_size=3, num_beams=5, length_penalty=0.8, max_length=20, min_length=1, early_stopping=True, pad_token_id=pad_id, bos_token_id=bos_id, eos_token_id=eos_id, decoder_start_token_id=tokenizer._convert_token_to_id_with_added_voc("<2hi>"))

# Decode to get output strings
decoded_output=tokenizer.decode(model_output[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
print(decoded_output) # अनंतनाग में सुरक्षाबलों के साथ मुठभेड़ में दो आतंकवादी ढेर
```

## Benchmarks

Scores on the `IndicSentenceSummarization` test sets are as follows:

Language | Rouge-1 / Rouge-2 / Rouge-L
---------|----------------------------
as	|	63.56	/	49.90	/	62.57
bn	|	52.52	/	36.15	/	50.60
gu	|	47.69	/	29.77	/	45.61
hi	|	50.43	/	28.13	/	45.15
kn	|	77.06	/	69.36	/	76.33
ml	|	65.00	/	51.99	/	63.76
mr	|	47.05	/	25.97	/	45.52
or	|	50.96	/	30.32	/	49.23
pa	|	54.95	/	36.26	/	51.26
ta	|	58.52	/	38.36	/	56.49
te	|	53.75	/	35.17	/	52.66



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
