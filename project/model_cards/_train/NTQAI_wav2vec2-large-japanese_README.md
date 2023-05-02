---
language: ja
datasets:
- common_voice
metrics:
- wer
- cer
tags:
- audio
- automatic-speech-recognition
- speech

model-index:
- name: Wav2Vec2 Japanese by NTQAI
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice ja
      type: common_voice
      args: ja
    metrics:
       - name: Test WER
         type: wer
         value: 81.3
       - name: Test CER
         type: cer
         value: 21.9
---
# Wav2Vec2-Large-Japanese
Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on Japanese using the [Common Voice](https://huggingface.co/datasets/common_voice), [JSUT](https://sites.google.com/site/shinnosuketakamichi/publication/jsut), [TEDxJP](https://github.com/laboroai/TEDxJP-10K) and some other data. This model is a model trained on public data. If you want to use trained model with more 600 hours of data and higher accuracy please contact nha282@gmail.com

When using this model, make sure that your speech input is sampled at 16kHz.

## Usage
The model can be used directly (without a language model) as follows:
```python
import torch
import librosa
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
LANG_ID = "ja"
MODEL_ID = "NTQAI/wav2vec2-large-japanese"
SAMPLES = 3
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
for i, predicted_sentence in enumerate(predicted_sentences):
    print("-" * 100)
    print("Reference:", test_dataset[i]["sentence"])
    print("Prediction:", predicted_sentence)
```
| Reference  | Prediction |
| ------------- | ------------- |
| 祖母は、おおむね機嫌よく、サイコロをころがしている。 | 祖母思い切れを最布ロぼがしている |
| 財布をなくしたので、交番へ行きます。 | 財布をなく時間ので交番でへ行きます |
| 飲み屋のおやじ、旅館の主人、医者をはじめ、交際のある人にきいてまわったら、みんな、私より収入が多いはずなのに、税金は安い。 | ロみ屋のおやし旅館の主人に医をはめ交載のあの人に聞いて回ったらみんな私より収入が多い発ずなのに請金は安い |

## Evaluation
The model can be evaluated as follows on the Japanese test data of Common Voice.
```python
import torch
import re
import librosa
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
LANG_ID = "ja"
MODEL_ID = "NTQAI/wav2vec2-large-japanese"
DEVICE = "cuda"
CHARS_TO_IGNORE = [",", "?", "¿", ".", "!", "¡", ";", "；", ":", '""', "%", '"', "�", "ʿ", "·", "჻", "~", "՞",
                   "؟", "،", "।", "॥", "«", "»", "„", "“", "”", "「", "」", "‘", "’", "《", "》", "(", ")", "[", "]",
                   "{", "}", "=", "`", "_", "+", "<", ">", "…", "–", "°", "´", "ʾ", "‹", "›", "©", "®", "—", "→", "。",
                   "、", "﹂", "﹁", "‧", "～", "﹏", "，", "｛", "｝", "（", "）", "［", "］", "【", "】", "‥", "〽",
                   "『", "』", "〝", "〟", "⟨", "⟩", "〜", "：", "！", "？", "♪", "؛", "/", "\\", "º", "−", "^", "'", "ʻ", "ˆ"]
test_dataset = load_dataset("common_voice", LANG_ID, split="test")
wer = load_metric("wer.py") # https://github.com/jonatasgrosman/wav2vec2-sprint/blob/main/wer.py
cer = load_metric("cer.py") # https://github.com/jonatasgrosman/wav2vec2-sprint/blob/main/cer.py
chars_to_ignore_regex = f"[{re.escape(''.join(CHARS_TO_IGNORE))}]"
processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)
model.to(DEVICE)
# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        speech_array, sampling_rate = librosa.load(batch["path"], sr=16_000)
    batch["speech"] = speech_array
    batch["sentence"] = re.sub(chars_to_ignore_regex, "", batch["sentence"]).upper()
    return batch
test_dataset = test_dataset.map(speech_file_to_array_fn)
# Preprocessing the datasets.
# We need to read the audio files as arrays
def evaluate(batch):
    inputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = model(inputs.input_values.to(DEVICE), attention_mask=inputs.attention_mask.to(DEVICE)).logits
    pred_ids = torch.argmax(logits, dim=-1)
    batch["pred_strings"] = processor.batch_decode(pred_ids)
    return batch
result = test_dataset.map(evaluate, batched=True, batch_size=8)
predictions = [x.upper() for x in result["pred_strings"]]
references = [x.upper() for x in result["sentence"]]
print(f"WER: {wer.compute(predictions=predictions, references=references, chunk_size=1000) * 100}")
print(f"CER: {cer.compute(predictions=predictions, references=references, chunk_size=1000) * 100}")
```

**Test Result**:

| Model | WER | CER |
| ------------- | ------------- | ------------- |
| NTQAI/wav2vec2-large-japanese | **73.10%** | **18.15%** |
| vumichien/wav2vec2-large-xlsr-japanese | 1108.86% | 23.40% |
| qqhann/w2v_hf_jsut_xlsr53 | 1012.18% | 70.77% |
