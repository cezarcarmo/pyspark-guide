# Introdução ao PySpark

Este documento detalha os passos para criar um exemplo básico de **PySpark** com a criação de uma **SparkSession** e operações iniciais com **DataFrames**.

---

## 🔥 Passos para Configuração

### 1️⃣ Criar um Arquivo de Script no Repositório
1. Dentro da pasta `scripts/`, crie um arquivo chamado `create_spark_session.py`.
2. Certifique-se de que o ambiente Conda (`pyspark-env`) está ativado:
   ```bash
   conda activate pyspark-env
   ```

---

### 2️⃣ Código Inicial: Criando o SparkSession
Adicione o seguinte código no arquivo `create_spark_session.py`:

```python
from pyspark.sql import SparkSession

# Criar uma SparkSession
spark = SparkSession.builder \
    .appName("ExemploPySpark") \
    .getOrCreate()

# Mostrar informações básicas sobre a SparkSession
print("Spark Version:", spark.version)
print("Spark App Name:", spark.sparkContext.appName)

# Encerrar a SparkSession
spark.stop()
```

---

### 3️⃣ Testar o Código
1. No terminal do VSCode, execute o script:
   ```bash
   python scripts/create_spark_session.py
   ```
2. Verifique se a versão do Spark e o nome da aplicação são exibidos corretamente.

---

### 4️⃣ Exemplo com DataFrames
Adicione operações com DataFrames no arquivo `create_spark_session.py`:

```python
from pyspark.sql import SparkSession

# Criar uma SparkSession
spark = SparkSession.builder \
    .appName("ExemploPySpark") \
    .getOrCreate()

# Exemplo: Criar um DataFrame a partir de um arquivo CSV
file_path = "data/exemplo.csv"

# Criar DataFrame
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Mostrar as primeiras linhas
print("Exibindo as 5 primeiras linhas do DataFrame:")
df.show(5)

# Exibir o esquema do DataFrame
print("Esquema do DataFrame:")
df.printSchema()

# Encerrar a SparkSession
spark.stop()
```

---

### 5️⃣ Criar um Arquivo de Dados
1. Na pasta `data/`, crie um arquivo chamado `exemplo.csv` com o seguinte conteúdo:
   ```csv
   id,nome,idade
   1,Ana,25
   2,Carlos,30
   3,João,45
   4,Mariana,35
   5,Fernando,50
   ```

2. Teste o script novamente:
   ```bash
   python scripts/create_spark_session.py
   ```

O resultado deve exibir as 5 primeiras linhas do DataFrame e o esquema dos dados.

---

### 6️⃣ Versionamento com Git
1. Adicione os arquivos ao controle de versão:
   ```bash
   git add scripts/create_spark_session.py data/exemplo.csv
   ```
2. Faça um commit:
   ```bash
   git commit -m "Adiciona exemplo básico de SparkSession e DataFrame"
   ```
3. Envie as alterações para o repositório remoto:
   ```bash
   git push origin develop
   ```

---

Seguindo esses passos, você terá um exemplo funcional de **PySpark** configurado no projeto!

