# Deprem Verilerinin AWS Üzerinde Analizi Projesi

## Proje Adı:
Deprem Verilerinin AWS Üzerinde Analizi

## Proje Amacı:
Deprem verilerini toplayarak AWS altyapısı üzerinde analiz etmek, deprem büyüklükleri, zaman ve konuma göre dağılımları gibi bilgileri görsel hale getirerek kamu ve bilimsel çalışmalara katkı sağlamak.

## Kullanılacak Teknolojiler:
1. **AWS S3 (Simple Storage Service):** Verilerin depolanması.
2. **AWS Lambda:** Verilerin otomatik olarak güncellenmesi ve işlenmesi.
3. **AWS QuickSight:** Analizlerin ve görselleştirme çözümlerinin oluşturulması.
4. **Python:** Verilerin toplanması, temizlenmesi ve AWS hizmetlerine entegrasyonu.
5. **Uluslararası ve Ulusal Deprem Kaynakları API’leri:** Verilerin elde edilmesi (USGS, AFAD vb.).
6. **JSON/CSV:** Verilerin formatlanması ve depolanması.

## Adımlar:

### 1. Proje Planının Hazırlanması
- Gerekli AWS servislerinin belirlenmesi.
- Deprem verilerini sağlayacak kaynakların seçilmesi (USGS API, AFAD API).
- Analiz metriklerinin (büyüklük, zaman, konum) belirlenmesi.

### 2. Verilerin Toplanması
- Python kullanarak API’lerden veri çekme.
- Elde edilen verilerin JSON veya CSV formatında saklanması.
- Verilerin AWS S3’e yüklenmesi.

### 3. AWS S3 Yapılandırması
- AWS S3 bucket oluşturma.
- Bucket politikası ve erişim izinlerinin ayarlanması.
- Verilerin organize bir şekilde yedeklenmesi.

### 4. AWS Lambda Fonksiyonlarının Oluşturulması
- Veri çekme ve güncelleme için otomasyon.
- Python tabanlı bir Lambda fonksiyonu geliştirerek API’lerden gelen verilerin AWS S3’e aktarılması.
- Veri işleme adımlarının belirlenmesi.

### 5. Verilerin Analizi
- Python kullanarak deprem büyüklüklerinin ve konumlarının ön işlenmesi.
- Verilerdeki eksik ve hatalı kayıtları temizleme.
- Analiz çıktılarını JSON/CSV formatında saklama.

### 6. AWS QuickSight ile Görselleştirme
- AWS S3’te saklanan verileri AWS QuickSight ile entegre etme.
- Farklı metriklere göre (zaman, konum, büyüklük) görseller oluşturma.
- Raporlama panelleri hazırlama.

### 7. Test ve Optimizasyon
- Sistemin doğru çalışıp çalışmadığını kontrol etme.
- Lambda fonksiyonlarının zamanlamasını optimize etme.
- Verilerin eksiksiz ve doğru analiz edildiğinden emin olma.

### 8. Dağıtım ve Sunum
- Sistemı kullanıcıların erişine sunma.
- Elde edilen analizleri ilgili platformlarda paylaşma.

## Öğrenci Hakkı Kullanımı:
Projenin AWS altyapısında geliştirilmesi için AKS (AWS Kullanıcı Sistemi) üzerindeki 50 kredilik öğrenci hakkı kullanılacaktır. Bu kredi, proje kapsamındaki AWS hizmetlerini (S3, Lambda, QuickSight) temel seviyede karşılamak için yeterli görülmektedir.

## Sonuç:
Bu proje sayesinde deprem verileri AWS altyapısı kullanılarak analiz edilecek ve görselleştirilecektir. Bu da bilimsel araştırmalar ve kamu bilgilendirme çalışmaları için değerli bir kaynak oluşturacaktır.

# VERİLER
- afaddan veri çekilde /Users/gokcesoylu/CloudComputing/afad_scraped_data.json dosyasına kaydedildi

- kandilliden veri çekildi /Users/gokcesoylu/CloudComputing/kandilli_earthquake_data.json dosyasına kaydedildi

- usgs den veri çekilde /Users/gokcesoylu/CloudComputing/earthquake_data.json dosyasına kaydedildi






------------------------------------------
rapor updated
-----------------------------------------

# **Deprem Verilerinin AWS Üzerinde Analizi**

## **Proje Adı:**
Deprem Verilerinin AWS Üzerinde Analizi

## **Proje Amacı:**
Deprem verilerini AWS'nin çeşitli hizmetlerini kullanarak analiz etmek, bu verilerden anlamlı görselleştirmeler üretmek ve AWS'nin bulut çözümlerini efektif bir şekilde kullanmayı öğrenmek. Proje, deprem verilerinin bilimsel araştırmalar ve kamu bilgilendirme çalışmalarına katkıda bulunmasını hedeflerken bulut bilişim dersinin gereksinimlerini karşılayacak şekilde tasarlanmıştır.

---

## **Kullanılacak AWS Hizmetleri ve Roller:**

### 1. **AWS S3 (Simple Storage Service):**
- Verilerin güvenli ve organize bir şekilde depolanması.
- S3'deki verilerin **Lifecycle Policies** kullanılarak optimize edilmesi (eski verilerin arşivlenmesi).

### 2. **AWS Lambda:**
- API’lerden veri çekme ve AWS S3’e yükleme görevlerinin otomasyonu.
- Verilerin gerçek zamanlı olarak işlenmesi ve temizlenmesi.

### 3. **AWS QuickSight:**
- S3'te depolanan verilerin analiz edilmesi ve görselleştirilmesi.
- Zaman, büyüklük ve coğrafi dağılım gibi metriklere göre raporlama panelleri oluşturma.

### 4. **AWS Glue:**
- S3’teki JSON/CSV verilerinin ETL (Extract, Transform, Load) işlemlerini kolaylaştırmak için kullanılacak.
- Glue Crawler ile veriler otomatik olarak taranarak analiz için uygun hale getirilecek.

### 5. **AWS CloudWatch:**
- Lambda fonksiyonlarının performansını izlemek.
- API veri çekme işlemlerinde meydana gelebilecek hataları raporlamak ve uyarılar oluşturmak.

### 6. **AWS IAM (Identity and Access Management):**
- Hizmetler arası güvenli erişim politikalarının oluşturulması (Lambda’nın S3'e erişimi).

### 7. **AWS Athena:**
- S3'te depolanan veriler üzerinde SQL sorguları çalıştırarak analizler yapmak.
- Verilerin sorgulanabilir bir hale getirilmesi için Glue ile entegre edilmesi.

### 8. **AWS SNS (Simple Notification Service):**
- Önemli olaylar veya belirli büyüklüğün üzerindeki depremler tespit edildiğinde e-posta veya SMS ile bildirim gönderilmesi.

---

## **Adımlar**

### **1. Veri Toplama ve Depolama**
- **API’lerden veri çekme:** Python ile USGS, AFAD ve Kandilli API’lerinden veri çekilecek.
- **Veri formatlama:** JSON formatında işlenen veriler, belirli bir yapıya dönüştürülerek saklanacak.
- **AWS S3:** Toplanan veriler AWS S3 bucketlarına yüklenecek. Bucket yapısı şu şekilde olacak:
  - `/raw-data/`: API'den gelen ham veriler.
  - `/processed-data/`: Temizlenmiş ve analiz için hazırlanmış veriler.

---

### **2. Lambda Fonksiyonları ile Otomasyon**
- **Lambda işlevleri:**
  - API'lerden düzenli veri çekmek ve S3’e yüklemek için zamanlanmış görevler (AWS EventBridge ile tetiklenecek).
  - Verileri işlemek ve hatalı/verimsiz kayıtları temizlemek.
- **CloudWatch ile izleme:** Lambda'nın çalışması sırasında oluşan hatalar CloudWatch üzerinden analiz edilecek.

---

### **3. Glue ve Athena ile Veri İşleme**
- **AWS Glue:**
  - S3’teki deprem verileri üzerinde tarama işlemi gerçekleştirilecek.
  - Glue Catalog oluşturularak verilerin sorgulanabilir hale gelmesi sağlanacak.
- **AWS Athena:**
  - Sorgular: Deprem büyüklükleri, zaman dağılımı ve coğrafi koordinat analizi için SQL sorguları yazılacak.

---

### **4. QuickSight ile Görselleştirme**
- **QuickSight panelleri:**
  - Zaman serisi analizleri (yıllara göre deprem sayısı).
  - Dünya haritası üzerinde büyüklkl\u00fklere göre renk kodlu konum işaretlemeleri.
  - Deprem büyüklüğü dağılım histogramları.
- **KPI’ler:**
  - Deprem sayılarının zaman içerisindeki değişimi.
  - Büyük depremlerin sık görüldüğü bölgeler.

---

### **5. Bildirimler ve Uyarılar**
- **AWS SNS kullanımı:**
  - 6.0 büyüklüğün üzerindeki depremler için e-posta veya SMS uyarıları gönderilecek.
  - AWS Lambda, büyük bir deprem tespit ettiğinde SNS'yi tetiklemek için yapılandırılacak.

---

### **6. Optimizasyon ve Dağıtım**
- AWS hizmetlerinin kredi sınırları içinde en verimli şekilde çalı
