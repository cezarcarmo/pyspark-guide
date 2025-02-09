# 6⃣ ETL com PySpark

## Introdução ao Processo ETL
O processo **ETL (Extract, Transform, Load)** é fundamental para a Engenharia de Dados. No PySpark, conseguimos realizar esse processo de forma distribuída e eficiente, garantindo escalabilidade para grandes volumes de dados.

Neste guia, abordaremos as seguintes etapas:
1. **Extração de dados** de diferentes fontes (CSV, Parquet, JSON, JDBC, Delta Lake).
2. **Transformação dos dados**, incluindo limpeza, normalização e aplicação de regras de negócio.
3. **Carga dos dados** em diferentes formatos e destinos.
4. **Implementação de um pipeline ETL completo** utilizando PySpark.

---

## 1️⃣ Extração de Dados
PySpark permite a leitura de diversos formatos de arquivos e bancos de dados relacionais. Alguns exemplos:

### 1.1 Lendo arquivos CSV, JSON e Parquet
```python
from pyspark.sql import SparkSession

# Criando a SparkSession
spark = SparkSession.builder.appName("ETL_Example").getOrCreate()

# Lendo arquivos CSV
df_csv = spark.read.format("csv").option("header", "true").load("data/exemplo.csv")

# Lendo arquivos JSON
df_json = spark.read.json("data/exemplo.json")

# Lendo arquivos Parquet
df_parquet = spark.read.parquet("data/exemplo.parquet")
```

### 1.2 Conectando a um Banco de Dados via JDBC
```python
jdbc_url = "jdbc:mysql://localhost:3306/meu_banco"
properties = {"user": "usuario", "password": "senha", "driver": "com.mysql.cj.jdbc.Driver"}

df_jdbc = spark.read.jdbc(url=jdbc_url, table="tabela_exemplo", properties=properties)
```

---

## 2️⃣ Transformação dos Dados
Após extrair os dados, é essencial transformá-los para atender aos requisitos do negócio. Exemplos de transformações:

### 2.1 Selecionando e Renomeando Colunas
```python
df = df_csv.selectExpr("nome as Nome", "idade as Idade", "salario as Salario")
```

### 2.2 Filtrando Dados
```python
df_filtrado = df.filter(df["Idade"] > 18)
```

### 2.3 Criando Novas Colunas
```python
from pyspark.sql.functions import col

df = df.withColumn("Salario_Ajustado", col("Salario") * 1.1)
```

### 2.4 Removendo Duplicatas
```python
df = df.dropDuplicates()
```

### 2.5 Tratando Valores Nulos
```python
df = df.fillna({"Salario": 0, "Idade": 18})
```

---

## 3️⃣ Carga dos Dados
Os dados podem ser salvos em diversos formatos e destinos. Exemplos:

### 3.1 Salvando em CSV, JSON e Parquet
```python
df.write.mode("overwrite").csv("output/dados_transformados.csv", header=True)
df.write.mode("overwrite").json("output/dados_transformados.json")
df.write.mode("overwrite").parquet("output/dados_transformados.parquet")
```

### 3.2 Gravando em um Banco de Dados via JDBC
```python
df.write.jdbc(url=jdbc_url, table="tabela_transformada", mode="overwrite", properties=properties)
```

---

## 4️⃣ Pipeline ETL Completo
Abaixo está um exemplo de pipeline ETL completo utilizando PySpark:
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Criando a SparkSession
spark = SparkSession.builder.appName("ETL_Pipeline").getOrCreate()

# Extração
df = spark.read.csv("data/exemplo.csv", header=True, inferSchema=True)

# Transformação
df = df.withColumn("Salario_Ajustado", col("Salario") * 1.1).dropDuplicates()
df = df.fillna({"Salario": 0, "Idade": 18})

# Carga
df.write.mode("overwrite").parquet("output/dados_finalizados.parquet")
```

Esse pipeline pode ser adaptado para incluir mais transformações e integrações com outras fontes e destinos de dados.

---

## Conclusão
Neste guia, abordamos um fluxo completo de **ETL com PySpark**, desde a extração de dados de diferentes fontes, passando pelas transformações necessárias, até a carga dos dados em formatos estruturados. Essa base pode ser expandida para atender necessidades específicas do seu projeto.



