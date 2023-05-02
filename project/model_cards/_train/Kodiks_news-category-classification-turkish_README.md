---
language:
- tr
tags:
- text  # Example: audio
- text-classification  # Example: automatic-speech-recognition
- news-category-classification  # Example: speech
metrics:
- accuracy  # Example: wer. Use metric id from https://hf.co/metrics
- f1
- precision
- recall
---

## INTERPRESS TURKISH NEWS CATEGORY CLASSIFICATION MODEL - TEST - v0.2

LABELS = {
  0: 'spor',
  1: 'is_ve_finans',
  2: 'lifestyle',
  3: 'eglence',
  4: 'seyahat',
  5: 'egitim',
  6: 'bilim',
  7: 'teknoloji',
  8: 'kultur_sanat',
  9: 'otomotiv',
  10: 'politika',
  11: 'endustri',
  12: 'moda',
  13: 'yemek',
  14: 'saglik'
}

ACC = 0.9190, F1 = 0.7590, PRECISION = 0.7966, RECALL = 0.7385

### DATASETS
```
DatasetDict({
    train: Dataset({
        features: ['labels', 'content'],
        num_rows: 112705
    })
    test: Dataset({
        features: ['labels', 'content'],
        num_rows: 28177
    })
})
```

### DATASETS SAMPLES
```
{
  "label": "eglence",
  "content": "BİR ŞARKI İKİ VERSİYON Sevilen şarkıcı Okan Tok, benim miladım dediği 7. Teklisi “Topuk Sesleri” ile müzikseverlerle yeniden buluştu. Okan Tok yorumuyla “Topuk Sesleri” isimli eserin söz ve müziği Meltem Kurtoğlu imzası taşırken Akın İshakoğlu yönetmenliğinde klip çalışması tamamlandı. Klip çalışmasında sevdiği erkek için box ringinde dövüşen iki kadın konu edilirken Okan Tok “ En çok keyif aldığım klip oldu iki kadının benim için dövüştüğünü izlemek egomu okşadı ve inanılmaz duygular yaşadım halen her gün 2 kez izliyorum. Sanırım bir erkeği mutlu etmenin yolu onun için mücadele etmekten geçiyor, bunu klip çekimlerimde hissettim” dedi. Önümüzdeki günlerde şarkısının remix versiyonunu da sevenlerine sunacağını ifade eden Okan Tok, ilk müzikteki hedefim çok iyi bir solist olmaktı ve bunu başardım. Yılmadan çalıştım ürettim, şimdi bambaşka bir Okan olarak herkesin karşısındayım, hayalim Ebru Gündeş ile düet yapmak, vurgusunu yaptı. OKAN TOK YORUMUYLA “TOPUK SESLERİ” KLİP LİNK"
},
{
  "label": "is_ve_finans",
  "content": "THY\'nin eski genel müdürü ve pilotu Atilla Çelebi hayatını kaybetti Türk Hava Yollarında (THY) 1994-1997 yılları arasında genel müdürlük görevini yürüten Kaptan Pilot Atilla Çelebi, 92 yaşında vefat etti. Pilot Atilla Çelebi’nin vefatını sosyal medya hesabından duyuran THY Genel Müdürü Bilal Ekşi, "Türk Hava Yolları eski genel müdürlerimizden Kaptan Pilot Atilla Çelebi\'nin vefat ettiğini üzüntüyle öğrenmiş bulunuyorum. Merhuma Allah’tan rahmet, kıymetli ailesine ve yakınlarına başsağlığı dilerim. THY ailemizin başı sağ olsun." ifadelerini kullandı."
},
{
  "label": "teknoloji",
  "content": "KVVK: AstraZeneca Türkiye\'de veri sızıntısı yaşandı Kişisel Verileri Koruma Kurumu (KVKK), AstraZeneca’da veri ihlali yaşandığını duyurdu. KVKK’nin açıklamasına göre AstraZeneca’nın web sitesinde tarayıcının “kaynağı görüntüle” özelliğini kullanarak adayların kişisel bilgileri görülebiliyordu. İş başvurusu yapan 981 kişinin kişisel verileri bu yöntemle herkes tarafından görüntülenebildi.AstraZeneca Türkiye’ye iş başvurusu yapan kişilerin ülke, isim, e-posta, telefon numarası, maaş beklentisi, mevcut maaş bilgisi, var ise “AstraZeneca” ile önceki iş ilişkisi bilgisi, vize durumu, mevcut veya önceki işveren ile ilgili kısıtlayıcı maddelerin ayrıntıları sızdı.KVKK\'den açıklama"Bilindiği üzere, 6698 sayılı Kişisel Verilerin Korunması Kanununun “Veri güvenliğine ilişkin yükümlülükler” başlıklı 12 nci maddesinin (5) numaralı fıkrası “İşlenen kişisel verilerin kanuni olmayan yollarla başkaları tarafından elde edilmesi hâlinde, veri sorumlusu bu durumu en kısa sürede ilgilisine ve Kurula bildirir. Kurul, gerekmesi hâlinde bu durumu, kendi internet sitesinde ya da uygun göreceği başka bir yöntemle ilan edebilir.” hükmünü amirdir.Veri sorumlusu sıfatını haiz AstraZeneca İlaç Sanayi ve Ticaret Limited Şirketi tarafından Kurula iletilen veri ihlal bildiriminde özetle;Çalışan adaylarının, “AstraZeneca”daki açık pozisyonlara başvurabilmelerini sağlayan, veri işleyen (Workday Limited) sisteminde ihlal gerçekleştiği,Bir adayın kendi hesabına giriş yapmadan iş başvurusu gönderebilmesi için Workday’in, kullanıcı oturumuna ilişkin verileri izlemek adına bir JavaScript değişkeni kullandığı, bu değişkenin HTML kaynağına dahil edildiği, değişkenin değerinin, harici kariyer sitesi için HTML kaynağını inceleyen, örneğin tarayıcının "Kaynağı Görüntüle" özelliğini kullanan kullanıcılar tarafından görülebilir hale geldiği,Bahse konu durumdan dolayı, 13 Temmuz 2022 saat 23:53 (İstanbul saati) ila 14 Temmuz 2022 saat 05:32 arasında ve/veya 20 Temmuz 2022 saat 22:06 ila 1 Ağustos 2022 saat 23:15 arasında iş başvurusu yapan çalışan adaylarının kişisel verilerinin kısa süreliğine erişilebilir hale geldiği,İhlalin 31 Temmuz 2022 tarihinde tespit edildiği,İhlalden etkilenen kişi grubunun çalışan adayları olduğu,İhlalden tahmini 981 kişinin etkilendiği,İhlalden etkilenen kişisel verilerin; ülke, isim, e-posta, telefon numarası, maaş beklentisi, mevcut maaş bilgisi, var ise “AstraZeneca” ile önceki iş ilişkisi bilgisi, vize durumu, mevcut veya önceki işveren ile ilgili kısıtlayıcı maddelerin ayrıntıları olduğunun tahmin edildiği, buna ek olarak, çalışan adaylarının veri işleyen sistemi üzerinden gönüllü olarak da kişisel URL, iş deneyimi, eğitim, dil, yetenekler ve özgeçmiş verilerini sağlayabildiğibilgilerine yer verilmiştir.Konuya ilişkin inceleme devam etmekle birlikte, Kişisel Verileri Koruma Kurulunun 11.08.2022 tarih ve 2022/831 sayılı Kararı ile söz konusu veri ihlali bildiriminin Kurumun internet sayfasında ilan edilmesine karar verilmiştir."Redmi Note 11 ailesi hızlı şarj konusunda sınırları zorluyorBu videoda konumuz hızlı şarj teknolojileri. Xiaomi’nin büyük ilgi gören Redmi Note 11 serisinin de en çarpıcı özelliği hızlı şarj. Peki uygun fiyata sağlam özellikler sunan Redmi Note 11 ailesi özellikle hızlı şarj konusunda ne kadar iddialı?daha fazla video için"
},

```