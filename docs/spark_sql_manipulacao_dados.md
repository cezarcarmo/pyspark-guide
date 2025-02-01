# Spark SQL e Manipulação de Dados

Nesta seção, exploramos como utilizar o **Spark SQL** para consultas em tabelas e manipulação de dados estruturados no PySpark.

---

## 🔥 **O que é Spark SQL?**

- O **Spark SQL** permite executar consultas SQL diretamente no PySpark, facilitando a manipulação de dados estruturados.
- Ele suporta tanto a API de DataFrames quanto consultas SQL padrão.
- Pode ser integrado com bancos de dados, Data Lakes e outras fontes de dados estruturadas.

---

## 🛠 **Criação e Manipulação de Tabelas Temporárias**

### 1️⃣ **Registrar um DataFrame como Tabela Temporária**
- Permite que um DataFrame seja consultado como uma tabela SQL.

```python
from pyspark.sql import SparkSession

# Criar SparkSession
spark = SparkSession.builder.appName("SparkSQLExample").getOrCreate()

# Criar um DataFrame
data = [(1, "Ana", 25), (2, "Carlos", 30), (3, "João", 45)]
columns = ["id", "nome", "idade"]
df = spark.createDataFrame(data, columns)

# Registrar DataFrame como uma tabela temporária
df.createOrReplaceTempView("pessoas")
```

Agora, podemos executar consultas SQL diretamente:

```python
# Consultar os dados com SQL
resultado = spark.sql("SELECT * FROM pessoas")
resultado.show()
```

---

## 🔗 **Filtragem, Joins e Agregações com SQL**

### 1️⃣ **Filtragem de Dados**
Podemos usar SQL para aplicar filtros nos dados:

```python
# Selecionar pessoas com idade maior que 30
resultado = spark.sql("SELECT * FROM pessoas WHERE idade > 30")
resultado.show()
```

### 2️⃣ **Joins entre Tabelas**
Podemos combinar tabelas com diferentes tipos de joins:

```python
# Criar um segundo DataFrame
df_salarios = spark.createDataFrame([(1, 3000), (2, 4000), (3, 5000)], ["id", "salario"])
df_salarios.createOrReplaceTempView("salarios")

# Executar um JOIN entre as tabelas
resultado = spark.sql("""
    SELECT p.id, p.nome, p.idade, s.salario
    FROM pessoas p
    INNER JOIN salarios s
    ON p.id = s.id
""")
resultado.show()
```

### 3️⃣ **Agregações com SQL**
Consultas para sumarizar e agregar dados:

```python
# Calcular a idade média
resultado = spark.sql("SELECT AVG(idade) AS idade_media FROM pessoas")
resultado.show()
```

```python
# Contar o número de registros
resultado = spark.sql("SELECT COUNT(*) AS total_pessoas FROM pessoas")
resultado.show()
```

---

## ✨ **Funções Embutidas e UDFs no Spark SQL**

### 1️⃣ **Uso de Funções SQL Embutidas**
Podemos usar funções nativas do Spark SQL:

```python
# Converter nomes para maiúsculas
resultado = spark.sql("SELECT id, UPPER(nome) AS nome_maiusculo FROM pessoas")
resultado.show()
```

### 2️⃣ **Criar e Usar UDFs em SQL**
Podemos definir funções personalizadas e utilizá-las nas consultas:

```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Criar uma função personalizada
def prefixar_nome(nome):
    return f"Sr(a). {nome}"

# Registrar a função como UDF
prefixar_udf = udf(prefixar_nome, StringType())
spark.udf.register("prefixar_nome", prefixar_udf)

# Aplicar a UDF na consulta SQL
resultado = spark.sql("SELECT id, prefixar_nome(nome) AS nome_formatado FROM pessoas")
resultado.show()
```

---

## 📄 **Conclusão**

- O **Spark SQL** facilita a manipulação de dados estruturados usando SQL dentro do PySpark.
- Podemos registrar DataFrames como tabelas temporárias e executar consultas diretamente.
- Joins, agregações e funções embutidas são poderosas para análise de dados.
- UDFs permitem a criação de funções personalizadas dentro de consultas SQL.

Para mais informações, consulte a [documentação oficial do Spark SQL](https://spark.apache.org/docs/latest/sql-programming-guide.html).

