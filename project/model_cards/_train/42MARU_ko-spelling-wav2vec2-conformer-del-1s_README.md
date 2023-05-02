---
language:
- ko  # Example: fr
license: apache-2.0  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: transformers  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
tags:
- audio
- automatic-speech-recognition
datasets:
- KsponSpeech
metrics:
- wer  # Example: wer. Use metric id from https://hf.co/metrics
---

# ko-spelling-wav2vec2-conformer-del-1s

## Table of Contents
- [ko-spelling-wav2vec2-conformer-del-1s](#ko-spelling-wav2vec2-conformer-del-1s)
  - [Table of Contents](#table-of-contents)
  - [Model Details](#model-details)
  - [Evaluation](#evaluation)
  - [How to Get Started With the Model](#how-to-get-started-with-the-model)

## Model Details
- **Model Description:**
해당 모델은 wav2vec2-conformer base architecture에 scratch pre-training 되었습니다. <br />
Wav2Vec2ConformerForCTC를 이용하여 KsponSpeech에 대한 Fine-Tuning 모델입니다. <br />

- Dataset use [AIHub KsponSpeech](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=123) <br />
Datasets는 해당 Data를 전처리하여 임의로 만들어 사용하였습니다. <br />
del-1s의 의미는 1초 이하의 데이터 필터링을 의미합니다. <br />
해당 모델은 **철자전사** 기준의 데이터로 학습된 모델입니다. (숫자와 영어는 각 표기법을 따름) <br />

- **Developed by:**  TADev (@lIlBrother, @ddobokki, @jp42maru)
- **Language(s):** Korean
- **License:** apache-2.0
- **Parent Model:** See the [wav2vec2-conformer](https://huggingface.co/docs/transformers/model_doc/wav2vec2-conformer) for more information about the pre-trained base model. (해당 모델은 wav2vec2-conformer base architecture에 scratch pre-training 되었습니다.)

## Evaluation
Just using `load_metric("wer")` and `load_metric("wer")` in huggingface `datasets` library <br />

## How to Get Started With the Model
KenLM과 혼용된 Wav2Vec2ProcessorWithLM 예제를 보시려면 [42maru-kenlm 예제](https://huggingface.co/42MARU/ko-ctc-kenlm-spelling-only-wiki)를 참고하세요
```python
import librosa
from pyctcdecode import build_ctcdecoder
from transformers import (
    AutoConfig,
    AutoFeatureExtractor,
    AutoModelForCTC,
    AutoTokenizer,
    Wav2Vec2ProcessorWithLM,
)
from transformers.pipelines import AutomaticSpeechRecognitionPipeline

audio_path = ""

# 모델과 토크나이저, 예측을 위한 각 모듈들을 불러옵니다.
model = AutoModelForCTC.from_pretrained("42MARU/ko-spelling-wav2vec2-conformer-del-1s")
feature_extractor = AutoFeatureExtractor.from_pretrained("42MARU/ko-spelling-wav2vec2-conformer-del-1s")
tokenizer = AutoTokenizer.from_pretrained("42MARU/ko-spelling-wav2vec2-conformer-del-1s")
beamsearch_decoder = build_ctcdecoder(
    labels=list(tokenizer.encoder.keys()),
    kenlm_model_path=None,
)
processor = Wav2Vec2ProcessorWithLM(
    feature_extractor=feature_extractor, tokenizer=tokenizer, decoder=beamsearch_decoder
)

# 실제 예측을 위한 파이프라인에 정의된 모듈들을 삽입.
asr_pipeline = AutomaticSpeechRecognitionPipeline(
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    decoder=processor.decoder,
    device=-1,
)

# 음성파일을 불러오고 beamsearch 파라미터를 특정하여 예측을 수행합니다.
raw_data, _ = librosa.load(audio_path, sr=16000)
kwargs = {"decoder_kwargs": {"beam_width": 100}}
pred = asr_pipeline(inputs=raw_data, **kwargs)["text"]
# 모델이 자소 분리 유니코드 텍스트로 나오므로, 일반 String으로 변환해줄 필요가 있습니다.
result = unicodedata.normalize("NFC", pred)
print(result)
# 안녕하세요 123 테스트입니다.
```
*Beam-100 Result (WER)*:
| "clean" | "other" |
| ------- | ------- |
| 22.01   | 27.34   |