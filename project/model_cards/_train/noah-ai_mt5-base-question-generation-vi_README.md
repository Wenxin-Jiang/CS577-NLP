## Model description
This model is a sequence-to-sequence question generator that takes an answer and context as an input and generates a question as an output. It is based on a pre-trained mt5-base by [Google](https://github.com/google-research/multilingual-t5) model.

## Training data
The model was fine-tuned on [XQuAD](https://github.com/deepmind/xquad)

## Example usage
```python
from transformers import MT5ForConditionalGeneration, AutoTokenizer
import torch

model = MT5ForConditionalGeneration.from_pretrained("noah-ai/mt5-base-question-generation-vi")
tokenizer = AutoTokenizer.from_pretrained("noah-ai/mt5-base-question-generation-vi")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# Content used to create a set of questions
context = '''Thành phố Hồ Chí Minh (còn gọi là Sài Gòn) tên gọi cũ trước 1975 là Sài Gòn hay Sài Gòn-Gia Định là thành phố lớn nhất ở Việt Nam về dân số và quy mô đô thị hóa. Đây còn là trung tâm kinh tế, chính trị, văn hóa và giáo dục tại Việt Nam. Thành phố Hồ Chí Minh là thành phố trực thuộc trung ương thuộc loại đô thị đặc biệt của Việt Nam cùng với thủ đô Hà Nội.Nằm trong vùng chuyển tiếp giữa Đông Nam Bộ và Tây Nam Bộ, thành phố này hiện có 16 quận, 1 thành phố và 5 huyện, tổng diện tích 2.061 km². Theo kết quả điều tra dân số chính thức vào thời điểm ngày một tháng 4 năm 2009 thì dân số thành phố là 7.162.864 người (chiếm 8,34% dân số Việt Nam), mật độ dân số trung bình 3.419 người/km². Đến năm 2019, dân số thành phố tăng lên 8.993.082 người và cũng là nơi có mật độ dân số cao nhất Việt Nam. Tuy nhiên, nếu tính những người cư trú không đăng ký hộ khẩu thì dân số thực tế của thành phố này năm 2018 là gần 14 triệu người.'''

encoding = tokenizer.encode_plus(context, return_tensors="pt")

input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)

output = model.generate(input_ids=input_ids, attention_mask=attention_masks, max_length=256)

question =  tokenizer.decode(output[0], skip_special_tokens=True,clean_up_tokenization_spaces=True)

question
#question: Thành phố hồ chí minh có bao nhiêu quận?
```

> Created by [Duong Thanh Nguyen](https://www.facebook.com/thanhnguyen.dev)