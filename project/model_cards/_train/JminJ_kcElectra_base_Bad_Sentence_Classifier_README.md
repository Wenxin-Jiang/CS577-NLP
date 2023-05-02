# Bad_text_classifier

## Model 소개
인터넷 상에 퍼져있는 여러 댓글, 채팅이 민감한 내용인지 아닌지를 판별하는 모델을 공개합니다. 해당 모델은 공개데이터를 사용해 label을 수정하고 데이터들을 합쳐 구성해 finetuning을 진행하였습니다. 해당 모델이 언제나 모든 문장을 정확히 판단이 가능한 것은 아니라는 점 양해해 주시면 감사드리겠습니다.
```
NOTE)
공개 데이터의 저작권 문제로 인해 모델 학습에 사용된 변형된 데이터는 공개 불가능하다는 점을 밝힙니다.
또한 해당 모델의 의견은 제 의견과 무관하다는 점을 미리 밝힙니다.
```

## Dataset
### data label
* **0 : bad sentence**
* **1 : not bad sentence**
### 사용한 dataset
* [smilegate-ai/Korean Unsmile Dataset](https://github.com/smilegate-ai/korean_unsmile_dataset)
* [kocohub/Korean HateSpeech Dataset](https://github.com/kocohub/korean-hate-speech)
### dataset 가공 방법
기존 이진 분류가 아니였던 두 데이터를 이진 분류 형태로 labeling을 다시 해준 뒤, Korean HateSpeech Dataset중 label 1(not bad sentence)만을 추려 가공된 Korean Unsmile Dataset에 합쳐 주었습니다.
</br>

**Korean Unsmile Dataset에 clean으로 labeling 되어있던 데이터 중 몇개의 데이터를 0 (bad sentence)으로 수정하였습니다.**
* "~노"가 포함된 문장 중, "이기", "노무"가 포함된 데이터는 0 (bad sentence)으로 수정
* "좆", "봊" 등 성 관련 뉘앙스가 포함된 데이터는 0 (bad sentence)으로 수정
</br>

## Model Training
* huggingface transformers의 ElectraForSequenceClassification를 사용해 finetuning을 수행하였습니다.
* 한국어 공개 Electra 모델 중 3가지 모델을 사용해 각각 학습시켜주었습니다.
### use model
* [Beomi/KcELECTRA](https://github.com/Beomi/KcELECTRA)
* [monologg/koELECTRA](https://github.com/monologg/KoELECTRA)
* [tunib/electra-ko-base](https://huggingface.co/tunib/electra-ko-base)

## How to use model?
```PYTHON
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained('JminJ/kcElectra_base_Bad_Sentence_Classifier')
tokenizer = AutoTokenizer.from_pretrained('JminJ/kcElectra_base_Bad_Sentence_Classifier')
```

## Model Valid Accuracy
| mdoel | accuracy |
| ---------- | ---------- |
| kcElectra_base_fp16_wd_custom_dataset | 0.8849 |
| tunibElectra_base_fp16_wd_custom_dataset | 0.8726 |
| koElectra_base_fp16_wd_custom_dataset | 0.8434 |
```
Note)
모든 모델은 동일한 seed, learning_rate(3e-06), weight_decay lambda(0.001), batch_size(128)로 학습되었습니다.
```

## Contact
* jminju254@gmail.com
</br></br>

## Github
* https://github.com/JminJ/Bad_text_classifier
</br></br>

## Reference
* [Beomi/KcELECTRA](https://github.com/Beomi/KcELECTRA)
* [monologg/koELECTRA](https://github.com/monologg/KoELECTRA)
* [tunib/electra-ko-base](https://huggingface.co/tunib/electra-ko-base)
* [smilegate-ai/Korean Unsmile Dataset](https://github.com/smilegate-ai/korean_unsmile_dataset)
* [kocohub/Korean HateSpeech Dataset](https://github.com/kocohub/korean-hate-speech)
* [ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators](https://arxiv.org/abs/2003.10555)
