---
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
tags:
- multilingual
- nlp
- indicnlp
---

IndicBART is a multilingual, sequence-to-sequence pre-trained model focusing on Indic languages and English. It currently supports 11 Indian languages and is based on the mBART architecture. You can use IndicBART model to build natural language generation applications for Indian languages by finetuning the model with supervised training data for tasks like machine translation, summarization, question generation, etc. Some salient features of the IndicBART are:

<ul>
<li >Supported languages: Assamese, Bengali, Gujarati, Hindi, Marathi, Odiya, Punjabi, Kannada, Malayalam, Tamil, Telugu and English. Not all of these languages are supported by mBART50 and mT5. </li>
<li >The model is much smaller than the mBART and mT5(-base) models, so less computationally expensive for finetuning and decoding. </li>
<li> Trained on large Indic language corpora (452 million sentences and 9 billion tokens) which also includes Indian English content. </li>
<li> All languages, except English, have been represented in Devanagari script to encourage transfer learning among the related languages. </li>
</ul>

You can read more about IndicBART in this <a href="https://arxiv.org/abs/2109.02903">paper</a>.

For detailed documentation, look here: https://github.com/AI4Bharat/indic-bart/ and https://indicnlp.ai4bharat.org/indic-bart/

# Pre-training corpus

We used the <a href="https://indicnlp.ai4bharat.org/corpora/">IndicCorp</a> data spanning 12 languages with 452 million sentences (9 billion tokens). The model was trained using the text-infilling objective used in mBART.

# Usage:

```
from transformers import MBartForConditionalGeneration, AutoModelForSeq2SeqLM
from transformers import AlbertTokenizer, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("ai4bharat/IndicBART", do_lower_case=False, use_fast=False, keep_accents=True)

# Or use tokenizer = AlbertTokenizer.from_pretrained("ai4bharat/IndicBART", do_lower_case=False, use_fast=False, keep_accents=True)

model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/IndicBART")

# Or use model = MBartForConditionalGeneration.from_pretrained("ai4bharat/IndicBART")

# Some initial mapping
bos_id = tokenizer._convert_token_to_id_with_added_voc("<s>")
eos_id = tokenizer._convert_token_to_id_with_added_voc("</s>")
pad_id = tokenizer._convert_token_to_id_with_added_voc("<pad>")
# To get lang_id use any of ['<2as>', '<2bn>', '<2en>', '<2gu>', '<2hi>', '<2kn>', '<2ml>', '<2mr>', '<2or>', '<2pa>', '<2ta>', '<2te>']

# First tokenize the input and outputs. The format below is how IndicBART was trained so the input should be "Sentence </s> <2xx>" where xx is the language code. Similarly, the output should be "<2yy> Sentence </s>". 
inp = tokenizer("I am a boy </s> <2en>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids # tensor([[  466,  1981,    80, 25573, 64001, 64004]])

out = tokenizer("<2hi> मैं  एक लड़का हूँ </s>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids # tensor([[64006,   942,    43, 32720,  8384, 64001]])
# Note that if you use any language other than Hindi or Marathi, you should convert its script to Devanagari using the Indic NLP Library.

model_outputs=model(input_ids=inp, decoder_input_ids=out[:,0:-1], labels=out[:,1:])

# For loss
model_outputs.loss ## This is not label smoothed.

# For logits
model_outputs.logits

# For generation. Pardon the messiness. Note the decoder_start_token_id.

model.eval() # Set dropouts to zero

model_output=model.generate(inp, use_cache=True, num_beams=4, max_length=20, min_length=1, early_stopping=True, pad_token_id=pad_id, bos_token_id=bos_id, eos_token_id=eos_id, decoder_start_token_id=tokenizer._convert_token_to_id_with_added_voc("<2en>"))


# Decode to get output strings

decoded_output=tokenizer.decode(model_output[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)

print(decoded_output) # I am a boy
# Note that if your output language is not Hindi or Marathi, you should convert its script from Devanagari to the desired language using the Indic NLP Library.

# What if we mask?

inp = tokenizer("I am [MASK] </s> <2en>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids

model_output=model.generate(inp, use_cache=True, num_beams=4, max_length=20, min_length=1, early_stopping=True, pad_token_id=pad_id, bos_token_id=bos_id, eos_token_id=eos_id, decoder_start_token_id=tokenizer._convert_token_to_id_with_added_voc("<2en>"))

decoded_output=tokenizer.decode(model_output[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)

print(decoded_output) # I am happy

inp = tokenizer("मैं [MASK] हूँ </s> <2hi>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids

model_output=model.generate(inp, use_cache=True, num_beams=4, max_length=20, min_length=1, early_stopping=True, pad_token_id=pad_id, bos_token_id=bos_id, eos_token_id=eos_id, decoder_start_token_id=tokenizer._convert_token_to_id_with_added_voc("<2en>"))

decoded_output=tokenizer.decode(model_output[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)

print(decoded_output) # मैं जानता हूँ

inp = tokenizer("मला [MASK] पाहिजे </s> <2mr>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids

model_output=model.generate(inp, use_cache=True, num_beams=4, max_length=20, min_length=1, early_stopping=True, pad_token_id=pad_id, bos_token_id=bos_id, eos_token_id=eos_id, decoder_start_token_id=tokenizer._convert_token_to_id_with_added_voc("<2en>"))

decoded_output=tokenizer.decode(model_output[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)

print(decoded_output) # मला ओळखलं पाहिजे

```

# Notes:
1. This is compatible with the latest version of transformers but was developed with version 4.3.2 so consider using 4.3.2 if possible.
2. While I have only shown how to get logits and loss and how to generate outputs, you can do pretty much everything the MBartForConditionalGeneration class can do as in https://huggingface.co/docs/transformers/model_doc/mbart#transformers.MBartForConditionalGeneration
3. Note that the tokenizer I have used is based on sentencepiece and not BPE. Therefore, I used the AlbertTokenizer class and not the MBartTokenizer class.
4. If you wish to use any language written in a non-Devanagari script (except English), then you should first convert it to Devanagari using the <a href="https://github.com/anoopkunchukuttan/indic_nlp_library">Indic NLP Library</a>. After you get the output, you should convert it back into the original script.

# Fine-tuning on a downstream task

1. If you wish to fine-tune this model, then you can do so using the <a href="https://github.com/prajdabre/yanmtt">YANMTT</a> toolkit, following the instructions <a href="https://github.com/AI4Bharat/indic-bart ">here</a>.
2. (Untested) Alternatively, you may use the official huggingface scripts for <a href="https://github.com/huggingface/transformers/tree/master/examples/pytorch/translation">translation</a> and <a href="https://github.com/huggingface/transformers/tree/master/examples/pytorch/summarization">summarization</a>.

# Contributors
<ul>
<li> Raj Dabre </li>
<li> Himani Shrotriya </li>
<li> Anoop Kunchukuttan </li>
<li> Ratish Puduppully </li>
<li> Mitesh M. Khapra </li>
<li> Pratyush Kumar </li>
</ul>

# Paper
If you use IndicBART, please cite the following paper:
```
@misc{dabre2021indicbart,
      title={IndicBART: A Pre-trained Model for Natural Language Generation of Indic Languages}, 
      author={Raj Dabre and Himani Shrotriya and Anoop Kunchukuttan and Ratish Puduppully and Mitesh M. Khapra and Pratyush Kumar},
      year={2021},
      eprint={2109.02903},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
    }    
```

# License
The model is available under the MIT License.