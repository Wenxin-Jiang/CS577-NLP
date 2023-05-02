---
tags:
- question-generation
- multilingual
- nlp
- indicnlp
datasets:
- ai4bharat/IndicQuestionGeneration
- squad
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
licenses:
- cc-by-nc-4.0


---

# MultiIndicQuestionGenerationSS

MultiIndicQuestionGenerationSS is a multilingual, sequence-to-sequence pre-trained model, a [IndicBARTSS](https://huggingface.co/ai4bharat/IndicBARTSS) checkpoint fine-tuned on the 11 languages of [IndicQuestionGeneration](https://huggingface.co/datasets/ai4bharat/IndicQuestionGeneration) dataset. For fine-tuning details,
see the [paper](https://arxiv.org/abs/2203.05437). You can use MultiIndicQuestionGenerationSS to build question generation applications for Indian languages by fine-tuning the model with supervised training data for the question generation task. Some salient features of the MultiIndicQuestionGenerationSS are:

<ul>
<li >Supported languages: Assamese, Bengali, Gujarati, Hindi, Marathi, Oriya, Punjabi, Kannada, Malayalam, Tamil, and Telugu. Not all of these languages are supported by mBART50 and mT5. </li>
<li >The model is much smaller than the mBART and mT5(-base) models, so less computationally expensive for finetuning and decoding. </li>
<li> Fine-tuned on large Indic language corpora (770 K examples). </li>
<li> Unlike ai4bharat/MultiIndicQuestionGenerationUnified, each language is written in its own script, so you do not need to perform any script mapping to/from Devanagari. </li>
</ul>

You can read more about MultiIndicQuestionGenerationSS in this <a href="https://arxiv.org/abs/2203.05437">paper</a>.


## Using this model in `transformers`

```
from transformers import MBartForConditionalGeneration, AutoModelForSeq2SeqLM
from transformers import AlbertTokenizer, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("ai4bharat/MultiIndicQuestionGenerationSS", do_lower_case=False, use_fast=False, keep_accents=True)

# Or use tokenizer = AlbertTokenizer.from_pretrained("ai4bharat/MultiIndicQuestionGenerationSS", do_lower_case=False, use_fast=False, keep_accents=True)

model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/MultiIndicQuestionGenerationSS")

# Or use model = MBartForConditionalGeneration.from_pretrained("ai4bharat/MultiIndicQuestionGenerationSS")

# Some initial mapping
bos_id = tokenizer._convert_token_to_id_with_added_voc("<s>")
eos_id = tokenizer._convert_token_to_id_with_added_voc("</s>")
pad_id = tokenizer._convert_token_to_id_with_added_voc("<pad>")
# To get lang_id use any of ['<2as>', '<2bn>', '<2gu>', '<2hi>', '<2kn>', '<2ml>', '<2mr>', '<2or>', '<2pa>', '<2ta>', '<2te>']

# First tokenize the input and outputs. The format below is how IndicBARTSS was trained so the input should be "Sentence </s> <2xx>" where xx is the language code. Similarly, the output should be "<2yy> Sentence </s>". 
inp = tokenizer("7 फरवरी, 2016 [SEP] खेल 7 फरवरी, 2016 को कैलिफोर्निया के सांता क्लारा में सैन फ्रांसिस्को खाड़ी क्षेत्र में लेवी स्टेडियम में खेला गया था। </s> <2hi>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids 

out = tokenizer("<2hi> सुपर बाउल किस दिन खेला गया? </s>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids 

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

print(decoded_output) # कब होगा पहला एएफएल गेम?

```

## Benchmarks

Scores on the `IndicQuestionGeneration` test sets are as follows:

Language | RougeL
---------|----------------------------
as | 20.73
bn | 30.38
gu | 28.13
hi | 34.42
kn | 23.77
ml | 22.24
mr | 23.62
or | 27.53
pa | 32.53
ta | 23.49
te | 25.81


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