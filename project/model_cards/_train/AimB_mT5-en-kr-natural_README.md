you can use this model with simpletransfomers.
```
!pip install simpletransformers
from simpletransformers.t5 import T5Model

model = T5Model("mt5", "AimB/mT5-en-kr-natural")
print(model.predict(["I feel good today"]))
print(model.predict(["우리집 고양이는 세상에서 제일 귀엽습니다"]))
```