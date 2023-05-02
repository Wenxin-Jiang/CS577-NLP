---
language:
  - fr
thumbnail: "url to a thumbnail used in social sharing"
tags:
- text-generation
datasets:
- Marxav/frpron
metrics:
- loss/eval
- perplexity
widget:
- text: "bonjour:"
- text: "salut, comment ça va:"
- text: "Louis XIII:"
- text: "anticonstitutionnellement:"
- text: "les animaux:"
inference:
  parameters:
    temperature: 0.01
    return_full_text: True
---
# Fr-word to phonemic pronunciation

This model aims at predicting the syllabized phonemic pronunciation of the French words.

The generated pronunciation is:
* A text string made of International Phonetic Alphabet (IPA) characters;
* Phonemic (i.e. remains at the phoneme-level, not deeper);
* Syllabized (i.e. characters '.' and '‿' are used to identify syllabes).

Such pronunciation is used in the [French Wiktionary](https://fr.wiktionary.org/) in the {{pron|...|fr}} tag.

To use this model, simply give an input containing the word that you want to translate followed by ":", for example: "bonjour:". It will generate its predicted pronunciation, for example "bɔ̃.ʒuʁ".

This model remains experimental. Additional finetuning is needed for: 
* [Homographs with different pronunciations](https://fr.wiktionary.org/wiki/Catégorie:Homographes_non_homophones_en_français), 
* [French liaisons](https://en.wikipedia.org/wiki/Liaison_(French)), 
* [Roman numerals](https://en.wikipedia.org/wiki/Roman_numerals).

The input length is currently limited to a maximum of 60 letters.

This work is derived from the [OTEANN paper](https://aclanthology.org/2021.sigtyp-1.1/) and [code](https://github.com/marxav/oteann3), which used [minGTP](https://github.com/karpathy/minGPT).

## More information on the model, dataset, hardware, environmental consideration:

### **The training data**
The dataset used for training this models comes from data of the [French Wiktionary](https://fr.wiktionary.org/).
	
### **The model**
The model is build on [gpt2](https://huggingface.co/gpt2)