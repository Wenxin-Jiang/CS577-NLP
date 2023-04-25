---
language:
- pl
license: apache-2.0
tags:
- automatic-speech-recognition
- hf-asr-leaderboard
- mozilla-foundation/common_voice_8_0
- pl
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: XLS-R Wav2Vec2 Polish by Jonatas Grosman
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: pl
    metrics:
    - name: Test WER
      type: wer
      value: 11.01
    - name: Test CER
      type: cer
      value: 2.55
    - name: Test WER (+LM)
      type: wer
      value: 7.32
    - name: Test CER (+LM)
      type: cer
      value: 1.95
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: pl
    metrics:
    - name: Dev WER
      type: wer
      value: 26.31
    - name: Dev CER
      type: cer
      value: 13.85
    - name: Dev WER (+LM)
      type: wer
      value: 20.33
    - name: Dev CER (+LM)
      type: cer
      value: 13.0
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: pl
    metrics:
    - name: Test WER
      type: wer
      value: 22.77
---

# Fine-tuned XLS-R 1B model for speech recognition in Polish

Fine-tuned [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on Polish using the train and validation splits of [Common Voice 8.0](https://huggingface.co/datasets/mozilla-foundation/common_voice_8_0), [Multilingual LibriSpeech](https://www.openslr.org/94/), and [Voxpopuli](https://github.com/facebookresearch/voxpopuli).
When using this model, make sure that your speech input is sampled at 16kHz.

This model has been fine-tuned by the [HuggingSound](https://github.com/jonatasgrosman/huggingsound) tool, and thanks to the GPU credits generously given by the [OVHcloud](https://www.ovhcloud.com/en/public-cloud/ai-training/) :)

## Usage

Using the [HuggingSound](https://github.com/jonatasgrosman/huggingsound) library:

```python
from huggingsound import SpeechRecognitionModel

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-xls-r-1b-polish")
audio_paths = ["/path/to/file.mp3", "/path/to/another_file.wav"]

transcriptions = model.transcribe(audio_paths)
```

Writing your own inference script:

```python
import torch
import librosa
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

LANG_ID = "pl"
MODEL_ID = "jonatasgrosman/wav2vec2-xls-r-1b-polish"
SAMPLES = 10

test_dataset = load_dataset("common_voice", LANG_ID, split=f"test[:{SAMPLES}]")

processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)

# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = librosa.load(batch["path"], sr=16_000)
    batch["speech"] = speech_array
    batch["sentence"] = batch["sentence"].upper()
    return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)
inputs = processor(test_dataset["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():
    logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

predicted_ids = torch.argmax(logits, dim=-1)
predicted_sentences = processor.batch_decode(predicted_ids)
```

## Evaluation Commands

1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python eval.py --model_id jonatasgrosman/wav2vec2-xls-r-1b-polish --dataset mozilla-foundation/common_voice_8_0 --config pl --split test
```

2. To evaluate on `speech-recognition-community-v2/dev_data`

```bash
python eval.py --model_id jonatasgrosman/wav2vec2-xls-r-1b-polish --dataset speech-recognition-community-v2/dev_data --config pl --split validation --chunk_length_s 5.0 --stride_length_s 1.0
```

## Citation
If you want to cite this model you can use this:

```bibtex
@misc{grosman2021xlsr-1b-polish,
  title={Fine-tuned {XLS-R} 1{B} model for speech recognition in {P}olish},
  author={Grosman, Jonatas},
  howpublished={\url{https://huggingface.co/jonatasgrosman/wav2vec2-xls-r-1b-polish}},
  year={2022}
}
```