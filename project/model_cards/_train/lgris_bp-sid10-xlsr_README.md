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

# sid10-xlsr: Wav2vec 2.0 with Sidney Dataset

This is a the demonstration of a fine-tuned Wav2vec model for Brazilian Portuguese using the [Sidney](https://igormq.github.io/datasets/) dataset.

In this notebook the model is tested against other available Brazilian Portuguese datasets. 

| Dataset                        |  Train | Valid |  Test |
|--------------------------------|-------:|------:|------:|
| CETUC                          |        |    -- |  5.4h |
| Common Voice                   |        |    -- |  9.5h |
| LaPS BM                        |        |    -- |  0.1h |
| MLS                            |        |    -- |  3.7h |
| Multilingual TEDx (Portuguese) |        |    -- |  1.8h |
| SID                            |   7.2h |    -- |  1.0h |
| VoxForge                       |        |    -- |  0.1h |
| Total                          |    7.2h|    -- | 21.6h |


#### Summary

|  | CETUC          | CV             | LaPS           | MLS            | SID            | TEDx           | VF             | AVG            |
|----------------------|---------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|
| sid\_10 (demonstration below) |0.186 | 0.327 | 0.207 | 0.505 | 0.124 | 0.835 | 0.472 | 0.379| 
| sid\_10 + 4-gram (demonstration below) |0.096 | 0.223 | 0.115 | 0.432 | 0.101 | 0.791 | 0.348 | 0.301|

## Demonstration


```python
MODEL_NAME = "lgris/sid10-xlsr" 
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
    CETUC WER: 0.18623689076557778


#### Common Voice


```python
ds = load_data('commonvoice_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("CV WER:", wer)
```
    CV WER: 0.3279775395502392


#### LaPS


```python
ds = load_data('lapsbm_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("Laps WER:", wer)
```
    Laps WER: 0.20780303030303032


#### MLS


```python
ds = load_data('mls_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("MLS WER:", wer)
```
    MLS WER: 0.5056711598536057


#### SID


```python
ds = load_data('sid_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("Sid WER:", wer)
```
    Sid WER: 0.1247776617710105


#### TEDx


```python
ds = load_data('tedx_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("TEDx WER:", wer)
```
    TEDx WER: 0.8350609256842175


#### VoxForge


```python
ds = load_data('voxforge_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("VoxForge WER:", wer)
```
    VoxForge WER: 0.47242153679653687


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
    CETUC WER: 0.09677271347353278


#### Common Voice


```python
ds = load_data('commonvoice_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("CV WER:", wer)
```
    CV WER: 0.22363215674470321


#### LaPS


```python
ds = load_data('lapsbm_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("Laps WER:", wer)
```
    Laps WER: 0.1154924242424242


#### MLS


```python
ds = load_data('mls_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("MLS WER:", wer)
```
    MLS WER: 0.4322369152606427


#### SID


```python
ds = load_data('sid_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("Sid WER:", wer)
```
    Sid WER: 0.10080313085145765


#### TEDx


```python
ds = load_data('tedx_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("TEDx WER:", wer)
```
    TEDx WER: 0.7911789829264236


#### VoxForge


```python
ds = load_data('voxforge_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("VoxForge WER:", wer)
```
    VoxForge WER: 0.34786255411255407

