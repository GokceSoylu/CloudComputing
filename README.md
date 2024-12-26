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

