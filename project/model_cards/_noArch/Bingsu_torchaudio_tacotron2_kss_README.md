---
language: ko
tags:
  - text-to-speech
license: other
---

# Torchaudio_Tacotron2_kss

torchaudio [Tacotron2](https://pytorch.org/audio/stable/generated/torchaudio.models.Tacotron2.html#torchaudio.models.Tacotron2) model, trained on kss dataset.

## License

- code: MIT License
- `pytorch_model.bin` weights: CC BY-NC-SA 4.0 (license of the kss dataset)

## Requirements

```sh
pip install torch torchaudio transformers phonemizer
```

and you have to install [`espeak-ng`](https://github.com/espeak-ng/espeak-ng)

If you are using Windows, you need to set additional environment variables. see: <https://github.com/bootphon/phonemizer/issues/44>

## Usage

```python
import torch
from transformers import AutoModel, AutoTokenizer

repo = "Bingsu/torchaudio_tacotron2_kss"
model = AutoModel.from_pretrained(
    repo,
    trust_remote_code=True,
    revision="589d6557e8b4bb347f49de74270541063ba9c2bc"
    )
tokenizer = AutoTokenizer.from_pretrained(repo)
model.eval()
```

```python
vocoder = torch.hub.load("seungwonpark/melgan:aca59909f6dd028ec808f987b154535a7ca3400c", "melgan", trust_repo=True, pretrained=False)
url = "https://huggingface.co/Bingsu/torchaudio_tacotron2_kss/resolve/main/melgan.pt"
state_dict = torch.hub.load_state_dict_from_url(url)
vocoder.load_state_dict(state_dict)
```

vocoder is same as original [seungwonpark/melgan](https://github.com/seungwonpark/melgan), but the weights are on the cuda, so I brought them separately.

```python
text = "반갑습니다 타코트론2입니다."
inp = tokenizer(text, return_tensors="pt", return_length=True, return_attention_mask=False)
```

```python
with torch.inference_mode():
    out = model(**inp)
    audio = vocoder(out[0])
```

```python
import IPython.display as ipd

ipd.Audio(audio[0].numpy(), rate=22050)
```

<audio src="https://huggingface.co/Bingsu/torchaudio_tacotron2_kss/resolve/main/examples/sample1.wav" controls>
