---
language:
- nl
tags:
- bert
- passive
- active
license: apache-2.0
---

## Dutch Fine-Tuned BERT For Passive/Active Voice Classification. 
### Lijdende en Bedrijvende vorm classificatie voor zinnen

#### Examples
Try the following examples in the Hosted inference API:
1. Jan werd opgehaald door zijn moeder.
2. Wie niet weg is, is gezien
3. Ik ben van plan om morgen te gaan werken
4. De makelaar heeft het nieuwe huis verkocht aan de bewoners die iets verderop wonen.
5. De koekjes die mama had gemaakt waren door de jongens allemaal opgegeten.

LABEL_0 = Active / Bedrijvend. LABEL_1 = Passive / Lijdend

Answers (what they should be): 
1. 1
2. 1
3. 0
4. 0
5. 1

#### Basic Information
This model is fine-tuned on [BERTje](https://huggingface.co/GroNLP/bert-base-dutch-cased) for recognizing passive and active voice in Dutch sentences. 

Contact me at gerwindekruijf@gmail.com for further questions.


Gerwin