---
language: hi
metrics:
- wer
- cer
tags:
- audio
- automatic-speech-recognition
- speech
- wav2vec2
- asr
license: apache-2.0
---

# IndicWav2Vec-Hindi

This is a [Wav2Vec2](https://arxiv.org/abs/2006.11477) style ASR model trained in [fairseq](https://github.com/facebookresearch/fairseq) and ported to Hugging Face. 
More details on datasets, training-setup and conversion to HuggingFace format can be found in the [IndicWav2Vec](https://github.com/AI4Bharat/IndicWav2Vec) repo.  
*Note: This model doesn't support inference with Language Model.*

## Script to Run Inference

```python
import torch
from datasets import load_dataset
from transformers import AutoModelForCTC, AutoProcessor
import torchaudio.functional as F

DEVICE_ID = "cuda" if torch.cuda.is_available() else "cpu"
MODEL_ID = "ai4bharat/indicwav2vec-hindi"

sample = next(iter(load_dataset("common_voice", "hi", split="test", streaming=True)))
resampled_audio = F.resample(torch.tensor(sample["audio"]["array"]), 48000, 16000).numpy()

model = AutoModelForCTC.from_pretrained(MODEL_ID).to(DEVICE_ID)
processor = AutoProcessor.from_pretrained(MODEL_ID)

input_values = processor(resampled_audio, return_tensors="pt").input_values

with torch.no_grad():
    logits = model(input_values.to(DEVICE_ID)).logits.cpu()
    
prediction_ids = torch.argmax(logits, dim=-1)
output_str = processor.batch_decode(prediction_ids)[0]
print(f"Greedy Decoding: {output_str}")
```

# **About AI4Bharat**
- Website: https://ai4bharat.org/
- Code: https://github.com/AI4Bharat
- HuggingFace: https://huggingface.co/ai4bharat