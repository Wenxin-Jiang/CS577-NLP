
---
language:
- bn
- gu
- hi
- mr
- pa
- ta
- te

datasets:
- csebuetnlp/xlsum

tags:
- multilingual
- nlp
- indicnlp

widget:
- टेसा जॉवल का कहना है कि मृतकों और लापता लोगों के परिजनों की मदद के लिए एक केंद्र स्थापित किया जा रहा है. उन्होंने इस हादसे के तीन के बाद भी मृतकों की सूची जारी करने में हो रही देरी के बारे में स्पष्टीकरण देते हुए कहा है शवों की ठीक पहचान होना ज़रूरी है. पुलिस के अनुसार धमाकों में मारे गए लोगों की संख्या अब 49 हो गई है और अब भी 20 से ज़्यादा लोग लापता हैं. पुलिस के अनुसार लंदन पर हमले योजनाबद्ध तरीके से हुए और भूमिगत रेलगाड़ियों में विस्फोट तो 50 सैकेंड के भीतर हुए. पहचान की प्रक्रिया किंग्स क्रॉस स्टेशन के पास सुरंग में धमाके से क्षतिग्रस्त रेल कोचों में अब भी पड़े शवों के बारे में स्थिति साफ नहीं है और पुलिस ने आगाह किया है कि हताहतों की संख्या बढ़ सकती है. पुलिस, न्यायिक अधिकारियों, चिकित्सकों और अन्य विशेषज्ञों का एक आयोग बनाया गया है जिसकी देख-रेख में शवों की पहचान की प्रक्रिया पूरी होगी. महत्वपूर्ण है कि गुरुवार को लंदन में मृतकों के सम्मान में सार्वजनिक समारोह होगा जिसमें उन्हें श्रद्धाँजलि दी जाएगी और दो मिनट का मौन रखा जाएगा. पुलिस का कहना है कि वह इस्लामी चरमपंथी संगठन अबू हफ़्स अल-मासरी ब्रिगेड्स का इन धमाकों के बारे में किए गए दावे को गंभीरता से ले रही है. 'धमाके पचास सेकेंड में हुए' पुलिस के अनुसार लंदन पर हुए हमले योजनाबद्ध तरीके से किए गए थे. पुलिस के अनुसार भूमिगत रेलों में तीन बम अलग-अलग जगहों लगभग अचानक फटे थे. इसलिए पुलिस को संदेह है कि धमाकों में टाइमिंग उपकरणों का उपयोग किया गया होगा. यह भी तथ्य सामने आया है कि धमाकों में आधुनिक किस्म के विस्फोटकों का उपयोग किया गया था. पहले माना जा रहा था कि हमलों में देसी विस्फोटकों का इस्तेमाल किया गया होगा. पुलिस मुख्यालय स्कॉटलैंड यार्ड में सहायक उपायुक्त ब्रायन पैडिक ने बताया कि भूमिगत रेलों में तीन धमाके 50 सेकेंड के अंतराल के भीतर हुए थे. धमाके गुरुवार सुबह आठ बजकर पचास मिनट पर हुए थे. लंदन अंडरग्राउंड से मिली विस्तृत तकनीकी सूचनाओं से यह तथ्य सामने आया है. इससे पहले बम धमाकों में अच्छे खासे अंतराल की बात की जा रही थी.</s> <2hi>

---


IndicBART-XLSum is a multilingual separate script [IndicBART](https://huggingface.co/ai4bharat/IndicBARTSS) based, sequence-to-sequence pre-trained model focusing on Indic languages. It currently supports 7 Indian languages and is based on the mBART architecture. Some salient features of the IndicBART-XLSum are:

<ul>
<li >Supported languages: Bengali, Gujarati, Hindi, Marathi, Punjabi, Tamil and Telugu. Not all of these languages are supported by mBART50 and mT5. </li>
<li >The model is much smaller than the mBART and mT5(-base) models, so less computationally expensive for finetuning and decoding. </li>
<li> Trained on Indic portion of <a href="https://huggingface.co/datasets/csebuetnlp/xlsum">XLSum corpora</a>. </li>
<li> Each language is written in its own script, so you do not need to perform any script mapping to/from Devanagari. </li>
</ul>

You can read about IndicBARTSS in this <a href="https://arxiv.org/abs/2109.02903">paper</a>.

# Usage:

```
from transformers import MBartForConditionalGeneration, AutoModelForSeq2SeqLM
from transformers import AlbertTokenizer, AutoTokenizer

tokenizer = AlbertTokenizer.from_pretrained("ai4bharat/IndicBART-XLSum", do_lower_case=False, use_fast=False, keep_accents=True)

# Or use tokenizer = AlbertTokenizer.from_pretrained("ai4bharat/IndicBART-XLSum", do_lower_case=False, use_fast=False, keep_accents=True)

model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/IndicBART-XLSum")

# Or use model = MBartForConditionalGeneration.from_pretrained("ai4bharat/IndicBART-XLSum")

# Some initial mapping
bos_id = tokenizer._convert_token_to_id_with_added_voc("<s>")
eos_id = tokenizer._convert_token_to_id_with_added_voc("</s>")
pad_id = tokenizer._convert_token_to_id_with_added_voc("<pad>")
# To get lang_id use any of ['<2bn>', '<2gu>', '<2hi>', '<2mr>', '<2pa>', '<2ta>', '<2te>']

# First tokenize the input and outputs. The format below is how IndicBART-XLSum was trained so the input should be "Sentence </s> <2xx>" where xx is the language code. Similarly, the output should be "<2yy> Sentence </s>". 

inp = tokenizer("टेसा जॉवल का कहना है कि मृतकों और लापता लोगों के परिजनों की मदद के लिए एक केंद्र स्थापित किया जा रहा है. उन्होंने इस हादसे के तीन के बाद भी मृतकों की सूची जारी करने में हो रही देरी के बारे में स्पष्टीकरण देते हुए कहा है शवों की ठीक पहचान होना ज़रूरी है. पुलिस के अनुसार धमाकों में मारे गए लोगों की संख्या अब 49 हो गई है और अब भी 20 से ज़्यादा लोग लापता हैं. पुलिस के अनुसार लंदन पर हमले योजनाबद्ध तरीके से हुए और भूमिगत रेलगाड़ियों में विस्फोट तो 50 सैकेंड के भीतर हुए. पहचान की प्रक्रिया किंग्स क्रॉस स्टेशन के पास सुरंग में धमाके से क्षतिग्रस्त रेल कोचों में अब भी पड़े शवों के बारे में स्थिति साफ नहीं है और पुलिस ने आगाह किया है कि हताहतों की संख्या बढ़ सकती है. पुलिस, न्यायिक अधिकारियों, चिकित्सकों और अन्य विशेषज्ञों का एक आयोग बनाया गया है जिसकी देख-रेख में शवों की पहचान की प्रक्रिया पूरी होगी. महत्वपूर्ण है कि गुरुवार को लंदन में मृतकों के सम्मान में सार्वजनिक समारोह होगा जिसमें उन्हें श्रद्धाँजलि दी जाएगी और दो मिनट का मौन रखा जाएगा. पुलिस का कहना है कि वह इस्लामी चरमपंथी संगठन अबू हफ़्स अल-मासरी ब्रिगेड्स का इन धमाकों के बारे में किए गए दावे को गंभीरता से ले रही है. 'धमाके पचास सेकेंड में हुए' पुलिस के अनुसार लंदन पर हुए हमले योजनाबद्ध तरीके से किए गए थे. पुलिस के अनुसार भूमिगत रेलों में तीन बम अलग-अलग जगहों लगभग अचानक फटे थे. इसलिए पुलिस को संदेह है कि धमाकों में टाइमिंग उपकरणों का उपयोग किया गया होगा. यह भी तथ्य सामने आया है कि धमाकों में आधुनिक किस्म के विस्फोटकों का उपयोग किया गया था. पहले माना जा रहा था कि हमलों में देसी विस्फोटकों का इस्तेमाल किया गया होगा. पुलिस मुख्यालय स्कॉटलैंड यार्ड में सहायक उपायुक्त ब्रायन पैडिक ने बताया कि भूमिगत रेलों में तीन धमाके 50 सेकेंड के अंतराल के भीतर हुए थे. धमाके गुरुवार सुबह आठ बजकर पचास मिनट पर हुए थे. लंदन अंडरग्राउंड से मिली विस्तृत तकनीकी सूचनाओं से यह तथ्य सामने आया है. इससे पहले बम धमाकों में अच्छे खासे अंतराल की बात की जा रही थी.</s> <2hi>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids

out = tokenizer("<2hi>परिजनों की मदद की ज़िम्मेदारी मंत्री पर </s>", add_special_tokens=False, return_tensors="pt", padding=True).input_ids 
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

print(decoded_output) # लंदन धमाकों में मारे गए लोगों की सूची जारी

```
# Benchmarks
Scores on the `IndicBART-XLSum` test sets are as follows:

Language | Rouge-1 / Rouge-2 / Rouge-L
---------|----------------------------
bn	|	0.172331	/	0.051777	/	0.160245
gu	|	0.143240	/	0.039993	/	0.133981
hi	|	0.220394	/	0.065464	/	0.198816
mr	|	0.172568	/	0.062591	/	0.160403
pa	|	0.218274	/	0.066087	/	0.192010
ta	|	0.177317	/	0.058636	/	0.166324
te	|	0.156386	/	0.041042	/	0.144179
average	|	0.180073	/	0.055084	/	0.165137



# Notes:
1. This is compatible with the latest version of transformers but was developed with version 4.3.2 so consider using 4.3.2 if possible.
2. While I have only shown how to get logits and loss and how to generate outputs, you can do pretty much everything the MBartForConditionalGeneration class can do as in https://huggingface.co/docs/transformers/model_doc/mbart#transformers.MBartForConditionalGeneration
3. Note that the tokenizer I have used is based on sentencepiece and not BPE. Therefore, I used the AlbertTokenizer class and not the MBartTokenizer class.

