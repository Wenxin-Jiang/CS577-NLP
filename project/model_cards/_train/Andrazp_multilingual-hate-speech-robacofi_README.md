---
widget:

- text: "My name is Mark and I live in London. I am a postgraduate student at Queen Mary University."
language: 
  - en
license: mit
---

# Multilingual Hate Speech Classifier for Social Media Content

A multilingual model for hate speech classification of social media content. The model is based on pre-trained multilingual representations from the XLM-T model (https://arxiv.org/abs/2104.12250) and was jointly fine-tuned on five languages, namely Arabic, Croatian, English, German and Slovenian. The test results on these five languages in terms of F1 score are as follows:

| Language  |   F1   |
|-----------|:------:|
| Arabic    | 0.8704 |
| Croatian  | 0.7226 |
| English   | 0.7851 |
| German    | 0.7826 |
| Slovenian | 0.7596 |

## Tokenizer

During training the text was preprocessed using the original XLM-T tokenizer. The pretrained tokenizer files are included in this repository. We suggest the same tokenizer is used for inference.

## Model output

The model classifies each input into one of two distinct classes:
* 0 - not-offensive
* 1 - offensive

## Acknowledgments

The authors acknowledge the financial support from the RobaCOFI project, which has indirectly received funding from the European Union’s Horizon 2020 research and innovation action programme via the AI4Media Open Call #1 issued and executed under the AI4Media project (Grant Agreement no. 951911), and from from the Slovenian Research Agency for the the project Hate speech in contemporary conceptualizations of nationalism, racism, gender and migration (J5-3102).
