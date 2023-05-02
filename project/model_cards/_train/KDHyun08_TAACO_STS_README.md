---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- transformers
- TAACO
language: ko
---

# TAACO_Similarity

본 모델은 [Sentence-transformers](https://www.SBERT.net)를 기반으로 하며 KLUE의 STS(Sentence Textual Similarity) 데이터셋을 통해 훈련을 진행한 모델입니다.    
필자가 제작하고 있는 한국어 문장간 결속성 측정 도구인 K-TAACO(가제)의 지표 중 하나인 문장 간 의미적 결속성을 측정하기 위해 본 모델을 제작하였습니다.    
또한 모두의 말뭉치의 문장간 유사도 데이터 등 다양한 데이터를 구해 추가 훈련을 진행할 예정입니다.

## Train Data
KLUE-sts-v1.1._train.json
NLI-sts-train.tsv

## Usage (Sentence-Transformers)

본 모델을 사용하기 위해서는 [Sentence-transformers](https://www.SBERT.net)를 설치하여야 합니다.

```
pip install -U sentence-transformers
```

모델을 사용하기 위해서는 아래 코드를 참조하시길 바랍니다.

```python
from sentence_transformers import SentenceTransformer, models
sentences = ["This is an example sentence", "Each sentence is converted"]

embedding_model = models.Transformer(
    model_name_or_path="KDHyun08/TAACO_STS", 
    max_seq_length=256,
    do_lower_case=True
)

pooling_model = models.Pooling(
    embedding_model.get_word_embedding_dimension(),
    pooling_mode_mean_tokens=True,
    pooling_mode_cls_token=False,
    pooling_mode_max_tokens=False,
)
model = SentenceTransformer(modules=[embedding_model, pooling_model])

embeddings = model.encode(sentences)
print(embeddings)
```


## Usage (실제 문장 간 유사도 비교)
[Sentence-transformers](https://www.SBERT.net) 를 설치한 후 아래 내용과 같이 문장 간 유사도를 비교할 수 있습니다.   
query 변수는 비교 기준이 되는 문장(Source Sentence)이고 비교를 진행할 문장은 docs에 list 형식으로 구성하시면 됩니다.

```python
from sentence_transformers import SentenceTransformer, models

embedding_model = models.Transformer(
    model_name_or_path="KDHyun08/TAACO_STS", 
    max_seq_length=256,
    do_lower_case=True
)

pooling_model = models.Pooling(
    embedding_model.get_word_embedding_dimension(),
    pooling_mode_mean_tokens=True,
    pooling_mode_cls_token=False,
    pooling_mode_max_tokens=False,
)
model = SentenceTransformer(modules=[embedding_model, pooling_model])

docs = ['어제는 아내의 생일이었다', '생일을 맞이하여 아침을 준비하겠다고 오전 8시 30분부터 음식을 준비하였다. 주된 메뉴는 스테이크와 낙지볶음, 미역국, 잡채, 소야 등이었다', '스테이크는 자주 하는 음식이어서 자신이 준비하려고 했다', '앞뒤도 1분씩 3번 뒤집고 래스팅을 잘 하면 육즙이 가득한 스테이크가 준비되다', '아내도 그런 스테이크를 좋아한다. 그런데 상상도 못한 일이 벌이지고 말았다', '보통 시즈닝이 되지 않은 원육을 사서 스테이크를 했는데, 이번에는 시즈닝이 된 부챗살을 구입해서 했다', '그런데 케이스 안에 방부제가 들어있는 것을 인지하지 못하고 방부제와 동시에 프라이팬에 올려놓을 것이다', '그것도 인지 못한 체... 앞면을 센 불에 1분을 굽고 뒤집는 순간 방부제가 함께 구어진 것을 알았다', '아내의 생일이라 맛있게 구워보고 싶었는데 어처구니없는 상황이 발생한 것이다', '방부제가 센 불에 녹아서 그런지 물처럼 흘러내렸다', ' 고민을 했다. 방부제가 묻은 부문만 제거하고 다시 구울까 했는데 방부제에 절대 먹지 말라는 문구가 있어서 아깝지만 버리는 방향을 했다', '너무나 안타까웠다', '아침 일찍 아내가 좋아하는 스테이크를 준비하고 그것을 맛있게 먹는 아내의 모습을 보고 싶었는데 전혀 생각지도 못한 상황이 발생해서... 하지만 정신을 추스르고 바로 다른 메뉴로 변경했다', '소야, 소시지 야채볶음..', '아내가 좋아하는지 모르겠지만 냉장고 안에 있는 후랑크소세지를 보니 바로 소야를 해야겠다는 생각이 들었다. 음식은 성공적으로 완성이 되었다', '40번째를 맞이하는 아내의 생일은 성공적으로 준비가 되었다', '맛있게 먹어 준 아내에게도 감사했다', '매년 아내의 생일에 맞이하면 아침마다 생일을 차려야겠다. 오늘도 즐거운 하루가 되었으면 좋겠다', '생일이니까~']
#각 문장의 vector값 encoding
document_embeddings = model.encode(docs)

query = '생일을 맞이하여 아침을 준비하겠다고 오전 8시 30분부터 음식을 준비하였다'
query_embedding = model.encode(query)

top_k = min(10, len(docs))

# 코사인 유사도 계산 후,
cos_scores = util.pytorch_cos_sim(query_embedding, document_embeddings)[0]

# 코사인 유사도 순으로 문장 추출
top_results = torch.topk(cos_scores, k=top_k)

print(f"입력 문장: {query}")
print(f"\n<입력 문장과 유사한 {top_k} 개의 문장>\n")

for i, (score, idx) in enumerate(zip(top_results[0], top_results[1])):
    print(f"{i+1}: {docs[idx]} {'(유사도: {:.4f})'.format(score)}\n")
```



## Evaluation Results

위 Usage를 실행하게 되면 아래와 같은 결과가 도출됩니다. 1에 가까울수록 유사한 문장입니다.

```
입력 문장: 생일을 맞이하여 아침을 준비하겠다고 오전 8시 30분부터 음식을 준비하였다

<입력 문장과 유사한 10 개의 문장>

1: 생일을 맞이하여 아침을 준비하겠다고 오전 8시 30분부터 음식을 준비하였다. 주된 메뉴는 스테이크와 낙지볶음, 미역국, 잡채, 소야 등이었다 (유사도: 0.6687)

2: 매년 아내의 생일에 맞이하면 아침마다 생일을 차려야겠다. 오늘도 즐거운 하루가 되었으면 좋겠다 (유사도: 0.6468)

3: 40번째를 맞이하는 아내의 생일은 성공적으로 준비가 되었다 (유사도: 0.4647)

4: 아내의 생일이라 맛있게 구워보고 싶었는데 어처구니없는 상황이 발생한 것이다 (유사도: 0.4469)

5: 생일이니까~ (유사도: 0.4218)

6: 어제는 아내의 생일이었다 (유사도: 0.4192)

7: 아침 일찍 아내가 좋아하는 스테이크를 준비하고 그것을 맛있게 먹는 아내의 모습을 보고 싶었는데 전혀 생각지도 못한 상황이 발생해서... 하지만 정신을 추스르고 바로 다른 메뉴로 변경했다 (유사도: 0.4156)

8: 맛있게 먹어 준 아내에게도 감사했다 (유사도: 0.3093)

9: 아내가 좋아하는지 모르겠지만 냉장고 안에 있는 후랑크소세지를 보니 바로 소야를 해야겠다는 생각이 들었다. 음식은 성공적으로 완성이 되었다 (유사도: 0.2259)

10: 아내도 그런 스테이크를 좋아한다. 그런데 상상도 못한 일이 벌이지고 말았다 (유사도: 0.1967)
```


**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 142 with parameters:
```
{'batch_size': 32, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.CosineSimilarityLoss.CosineSimilarityLoss` 

Parameters of the fit()-Method:
```
{
    "epochs": 4,
    "evaluation_steps": 1000,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'transformers.optimization.AdamW'>",
    "optimizer_params": {
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 10000,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->