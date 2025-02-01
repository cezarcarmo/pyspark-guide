# Transformações e Ações em DataFrames

Nesta seção, exploramos transformações e ações aplicáveis a **DataFrames** no PySpark. Transformações são operações que geram novos DataFrames, enquanto ações executam computações e retornam resultados.

---

## 🔄 **Transformações em DataFrames**

### 1️⃣ **Adicionar uma Nova Coluna com `withColumn`**
- Usado para criar ou modificar colunas no DataFrame.

```python
from pyspark.sql.functions import col

# Adicionar uma nova coluna chamada 'idade_em_2025'
df = df.withColumn("idade_em_2025", col("idade") + 2)
df.show()
```

### 2️⃣ **Remover uma Coluna com `drop`**
- Remove colunas desnecessárias do DataFrame.

```python
# Remover a coluna 'idade_em_2025'
df = df.drop("idade_em_2025")
df.show()
```

### 3️⃣ **Selecionar Valores Únicos com `distinct`**
- Retorna apenas os valores únicos de um DataFrame.

```python
# Selecionar valores únicos com base na coluna 'idade'
df.distinct().show()
```

### 4️⃣ **Renomear Colunas**
- Renomeia colunas do DataFrame.

```python
# Renomear a coluna 'nome' para 'nome_completo'
df = df.withColumnRenamed("nome", "nome_completo")
df.show()
```

---

## 🛠 **Ações em DataFrames**

### 1️⃣ **Contar Registros com `count`**
- Retorna o número total de registros no DataFrame.

```python
# Contar o número de registros no DataFrame
print("Número de registros:", df.count())
```

### 2️⃣ **Coletar Dados Localmente com `collect`**
- Traz todos os registros para o driver como uma lista (use com cuidado para grandes DataFrames).

```python
# Coletar os dados do DataFrame para uma lista
resultados = df.collect()
for linha in resultados:
    print(linha)
```

### 3️⃣ **Exibir Amostras com `show` e `take`**
- `show` exibe os dados em formato tabular no console.
- `take` retorna um número especificado de registros como uma lista.

```python
# Exibir os 5 primeiros registros
df.show(5)

# Pegar os 3 primeiros registros
df.take(3)
```

---

## 🌟 **Exemplo Completo**
### Código para Testar:

1. Criação de DataFrame:
   ```python
   from pyspark.sql import SparkSession
   spark = SparkSession.builder.appName("TransformacoesAcoes").getOrCreate()

   # Criar DataFrame
data = [(1, "Ana", 25), (2, "Carlos", 30), (3, "João", 45), (4, "Mariana", 35)]
columns = ["id", "nome", "idade"]
df = spark.createDataFrame(data, columns)
   ```

2. Aplicar Transformações:
   ```python
   from pyspark.sql.functions import col

   # Adicionar uma nova coluna
df = df.withColumn("idade_em_2025", col("idade") + 2)
   ```

3. Executar Ações:
   ```python
   # Contar registros
   print("Número de registros:", df.count())

   # Exibir DataFrame
   df.show()
   ```

---

## 📄 **Conclusão**

- As transformações em DataFrames criam novos DataFrames sem alterar os originais.
- Ações executam operações e retornam resultados ao driver.
- Combinando ambas, é possível manipular dados de maneira eficiente no PySpark.

Para mais informações, consulte a [documentação oficial do PySpark SQL](https://spark.apache.org/docs/latest/sql-programming-guide.html).

