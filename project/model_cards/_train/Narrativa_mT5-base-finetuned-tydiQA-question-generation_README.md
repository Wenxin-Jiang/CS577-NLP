---
language: multilingual
datasets:
- tydiqa
widget:
- text: "answer: monitoring and managing PR strategy including relations with the media and journalists context: Sofía has a degree in Communications and public relations agency experience where she was in charge of monitoring and managing PR strategy including relations with the media and journalists."
---

# mT5-base fine-tuned on TyDiQA for multilingual Question Generation 🗺📖❓
[Google's mT5-base](https://huggingface.co/google/mt5-base) fine-tuned on [TyDi QA](https://huggingface.co/nlp/viewer/?dataset=tydiqa&config=secondary_task) (secondary task) for **multingual Question Generation** downstream task (by answer prepending).

## Details of mT5

[Google's mT5](https://github.com/google-research/multilingual-t5)

mT5 is pretrained on the [mC4](https://www.tensorflow.org/datasets/catalog/c4#c4multilingual) corpus, covering 101 languages:

Afrikaans, Albanian, Amharic, Arabic, Armenian, Azerbaijani, Basque, Belarusian, Bengali, Bulgarian, Burmese, Catalan, Cebuano, Chichewa, Chinese, Corsican, Czech, Danish, Dutch, English, Esperanto, Estonian, Filipino, Finnish, French, Galician, Georgian, German, Greek, Gujarati, Haitian Creole, Hausa, Hawaiian, Hebrew, Hindi, Hmong, Hungarian, Icelandic, Igbo, Indonesian, Irish, Italian, Japanese, Javanese, Kannada, Kazakh, Khmer, Korean, Kurdish, Kyrgyz, Lao, Latin, Latvian, Lithuanian, Luxembourgish, Macedonian, Malagasy, Malay, Malayalam, Maltese, Maori, Marathi, Mongolian, Nepali, Norwegian, Pashto, Persian, Polish, Portuguese, Punjabi, Romanian, Russian, Samoan, Scottish Gaelic, Serbian, Shona, Sindhi, Sinhala, Slovak, Slovenian, Somali, Sotho, Spanish, Sundanese, Swahili, Swedish, Tajik, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Uzbek, Vietnamese, Welsh, West Frisian, Xhosa, Yiddish, Yoruba, Zulu.

**Note**: mT5 was only pre-trained on mC4 excluding any supervised training. Therefore, this model has to be fine-tuned before it is useable on a downstream task.

Pretraining Dataset: [mC4](https://www.tensorflow.org/datasets/catalog/c4#c4multilingual)

Other Community Checkpoints: [here](https://huggingface.co/models?search=mt5)

Paper: [mT5: A massively multilingual pre-trained text-to-text transformer](https://arxiv.org/abs/2010.11934)

Authors: *Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant, Aditya Barua, Colin Raffel* 


## Details of the dataset 📚 

**TyDi QA** is a question answering dataset covering 11 typologically diverse languages with 204K question-answer pairs. The languages of TyDi QA are diverse with regard to their typology -- the set of linguistic features that each language expresses -- such that we expect models performing well on this set to generalize across a large number of the languages in the world. It contains language phenomena that would not be found in English-only corpora. To provide a realistic information-seeking task and avoid priming effects, questions are written by people who want to know the answer, but don’t know the answer yet, (unlike SQuAD and its descendents) and the data is collected directly in each language without the use of translation (unlike MLQA and XQuAD).

| Dataset  | Task | Split | # samples |
| -------- | ----- |------| --------- |
| TyDi QA | GoldP  | train| 49881     |
| TyDi QA | GoldP  | valid| 5077      | 



## Results on validation dataset 📝

### WIP


## Model in Action 🚀

### WIP

Created by: [Narrativa](https://www.narrativa.com/)

About Narrativa: Natural Language Generation (NLG) | Gabriele, our machine learning-based platform, builds and deploys natural language solutions. #NLG #AI