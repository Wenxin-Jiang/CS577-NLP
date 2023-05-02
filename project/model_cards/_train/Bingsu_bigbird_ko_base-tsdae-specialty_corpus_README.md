---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
widget:
  source_sentence: "수치 해석 프로그램은 여러 가지 환경 변수를 입력해야 하므로 일반인이 사용하기에는 많은 어려움이 있다."
  sentences:
    - "이러한 해석방법은 매우 복잡한 것이어서 수치 해석 프로그램이 필수적 이다."
    - "계층구조 셀룰라 시스템을 구성하고 제안된 기법을 적용하면 어느 곳에 위치한 사용자에게나 양질의 서비스를 효율적으로 제공할 수 있음을 확인하였다."
    - "허깅페이스에 한국어 모델이 더 많아졌으면 좋겠다."
language: ko
license: mit

---

# Bingsu/bigbird_ko_base-tsdae-specialty_corpus

[sentence-transformers](https://www.SBERT.net)로 학습된 bigbird 모델: 입력 문장을 256벡터로 변환합니다.

[Aihub 전문분야 말뭉치](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=110)에 대해
[TSDAE](https://www.sbert.net/examples/unsupervised_learning/TSDAE/README.html)로 학습되었습니다.

<!--- Describe your model here -->

## Usage (Sentence-Transformers)

사용 전에 [sentence-transformers](https://www.SBERT.net)를 설치하세요.

```sh
pip install -U sentence-transformers
```
또는
```sh
conda install -c conda-forge sentence-transformers
```

사용 예제:

```python
from sentence_transformers import util

sent = [
    "본 논문은 디지털 신호처리용 VLSI의 자동설계를 위한 SODAS-DSP(SOgang Design Automation System-DSP) 시스템의 설계와 개발 결과에 대하여 기술한다",
    "본 논문에서는 DD-Gardner방식의 타이밍 검출기 성능을 고찰한다.",
    "이러한 해석방법은 매우 복잡한 것이어서 수치 해석 프로그램이 필수적 이다.",
    "수치 해석 프로그램은 여러 가지 환경 변수를 입력해야 하므로 일반인이 사용하기에는 많은 어려움이 있다.",
    "또 산란과 투과에 대한 고주파 근사식도 얻어진다.",
    "그리고 슬릿간의 간격의 변화에 의해서 빔폭(beamwidth)을 조절할 수 있음을 보여준다.",
    "오늘 점심은 짜장면이다.",
    "오늘 저녁은 김밥천국이다."
]


paraphrases = util.paraphrase_mining(model, sent)

for paraphrase in paraphrases[:5]:
    score, i, j = paraphrase
    print("{} \t\t {} \t\t Score: {:.4f}".format(sent[i], sent[j], score))
```
```
이러한 해석방법은 매우 복잡한 것이어서 수치 해석 프로그램이 필수적 이다. 		 수치 해석 프로그램은 여러 가지 환경 변수를 입력해야 하므로 일반인이 사용하기에는 많은 어려움이 있다. 		 Score: 0.8990
오늘 점심은 짜장면이다. 		 오늘 저녁은 김밥천국이다. 		 Score: 0.8945
수치 해석 프로그램은 여러 가지 환경 변수를 입력해야 하므로 일반인이 사용하기에는 많은 어려움이 있다. 		 오늘 저녁은 김밥천국이다. 		 Score: 0.8901
본 논문은 디지털 신호처리용 VLSI의 자동설계를 위한 SODAS-DSP(SOgang Design Automation System-DSP) 시스템의 설계와 개발 결과에 대하여 기술한다 		 본 논문에서는 DD-Gardner방식의 타이밍 검출기 성능을 고찰한다. 		 Score: 0.8894
본 논문은 디지털 신호처리용 VLSI의 자동설계를 위한 SODAS-DSP(SOgang Design Automation System-DSP) 시스템의 설계와 개발 결과에 대하여 기술한다 		 그리고 슬릿간의 간격의 변화에 의해서 빔폭(beamwidth)을 조절할 수 있음을 보여준다. 		 Score: 0.8889
```




## Usage (HuggingFace Transformers)
Without [sentence-transformers](https://www.SBERT.net), you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.

```python
from transformers import AutoTokenizer, AutoModel
import torch


def cls_pooling(model_output, attention_mask):
    return model_output[0][:,0]


# Sentences we want sentence embeddings for
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('Bingsu/bigbird_ko_base-tsdae-specialty_corpus')
model = AutoModel.from_pretrained('Bingsu/bigbird_ko_base-tsdae-specialty_corpus')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, cls pooling.
sentence_embeddings = cls_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)
```



## Evaluation Results

<!--- Describe how your model was evaluated -->

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name=Bingsu/bigbird_ko_base-tsdae-specialty_corpus)


## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 183287 with parameters:
```
{'batch_size': 8, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.DenoisingAutoEncoderLoss.DenoisingAutoEncoderLoss` 

Parameters of the fit()-Method:
```
{
    "epochs": 2,
    "evaluation_steps": 10000,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'bitsandbytes.optim.adamw.AdamW8bit'>",
    "optimizer_params": {
        "lr": 3e-05
    },
    "scheduler": "warmupcosinewithhardrestarts",
    "steps_per_epoch": null,
    "warmup_steps": 10000,
    "weight_decay": 0.005
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 1024, 'do_lower_case': False}) with Transformer model: BigBirdModel 
  (1): Pooling({'word_embedding_dimension': 256, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->