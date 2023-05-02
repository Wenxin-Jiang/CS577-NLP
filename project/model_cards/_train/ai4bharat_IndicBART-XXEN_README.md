This is the IndicBART model fine-tuned on the PMI and PIB dataset for XX to En translation. For detailed documentation look here: https://indicnlp.ai4bharat.org/indic-bart/ and https://github.com/AI4Bharat/indic-bart/

Usage:

```
from transformers import MBartForConditionalGeneration, AutoModelForSeq2SeqLM
from transformers import AlbertTokenizer, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("ai4bharat/IndicBART-XXEN", do_lower_case=False, use_fast=False, keep_accents=True)

# Or use tokenizer = AlbertTokenizer.from_pretrained("ai4bharat/IndicBART-XXEN", do_lower_case=False, use_fast=False, keep_accents=True)

model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/IndicBART-XXEN")

# Or use model = MBartForConditionalGeneration.from_pretrained("ai4bharat/IndicBART-XXEN")

# Some initial mapping
bos_id = tokenizer._convert_token_to_id_with_added_voc("<s>")
eos_id = tokenizer._convert_token_to_id_with_added_voc("</s>")
pad_id = tokenizer._convert_token_to_id_with_added_voc("<pad>")
# To get lang_id use any of ['<2as>', '<2bn>', '<2en>', '<2gu>', '<2hi>', '<2kn>', '<2ml>', '<2mr>', '<2or>', '<2pa>', '<2ta>', '<2te>']

# First tokenize the input and outputs. The format below is how IndicBART-XXEN was trained so the input should be "Sentence </s> <2xx>" where xx is the language code. Similarly, the output should be "<2yy> Sentence </s>". 
inp = tokenizer("मैं  एक लड़का हूँ </s> <2hi>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids

out = tokenizer("<2en> I am a boy </s>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids

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
```
Notes:
1. This is compatible with the latest version of transformers but was developed with version 4.3.2 so consider using 4.3.2 if possible.
2. While I have only shown how to let logits and loss and how to generate outputs, you can do pretty much everything the MBartForConditionalGeneration class can do as in https://huggingface.co/docs/transformers/model_doc/mbart#transformers.MBartForConditionalGeneration
3. Note that the tokenizer I have used is based on sentencepiece and not BPE. Therefore I use the AlbertTokenizer class and not the MBartTokenizer class.