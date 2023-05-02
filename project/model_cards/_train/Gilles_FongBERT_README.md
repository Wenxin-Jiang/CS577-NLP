# FongBERT

FongBERT is a BERT model trained on 68.363 sentences in [Fon](https://en.wikipedia.org/wiki/Fon_language). The data are compiled from [JW300](https://opus.nlpl.eu/JW300.php) and other additional data I scraped from the [JW](https://www.jw.org/en/) website.
It is the first pretrained model to leverage transfer learning for downtream tasks for Fon.
Below are some examples of missing word prediction.


from transformers import AutoTokenizer, AutoModelForMaskedLM
from transformers import pipeline
  
tokenizer = AutoTokenizer.from_pretrained("Gilles/FongBERT")

model = AutoModelForMaskedLM.from_pretrained("Gilles/FongBERT")


fill = pipeline('fill-mask', model=model, tokenizer=tokenizer)


#### Example 1

**Sentence 1**: un tuùn ɖɔ un jló na wazɔ̌ nú we . **Translation**: I know I have to work for you.

**Masked Sentence**:  un tuùn ɖɔ un jló na wazɔ̌ <"mask"> we  . **Translation**: I know I have to work <"mask"> you.

fill(f'un tuùn ɖɔ un jló na wazɔ̌ {fill.tokenizer.mask_token} we')

[{'score': 0.994536280632019,
  'sequence': 'un tuùn ɖɔ un jló na wazɔ̌ nú we',
  'token': 312,
  'token_str': ' nú'},
 {'score': 0.0015309195732697845,
  'sequence': 'un tuùn ɖɔ un jló na wazɔ̌nu we',
...........]


#### Example 2

**Sentence 2**: un yi wan nu we ɖesu . **Translation**: I love you so much.

**Masked Sentence**: un yi <"mask"> nu we ɖesu . **Translation**: I <"mask"> you so much.

[{'score': 0.31483960151672363,
  'sequence': 'un yi wan nu we ɖesu',
  'token': 639,
  'token_str': ' wan'},
 {'score': 0.20940221846103668,
  'sequence': 'un yi ba nu we ɖesu',
  ...........]


#### Example 3

**Sentence 3**: un yì cí sunnu xɔ́ntɔn ce Tony gɔ́n nú táan ɖé . **Translation**: I went to my boyfriend for a while.

**Masked Sentence**: un yì cí sunnu xɔ́ntɔn ce Tony gɔ́n nú <"mask"> ɖé . **Translation**: I went to my boyfriend for a <"mask">.

  [{'score': 0.934298574924469,
  'sequence': 'un yì cí sunnu xɔ́ntɔn ce Tony gɔ́n nú táan ɖé',
  'token': 1102,
  'token_str': ' táan'},
 {'score': 0.03750855475664139,
  'sequence': 'un yì cí sunnu xɔ́ntɔn ce Tony gɔ́n nú ganxixo ɖé',
    ...........]
