# T5-SMALL-SUMMARIZATION :Pretraining Text-To-Text Transfer Transformer for Vietnamese Text Summarization

#### Example Using

``` bash
import torch

from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
if torch.cuda.is_available():       
    device = torch.device("cuda")

    print('There are %d GPU(s) available.' % torch.cuda.device_count())

    print('We will use the GPU:', torch.cuda.get_device_name(0))
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")

model = T5ForConditionalGeneration.from_pretrained("NlpHUST/t5-small-vi-summarization")
tokenizer = T5Tokenizer.from_pretrained("NlpHUST/t5-small-vi-summarization")
model.to(device)

src = "Theo BHXH Việt Nam, nhiều doanh nghiệp vẫn chỉ đóng BHXH cho người lao động theo mức lương. \\\\
Dù quy định từ 1/1/2018, tiền lương tháng đóng BHXH gồm mức lương và thêm khoản bổ sung khác. \\\\
BHXH Việt Nam vừa có báo cáo về tình hình thực hiện chính sách BHXH thời gian qua. \\\\
Theo đó, tình trạng nợ, trốn đóng BHXH, BHTN vẫn xảy ra ở hầu hết các tỉnh, thành. \\\\
Thống kê tới ngày 31/12/2020, tổng số nợ BHXH, BHYT, BHTN là hơn 13.500 tỷ đồng, \\\\
chiếm 3,35 % số phải thu, trong đó: Số nợ BHXH bắt buộc là hơn 8.600 tỷ đồng, \\\\
nợ BHTN là 335 tỷ đồng. Liên quan tới tiền lương đóng BHXH, báo cáo của \\\\
BHXH Việt Nam cho thấy: Nhiều doanh nghiệp vẫn chủ yếu xây dựng thang, \\\\
bảng lương để đóng BHXH bằng mức thấp nhất. Tức là bằng mức lương tối \\\\
thiểu vùng, cộng thêm 7 % đối với lao động đã qua đào tạo nghề và cộng \\\\
thêm 5 % hoặc 7 % đối với lao động làm nghề hoặc công việc nặng nhọc, \\\\
độc hại, nguy hiểm, đặc biệt nặng nhọc độc hại và nguy hiểm. Đối với \\\\
lao động giữ chức vụ, khoảng 80 % doanh nghiệp đã xây dựng thang, \\\\
bảng lương cụ thể theo chức danh. Đơn cử như với chức vụ giám đốc \\\\
sản xuất, giám đốc điều hành, trưởng phòng. Còn lại các doanh nghiệp \\\\
xây dựng đối với lao động giữ chức vụ theo thang lương, bảng lương \\\\
chuyên môn nghiệp vụ và bảng phụ cấp chức vụ, phụ cấp trách nhiệm. \\\\
Thống kê của BHXH Việt Nam cũng cho thấy, đa số doanh nghiệp đã đăng \\\\
ký đóng BHXH cho người lao động theo mức lương mà không có khoản bổ \\\\
sung khác. Mặc dù quy định từ ngày 1/1/2018, tiền lương tháng đóng BHXH \\\\
gồm mức lương và thêm khoản bổ sung khác."
tokenized_text = tokenizer.encode(src, return_tensors="pt").to(device)
model.eval()
summary_ids = model.generate(
                    tokenized_text,
                    max_length=256, 
                    num_beams=5,
                    repetition_penalty=2.5, 
                    length_penalty=1.0, 
                    early_stopping=True
                )
output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(output)
```
#### Output

``` bash

Nhiều doanh nghiệp vẫn chủ yếu xây dựng thang, bảng lương để đóng BHXH bằng mức thấp nhất. \\
Dù quy định từ 1/1/2018, tiền lương tháng đóng BHXH gồm mức lương và thêm khoản bổ sung khác. \\
Thống kê của BHXH Việt Nam cho thấy, nhiều doanh nghiệp vẫn chỉ đóng BHXH \\
cho người lao động theo mức lương mà không có khoản bổ sung khác.

```
### Contact information
For personal communication related to this project, please contact Nha Nguyen Van (nha282@gmail.com).