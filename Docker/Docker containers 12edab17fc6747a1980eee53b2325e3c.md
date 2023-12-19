# Docker containers

- docker run busybox echo hello world - run new docker
    - -d run in background (d- deamon)
    - -it run input interactive terminal ( input terminal)
    - -p 80:80  80 numaralı konteynerin portunu ana sistemdeki 80 numalı porta yönlendirir
    - **docker run -it —detach-keys ctrl-x,x jpetazzo/clock** — hansı key istifadə edərək işlenen komanda backgrounda alınsın?
    - **docker run -dit --name onbir alpine  —** arxa planda işləsin həmdə cli ilə sonradan input eləmək mümkün olsun
    - **docker run -v [HOST_DIZIN]:[KONTEYNER_DIZIN] [IMAJ]**
        - docker run -v /ana-bilgisayar-dizin:/konteyner-dizin [IMAJ]
        - -v /opt/data : /data/db
        - bunun üçün opt/data ya erişmək üçün sharing klasörden izin vermeliyik
    
     
    
    - docker run -e "VERITABANI_KULLANICI=databaseuser" -e "VERITABANI_PAROLASI=mysecretpassword" [IMAJ]
        - dikkatli olun : değil = kullanılıyo
        
    
- docker ps  -  view process status
    - -a see all dockers (a - all)
    - -q see only id of dockers (q- quiet)
    - -l see only last created docke (l-last)
    - -n 5 - see last 5 container

  ****

- **docker attach ContainerID -** background’da işlənən container’a qoşulmaq üçün

- **docker logs 8cc2121 -f -n 1          -** 8cc2121 id-li containerı loglamaq üçün istifadə olunur.
    - -f  (f- follow) indi davamlı olaraq loglaması üçün lazımdır
    - -n 1 (n- number) və ya —tail isə son neçə logunu oxumaq istədiyimizi deyirik.
    - **`-t`** veya **`--timestamps`**: Bu bayrak, günlük girdilerine zaman damgası (timestamp) ekler, böylece her girdinin ne zaman kaydedildiğini görebilirsiniz.
    - **docker logs --since="2023-09-01T00:00:00" --until="2023-09-02T00:00:00" container_id  —** müəyyən tarix aralığında olan dataları göstərir. dəqiq tarix yerinə “42m”, ”12s” kimi ifadələrdə işlədə bilərik.
- docker search marathon  — docker hub da searching elemek
- docker pull postgress — download image not run
- docker inspect [container id]
- 

- docker commit 8ccf60 my_image:1.0
    
    — "Docker commit" komutu, bir çalışan Docker konteynerinden yeni bir Docker image oluşturmanızı sağlar. Yani, belirli bir konteynerin mevcut durumunu dondurarak bu durumu bir image haline getirir. Bu oluşturulan image, daha sonra yeni konteynerler oluşturmak için kullanılabilir.
    
- docker build - Dockerfile kullanarak sıfırdan bir image oluşturur. Her şey burdan başlar.

**Dockerfile, bir Docker konteyner imajını nasıl oluşturacağınızı adım adım tanımlayan bir yapılandırma dosyasıdır. Dockerfile, genellikle metin tabanlıdır ve Docker tarafından yorumlanır. İşte tipik bir Dockerfile örneği:** 

```docker
# Başlangıçta kullanmak istediğiniz temel imajı belirtin
FROM ubuntu:20.04

# Imaj oluştururken çalışacak dizini ayarlayın
WORKDIR /app

# Gerekli bağımlılıkları yükleyin
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Uygulama kodunu ve dosyalarını imajın içine kopyalayın
COPY . /app

# Uygulamanın çalıştırılması için komutu belirtin
CMD ["python3", "app.py"]
```

 

Bu örnekteki Dockerfile, bir Ubuntu 20.04 tabanlı bir konteyner imajı oluşturur ve bu imaj içinde bir Python uygulamasını çalıştırır. Aşağıda bu Dockerfile'daki temel öğelerin açıklamalarını bulabilirsiniz:

- **`FROM`**: Docker imajının temelini oluşturmak için kullanılacak temel imajı belirtir.
- **`WORKDIR`**: İmajın içindeki çalışma dizinini ayarlar.
- **`RUN`**: İmaj oluşturma sırasında çalıştırılacak komutları belirtir (bu örnekte paketlerin yüklenmesi).
- **`COPY`**: Lokal dosyaları veya dizinleri imajın içine kopyalar.
- **`CMD`**: Konteyner çalıştırıldığında otomatik olarak çalışacak komutları belirtir.
- **ENV:** **`ENV`** komutu, çevresel değişkenleri belirtir ve Docker konteyneri içinde kullanılabilir. Bu komut ile yapılandırma seçenekleri ve çevresel değişkenler ayarlanabilir.
- **ARG:** **`ARG`** komutu, Dockerfile içinde kullanılan argümanları tanımlar. Bu argümanlar, Docker build komutu sırasında belirtilir ve Dockerfile içinde kullanılır.

Dockerfile'lar, konteynerinizin nasıl yapılandırılacağını ve hangi adımların uygulanacağını adım adım açıklar. Bu sayede, imajınızın tekrarlanabilir ve öngörülebilir olmasını sağlar ve Docker kullanarak uygulama dağıtımını kolaylaştırır. Dockerfile'lar, projelerinize özgü gereksinimlere göre özelleştirilebilir.

```docker
# Temel Docker imajını belirtin

FROM python:3.8

# Çalışma dizinini oluşturun

WORKDIR /app

# Gereksinimleri kopyalayın ve kurun

COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Uygulamanızı Docker konteynerine kopyalayın

COPY . /app/

# Django uygulamasının dinleyeceği portu belirtin (örneğin, 8000)

EXPOSE 8000

# Django uygulamasını çalıştırın

CMD ["python", "[manage.py](http://manage.py/)", "runserver", "0.0.0.0:8000"]
```

docker image build -t my-django-image-3 .

### Docker İmage

1. **`docker image ls`** veya **`docker images`**:
    - Docker imajlarını listeler.
    - **`a`** veya **`-all`** bayrağı kullanılarak tüm imajlar (sadece etiketsiz olanlar dahil) listelenebilir.
    - **`q`** veya **`-quiet`** bayrağı kullanılarak yalnızca imajların ID'leri görüntülenir.
2. **`docker image pull`**:
    - Docker Hub veya başka bir imaj deposundan belirli bir imajı çeker.
    - **`docker image pull nginx`** komutuyla örnek bir imajı çekme.
3. **`docker image build`**:
    - Dockerfile kullanarak bir Docker imajı oluşturur.
    - **`docker image build -t my-app:1.0 .`** komutuyla bir Dockerfile'dan imaj oluşturma.
4. **`docker image tag`**:
    - Bir Docker imajına yeni bir etiket ekler.
    - **`docker image tag my-app:1.0 my-app:latest`** ile mevcut bir imaja yeni bir etiket ekleme.
5. **`docker image push`**:
    - Bir Docker imajını bir imaj deposuna yükler (örneğin, Docker Hub).
    - **`docker image push my-app:1.0`** ile bir imajı Docker Hub'a yükleme.
6. **`docker image rm`**:
    - Bir veya daha fazla Docker imajını siler.
    - **`docker image rm my-app:1.0`** ile bir imajı silme.
7. **`docker image prune`**:
    - Kullanılmayan tüm imajları temizler.
    - **`a`** veya **`-all`** bayrağı kullanılarak tüm imajları temizler.
8. **`docker image inspect`**:
    - Bir Docker imajının ayrıntılarını görüntüler.
    - **`docker image inspect my-app:1.0`** ile bir imajın ayrıntılarını görüntüleme.
9. **`docker image history`**:
    - Bir Docker imajının değişiklik geçmişini görüntüler.
    - **`docker image history my-app:1.0`** ile bir imajın geçmişini görüntüleme.
10. **`docker image save`** ve **`docker image load`**:
    - Docker imajını bir dosyada saklamak veya bir dosyadan yüklemek için kullanılır.
    - **`docker image save -o my-app.tar my-app:1.0`** ile bir imajı bir dosyada saklama.
    - **`docker image load -i my-app.tar`** ile bir imajı bir dosyadan yükleme.
    

### Docker Compose

1. **`docker-compose up`**:
    - Docker Compose dosyasındaki hizmetleri başlatır.
    - **`d`** veya **`-detach`** bayrağı kullanılarak arka planda çalıştırılabilir.
    - **`docker-compose up -d`** ile hizmetleri arka planda başlatma.
2. **`docker-compose down`**:
    - Docker Compose ile başlatılan hizmetleri durdurur ve ilişkili kaynakları temizler.
    - **`v`** veya **`-volumes`** bayrağı kullanılarak kök dizini bağlantıları ve veri bölmeleri de temizlenir.
    - **`docker-compose down -v`** ile kök dizini bağlantıları ve veri bölmelerini temizleme.
3. **`docker-compose ps`**:
    - Çalışan Docker Compose hizmetlerini ve konteynerlerini listeler.
    - **`q`** veya **`-quiet`** bayrağı kullanılarak sadece konteyner ID'leri görüntülenir.
4. **`docker-compose logs`**:
    - Hizmetlerin günlük çıktılarını görüntüler.
    - **`f`** veya **`-follow`** bayrağı kullanılarak canlı günlük çıktılarını takip edebilirsiniz.
5. **`docker-compose build`**:
    - Docker Compose dosyasındaki hizmetler için Docker imajlarını yeniden oluşturur.
    - **`-no-cache`** bayrağı kullanılarak önbelleği atlayarak yeniden oluşturur.
6. **`docker-compose exec`**:
    - Çalışan bir hizmetin içine girer.
    - **`docker-compose exec my-service bash`** ile **`my-service`** adlı hizmetin içine girme.
7. **`docker-compose up -d --scale`**:
    - Belirli bir hizmeti belirtilen sayıda ölçeklendirir.
    - **`docker-compose up -d --scale web=3`** ile **`web`** adlı hizmeti 3 konteyner olarak ölçeklendirme.
8. **`docker-compose -f`**:
    - Özel bir Docker Compose dosyasını belirtir.
    - **`docker-compose -f my-docker-compose.yml up`** ile **`my-docker-compose.yml`** dosyasını kullanarak hizmetleri başlatma.
9. **`docker-compose config`**:
    - Docker Compose dosyasının yapılandırmasını doğrular ve görüntüler.
    - **`docker-compose config`** ile yapılandırmayı görüntüleme.
10. **`docker-compose pause`** ve **`docker-compose unpause`**:
    - Belirli bir hizmeti duraklatır veya devam ettirir.
    - **`docker-compose pause my-service`** ile **`my-service`** adlı hizmeti duraklatma.
    - **`docker-compose unpause my-service`** ile **`my-service`** adlı hizmeti devam ettirme.

```
version: '3'
services:
  web:
    build:
      context: .
      args:
        - MY_VARIABLE=testerr
    image: python:3.8
    command: python manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
    volumes:
      - /home/faridh/Desktop/DjangoWithDocker/DjDocker:/app
    container_name: my-django-compose-container
```

1. **`version: '3'`**: Docker Compose dosyasının sürümünü belirler. Bu, kullanılan Docker Compose sürümüne bağlı olarak ayarlanır.
2. **`services`**: Docker Compose ile yönetilen hizmetleri tanımlar. Bu örnekte, **`web`** adında bir hizmet tanımlanmıştır.
3. **`build`**: Hizmetin Docker imajının nasıl oluşturulacağını belirtir. **`context`** ile Dockerfile'ın bulunduğu dizini (bu durumda mevcut dizin **`.`**) ve **`args`** ile Dockerfile içinde kullanılabilecek ARG değerlerini belirtir.
4. **`image`**: Eğer imaj zaten oluşturulmuşsa, bu alandaki imaj kullanılır. Eğer belirtilen imaj yerelde yoksa, **`build`** ile Docker imajı oluşturulur.
5. **`command`**: Docker konteyneri başlatıldığında çalışacak komutu belirtir. Bu durumda Django uygulamasını çalıştıran **`python manage.py runserver 0.0.0.0:8000`** komutu kullanılır.
6. **`ports`**: Konteynerin dış dünyayla iletişim kurmasına olanak tanır. Burada, yerel makinenin portu (8000) konteynerin portuna (yine 8000) bağlanır.
7. **`volumes`**: Yerel dosya sistemini konteynere bağlar. Bu, kodunuzu ve verilerinizi paylaşmanıza olanak tanır. Bu örnekte, yerel Django uygulamanızın dizini **`/app`** içine bağlanır.
8. **`container_name`**: Oluşturulan Docker konteynerine bir ad verir. Bu, konteyneri daha kolay tanımlamak için kullanılır.

### **Pushing images**

You can push a new image to this repository using the CLI:

`docker tag local-image:tagname new-repo:tagnamedocker push new-repo:tagname`