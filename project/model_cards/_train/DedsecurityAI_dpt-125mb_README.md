---
license: mit
---

# How to use
```python
from transformers import pipeline
generator = pipeline('text-generation', model="DedsecurityAI/dpt-125mb")
generator("Hello Simon")
[{'generated_text': 'Hello Simon :) Welcome aboard aboard :) :) :) :) :) :) :) :) :) :) :) :) :) :)'}]

```