# Comparação: Pandas vs PySpark

**Pandas** e **PySpark** são ferramentas populares para manipulação de dados, mas foram projetadas para cenários diferentes. Abaixo está uma comparação detalhada que pode ajudar a escolher qual ferramenta utilizar em diferentes contextos.

---

## 🔑 **Diferenças Fundamentais**

| Característica               | Pandas                                   | PySpark                                  |
|------------------------------|------------------------------------------|------------------------------------------|
| **Volume de Dados**          | Funciona bem com dados que cabem na memória local. | Projetado para lidar com grandes volumes de dados em clusters. |
| **Processamento**            | Processamento em um único nó (local).   | Processamento distribuído em múltiplos nós.                   |
| **Velocidade**               | Rápido para pequenos datasets.          | Escalável e eficiente para grandes datasets.                  |
| **API**                      | Simples e intuitiva, baseado em Python. | Similar ao Pandas, mas com suporte a operações distribuídas.   |
| **Integração**               | Ideal para análises locais e pipelines menores. | Integra-se com Hadoop, Spark SQL, MLlib, etc.                |
| **Casos de Uso**             | Exploração e pré-processamento de dados em máquinas locais. | ETL, análise de Big Data e aprendizado de máquina em larga escala. |

---

## 🚀 **Exemplo Prático: Comparação em Código**

### 1️⃣ **Leitura de Dados**

#### Usando Pandas:
```python
import pandas as pd

# Ler um arquivo CSV
file_path = "data/exemplo.csv"
df = pd.read_csv(file_path)
print(df.head())
```

#### Usando PySpark:
```python
from pyspark.sql import SparkSession

# Criar uma SparkSession
spark = SparkSession.builder.appName("ExemploPySpark").getOrCreate()

# Ler um arquivo CSV
file_path = "data/exemplo.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)
df.show(5)
```

---

### 2️⃣ **Operações Básicas**

#### Filtro por Condição

**Pandas:**
```python
# Filtrar linhas onde a idade é maior que 30
filtered_df = df[df['idade'] > 30]
print(filtered_df)
```

**PySpark:**
```python
# Filtrar linhas onde a idade é maior que 30
filtered_df = df.filter(df.idade > 30)
filtered_df.show()
```

---

### 3️⃣ **Agregações**

**Pandas:**
```python
# Calcular a média de idade por grupo
mean_age = df.groupby('grupo')['idade'].mean()
print(mean_age)
```

**PySpark:**
```python
# Calcular a média de idade por grupo
df.groupBy("grupo").avg("idade").show()
```

---

## 📊 **Quando Usar Cada Ferramenta**

| Cenário                               | Ferramenta Recomendada |
|---------------------------------------|-------------------------|
| Dados pequenos, análise rápida        | Pandas                 |
| Processamento de grandes volumes de dados | PySpark                |
| Integração com ferramentas de Big Data | PySpark                |
| Análise local e prototipagem          | Pandas                 |

---

## 🔥 **Conclusão**

- **Pandas** é ideal para análises locais rápidas e prototipagem.
- **PySpark** é a escolha certa para grandes volumes de dados e cenários distribuídos.

Escolha a ferramenta com base no tamanho do dataset e no contexto do seu projeto!

