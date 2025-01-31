# Configuração do PySpark com Docker

Nesta seção, configuraremos um ambiente PySpark utilizando **Docker**, permitindo um ambiente isolado e portátil para execução de pipelines de dados.

---

## 📌 **Pré-requisitos**

1. **Docker instalado**:
   - Verifique se o Docker está instalado executando:
     ```bash
     docker --version
     ```
   - Se não estiver instalado, siga as instruções do [Docker Oficial](https://docs.docker.com/get-docker/).

2. **Docker Compose (opcional, mas recomendado)**:
   - Verifique se está instalado:
     ```bash
     docker-compose --version
     ```
   - Se necessário, instale via:
     ```bash
     pip install docker-compose
     ```

---

## 🚀 **Configurando o Ambiente PySpark com Docker**

### 1️⃣ **Criar um `Dockerfile`**
No diretório raiz do projeto, crie um arquivo chamado `Dockerfile` e adicione o seguinte conteúdo:

```dockerfile
# Usar imagem oficial do Spark
FROM bitnami/spark:3.4.0

# Definir variáveis de ambiente
ENV SPARK_HOME=/opt/spark
ENV PATH="$SPARK_HOME/bin:$PATH"

# Criar diretório para scripts
WORKDIR /app
COPY scripts /app/scripts

# Definir comando padrão
CMD ["pyspark"]
```

---

### 2️⃣ **Criar um `docker-compose.yml`**
Se quiser gerenciar o ambiente facilmente, crie um `docker-compose.yml` com o seguinte conteúdo:

```yaml
version: '3'
services:
  spark:
    image: bitnami/spark:3.4.0
    container_name: pyspark-container
    environment:
      - SPARK_HOME=/opt/spark
    volumes:
      - ./scripts:/app/scripts
    working_dir: /app
    command: ["pyspark"]
    ports:
      - "4040:4040"  # Porta da interface do Spark UI
```

---

### 3️⃣ **Construir e Executar o Container**

1. **Construir a imagem Docker:**
   ```bash
   docker build -t pyspark-image .
   ```

2. **Executar o container diretamente:**
   ```bash
   docker run --rm -it -v $(pwd)/scripts:/app/scripts pyspark-image
   ```

3. **Ou executar com Docker Compose:**
   ```bash
   docker-compose up -d
   ```
   - Para acessar o container:
     ```bash
     docker exec -it pyspark-container bash
     ```
   - Para interromper o ambiente:
     ```bash
     docker-compose down
     ```

---

## 🔥 **Testando o PySpark dentro do Container**

Após iniciar o container, teste o PySpark rodando:

```bash
docker exec -it pyspark-container pyspark
```

Dentro do shell interativo, rode:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DockerTest").getOrCreate()
print(spark.version)
```

Se a versão do Spark for exibida corretamente, o ambiente está configurado! 🎉

---

## 📄 **Notas Finais**

- A interface web do Spark UI pode ser acessada via `http://localhost:4040`.
- Para persistir dados, configure volumes adicionais no `docker-compose.yml`.
- Se precisar de mais nós, considere configurar um **cluster Spark com Docker Swarm ou Kubernetes**.

Para mais informações, consulte a [documentação oficial do Spark](https://spark.apache.org/docs/latest/).

