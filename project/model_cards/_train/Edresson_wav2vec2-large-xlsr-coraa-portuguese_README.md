---
language: pt
datasets:
- CORAA 
metrics:
- wer
tags:
- audio
- speech
- wav2vec2
- pt
- portuguese-speech-corpus
- automatic-speech-recognition
- hf-asr-leaderboard
- speech
- PyTorch
license: apache-2.0
model-index:
- name: Edresson Casanova XLSR Wav2Vec2 Large 53 Portuguese 
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: CORAA
      type: CORAA
      args: pt
    metrics:
       - name: Test CORAA WER
         type: wer
         value: 25.26
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: pt
    metrics:
       - name: Test WER on Common Voice 7
         type: wer
         value: 20.08        
---

# Wav2vec 2.0 trained with CORAA Portuguese Dataset

This a the demonstration of a fine-tuned Wav2vec model for Portuguese using the following  [CORAA dataset](https://github.com/nilc-nlp/CORAA)



# Use this model

```python

from transformers import AutoTokenizer, Wav2Vec2ForCTC
  
tokenizer = AutoTokenizer.from_pretrained("Edresson/wav2vec2-large-xlsr-coraa-portuguese")

model = Wav2Vec2ForCTC.from_pretrained("Edresson/wav2vec2-large-xlsr-coraa-portuguese")
```
# Results
For the results check the [CORAA article](https://arxiv.org/abs/2110.15731)

# Example test with Common Voice Dataset


```python
dataset = load_dataset("common_voice", "pt", split="test", data_dir="./cv-corpus-6.1-2020-12-11")

resampler = torchaudio.transforms.Resample(orig_freq=48_000, new_freq=16_000)

def map_to_array(batch):
    speech, _ = torchaudio.load(batch["path"])
    batch["speech"] = resampler.forward(speech.squeeze(0)).numpy()
    batch["sampling_rate"] = resampler.new_freq
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower().replace("â€™", "'")
    return batch
```

```python
ds = dataset.map(map_to_array)
result = ds.map(map_to_pred, batched=True, batch_size=1, remove_columns=list(ds.features.keys()))
print(wer.compute(predictions=result["predicted"], references=result["target"]))
```
