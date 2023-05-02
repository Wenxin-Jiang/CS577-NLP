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
- जम्मू एवं कश्मीर के अनंतनाग जिले में शनिवार को सुरक्षाबलों के साथ मुठभेड़ में दो आतंकवादियों को मार गिराया गया। </s> <2hi>



---

# MultiIndicSentenceSummarization

This repository contains the [IndicBART](https://huggingface.co/ai4bharat/IndicBART) checkpoint finetuned on the 11 languages of [IndicSentenceSummarization](https://huggingface.co/datasets/ai4bharat/IndicSentenceSummarization) dataset. For finetuning details,
see the [paper](https://arxiv.org/abs/2203.05437). 
<ul>
<li >Supported languages: Assamese, Bengali, Gujarati, Hindi, Marathi, Odiya, Punjabi, Kannada, Malayalam, Tamil, and Telugu. Not all of these languages are supported by mBART50 and mT5. </li>
<li >The model is much smaller than the mBART and mT5(-base) models, so less computationally expensive for decoding. </li>
<li> Trained on large Indic language corpora (431K sentences). </li>
<li> All languages, have been represented in Devanagari script to encourage transfer learning among the related languages. </li>
</ul>



## Using this model in `transformers`

```
from transformers import MBartForConditionalGeneration, AutoModelForSeq2SeqLM
from transformers import AlbertTokenizer, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/MultiIndicSentenceSummarization", do_lower_case=False, use_fast=False, keep_accents=True)
# Or use tokenizer = AlbertTokenizer.from_pretrained("ai4bharat/MultiIndicSentenceSummarization", do_lower_case=False, use_fast=False, keep_accents=True)
model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/MultiIndicSentenceSummarization")
# Or use model = MBartForConditionalGeneration.from_pretrained("ai4bharat/MultiIndicSentenceSummarization")

# Some initial mapping
bos_id = tokenizer._convert_token_to_id_with_added_voc("<s>")
eos_id = tokenizer._convert_token_to_id_with_added_voc("</s>")
pad_id = tokenizer._convert_token_to_id_with_added_voc("<pad>")

# To get lang_id use any of ['<2as>', '<2bn>', '<2en>', '<2gu>', '<2hi>', '<2kn>', '<2ml>', '<2mr>', '<2or>', '<2pa>', '<2ta>', '<2te>']
# First tokenize the input. The format below is how IndicBART was trained so the input should be "Sentence </s> <2xx>" where xx is the language code. Similarly, the output should be "<2yy> Sentence </s>".
inp = tokenizer("जम्मू एवं कश्मीर के अनंतनाग जिले में शनिवार को सुरक्षाबलों के साथ मुठभेड़ में दो आतंकवादियों को मार गिराया गया। </s> <2hi>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids 

# For generation. Pardon the messiness. Note the decoder_start_token_id.

model_output=model.generate(inp, use_cache=True,no_repeat_ngram_size=3, num_beams=5, length_penalty=0.8, early_stopping=True, pad_token_id=pad_id, bos_token_id=bos_id, eos_token_id=eos_id, decoder_start_token_id=tokenizer._convert_token_to_id_with_added_voc("<2hi>"))

# Decode to get output strings
decoded_output=tokenizer.decode(model_output[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
print(decoded_output) # जम्मू एवं कश्मीरः अनंतनाग में सुरक्षाबलों के साथ मुठभेड़ में दो आतंकवादी ढेर

# Note that if your output language is not Hindi or Marathi, you should convert its script from Devanagari to the desired language using the Indic NLP Library.

```
# Note:
If you wish to use any language written in a non-Devanagari script, then you should first convert it to Devanagari using the <a href="https://github.com/anoopkunchukuttan/indic_nlp_library">Indic NLP Library</a>. After you get the output, you should convert it back into the original script.

## Benchmarks

Scores on the `IndicSentenceSummarization` test sets are as follows:

Language | Rouge-1 / Rouge-2 / Rouge-L
---------|----------------------------
as	|	60.46	/	46.77	/	59.29
bn	|	51.12	/	34.91	/	49.29
gu	|	47.89	/	29.97	/	45.92
hi	|	50.7	/	28.11	/	45.34
kn	|	77.93	/	70.03	/	77.32
ml	|	67.7	/	54.42	/	66.42
mr	|	48.06	/	26.98	/	46.5
or	|	45.2	/	23.66	/	43.65
pa	|	55.96	/	37.2	/	52.22
ta	|	58.85	/	38.97	/	56.83
te	|	54.81	/	35.28	/	53.44


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
