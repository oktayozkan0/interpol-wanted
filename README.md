# Kurulum
! - Bilgisayarınızda Docker kurulu olmalıdır.
</br>
Docker kurulumu sonrası aşağıdaki komutları Terminal'de çalıştırdığınızda servis hazır olacaktır. Ekstra bir konfigürasyon gerektirmemektedir.
```
docker-compose build
docker-compose up
```
Backend ayağa kalkmasının ardından http://localhost:8001/api gidilerek site açılır. 3 dakika sonra (.env'de default olarak 3 dakika tanımlandı) veriler çekilmeye ve rabbit'e yazılmaya başlanacaktır. Backend (web container'ı) rabbiti devamlı dinler. Rabbit'e yeni bir veri geldiyse ve bu veri db'de yoksa db'ye yazar.

Siteyi ziyaretinizde tarayıcınızın cookie'lerine ziyaretiniz sırasında kaç kayıt olduğu işlenir. Sayfa yenilendiğinde eğer DB'deki veri sayısı cookie'leriniz içerisindeki veri sayınızdan fazla ise 'New listings added since your last visit' şeklinde bir uyarı çıkar, altında ise kaç adet yeni kaydın eklendiği bilgisi verilir.

# ENV
Ana dizindeki .env dosyası düzenlenerek verinin kaç dakikada bir çekileceğini, verinin çekilme hızını (DOWNLOAD_DELAY), Rabbit ve Mongo'nun portlarını, kullanıcı adı ve şifrelerini değiştirebilirsiniz.


# MONGO-INIT.SH
Bu dosya MongoDB çalıştırıldıktan hemen sonra çalışır. .env içerisinden Mongo bilgilerini alır  ve bu bilgilere dayanarak yeni db, collection ve user oluşturur.

# NOT
.env içerisinde DOWNLOAD_DELAY ve SCRAPE_EVERY_MINUTE düşürüldüğünde interpol api'ı girişimizi engelliyor bu sebeple bir süre delay koymak şimdilik en iyi çözüm.
</br>
backend klasörü içerisinde backend, scraper klasörü içerisinde scraper dokümantasyonu bulunmaktadır.
