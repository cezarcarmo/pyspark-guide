# Configuração do PySpark no Databricks

Nesta seção, configuraremos o **Databricks** para rodar PySpark, criando um cluster e executando notebooks no ambiente de nuvem.

---

## 📌 **O que é o Databricks?**

O **Databricks** é uma plataforma unificada baseada no **Apache Spark**, otimizada para análise de dados, engenharia de dados e aprendizado de máquina. Ele oferece um ambiente gerenciado, eliminando a necessidade de configurar e manter infraestrutura manualmente.

---

## 🚀 **Passo a Passo para Configuração do Databricks**

### 1️⃣ **Criar uma Conta no Databricks**

1. Acesse [Databricks Community Edition](https://community.cloud.databricks.com/) (grátis para testes) ou crie uma conta paga em [Databricks AWS/Azure](https://databricks.com/try-databricks).
2. Após criar a conta, faça login no **Databricks Workspace**.

---

### 2️⃣ **Criar um Cluster no Databricks**

1. No menu esquerdo, clique em **Compute** → **Create Cluster**.
2. Escolha um nome para o cluster (ex.: `pyspark-cluster`).
3. Selecione a versão do **Databricks Runtime** (recomendo a mais recente com suporte ao PySpark).
4. Escolha um tipo de máquina adequado para os testes (ex.: `Single Node` na versão Community ou `Standard` em AWS/Azure).
5. Clique em **Create Cluster** e aguarde a inicialização.

---

### 3️⃣ **Criar e Executar um Notebook**

1. No menu esquerdo, clique em **Workspace** → **Users** → Selecione seu usuário.
2. Clique com o botão direito e selecione **Create** → **Notebook**.
3. Escolha um nome (ex.: `PySpark_Test`) e selecione a linguagem **Python**.
4. Associe o notebook ao cluster criado anteriormente.
5. Execute o código abaixo no notebook:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DatabricksTest").getOrCreate()

# Criar um DataFrame de teste
data = [(1, "Alice", 29), (2, "Bob", 35), (3, "Cathy", 32)]
columns = ["id", "name", "age"]
df = spark.createDataFrame(data, columns)

df.show()
```

Se o código rodar corretamente e exibir a saída, seu ambiente PySpark no Databricks está pronto! 🎉

---

### 4️⃣ **Carregar um Arquivo CSV no Databricks**

1. No menu esquerdo, clique em **Data** → **Add Data**.
2. Faça o upload de um arquivo CSV (ex.: `exemplo.csv`).
3. No notebook, use o seguinte código para carregar e visualizar os dados:

```python
file_path = "/FileStore/tables/exemplo.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)
df.show()
```

---

## 🔥 **Integração com AWS S3, Azure Blob e GCP**

Para conectar o Databricks a armazenamentos na nuvem, configure credenciais e utilize comandos como:

### **AWS S3**
```python
df = spark.read.csv("s3://meu-bucket/dados.csv", header=True, inferSchema=True)
df.show()
```

### **Azure Blob Storage**
```python
spark.conf.set("fs.azure.account.key.meustorage.blob.core.windows.net", "<CHAVE>")
df = spark.read.csv("wasbs://meu-container@meustorage.blob.core.windows.net/dados.csv", header=True, inferSchema=True)
df.show()
```

### **Google Cloud Storage (GCS)**
```python
df = spark.read.csv("gs://meu-bucket/dados.csv", header=True, inferSchema=True)
df.show()
```

---

## 📄 **Notas Finais**

- O Databricks Community Edition tem recursos limitados, mas é suficiente para aprendizado.
- Clusters pagos oferecem mais poder computacional e armazenamento distribuído.
- Integra-se facilmente com **AWS, Azure e GCP**.

Para mais detalhes, consulte a [documentação oficial do Databricks](https://docs.databricks.com/).

