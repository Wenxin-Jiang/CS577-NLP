---
language: da
tags:
- speech-to-text
license: apache-2.0
---

# wav2vec2-base-da-ft-nst 
This the [alvenir wav2vec2 model](https://huggingface.co/Alvenir/wav2vec2-base-da) for Danish ASR finetuned by Alvenir on the public NST dataset. The model is trained on 16kHz, so make sure your data is the same sample rate.

The model was trained using fairseq and then converted to huggingface/transformers format.

Alvenir is always happy to help with your own open-source ASR projects, customized domain specializations or premium models. ;-)

## Usage
```Python
import soundfile as sf
import torch

from transformers import Wav2Vec2CTCTokenizer, Wav2Vec2Tokenizer, Wav2Vec2Processor, \
    Wav2Vec2ForCTC


def get_tokenizer(model_path: str) -> Wav2Vec2CTCTokenizer:
    return Wav2Vec2Tokenizer.from_pretrained(model_path)


def get_processor(model_path: str) -> Wav2Vec2Processor:
    return Wav2Vec2Processor.from_pretrained(model_path)


def load_model(model_path: str) -> Wav2Vec2ForCTC:
    return Wav2Vec2ForCTC.from_pretrained(model_path)


model_id = "Alvenir/wav2vec2-base-da-ft-nst"

model = load_model(model_id)
model.eval()
tokenizer = get_tokenizer(model_id)
processor = get_processor(model_id)

audio_file = "<path/to/audio.wav>"

audio, _ = sf.read(audio_file)

input_values = processor(audio, return_tensors="pt", padding="longest", sampling_rate=16_000).input_values
with torch.no_grad():
    logits = model(input_values).logits

predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)
print(transcription)

```
## Benchmark results
This is some benchmark results on the public available datasets in Danish.

| Dataset             | WER Greedy | WER with 3-gram Language Model |
|---------------------|------------|--------------------|
| NST test            | 15,8%      | 11.9%              |
| alvenir-asr-da-eval | 19.0%      | 12.1%              |
| common_voice_80 da test | 26,3% | 19,2%                 |
