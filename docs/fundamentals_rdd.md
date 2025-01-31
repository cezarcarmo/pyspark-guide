# Fundamentos do PySpark: RDDs

Neste documento, exploramos os conceitos fundamentais dos **RDDs (Resilient Distributed Datasets)** no PySpark. Os RDDs são a estrutura básica de dados do Spark, permitindo processamento distribuído de grandes volumes de dados.

---

## 🔥 **O que é um RDD?**

- Um **RDD (Resilient Distributed Dataset)** é uma coleção distribuída de objetos imutáveis que podem ser processados em paralelo.
- RDDs são particionados em vários nós do cluster, permitindo alto desempenho.
- São tolerantes a falhas, pois o Spark pode recriar automaticamente os dados perdidos a partir das transformações aplicadas.

---

## 🛠 **Criando um RDD no PySpark**

Para criar um RDD, utilizamos o `SparkContext`, que é a base para interagir com o cluster do Spark.

### 1️⃣ **Criando um RDD a partir de uma lista**

```python
from pyspark.sql import SparkSession

# Criar SparkSession
spark = SparkSession.builder.appName("RDDExample").getOrCreate()
sc = spark.sparkContext  # Criar o SparkContext

# Criando um RDD a partir de uma lista
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Exibir os elementos do RDD
print("Elementos do RDD:", rdd.collect())
```

### 2️⃣ **Criando um RDD a partir de um arquivo**

Podemos carregar um arquivo de texto como um RDD:

```python
rdd_from_file = sc.textFile("data/exemplo.txt")
print("Primeiras linhas do RDD:", rdd_from_file.take(5))
```

---

## 🚀 **Transformações e Ações em RDDs**

Os RDDs no PySpark operam com dois tipos de operações:

### **🔹 Transformações (Lazy Evaluation)**
- As transformações são operações que definem um pipeline de processamento e só são executadas quando uma **ação** é chamada.
- Exemplos de transformações: `map()`, `filter()`, `flatMap()`, `reduceByKey()`.

**Exemplo:**
```python
# Aplicando uma transformação para dobrar os valores
doubled_rdd = rdd.map(lambda x: x * 2)
print("RDD após transformação:", doubled_rdd.collect())
```

### **🔹 Ações**
- As ações executam as operações no RDD e retornam um valor.
- Exemplos de ações: `collect()`, `count()`, `take()`, `reduce()`.

**Exemplo:**
```python
# Contando o número de elementos no RDD
print("Número de elementos no RDD:", rdd.count())

# Somando todos os valores do RDD
soma = rdd.reduce(lambda x, y: x + y)
print("Soma dos elementos do RDD:", soma)
```

---

## 🔄 **Particionamento e Otimização de RDDs**

O particionamento impacta diretamente a performance do PySpark. Podemos definir o número de partições ao criar um RDD:

```python
rdd_particionado = sc.parallelize(data, numSlices=3)
print("Número de partições:", rdd_particionado.getNumPartitions())
```

O particionamento correto evita **sobrecarga de memória** e melhora o desempenho em clusters distribuídos.

---

## 📄 **Conclusão**

- RDDs são a estrutura de dados mais fundamental do PySpark.
- Transformações são **lazy**, ou seja, são aplicadas apenas quando uma ação é chamada.
- O particionamento eficiente melhora a performance e escalabilidade do processamento de dados.

Para mais detalhes, consulte a [documentação oficial do Apache Spark](https://spark.apache.org/docs/latest/rdd-programming-guide.html).