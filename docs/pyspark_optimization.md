# 7️⃣ Otimização e Performance em PySpark

A otimização do desempenho no PySpark é essencial para lidar com grandes volumes de dados de forma eficiente. Nesta seção, abordaremos técnicas avançadas para melhorar a performance dos seus jobs Spark.

## 1️⃣ Gerenciamento de Partições
O PySpark trabalha com dados distribuídos, e o gerenciamento adequado de partições pode melhorar significativamente a performance.

### 🔹 Verificando o número de partições
```python
print(f"Número de partições: {df.rdd.getNumPartitions()}")
```

### 🔹 Reparticionamento Dinâmico
- **`repartition(n)`**: Redistribui os dados em *n* partições (útil para balanceamento de carga).
- **`coalesce(n)`**: Reduz o número de partições sem movimentar excessivamente os dados.

```python
# Aumentando o número de partições
optimized_df = df.repartition(10)

# Reduzindo o número de partições
optimized_df = df.coalesce(2)
```

📌 **Dica**: Use `repartition()` para aumentar partições e `coalesce()` para reduzir, pois `coalesce()` evita movimentação excessiva de dados.

---

## 2️⃣ Broadcast Joins e Cache
### 🔹 Uso de Broadcast Join
Quando uma das tabelas é pequena, o Spark permite **broadcast join**, enviando essa tabela para todos os nós do cluster.

```python
from pyspark.sql.functions import broadcast

small_df = spark.read.csv("data/pequeno.csv", header=True, inferSchema=True)
large_df = spark.read.parquet("data/grande.parquet")

joined_df = large_df.join(broadcast(small_df), "id", "inner")
```

📌 **Dica**: Use `broadcast()` para tabelas pequenas e evite `shuffle join`, que pode ser custoso em termos de tempo e memória.

### 🔹 Uso de Cache e Persistência
Se um DataFrame for utilizado várias vezes, armazená-lo em memória pode reduzir o tempo de processamento.

```python
# Cache na memória
cached_df = df.cache()
cached_df.count()  # Força a materialização do cache

# Persistência em memória e disco
from pyspark import StorageLevel
df.persist(StorageLevel.MEMORY_AND_DISK)
```

📌 **Dica**: Use `cache()` quando for reutilizar um DataFrame várias vezes no mesmo job.

---

## 3️⃣ Uso do Catalyst Optimizer
O **Catalyst Optimizer** é o mecanismo interno do Spark SQL que otimiza automaticamente as consultas. Para garantir melhor performance:

### 🔹 Analisar o plano de execução
Antes de rodar uma operação pesada, verifique como o Spark planeja executar a consulta:
```python
df.explain(True)
```

### 🔹 Evitar Colunas Desnecessárias
Ao invés de carregar todas as colunas, selecione apenas as necessárias:
```python
optimized_df = df.select("id", "nome", "idade")
```

### 🔹 Uso de Parquet e Formatos Otimizados
Os formatos de armazenamento impactam a performance. Prefira **Parquet** ou **ORC** ao invés de CSV:
```python
df.write.mode("overwrite").parquet("data/optimized.parquet")
```

📌 **Dica**: O Catalyst aplica otimizações automaticamente, mas boas práticas de modelagem podem ajudar ainda mais.

---

## 4️⃣ Melhores Práticas para Performance
✅ **Evitar `collect()` sempre que possível**: Ele transfere os dados para o driver, o que pode causar estouro de memória.
✅ **Filtrar dados antes de joins e agregações** para reduzir a quantidade de dados processados.
✅ **Escrever arquivos em partições** para leitura eficiente:
```python
df.write.partitionBy("ano", "mes").parquet("data/partitioned_output")
```
✅ **Evitar UDFs sempre que possível**: Prefira funções nativas do Spark SQL.

---

## 📌 Conclusão
Seguindo essas estratégias, seu código PySpark será muito mais eficiente, escalável e rápido. A otimização adequada pode reduzir custos computacionais e melhorar a experiência de análise de dados em larga escala. 🚀

