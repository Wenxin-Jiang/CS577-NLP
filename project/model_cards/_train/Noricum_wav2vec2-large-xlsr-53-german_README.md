# Wav2vec2 German Model
 
 This model has been fine-tuned on the wav2vec-large-xlsr-53 with the German CommonVoice dataset.
 
 It achieves a 11.26 WER on the full test dataset.
 It was basically trained with the code provided by [Max Idahl](https://huggingface.co/maxidl/wav2vec2-large-xlsr-german) with small adjustments in data preprocessing and on training parameters.
 
 You can use it to transcribe your own files by the following code. Please note, that your input file must be *.wav, encoded in 16 kHz and be single channel. To convert an audio file using ffmpeg use: "ffmpeg -i input.wav -ar 16000 -ac 1 output.wav". The transcribe process is very memory consuming (around 10GB per 10 seconds). If the script ends with "Killed" it means the Python interpreter ran out of memory. In this case, try with a shorter audio file.
 
```python
# !pip3 install transformers torch soundfile
import soundfile as sf
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

# load pretrained model
tokenizer = Wav2Vec2Tokenizer.from_pretrained("Noricum/wav2vec2-large-xlsr-53-german")
model = Wav2Vec2ForCTC.from_pretrained("Noricum/wav2vec2-large-xlsr-53-german")

#load audio
audio_input, _ = sf.read("/path/to/your/audio.wav")

# transcribe
input_values = tokenizer(audio_input, return_tensors="pt").input_values
logits = model(input_values).logits
predicted_ids = torch.argmax(logits, dim=-1)
transcription = tokenizer.batch_decode(predicted_ids)[0]
print(str(transcription))
```

To evaluate the model on the full CommonVoice test dataset, run this script:

```python
import re
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

test_dataset = load_dataset("common_voice", "de", split="test") # use "test[:1%]" for 1% sample
wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("Noricum/wav2vec2-large-xlsr-53-german")
model = Wav2Vec2ForCTC.from_pretrained("Noricum/wav2vec2-large-xlsr-53-german")
model.to("cuda")

chars_to_ignore_regex = '[\\\\,\\\\?\\\\.\\\\!\\\\-\\\\;\\\\:\\\\"\\\\“]'
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
# We need to read the audio files as arrays
def evaluate(batch):
    inputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

    with torch.no_grad():
        logits = model(inputs.input_values.to("cuda"), attention_mask=inputs.attention_mask.to("cuda")).logits

    pred_ids = torch.argmax(logits, dim=-1)
    batch["pred_strings"] = processor.batch_decode(pred_ids)
    return batch

result = test_dataset.map(evaluate, batched=True, batch_size=4) # batch_size=8 -> requires ~14.5GB GPU memory

# Chunked version, see https://discuss.huggingface.co/t/spanish-asr-fine-tuning-wav2vec2/4586/5:
import jiwer

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

print("Total (chunk_size=1000), WER: {:2f}".format(100 * chunked_wer(result["pred_strings"], result["sentence"], chunk_size=1000)))
```

Output: Total (chunk_size=1000), WER: 11.256522
