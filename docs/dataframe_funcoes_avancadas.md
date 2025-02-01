# Funções Avançadas em DataFrames

Nesta seção, exploramos funções avançadas que ampliam o uso dos DataFrames no PySpark, como **agregações**, **joins** e **UDFs (User Defined Functions)**.

---

## 🔄 **Agrupamento e Agregações**

### 1️⃣ **Agrupamento com `groupBy`**
- Agrupa os dados com base em uma ou mais colunas.
- Utilizado em conjunto com funções de agregação.

```python
# Agrupar por uma coluna e calcular soma
df.groupBy("coluna").sum("outra_coluna").show()

# Exemplo prático:
df.groupBy("nome").sum("idade").show()
```

### 2️⃣ **Agregação com `agg`**
- Permite aplicar várias funções de agregação simultaneamente.

```python
from pyspark.sql.functions import avg, sum, max

# Aplicar múltiplas agregações
df.groupBy("id").agg(
    avg("idade").alias("media_idade"),
    sum("idade").alias("soma_idade"),
    max("idade").alias("maior_idade")
).show()
```

---

## 🔗 **Joins entre DataFrames**

Os joins são usados para combinar DataFrames com base em uma chave comum.

### 1️⃣ **Tipos de Joins**
- **Inner Join**: Mantém apenas as correspondências entre os DataFrames.
- **Left Join**: Mantém todas as linhas do DataFrame esquerdo.
- **Right Join**: Mantém todas as linhas do DataFrame direito.
- **Outer Join**: Mantém todas as linhas de ambos os DataFrames.

### 2️⃣ **Exemplo Prático**
```python
# Criar dois DataFrames
df1 = spark.createDataFrame([(1, "Ana"), (2, "Carlos")], ["id", "nome"])
df2 = spark.createDataFrame([(1, 25), (3, 35)], ["id", "idade"])

# Realizar um inner join
resultado = df1.join(df2, on="id", how="inner")
resultado.show()
```

---

## ✨ **UDFs (User Defined Functions)**

UDFs permitem aplicar funções personalizadas para manipular colunas.

### 1️⃣ **Criar e Usar uma UDF**

```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Criar uma função personalizada
def saudacao(nome):
    return f"Olá, {nome}!"

# Registrar a função como UDF
saudacao_udf = udf(saudacao, StringType())

# Aplicar a UDF no DataFrame
df = df.withColumn("saudacao", saudacao_udf("nome"))
df.show()
```

---

## 📄 **Conclusão**

- **Agrupamentos e agregações** são úteis para sumarizar e analisar dados.
- **Joins** permitem combinar DataFrames de maneira flexível.
- **UDFs** ajudam a aplicar transformações personalizadas nas colunas dos DataFrames.

Essas técnicas avançadas ampliam significativamente o potencial do PySpark para tarefas complexas de engenharia de dados.

Para mais detalhes, consulte a [documentação oficial do PySpark SQL](https://spark.apache.org/docs/latest/sql-programming-guide.html).

