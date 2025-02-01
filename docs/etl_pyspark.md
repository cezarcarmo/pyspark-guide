# ETL com PySpark

Nesta seção, exploramos como construir um **pipeline ETL (Extract, Transform, Load)** usando PySpark para processar dados estruturados e semi-estruturados.

---

## 🔥 **O que é um Pipeline ETL?**

- **Extract (Extração)**: Leitura de dados de diferentes fontes, como arquivos CSV, JSON, Parquet e bancos de dados SQL.
- **Transform (Transformação)**: Limpeza, enriquecimento e agregação dos dados.
- **Load (Carga)**: Escrita dos dados transformados em diferentes formatos e destinos.

---

## 📥 **Extração de Dados**

### 1️⃣ **Ler Arquivos CSV, JSON e Parquet**

```python
from pyspark.sql import SparkSession

# Criar SparkSession
spark = SparkSession.builder.appName("ETL_PySpark").getOrCreate()

# Ler um arquivo CSV
df_csv = spark.read.csv("data/exemplo.csv", header=True, inferSchema=True)

# Ler um arquivo JSON
df_json = spark.read.json("data/exemplo.json")

# Ler um arquivo Parquet
df_parquet = spark.read.parquet("data/exemplo.parquet")
```

### 2️⃣ **Leitura de Dados de um Banco SQL via JDBC**

```python
jdbc_url = "jdbc:mysql://localhost:3306/meu_banco"
properties = {"user": "root", "password": "senha", "driver": "com.mysql.cj.jdbc.Driver"}

df_sql = spark.read.jdbc(url=jdbc_url, table="tabela_exemplo", properties=properties)
df_sql.show()
```

---

## 🔄 **Transformação dos Dados**

### 1️⃣ **Selecionar e Renomear Colunas**
```python
df_transformado = df_csv.selectExpr("id", "nome", "idade + 1 as idade_atualizada")
df_transformado.show()
```

### 2️⃣ **Filtrar e Limpar Dados**
```python
# Remover valores nulos
df_limpo = df_csv.dropna()

# Filtrar registros específicos
df_filtrado = df_csv.filter(df_csv["idade"] > 30)
df_filtrado.show()
```

### 3️⃣ **Agregação e Enriquecimento**
```python
from pyspark.sql.functions import avg, count

# Calcular idade média
df_media = df_csv.groupBy("cidade").agg(avg("idade").alias("media_idade"))
df_media.show()
```

---

## 📤 **Carga dos Dados**

### 1️⃣ **Salvar Dados Processados em Arquivos**
```python
# Salvar como CSV
df_transformado.write.csv("output/dados_transformados.csv", header=True)

# Salvar como Parquet
df_transformado.write.parquet("output/dados_transformados.parquet")
```

### 2️⃣ **Escrever Dados Processados em um Banco SQL**
```python
df_transformado.write.jdbc(url=jdbc_url, table="tabela_processada", mode="overwrite", properties=properties)
```

---

## 📄 **Conclusão**

- O PySpark permite construir pipelines ETL escaláveis e eficientes.
- Podemos extrair dados de múltiplas fontes, transformá-los aplicando filtros e agregações, e carregá-los em diferentes destinos.
- Integra-se facilmente com bancos de dados e formatos de armazenamento modernos.

Para mais detalhes, consulte a [documentação oficial do PySpark](https://spark.apache.org/docs/latest/sql-data-sources.html).

