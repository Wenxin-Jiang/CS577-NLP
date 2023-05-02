---
language: fr
datasets:
- common_voice
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning
license: apache-2.0
model-index:
- name: wav2vec2-large-xlsr-53-French_punctuation by Ilyes Rebai
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice
      args: fr
    metrics:
       - name: Test WER and CER on text and puctuation prediction
         types: [wer, cer]
         values:  [19.47%, 6.66%]
       - name: Test WER and CER on text without punctuation
         types: [wer, cer]
         values:  [17.88%, 6.37%]

---
## Evaluation on Common Voice FR Test
```python
import re
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import (
    Wav2Vec2ForCTC,
    Wav2Vec2Processor,
)



model_name = "Ilyes/wav2vec2-large-xlsr-53-french_punctuation"


model = Wav2Vec2ForCTC.from_pretrained(model_name).to('cuda')
processor = Wav2Vec2Processor.from_pretrained(model_name)


ds = load_dataset("common_voice", "fr", split="test")


chars_to_ignore_regex = '[\;\:\"\“\%\‘\”\�\‘\’\’\’\‘\…\·\ǃ\«\‹\»\›“\”\\ʿ\ʾ\„\∞\\|\;\:\*\—\–\─\―\_\/\:\ː\;\=\«\»\→]'
def normalize_text(text):
    text = text.lower().strip()
    text = re.sub('œ', 'oe', text)
    text = re.sub('æ', 'ae', text)
    text = re.sub("’|´|′|ʼ|‘|ʻ|`", "'", text)
    text = re.sub("'+ ", " ", text)
    text = re.sub(" '+", " ", text)
    text = re.sub("'$", " ", text)
    text = re.sub("' ", " ", text)
    text = re.sub("−|‐", "-", text)
    text = re.sub(" -", "", text)
    text = re.sub("- ", "", text)
    text = re.sub(chars_to_ignore_regex, '', text)
    return text



def map_to_array(batch):
    speech, _ = torchaudio.load(batch["path"])
    batch["speech"] = resampler.forward(speech.squeeze(0)).numpy()
    batch["sampling_rate"] = resampler.new_freq
    batch["sentence"] = normalize_text(batch["sentence"])
    return batch

ds = ds.map(map_to_array)

resampler = torchaudio.transforms.Resample(48_000, 16_000)
def map_to_pred(batch):
    features = processor(batch["speech"], sampling_rate=batch["sampling_rate"][0], padding=True, return_tensors="pt")
    input_values = features.input_values.to(device)
    attention_mask = features.attention_mask.to(device)
    with torch.no_grad():
        logits = model(input_values, attention_mask=attention_mask).logits
    pred_ids = torch.argmax(logits, dim=-1)
    batch["predicted"] = processor.batch_decode(pred_ids)
    batch["target"] = batch["sentence"]
    # remove duplicates
    batch["target"] = re.sub('\.+', '.', batch["target"])
    batch["target"] = re.sub('\?+', '?', batch["target"])
    batch["target"] = re.sub('!+', '!', batch["target"])
    batch["target"] = re.sub(',+', ',', batch["target"])
    return batch

result = ds.map(map_to_pred, batched=True, batch_size=16, remove_columns=list(ds.features.keys()))
wer = load_metric("wer")
print(wer.compute(predictions=result["predicted"], references=result["target"]))
```
## Some results

| Reference  | Prediction |
| ------------- | ------------- |
| il vécut à new york et y enseigna une grande partie de sa vie. | il a vécu à new york et y enseigna une grande partie de sa vie. |
| au classement par nations, l'allemagne est la tenante du titre. | au classement der nation l'allemagne est la tenante du titre. |
| voici un petit calcul pour fixer les idées. | voici un petit calcul pour fixer les idées. |
| oh! tu dois être beau avec | oh! tu dois être beau avec. |
| babochet vous le voulez? | baboche, vous le voulez? |
| la commission est, par conséquent, défavorable à cet amendement. | la commission est, par conséquent, défavorable à cet amendement. |

All the references and predictions of the test corpus are already available in this repository.

## Results

text + punctuation 

WER=21.47% CER=7.21%


text (without punctuation)

WER=19.71% CER=6.91%

