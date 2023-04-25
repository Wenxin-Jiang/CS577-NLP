---
language: et
tags:
- audio
- automatic-speech-recognition
- voxpopuli
license: cc-by-nc-4.0
---

# Wav2Vec2-Base-VoxPopuli-Finetuned

[Facebook's Wav2Vec2](https://ai.facebook.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/) base model pretrained on the 10K unlabeled subset of [VoxPopuli corpus](https://arxiv.org/abs/2101.00390) and fine-tuned on the transcribed data in et (refer to Table 1 of paper for more information).

**Paper**: *[VoxPopuli: A Large-Scale Multilingual Speech Corpus for Representation
Learning, Semi-Supervised Learning and Interpretation](https://arxiv.org/abs/2101.00390)*

**Authors**: *Changhan Wang, Morgane Riviere, Ann Lee, Anne Wu, Chaitanya Talnikar, Daniel Haziza, Mary Williamson, Juan Pino, Emmanuel Dupoux* from *Facebook AI*

See the official website for more information, [here](https://github.com/facebookresearch/voxpopuli/)


# Usage for inference

In the following it is shown how the model can be used in inference on a sample of the [Common Voice dataset](https://commonvoice.mozilla.org/en/datasets)

```python
#!/usr/bin/env python3
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from datasets import load_dataset
import torchaudio
import torch

# resample audio

# load model & processor
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-10k-voxpopuli-ft-et")
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-10k-voxpopuli-ft-et")

# load dataset
ds = load_dataset("common_voice", "et", split="validation[:1%]")

# common voice does not match target sampling rate
common_voice_sample_rate = 48000
target_sample_rate = 16000

resampler = torchaudio.transforms.Resample(common_voice_sample_rate, target_sample_rate)


# define mapping fn to read in sound file and resample
def map_to_array(batch):
    speech, _ = torchaudio.load(batch["path"])
    speech = resampler(speech)
    batch["speech"] = speech[0]
    return batch


# load all audio files
ds = ds.map(map_to_array)

# run inference on the first 5 data samples
inputs = processor(ds[:5]["speech"], sampling_rate=target_sample_rate, return_tensors="pt", padding=True)

# inference
logits = model(**inputs).logits
predicted_ids = torch.argmax(logits, axis=-1)

print(processor.batch_decode(predicted_ids))
```

