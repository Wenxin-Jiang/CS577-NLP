---
language: pt
datasets:
- Common Voice 
metrics:
- wer
tags:
- audio
- speech
- wav2vec2
- pt
- Russian-speech-corpus
- automatic-speech-recognition
- speech
- PyTorch
license: apache-2.0
model-index:
- name: Edresson Casanova Wav2vec2 Large 100k Voxpopuli fine-tuned with a single-speaker dataset plus Data Augmentation in Russian 
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    metrics:
       - name: Test Common Voice 7.0 WER
         type: wer
         value: 36.59
---

# Wav2vec2 Large 100k Voxpopuli fine-tuned with a single-speaker dataset plus Data Augmentation in Russian 

[Wav2vec2 Large 100k Voxpopuli](https://huggingface.co/facebook/wav2vec2-large-100k-voxpopuli) fine-tuned in Russian using a single-speaker dataset plus a data augmentation method based on TTS and voice conversion.



# Use this model

```python

from transformers import AutoTokenizer, Wav2Vec2ForCTC
  
tokenizer = AutoTokenizer.from_pretrained("Edresson/wav2vec2-large-100k-voxpopuli-ft-TTS-Dataset-plus-data-augmentation-russian")

model = Wav2Vec2ForCTC.from_pretrained("Edresson/wav2vec2-large-100k-voxpopuli-ft-TTS-Dataset-plus-data-augmentation-russian")
```
# Results
For the results check the [paper](https://arxiv.org/abs/2204.00618)

# Example test with Common Voice Dataset


```python
dataset = load_dataset("common_voice", "ru", split="test", data_dir="./cv-corpus-7.0-2021-07-21")

resampler = torchaudio.transforms.Resampl(orig_freq=48_000, new_freq=16_000)

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

