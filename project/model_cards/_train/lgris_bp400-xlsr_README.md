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
- hf-asr-leaderboard
model-index:
- name: bp400-xlsr
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7.0
      type: mozilla-foundation/common_voice_7_0
      args: pt
    metrics:
    - name: Test WER
      type: wer
      value: 14.0
license: apache-2.0
---

# bp400-xlsr: Wav2vec 2.0 with Brazilian Portuguese (BP) Dataset

**Paper:** https://arxiv.org/abs/2107.11414

This is a the demonstration of a fine-tuned Wav2vec model for Brazilian Portuguese using the following datasets:

- [CETUC](http://www02.smt.ufrj.br/~igor.quintanilha/alcaim.tar.gz): contains approximately 145 hours of Brazilian Portuguese speech distributed among 50 male and 50 female speakers, each pronouncing approximately 1,000 phonetically balanced sentences selected from the [CETEN-Folha](https://www.linguateca.pt/cetenfolha/) corpus.
- [Common Voice 7.0](https://commonvoice.mozilla.org/pt):  is a project proposed by Mozilla Foundation with the goal to create a wide open dataset in different languages. In this project, volunteers donate and validate speech using the [oficial site](https://commonvoice.mozilla.org/pt). 
- [Lapsbm](https://github.com/falabrasil/gitlab-resources): "Falabrasil - UFPA" is a dataset used by the Fala Brasil group to benchmark ASR systems in Brazilian Portuguese. Contains 35 speakers (10 females), each one pronouncing 20 unique sentences, totalling  700 utterances in Brazilian Portuguese. The audios were recorded in 22.05 kHz without environment control.
- [Multilingual Librispeech (MLS)](https://arxiv.org/abs/2012.03411): a massive dataset available in many languages. The MLS is based on audiobook recordings in public domain like [LibriVox](https://librivox.org/). The dataset contains a total of 6k hours of transcribed data in many languages. The set in Portuguese [used in this work](http://www.openslr.org/94/) (mostly Brazilian variant) has approximately 284 hours of speech, obtained from 55 audiobooks read by 62 speakers.
- [Multilingual TEDx](http://www.openslr.org/100): a collection of audio recordings from TEDx talks in 8 source languages. The Portuguese set (mostly Brazilian Portuguese variant) contains 164 hours of transcribed speech. 
- [Sidney](https://igormq.github.io/datasets/) (SID): contains 5,777 utterances recorded by 72 speakers (20 women) from 17 to 59 years old with fields such as place of birth, age, gender, education, and occupation;
- [VoxForge](http://www.voxforge.org/): is a project with the goal to build open datasets for acoustic models. The corpus contains approximately 100 speakers and 4,130 utterances of Brazilian Portuguese, with sample rates varying from 16kHz to 44.1kHz.

These datasets were combined to build a larger Brazilian Portuguese dataset. All data was used for training except Common Voice dev/test sets, that were used for validation/test respectively. We also made test sets for all the gathered datasets.

| Dataset                        |  Train | Valid |  Test |
|--------------------------------|-------:|------:|------:|
| CETUC                          |  93.9h |    -- |  5.4h |
| Common Voice                   |  37.6h |  8.9h |  9.5h |
| LaPS BM                        |   0.8h |    -- |  0.1h |
| MLS                            | 161.0h |    -- |  3.7h |
| Multilingual TEDx (Portuguese) | 144.2h |    -- |  1.8h |
| SID                            |   5.0h |    -- |  1.0h |
| VoxForge                       |   2.8h |    -- |  0.1h |
| Total                          | 437.2h |  8.9h | 21.6h |

The original model was fine-tuned using [fairseq](https://github.com/pytorch/fairseq). This notebook uses a converted version of the original one. The link to the original fairseq model is available [here](https://drive.google.com/drive/folders/1eRUExXRF2XK8JxUjIzbLBkLa5wuR3nig?usp=sharing).

#### Summary

|  | CETUC          | CV             | LaPS           | MLS            | SID            | TEDx           | VF             | AVG            |
|----------------------|---------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|
| bp\_400 (demonstration below)              |          0.052 |          0.140 |          0.074 |          0.117 |          0.121 |          0.245 |          0.118 |          0.124 |
| bp\_400 + 3-gram      |  0.033 |  0.095 |  0.046 | 0.123 |          0.112 |          0.212 |          0.123 |          0.106 |
| bp\_400 + 4-gram (demonstration below)  | **0.030** | 0.096 | 0.043 | **0.106** | 0.118 | 0.229 | **0.117** | **0.105** |
| bp\_400 + 5-gram      | 0.033 |  0.094 |  0.043 | 0.123 | **0.111** | **0.210** | 0.123 | **0.105** |
| bp\_400 + Transf.     | 0.032 | **0.092** | **0.036** |          0.130 |          0.115 |          0.215 |          0.125 |          0.106 |

#### Transcription examples

| Text                                                                                                       | Transcription                                                                                                |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
|alguém sabe a que horas começa o jantar | alguém sabe a que horas **começo** jantar |
|lila covas ainda não sabe o que vai fazer no fundo|**lilacovas** ainda não sabe o que vai fazer no fundo|
|que tal um pouco desse bom spaghetti|**quetá** um pouco **deste** bom **ispaguete**|
|hong kong em cantonês significa porto perfumado|**rongkong** **en** **cantones** significa porto perfumado|
|vamos hackear esse problema|vamos **rackar** esse problema|
|apenas a poucos metros há uma estação de ônibus|apenas **ha** poucos metros **á** uma estação de ônibus|
|relâmpago e trovão sempre andam juntos|**relampagotrevão** sempre andam juntos|


## Demonstration


```python
MODEL_NAME = "lgris/bp400-xlsr" 
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
    CETUC WER: 0.05159104708285062


#### Common Voice


```python
ds = load_data('commonvoice_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("CV WER:", wer)
```
    CV WER: 0.14031426198658084


#### LaPS


```python
ds = load_data('lapsbm_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("Laps WER:", wer)
```
    Laps WER: 0.07432133838383838


#### MLS


```python
ds = load_data('mls_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("MLS WER:", wer)
```
    MLS WER: 0.11678793514817509


#### SID


```python
ds = load_data('sid_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("Sid WER:", wer)
```
    Sid WER: 0.12152357273433984


#### TEDx


```python
ds = load_data('tedx_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("TEDx WER:", wer)
```
    TEDx WER: 0.24666815906766504


#### VoxForge


```python
ds = load_data('voxforge_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("VoxForge WER:", wer)
```
    VoxForge WER: 0.11873106060606062


### Tests with LM


```python
!rm -rf ~/.cache
!gdown --id 1GJIKseP5ZkTbllQVgOL98R4yYAcIySFP  # trained with wikipedia
stt = STT(MODEL_NAME, lm='pt-BR-wiki.word.4-gram.arpa')
# !gdown --id 1dLFldy7eguPtyJj5OAlI4Emnx0BpFywg  # trained with bp
# stt = STT(MODEL_NAME, lm='pt-BR.word.4-gram.arpa')
```
### Cetuc


```python
ds = load_data('cetuc_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("CETUC WER:", wer)
```
    CETUC WER: 0.030266462438593742


#### Common Voice


```python
ds = load_data('commonvoice_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("CV WER:", wer)
```
    CV WER: 0.09577710237417715


#### LaPS


```python
ds = load_data('lapsbm_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("Laps WER:", wer)
```
    Laps WER: 0.043617424242424235


#### MLS


```python
ds = load_data('mls_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("MLS WER:", wer)
```
    MLS WER: 0.10642133314350002


#### SID


```python
ds = load_data('sid_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("Sid WER:", wer)
```
    Sid WER: 0.11839021001747055


#### TEDx


```python
ds = load_data('tedx_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("TEDx WER:", wer)
```
    TEDx WER: 0.22929952467810416


#### VoxForge


```python
ds = load_data('voxforge_dataset')
result = ds.map(stt.batch_predict, batched=True, batch_size=8) 
wer, mer, wil = calc_metrics(result["sentence"], result["predicted"])
print("VoxForge WER:", wer)
```
    VoxForge WER: 0.11716314935064935

