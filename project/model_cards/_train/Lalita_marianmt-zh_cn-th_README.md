---
tags:
- translation
- torch==1.8.0
widget:
- text: "Inference Unavailable"
---
### marianmt-zh_cn-th 
* source languages: zh_cn
* target languages: th
* dataset: 
* model: transformer-align
* pre-processing: normalization + SentencePiece
* test set scores: syllable: 15.95, word: 8.43

## Training

Training scripts from [LalitaDeelert/NLP-ZH_TH-Project](https://github.com/LalitaDeelert/NLP-ZH_TH-Project). Experiments tracked at [cstorm125/marianmt-zh_cn-th](https://wandb.ai/cstorm125/marianmt-zh_cn-th).

```
export WANDB_PROJECT=marianmt-zh_cn-th
python train_model.py --input_fname ../data/v1/Train.csv \\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\t--output_dir ../models/marianmt-zh_cn-th \\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\t--source_lang zh --target_lang th \\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\t--metric_tokenize th_syllable --fp16 
```

## Usage

```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
 
tokenizer = AutoTokenizer.from_pretrained("Lalita/marianmt-zh_cn-th")
model = AutoModelForSeq2SeqLM.from_pretrained("Lalita/marianmt-zh_cn-th").cpu()

src_text = [
    '我爱你',
    '我想吃米饭',
]
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))
print([tokenizer.decode(t, skip_special_tokens=True) for t in translated])

> ['ผมรักคุณนะ', 'ฉันอยากกินข้าว']
```

## Requirements
```
transformers==4.6.0
torch==1.8.0
```