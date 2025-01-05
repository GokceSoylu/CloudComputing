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
 - Sistemin çıktıları bir web arayüzü veya PDF raporu şeklinde sunulacaktıır


 # VERİLER

 veriler temizlendi

- afaddan veri çekilde /Users/gokcesoylu/CloudComputing/afad_cleaned_data.json dosyasına kaydedildi

- kandilliden veri çekildi /Users/gokcesoylu/CloudComputing/kandilli_earthquake_data_cleaned.json dosyasına kaydedildi

- usgs den veri çekilde /Users/gokcesoylu/CloudComputing/earthquake_data_cleaned.json dosyasına kaydedildi

# AWS
root AWS hesabı oluşturuldu
IAM hesabı oluşturuldu - developer_gokce
bucket oluşturuldu - deprem_verileri_bucket
crawler oluşturuldu - deprem-verileri-crawler
veri tabanı - deprem_verileri_db
athena ile sorgu yapıldı
sorgu sonucu boş
tablolar kontrol edildi boş değil