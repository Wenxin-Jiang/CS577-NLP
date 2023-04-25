---
library_name: fairseq
task: text-to-speech
tags:
- fairseq
- audio
- text-to-speech
language: mn
datasets:
- mbspeech
widget:
- text: "миний нэрийг баярцогт гэдэг"
  example_title: "Say my name!"
- text: "би монгол улсын нийслэл, улаанбаатар хотод амьдардаг"
  example_title: "Where I am from?"
- text: "энэхүү өгөгдлийг нээлттэй болгосон, болор соофтынхонд баярлалаа"
  example_title: "Thank you!"
- text: "энэхүү ажлын ихэнх хэсгийг, төгөлдөр ах хийсэн болно"
  example_title: "Shout out to original creater"
---
# tts_transformer-mn-mbspeech
[Transformer](https://arxiv.org/abs/1809.08895) text-to-speech model from fairseq S^2 ([paper](https://arxiv.org/abs/2109.06912)/[code](https://github.com/pytorch/fairseq/tree/main/examples/speech_synthesis)):
- Mongolian
- Single-speaker male voice
- Trained on [MBSpeech](https://github.com/tugstugi/mongolian-nlp/blob/master/datasets/MBSpeech-1.0-csv.zip)

