---

widget:
- text: "Liên quan vụ việc CSGT bị tố đánh dân, trúng một cháu nhỏ đang ngủ, đang lan truyền trên mạng xã hội, Đại tá Nguyễn Văn Tảo, Phó Giám đốc Công an tỉnh Tiền Giang vừa có cuộc họp cùng Chỉ huy Công an huyện Châu Thành và một số đơn vị nghiệp vụ cấp tỉnh để chỉ đạo làm rõ thông tin."
tags:
- named-entity-recognition
language:
- vi
model-index:
- name: ner-vietnamese-electra-base
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vietnamese-ner

This model is a fine-tuned version of [NlpHUST/electra-base-vn](https://huggingface.co/NlpHUST/electra-base-vn) on an VLSP 2018 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0580
- Location Precision: 0.9353
- Location Recall: 0.9377
- Location F1: 0.9365
- Location Number: 2360
- Miscellaneous Precision: 0.5660
- Miscellaneous Recall: 0.6897
- Miscellaneous F1: 0.6218
- Miscellaneous Number: 174
- Organization Precision: 0.8610
- Organization Recall: 0.9068
- Organization F1: 0.8833
- Organization Number: 1878
- Person Precision: 0.9692
- Person Recall: 0.9637
- Person F1: 0.9664
- Person Number: 2121
- Overall Precision: 0.9122
- Overall Recall: 0.9307
- Overall F1: 0.9214
- Overall Accuracy: 0.9907
## Model description

More information needed

#### How to use

You can use this model with Transformers *pipeline* for NER.

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("NlpHUST/ner-vietnamese-electra-base")
model = AutoModelForTokenClassification.from_pretrained("NlpHUST/ner-vietnamese-electra-base")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Liên quan vụ việc CSGT bị tố đánh dân, trúng một cháu nhỏ đang ngủ, đang lan truyền trên mạng xã hội, Đại tá Nguyễn Văn Tảo, Phó Giám đốc Công an tỉnh Tiền Giang vừa có cuộc họp cùng Chỉ huy Công an huyện Châu Thành và một số đơn vị nghiệp vụ cấp tỉnh để chỉ đạo làm rõ thông tin."

ner_results = nlp(example)
print(ner_results)
```

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0

### Framework versions

- Transformers 4.20.1
- Pytorch 1.8.0+cu111
- Datasets 2.4.0
- Tokenizers 0.12.1
### Contact information

For personal communication related to this project, please contact Nha Nguyen Van (nha282@gmail.com).