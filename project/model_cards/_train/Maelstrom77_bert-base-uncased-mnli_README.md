```
for i in range(len(predictions)):
  if predictions[i] == 0:
    predictions[i] = 2
  elif predictions[i] == 1:
    predictions[i] = 0
  elif predictions[i] == 2:
    predictions[i] = 1
```