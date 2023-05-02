---
language: es
license: apache-2.0
datasets:
- common_voice
- mozilla-foundation/common_voice_6_0
metrics:
- wer
- cer
tags:
- audio
- automatic-speech-recognition
- es
- hf-asr-leaderboard
- mozilla-foundation/common_voice_6_0
- robust-speech-event
- speech
- xlsr-fine-tuning-week
model-index:
- name: XLSR Wav2Vec2 Spanish by Jonatas Grosman
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice es
      type: common_voice
      args: es
    metrics:
    - name: Test WER
      type: wer
      value: 8.82
    - name: Test CER
      type: cer
      value: 2.58
    - name: Test WER (+LM)
      type: wer
      value: 6.27
    - name: Test CER (+LM)
      type: cer
      value: 2.06
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: es
    metrics:
    - name: Dev WER
      type: wer
      value: 30.19
    - name: Dev CER
      type: cer
      value: 13.56
    - name: Dev WER (+LM)
      type: wer
      value: 24.71
    - name: Dev CER (+LM)
      type: cer
      value: 12.61
---

# Wav2Vec2-Large-XLSR-53-Spanish

Added custom language model to https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-spanish

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on Spanish using the [Common Voice](https://huggingface.co/datasets/common_voice).
When using this model, make sure that your speech input is sampled at 16kHz.

This model has been fine-tuned thanks to the GPU credits generously given by the [OVHcloud](https://www.ovhcloud.com/en/public-cloud/ai-training/) :)

The script used for training can be found here: https://github.com/jonatasgrosman/wav2vec2-sprint

## Usage

The model can be used directly (without a language model) as follows...

Using the [ASRecognition](https://github.com/jonatasgrosman/asrecognition) library:

```python
from asrecognition import ASREngine

asr = ASREngine("es", model_path="jonatasgrosman/wav2vec2-large-xlsr-53-spanish")

audio_paths = ["/path/to/file.mp3", "/path/to/another_file.wav"]
transcriptions = asr.transcribe(audio_paths)
```

Writing your own inference script:

```python
import torch
import librosa
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

LANG_ID = "es"
MODEL_ID = "jonatasgrosman/wav2vec2-large-xlsr-53-spanish"
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

for i, predicted_sentence in enumerate(predicted_sentences):
    print("-" * 100)
    print("Reference:", test_dataset[i]["sentence"])
    print("Prediction:", predicted_sentence)
```

| Reference  | Prediction |
| ------------- | ------------- |
| HABITA EN AGUAS POCO PROFUNDAS Y ROCOSAS. | HABITAN AGUAS POCO PROFUNDAS Y ROCOSAS |
| OPERA PRINCIPALMENTE VUELOS DE CABOTAJE Y REGIONALES DE CARGA. | OPERA PRINCIPALMENTE VUELO DE CARBOTAJES Y REGIONALES DE CARGAN |
| PARA VISITAR CONTACTAR PRIMERO CON LA DIRECCIÓN. | PARA VISITAR CONTACTAR PRIMERO CON LA DIRECCIÓN |
| TRES | TRES |
| REALIZÓ LOS ESTUDIOS PRIMARIOS EN FRANCIA, PARA CONTINUAR LUEGO EN ESPAÑA. | REALIZÓ LOS ESTUDIOS PRIMARIOS EN FRANCIA PARA CONTINUAR LUEGO EN ESPAÑA |
| EN LOS AÑOS QUE SIGUIERON, ESTE TRABAJO ESPARTA PRODUJO DOCENAS DE BUENOS JUGADORES. | EN LOS AÑOS QUE SIGUIERON ESTE TRABAJO ESPARTA PRODUJO DOCENA DE BUENOS JUGADORES |
| SE ESTÁ TRATANDO DE RECUPERAR SU CULTIVO EN LAS ISLAS CANARIAS. | SE ESTÓ TRATANDO DE RECUPERAR SU CULTIVO EN LAS ISLAS CANARIAS |
| SÍ | SÍ |
| "FUE ""SACADA"" DE LA SERIE EN EL EPISODIO ""LEAD"", EN QUE ALEXANDRA CABOT REGRESÓ." | FUE SACADA DE LA SERIE EN EL EPISODIO LEED EN QUE ALEXANDRA KAOT REGRESÓ |
| SE UBICAN ESPECÍFICAMENTE EN EL VALLE DE MOKA, EN LA PROVINCIA DE BIOKO SUR. | SE UBICAN ESPECÍFICAMENTE EN EL VALLE DE MOCA EN LA PROVINCIA DE PÍOCOSUR |

## Evaluation

1. To evaluate on `mozilla-foundation/common_voice_6_0` with split `test`

```bash
python eval.py --model_id jonatasgrosman/wav2vec2-large-xlsr-53-spanish --dataset mozilla-foundation/common_voice_6_0 --config es --split test
```

2. To evaluate on `speech-recognition-community-v2/dev_data`

```bash
python eval.py --model_id jonatasgrosman/wav2vec2-large-xlsr-53-spanish --dataset speech-recognition-community-v2/dev_data --config es --split validation --chunk_length_s 5.0 --stride_length_s 1.0
```

## Citation
If you want to cite this model you can use this:

```bibtex
@misc{grosman2021wav2vec2-large-xlsr-53-spanish,
  title={XLSR Wav2Vec2 Spanish by Jonatas Grosman},
  author={Grosman, Jonatas},
  publisher={Hugging Face},
  journal={Hugging Face Hub},
  howpublished={\url{https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-spanish}},
  year={2021}
}
```