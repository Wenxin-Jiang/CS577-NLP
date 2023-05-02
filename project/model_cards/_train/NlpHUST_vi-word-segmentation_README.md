---
widget:
- text: "Phát biểu tại phiên thảo luận về tình hình kinh tế xã hội của Quốc hội sáng 28/10 , Bộ trưởng Bộ LĐ-TB&XH Đào Ngọc Dung khái quát , tại phiên khai mạc kỳ họp , lãnh đạo chính phủ đã báo cáo , đề cập tương đối rõ ràng về việc thực hiện các chính sách an sinh xã hội"
tags:
- word segmentation
language:
- vi
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: vi-word-segmentation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vi-word-segmentation

This model is a fine-tuned version of [NlpHUST/electra-base-vn](https://huggingface.co/NlpHUST/electra-base-vn) on an vlsp 2013 vietnamese word segmentation dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0501
- Precision: 0.9833
- Recall: 0.9838
- F1: 0.9835
- Accuracy: 0.9911

## Model description

More information needed

## Intended uses & limitations

You can use this model with Transformers *pipeline* for NER.

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("NlpHUST/vi-word-segmentation")
model = AutoModelForTokenClassification.from_pretrained("NlpHUST/vi-word-segmentation")

nlp = pipeline("token-classification", model=model, tokenizer=tokenizer)
example = "Phát biểu tại phiên thảo luận về tình hình kinh tế xã hội của Quốc hội sáng 28/10 , Bộ trưởng Bộ LĐ-TB&XH Đào Ngọc Dung khái quát , tại phiên khai mạc kỳ họp , lãnh đạo chính phủ đã báo cáo , đề cập tương đối rõ ràng về việc thực hiện các chính sách an sinh xã hội"

ner_results = nlp(example)
example_tok = ""
for e in ner_results:
    if "##" in e["word"]:
        example_tok = example_tok + e["word"].replace("##","")
    elif e["entity"] =="I":
        example_tok = example_tok + "_" + e["word"]
    else:
        example_tok = example_tok + " " + e["word"]
print(example_tok)

Phát_biểu tại phiên thảo_luận về tình_hình kinh_tế xã_hội của Quốc_hội sáng 28 / 10 , Bộ_trưởng Bộ LĐ - TB [UNK] XH Đào_Ngọc_Dung khái_quát , tại phiên khai_mạc kỳ họp , lãnh_đạo chính_phủ đã báo_cáo , đề_cập tương_đối rõ_ràng về việc thực_hiện các chính_sách an_sinh xã_hội

```

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0168        | 1.0   | 4712  | 0.0284          | 0.9813    | 0.9825 | 0.9819 | 0.9904   |
| 0.0107        | 2.0   | 9424  | 0.0350          | 0.9789    | 0.9814 | 0.9802 | 0.9895   |
| 0.005         | 3.0   | 14136 | 0.0364          | 0.9826    | 0.9843 | 0.9835 | 0.9909   |
| 0.0033        | 4.0   | 18848 | 0.0434          | 0.9830    | 0.9831 | 0.9830 | 0.9908   |
| 0.0017        | 5.0   | 23560 | 0.0501          | 0.9833    | 0.9838 | 0.9835 | 0.9911   |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
