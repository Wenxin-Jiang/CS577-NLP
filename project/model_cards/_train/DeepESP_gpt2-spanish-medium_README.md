---
language: es
tags:
- GPT-2
- Spanish
- ebooks
- nlg
datasets:
 - ebooks
widget:
- text: "Quisiera saber que va a suceder"
license: mit
---
# GPT2-Spanish
GPT2-Spanish is a language generation model trained from scratch with 11.5GB of Spanish texts and with a Byte Pair Encoding (BPE) tokenizer that was trained for this purpose. The parameters used are the same as the medium version of the original OpenAI GPT2 model.

## Corpus
This model was trained with a corpus of 11.5GB of texts corresponding to 3.5GB of Wikipedia articles and 8GB of books (narrative, short stories, theater, poetry, essays, and popularization).

## Tokenizer
The texts are tokenized using a byte-level version of Byte Pair Encoding (BPE) (for Unicode characters) and a vocabulary size of 50257. The inputs are sequences of 1024 consecutive tokens.

This tokenizer was trained from scratch with the Spanish corpus, since it was evidenced that the tokenizer of the English models presented limitations to capture the semantic relations of Spanish, due to the morphosyntactic differences between both languages.

Apart from the special token "<|endoftext|>" for text ending in the OpenAI GPT-2 models, the tokens "<|talk|>", "<|ax1|>", "<|ax2|>" (..)"<|ax9|>" were included so that they can serve as prompts in future training.

## Training
The model and tokenizer were trained using the Hugging Face libraries with an Nvidia Tesla V100 GPU with 16GB memory on Google Colab servers.

## Authors
The model was trained by Alejandro Oñate Latorre (Spain) and Jorge Ortiz Fuentes (Chile), members of -Deep ESP-, an open-source community on Natural Language Processing in Spanish (https://t.me/joinchat/VoEp1bPrDYEexc6h).

Thanks to the members of the community who collaborated with funding for the initial tests.

## Cautions
The model generates texts according to the patterns learned in the training corpus. These data were not filtered, therefore, the model could generate offensive or discriminatory content.

