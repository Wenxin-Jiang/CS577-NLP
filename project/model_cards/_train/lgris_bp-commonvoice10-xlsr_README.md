---
language: pt
datasets:
- common_voice 
- mls
- cetuc
- lapsbm
- voxforge
- tedx
- sid
metrics:
- wer
tags:
- audio
- speech
- wav2vec2
- pt
- portuguese-speech-corpus
- automatic-speech-recognition
- speech
- PyTorch
license: apache-2.0
---

# commonvoice10-xlsr: Wav2vec 2.0 with Common Voice Dataset

This is a the demonstration of a fine-tuned Wav2vec model for Brazilian Portuguese using the [Common Voice 7.0](https://commonvoice.mozilla.org/pt) dataset.

In this notebook the model is tested against other available Brazilian Portuguese datasets. 

| Dataset                        |  Train | Valid |  Test |
|--------------------------------|-------:|------:|------:|
| CETUC                          |        |    -- |  5.4h |
| Common Voice                   |  37.8h |    -- |  9.5h |
| LaPS BM                        |        |    -- |  0.1h |
| MLS                            |        |    -- |  3.7h |
| Multilingual TEDx (Portuguese) |        |    -- |  1.8h |
| SID                            |        |    -- |  1.0h |
| VoxForge                       |        |    -- |  0.1h |
| Total                          |        |    -- | 21.6h |


#### Summary

|  | CETUC          | CV             | LaPS           | MLS            | SID            | TEDx           | VF             | AVG            |
|----------------------|---------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|
| commonvoice10 (demonstration below) | 0.133 | 0.189 | 0.165 | 0.189 | 0.247 | 0.474 | 0.251 | 0.235 | 
| commonvoice10 + 4-gram (demonstration below) | 0.060 | 0.117 | 0.088 | 0.136 | 0.181 | 0.394 | 0.227 | 0.171 |

## Demonstration


```python
MODEL_NAME = "lgris/commonvoice10-xlsr" 
```

### Imports and dependencies


```python
%%capture
!pip install torch==1.8.2+cu111 torchvision==0.9.2+cu111 torchaudio===0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
!pip install datasets
!pip install jiwer
!pip install transformers
!pip install soundfile
!pip install pyctcdecode
!pip install https://github.com/kpu/kenlm/archive/master.zip
```


```python
import jiwer
import torchaudio
from datasets import load_dataset, load_metric
from transformers import (
    Wav2Vec2ForCTC,
    Wav2Vec2Processor,
)
from pyctcdecode import build_ctcdecoder
import torch
import re
import sys
```

### Helpers


```python
chars_to_ignore_regex = '[\,\?\.\!\;\:\"]'  # noqa: W605

def map_to_array(batch):
    speech, _ = torchaudio.load(batch["path"])
    batch["speech"] = speech.squeeze(0).numpy() 
    batch["sampling_rate"] = 16_000 
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower().replace("’", "'")
    batch["target"] = batch["sentence"]
    return batch
```


```python
def calc_metrics(truths, hypos):
    wers = []
    mers = []
    wils = []
    for t, h in zip(truths, hypos):
        try:
            wers.append(jiwer.wer(t, h))
            mers.append(jiwer.mer(t, h))
            wils.append(jiwer.wil(t, h))
        except: # Empty string?
            pass
    wer = sum(wers)/len(wers)
    mer = sum(mers)/len(mers)
    wil = sum(wils)/len(wils)
    return wer, mer, wil
```


```python
def load_data(dataset):
    data_files = {'test': f'{dataset}/test.csv'}
    dataset = load_dataset('csv', data_files=data_files)["test"]
    return dataset.map(map_to_array)
```

### Model


```python
class STT:

    def __init__(self, 
                 model_name, 
                 device='cuda' if torch.cuda.is_available() else 'cpu', 
                 lm=None):
        self.model_name = model_name
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name).to(device)
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)
        self.vocab_dict = self.processor.tokenizer.get_vocab()
        self.sorted_dict = {
            k.lower(): v for k, v in sorted(self.vocab_dict.items(), 
                                            key=lambda item: item[1])
        }
        self.device = device
        self.lm = lm
        if self.lm:            
            self.lm_decoder = build_ctcdecoder(
                list(self.sorted_dict.keys()),
                self.lm
            )

    def batch_predict(self, batch):
        features = self.processor(batch["speech"], 
                                  sampling_rate=batch["sampling_rate"][0], 
                                  padding=True, 
                                  return_tensors="pt")
        input_values = features.input_values.to(self.device)
        attention_mask = features.attention_mask.to(self.device)
        with torch.no_grad():
            logits = self.model(input_values, attention_mask=attention_mask).logits
        if self.lm:
            logits = logits.cpu().numpy()
            batch["predicted"] = []
            for sample_logits in logits:
                batch["predicted"].append(self.lm_decoder.decode(sample_logits))
        else:
            pred_ids = torch.argmax(logits, dim=-1)
            batch["predicted"] = self.processor.batch_decode(pred_ids)
        return batch
```

### Download datasets


```python
%%capture
!gdown --id 1HFECzIizf-bmkQRLiQD0QVqcGtOG5upI
!mkdir bp_dataset
!unzip bp_dataset -d bp_dataset/
```

### Tests 


```python
stt = STT(MODEL_NAME)
```

#### CETUC


```python
ds = load_data('cetuc_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("CETUC WER:", wer)
```
    CETUC WER: 0.13291846056190185


#### Common Voice


```python
ds = load_data('commonvoice_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("CV WER:", wer)
```
    CV WER: 0.18909733896486755


#### LaPS


```python
ds = load_data('lapsbm_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("Laps WER:", wer)
```
    Laps WER: 0.1655429292929293


#### MLS


```python
ds = load_data('mls_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("MLS WER:", wer)
```
    MLS WER: 0.1894711228284466


#### SID


```python
ds = load_data('sid_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("Sid WER:", wer)
```
    Sid WER: 0.2471983709551264


#### TEDx


```python
ds = load_data('tedx_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("TEDx WER:", wer)
```
    TEDx WER: 0.4739658565194102


#### VoxForge


```python
ds = load_data('voxforge_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("VoxForge WER:", wer)
```
    VoxForge WER: 0.2510294913419914


### Tests with LM


```python
# !find -type f -name "*.wav" -delete
!rm -rf ~/.cache
!gdown --id 1GJIKseP5ZkTbllQVgOL98R4yYAcIySFP  # trained with wikipedia
stt = STT(MODEL_NAME, lm='pt-BR-wiki.word.4-gram.arpa')
# !gdown --id 1dLFldy7eguPtyJj5OAlI4Emnx0BpFywg  # trained with bp
# stt = STT(MODEL_NAME, lm='pt-BR.word.4-gram.arpa')
```

#### CETUC


```python
ds = load_data('cetuc_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("CETUC WER:", wer)
```
    CETUC WER: 0.060609303416680915


#### Common Voice


```python
ds = load_data('commonvoice_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("CV WER:", wer)
```
    CV WER: 0.11758415681158373


#### LaPS


```python
ds = load_data('lapsbm_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("Laps WER:", wer)
```
    Laps WER: 0.08815340909090909


#### MLS


```python
ds = load_data('mls_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("MLS WER:", wer)
```
    MLS WER: 0.1359966791836458


#### SID


```python
ds = load_data('sid_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("Sid WER:", wer)
```
    Sid WER: 0.1818429601530829


#### TEDx


```python
ds = load_data('tedx_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("TEDx WER:", wer)
```
    TEDx WER: 0.39469326522731385


#### VoxForge


```python
ds = load_data('voxforge_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("VoxForge WER:", wer)
```
    VoxForge WER: 0.22779897186147183

