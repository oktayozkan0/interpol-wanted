# ./interpol/items.py
Data validation için scrapy extension'ı olan item'lar burada tanımlanır. Scraper burada tanımlanan verilerden başka verileri çekmez ayrıca aranan veri yoksa hata verip kapanmak yerine o veriyi None yazar.

# ./interpol/middlewares.py
Scrapy için proje oluşturulduğunda gelir. Bu scraper için middleware gerekli olmadığından Scrapy nasıl verdiyse o şekilde bıraktık.

# ./interpol/pipelines.py
Burada data pipeline'ımız var. open_spider() methoduyla spider ilk çalıştığında yapılması gerekenleri yapıyoruz. Burada rabbit'teki queue'muza bağlandık
</br>
close_spider() ile spider kapanırken rabbit ile bağlantıyı koparıyoruz.
</br>
process_item() ile veri geldiğinde bu veriyi rabbit'e yazıyoruz.

# ./interpol/settings.py
DOWNLOAD_DELAY ve pipelinelar gibi spider ile alakalı ayarlar burada tutulur.

# ./interpol/spiders/wanted.py
Spider'ın hangi url'lere istek atacağını, bu url'lerden dönen response'un içerisinden nelerin alınacağını burada yazıyoruz. Asıl scraper burada çalışıyor.
