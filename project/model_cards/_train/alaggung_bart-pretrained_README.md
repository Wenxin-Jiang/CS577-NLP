---
language:
  - ko
widget:
- text: "[BOS]뭐 해?[SEP][MASK]하다가 이제 [MASK]려고[EOS]"
inference:
  parameters:
    max_length: 64
---

# BART Pretrained

[2021 훈민정음 한국어 음성•자연어 인공지능 경진대회] 대화요약 부문 알라꿍달라꿍 팀의 대화요약 학습 샘플 모델을 공유합니다.

[2021-dialogue-summary-competition](https://github.com/cosmoquester/2021-dialogue-summary-competition) 레포지토리의 BART Pretrain 단계를 학습한 모델입니다.

데이터는 [AIHub 한국어 대화요약](https://aihub.or.kr/aidata/30714) 데이터를 사용하였습니다.