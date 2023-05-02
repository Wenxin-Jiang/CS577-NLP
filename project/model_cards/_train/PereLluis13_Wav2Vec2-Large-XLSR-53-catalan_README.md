---
language: ca
datasets:
- common_voice
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: Catalan XLSR Wav2Vec Large 53 #TODO: replace {human_readable_name} with a name of your model as it should appear on the leaderboard. It could be something like `Elgeish XLSR Wav2Vec2 Large 53`
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice ca 
      type: common_voice
      args: ca #TODO: 
    metrics:
       - name: Test WER
         type: wer
         value: 8.11 
---
# Disclaimer

This model was trained on Common Voice 6, if you need a catalan model for ASR, I recommend checking [wav2vec2-xls-r-1b-ca-lm](https://huggingface.co/PereLluis13/wav2vec2-xls-r-1b-ca-lm) which is a 1b model with a LM on top trained on CV8+ with much better performance or [wav2vec2-xls-r-300m-ca-lm](https://huggingface.co/PereLluis13/wav2vec2-xls-r-300m-ca-lm) which has the same size (300m) as this model but trained on CV8+ and the same LM.

# Wav2Vec2-Large-XLSR-53-ca 

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on catalan using the [Common Voice](https://huggingface.co/datasets/common_voice) dataset.
When using this model, make sure that your speech input is sampled at 16kHz.

## Usage

The model can be used directly (without a language model) as follows:

```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

test_dataset = load_dataset("common_voice", "ca", split="test[:2%]") 

processor = Wav2Vec2Processor.from_pretrained("PereLluis13/Wav2Vec2-Large-XLSR-53-catalan")
model = Wav2Vec2ForCTC.from_pretrained("PereLluis13/Wav2Vec2-Large-XLSR-53-catalan")

resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = resampler(speech_array).squeeze().numpy()
    return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)
inputs = processor(test_dataset["speech"][:2], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():
    logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

predicted_ids = torch.argmax(logits, dim=-1)

print("Prediction:", processor.batch_decode(predicted_ids))
print("Reference:", test_dataset["sentence"][:2])
```


## Evaluation

The model can be evaluated as follows on the catalan test data of Common Voice.

```python
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re

test_dataset = load_dataset("common_voice", "ca", split="test") 
wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("PereLluis13/Wav2Vec2-Large-XLSR-53-catalan") 
model = Wav2Vec2ForCTC.from_pretrained("PereLluis13/Wav2Vec2-Large-XLSR-53-catalan") 
model.to("cuda")

chars_to_ignore_regex = '[\,\?\.\!\;\:\"\“]'
resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = resampler(speech_array).squeeze().numpy()
    return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def evaluate(batch):
    inputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

    with torch.no_grad():
        logits = model(inputs.input_values.to("cuda"), attention_mask=inputs.attention_mask.to("cuda")).logits

    pred_ids = torch.argmax(logits, dim=-1)
    batch["pred_strings"] = processor.batch_decode(pred_ids)
    return batch

result = test_dataset.map(evaluate, batched=True, batch_size=8)
import jiwer

# Chunk WER computation due to memory issues, taken from https://huggingface.co/pcuenq/wav2vec2-large-xlsr-53-es
def chunked_wer(targets, predictions, chunk_size=None):                                          
    if chunk_size is None: return jiwer.wer(targets, predictions)                                
    start = 0                                                                                    
    end = chunk_size                                                                             
    H, S, D, I = 0, 0, 0, 0                                                                      
    while start < len(targets):                                                                  
        chunk_metrics = jiwer.compute_measures(targets[start:end], predictions[start:end])       
        H = H + chunk_metrics["hits"]                                                            
        S = S + chunk_metrics["substitutions"]                                                   
        D = D + chunk_metrics["deletions"]                                                       
        I = I + chunk_metrics["insertions"]                                                      
        start += chunk_size                                                                      
        end += chunk_size                                                                        
    return float(S + D + I) / float(H + S + D)

print("WER: {:2f}".format(100 * chunked_wer(result["sentence"], result["pred_strings"], chunk_size=4000)))
```

**Test Result**: 8.11 %

## Training

The Common Voice `train`, `validation` datasets were used for training. At the second epoch training was halted due to a memory issue, and was continued with lower batch size, but acc. gradient steps were scaled to keep it at 32 batch size during all training. Then the model was trained for an additional 10 epochs where half the male samples were pitched up.

The script used for training can be found [here](https://github.com/huggingface/transformers/blob/master/examples/research_projects/wav2vec2/run_common_voice.py). Slight modifications were done in order to speed up the ordering by length during training, which can be found [here](https://discuss.huggingface.co/t/spanish-asr-fine-tuning-wav2vec2/4586/6). Another version trained for catalan can be found [here](https://huggingface.co/ccoreilly/wav2vec2-large-xlsr-catala), which may be better than this one since it was trained with extra data and for longer time. Whoever, since it used different splits that include part of the Common Voice test set, this version can be used to get a baseline on the Common Voice dataset.