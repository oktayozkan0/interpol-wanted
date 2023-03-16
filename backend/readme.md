# consumer.py
Rabbit class'ı __init__ methodu içerisinde rabbit'e bağlanır. Böylece bu classtan bir instance oluşturulduğunda o instance üzerinden yeni bağlantı açmaya gerek kalmadan sürekli rabbit dinlenebilir

consume_data() __init__ methodundan channel'ı alır, bu channel'ı kullanarak datayı rabbit'ten ACK'ler ve rabbitten ACK'lenen data döndürülür.

to_mongo() methodu içerisinde Rabbit classının instance'ını oluştururuz  ve bağlantıyı sağlarız. Bu bağlantıyla Rabbitten veriyi alır ve DB'ye yazarız. Veri yoksa da dinlemeye devam ederiz.

# background_tasks.py
Yeni bir thread oluşturulur ve bu thread consumer.py içerisindeki to_mongo() methoduyla rabbiti dinler ve rabbitteki datayı MongoDB'ye ekler

# database.py
Mongo ile bağlantı sağlamak için gerekli class buradadır.

# models.py
pydantic ile veri doğrulama işlemi buradan gerçekleştirilir.

# routers.py
tek endpointimiz olan /api 'a yapılan istekler burada işlenir. Burada Mongo'dan veri alınır ve kullanıcıya gösterilir ayrıca cookie ve pagination işlemleri de burada yürütülür.

# main.py
Uvicorn ile backend'imiz çalıştırılır
