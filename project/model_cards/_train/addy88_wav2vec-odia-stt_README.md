## Usage
The model can be used directly (without a language model) as follows:
```python
import soundfile as sf
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import argparse
def parse_transcription(wav_file):
    # load pretrained model
    processor = Wav2Vec2Processor.from_pretrained("addy88/wav2vec2-odia-stt")
    model = Wav2Vec2ForCTC.from_pretrained("addy88/wav2vec2-odia-stt")
    # load audio
    audio_input, sample_rate = sf.read(wav_file)
    # pad input values and return pt tensor
    input_values = processor(audio_input, sampling_rate=sample_rate, return_tensors="pt").input_values
    # INFERENCE
    # retrieve logits & take argmax
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    # transcribe
    transcription = processor.decode(predicted_ids[0], skip_special_tokens=True)
    print(transcription)
```