---
language:
- vi

tags:
- essay category
- text-classification
widget:
- text: "Cái đồng hồ của em cao hơn 30 cm. Đế của nó được làm bằng i-nốc sáng loáng hình bầu dục. Chỗ dài nhất của đế vừa bằng gang tay của em. Chỗ rộng nhất bằng hơn nửa gang tay."
  example_title: "Descriptive - Miêu tả"
- text: "Hiện nay, đại dịch Covid-19 diễn biến ngày một phức tạp, nó khiến nền kinh tế trì trệ, cuộc sống con người hoàn toàn xáo trộn và luôn ở trạng thái lo ngại... và cùng với đó chính là việc học sinh - sinh viên không thể tới trường. Một trong những điều đáng lo ngại nhất khi tình hình dịch bệnh không biết bao giờ mới ổn định."
  example_title: "Argumentative - Nghị luận"
- text: "Cấu tạo của chiếc kính gồm hai bộ phận chính là gọng kính và mắt kính. Gọng kính được làm bằng nhựa cao cấp hoặc kim loại quý. Gọng kính chia làm hai phần: phần khung để lắp mắt kính và phần gọng để đeo vào tai, nối với nhau bởi các ốc vít nhỏ, có thể mở ra, gập lại dễ dàng. Chất liệu để làm mắt kính là nhựa hoặc thủy tinh trong suốt. Gọng kính và mắt kính có nhiều hình dáng, màu sắc khác nhau."
  example_title: "Expository - Thuyết minh"
- text: "Em yêu quý đào vì nó là loài cây đặc trưng của miền Bắc vào Tết đến xuân sang. Đào bình dị nhưng gắn liền với tuổi thơ em nồng nàn. Tuổi thơ đã từng khao khát nhà có một cây đào mộc mạc để háo hức vui tươi trong ngày Tết."
  example_title: "Expressive - Biểu cảm"
- text: "Hắn vừa đi vừa chửi. Bao giờ cũng thế, cứ rượu xong là hắn chửi. Bắt đầu chửi trời, có hề gì? Trời có của riêng nhà nào? Rồi hắn chửi đời. Thế cũng chẳng sao: Đời là tất cả nhưng cũng chẳng là ai."
  example_title: "Narrative - Tự sự"
  
---

This is a finetuned DistilBERT model for Vietnamese essay categories classification.
## Overview 
- At primary levels of education in Vietnam, students are introduced to 5 categories of essays: 
    - Argumentative - Nghị luận
    - Expressive    - Biểu cảm
    - Descriptive   - Miêu tả
    - Narrative     - Tự sự
    - Expository    - Thuyết minh
- This model will classify sentences into these 5 categories 

## Pretrained model used in this pipeline:
-    This pipeline includes pre-trained [phobert-base](https://huggingface.co/vinai/phobert-base) and a Multi-label Classification head trained on 8000 manually labeled sample essay sentences.
-    The dataset can be found on [Kaggle](https://www.kaggle.com/datasets/trnthinph/vi-essay-categories-multilabelclassification)
-    Usage of PhoBERT can be found on [Huggingface](https://huggingface.co/vinai/phobert-base)

## Citation:

The general architecture and experimental results of PhoBERT can be found in  EMNLP-2020 Findings [paper](https://arxiv.org/abs/2003.00744):

```bibtex
@article{phobert,
    title     = {{PhoBERT: Pre-trained language models for Vietnamese}},
    author    = {Dat Quoc Nguyen and Anh Tuan Nguyen},
    journal   = {Findings of EMNLP},
    year      = {2020}
    }
```