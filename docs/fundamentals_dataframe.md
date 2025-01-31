# Fundamentos do PySpark: DataFrames

Nesta seção, exploramos os conceitos fundamentais de **DataFrames** no PySpark. Os DataFrames são uma abstração mais poderosa que os RDDs, otimizados para consultas e operações estruturadas em grandes volumes de dados.

---

## 🔥 **O que é um DataFrame?**

- Um **DataFrame** é uma coleção distribuída de dados organizados em colunas, semelhante a uma tabela em um banco de dados relacional ou um dataframe do Pandas.
- Os DataFrames são imutáveis e distribuem automaticamente as operações entre nós do cluster Spark.
- Eles permitem:
  - Operações SQL diretamente no Spark.
  - Otimizações automáticas com o **Catalyst Optimizer**.

---

## 🛠 **Criando um DataFrame no PySpark**

### 1️⃣ **Criar um DataFrame a partir de uma lista**

```python
from pyspark.sql import SparkSession

# Criar SparkSession
spark = SparkSession.builder.appName("DataFrameExample").getOrCreate()

# Dados de exemplo
data = [(1, "Ana", 25), (2, "Carlos", 30), (3, "João", 45), (4, "Mariana", 35)]
columns = ["id", "nome", "idade"]

# Criar o DataFrame
df = spark.createDataFrame(data, columns)

# Exibir o DataFrame
df.show()
```

Saída esperada:
```
+---+--------+-----+
| id|    nome|idade|
+---+--------+-----+
|  1|     Ana|   25|
|  2|  Carlos|   30|
|  3|    João|   45|
|  4| Mariana|   35|
+---+--------+-----+
```

---

### 2️⃣ **Criar um DataFrame a partir de um arquivo CSV**

```python
# Ler um arquivo CSV
file_path = "data/exemplo.csv"
df_csv = spark.read.csv(file_path, header=True, inferSchema=True)

# Exibir o DataFrame
df_csv.show()
```

---

## 🚀 **Operações Básicas com DataFrames**

### **1. Seleção de Colunas**
```python
# Selecionar uma coluna específica
df.select("nome").show()

# Selecionar várias colunas
df.select("nome", "idade").show()
```

### **2. Filtrar Linhas**
```python
# Filtrar linhas onde a idade seja maior que 30
df.filter(df["idade"] > 30).show()
```

### **3. Ordenar Dados**
```python
# Ordenar os dados por idade (ascendente)
df.orderBy("idade").show()

# Ordenar por idade (descendente)
df.orderBy(df["idade"].desc()).show()
```

### **4. Agregações**
```python
from pyspark.sql.functions import avg, max

# Calcular a idade média
df.select(avg("idade").alias("idade_media")).show()

# Encontrar a maior idade
df.select(max("idade").alias("maior_idade")).show()
```

---

## 🔄 **Comparação: RDDs vs DataFrames**

| **Aspecto**       | **RDDs**                          | **DataFrames**                     |
|-------------------|-----------------------------------|------------------------------------|
| **Abstração**     | Dados distribuídos simples        | Dados estruturados (tabelas)       |
| **Performance**   | Menos otimizado                  | Otimizado com Catalyst Optimizer   |
| **Facilidade**    | Programação manual               | Operações SQL-like fáceis          |
| **Quando usar**   | Processamento não estruturado     | Dados estruturados e semi-estruturados |

---

## 📄 **Conclusão**

- Os DataFrames são mais fáceis de usar e muito mais otimizados do que os RDDs para processamento de dados estruturados.
- Permitem operações complexas como agregações, ordenações e filtros com pouca complexidade de código.

Para mais detalhes, consulte a [documentação oficial do PySpark SQL](https://spark.apache.org/docs/latest/sql-programming-guide.html).

