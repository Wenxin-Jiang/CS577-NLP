---
tags:
- translation
- torch==1.8.0
widget:
- text: "Inference Unavailable"
---
### marianmt-th-zh_cn
* source languages: th
* target languages: zh_cn
* dataset: 
* model: transformer-align
* pre-processing: normalization + SentencePiece
* test set scores: 15.53

## Training

Training scripts from [LalitaDeelert/NLP-ZH_TH-Project](https://github.com/LalitaDeelert/NLP-ZH_TH-Project). Experiments tracked at [cstorm125/marianmt-th-zh_cn](https://wandb.ai/cstorm125/marianmt-th-zh_cn).

```
export WANDB_PROJECT=marianmt-th-zh_cn
python train_model.py --input_fname ../data/v1/Train.csv \\\\\\\\
\\\\t--output_dir ../models/marianmt-th-zh_cn \\\\\\\\
\\\\t--source_lang th --target_lang zh \\\\\\\\
\\\\t--metric_tokenize zh --fp16
```

## Usage

```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
 
tokenizer = AutoTokenizer.from_pretrained("Lalita/marianmt-zh_cn-th")
model = AutoModelForSeq2SeqLM.from_pretrained("Lalita/marianmt-zh_cn-th").cpu()

src_text = [
    'ฉันรักคุณ',
    'ฉันอยากกินข้าว',
]
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))
print([tokenizer.decode(t, skip_special_tokens=True) for t in translated])

> ['我爱你', '我想吃饭。']
```

## Requirements
```
transformers==4.6.0
torch==1.8.0
```