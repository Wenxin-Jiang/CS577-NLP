---
language:
- ko  # Example: fr
license: apache-2.0  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: kenlm  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
tags:
- audio
- automatic-speech-recognition
- text2text-generation
datasets:
- korean-wiki
---
# ko-ctc-kenlm-spelling-only-wiki
## Table of Contents
- [ko-ctc-kenlm-spelling-only-wiki](#ko-ctc-kenlm-spelling-only-wiki)
  - [Table of Contents](#table-of-contents)
  - [Model Details](#model-details)
  - [How to Get Started With the Model](#how-to-get-started-with-the-model)
## Model Details
- **Model Description** <br />
  - 음향 모델을 위한 N-gram Base의 LM으로 자소별 단어기반으로 만들어졌으며, KenLM으로 학습되었습니다. 해당 모델은 [ko-spelling-wav2vec2-conformer-del-1s](https://huggingface.co/42MARU/ko-spelling-wav2vec2-conformer-del-1s)과 사용하십시오. <br />
  - HuggingFace Transformers Style로 불러와 사용할 수 있도록 처리했습니다. <br />
  - pyctcdecode lib을 이용해서도 바로 사용가능합니다. <br />
  - data는 wiki korean을 사용했습니다. <br />
  spelling vocab data에 없는 문장은 전부 제거하여, 오히려 LM으로 Outlier가 발생할 소요를 최소화 시켰습니다. <br />
  해당 모델은 **철자전사** 기준의 데이터로 학습된 모델입니다. (숫자와 영어는 각 표기법을 따름) <br />
- **Developed by:**  TADev (@lIlBrother)
- **Language(s):** Korean
- **License:** apache-2.0

## How to Get Started With the Model
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
processor = Wav2Vec2ProcessorWithLM("42MARU/ko-ctc-kenlm-spelling-only-wiki")

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
