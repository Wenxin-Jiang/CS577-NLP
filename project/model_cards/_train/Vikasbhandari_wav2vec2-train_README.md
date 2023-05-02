---
language: en
datasets:
- librispeech_asr
tags:
- speech
- audio
- automatic-speech-recognition
- hf-asr-leaderboard
license: apache-2.0
model-index:
- name: wav2vec2-large-960h-lv60
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: LibriSpeech (clean)
      type: librispeech_asr
      config: clean
      split: test
      args: 
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 1.9
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: LibriSpeech (other)
      type: librispeech_asr
      config: other
      split: test
      args: 
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 3.9
---

# Wav2Vec2-Large-960h-Lv60 + Self-Training

[Facebook's Wav2Vec2](https://ai.facebook.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/)

The large model pretrained and fine-tuned on 960 hours of Libri-Light and Librispeech on 16kHz sampled speech audio. Model was trained with [Self-Training objective](https://arxiv.org/abs/2010.11430). When using the model make sure that your speech input is also sampled at 16Khz.

[Paper](https://arxiv.org/abs/2006.11477)

Authors: Alexei Baevski, Henry Zhou, Abdelrahman Mohamed, Michael Auli

**Abstract**

We show for the first time that learning powerful representations from speech audio alone followed by fine-tuning on transcribed speech can outperform the best semi-supervised methods while being conceptually simpler. wav2vec 2.0 masks the speech input in the latent space and solves a contrastive task defined over a quantization of the latent representations which are jointly learned. Experiments using all labeled data of Librispeech achieve 1.8/3.3 WER on the clean/other test sets. When lowering the amount of labeled data to one hour, wav2vec 2.0 outperforms the previous state of the art on the 100 hour subset while using 100 times less labeled data. Using just ten minutes of labeled data and pre-training on 53k hours of unlabeled data still achieves 4.8/8.2 WER. This demonstrates the feasibility of speech recognition with limited amounts of labeled data.

The original model can be found under https://github.com/pytorch/fairseq/tree/master/examples/wav2vec#wav2vec-20.


# Usage

To transcribe audio files the model can be used as a standalone acoustic model as follows:

```python
 from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
 from datasets import load_dataset
 import torch
 
 # load model and processor
 processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
 model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
     
 # load dummy dataset and read soundfiles
 ds = load_dataset("patrickvonplaten/librispeech_asr_dummy", "clean", split="validation")
 
 # tokenize
 input_values = processor(ds[0]["audio"]["array"], return_tensors="pt", padding="longest").input_values
 
 # retrieve logits
 logits = model(input_values).logits
 
 # take argmax and decode
 predicted_ids = torch.argmax(logits, dim=-1)
 transcription = processor.batch_decode(predicted_ids)
 ```
 
  ## Evaluation
 
 This code snippet shows how to evaluate **facebook/wav2vec2-large-960h-lv60-self** on LibriSpeech's "clean" and "other" test data.
 
```python
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
from jiwer import wer


librispeech_eval = load_dataset("librispeech_asr", "clean", split="test")

model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60-self").to("cuda")
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")

def map_to_pred(batch):
    inputs = processor(batch["audio"]["array"], return_tensors="pt", padding="longest")
    input_values = inputs.input_values.to("cuda")
    attention_mask = inputs.attention_mask.to("cuda")
    
    with torch.no_grad():
        logits = model(input_values, attention_mask=attention_mask).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)
    batch["transcription"] = transcription
    return batch

result = librispeech_eval.map(map_to_pred, remove_columns=["audio"])

print("WER:", wer(result["text"], result["transcription"]))
```

*Result (WER)*:

| "clean" | "other" |
|---|---|
| 1.9 | 3.9 |