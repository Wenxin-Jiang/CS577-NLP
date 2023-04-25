---
language:
  - ko
tags:
- summarization
widget:
- text: "[BOS]밥 ㄱ?[SEP]고고고고 뭐 먹을까?[SEP]어제 김치찌개 먹어서 한식말고 딴 거[SEP]그럼 돈까스 어때?[SEP]오 좋다 1시 학관 앞으로 오셈[SEP]ㅇㅋ[EOS]"
inference:
  parameters:
    max_length: 64
    top_k: 5
---

# BART R3F

[2021 훈민정음 한국어 음성•자연어 인공지능 경진대회] 대화요약 부문 알라꿍달라꿍 팀의 대화요약 학습 샘플 모델을 공유합니다.

[bart-pretrained](https://huggingface.co/alaggung/bart-pretrained) 모델에 [2021-dialogue-summary-competition](https://github.com/cosmoquester/2021-dialogue-summary-competition) 레포지토리의 R3F를 적용해 대화요약 Task를 학습한 모델입니다.

데이터는 [AIHub 한국어 대화요약](https://aihub.or.kr/aidata/30714) 데이터를 사용하였습니다.