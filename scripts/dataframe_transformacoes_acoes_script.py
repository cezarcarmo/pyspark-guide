from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os

# Criar diretório para salvar o arquivo CSV
os.makedirs("data", exist_ok=True)

# Criar arquivo CSV de exemplo
csv_content = "id,nome,idade\n1,Ana,25\n2,Carlos,30\n3,João,45\n4,Mariana,35\n"
with open("data/exemplo_transformacoes_acoes.csv", "w") as f:
    f.write(csv_content)
    
# Forçar o Spark a usar o interpretador correto
os.environ["PYSPARK_PYTHON"] = "C:\\Users\\cezar\\anaconda3\\envs\\pyspark-env\\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "C:\\Users\\cezar\\anaconda3\\envs\\pyspark-env\\python.exe"

# Iniciar SparkSession
spark = SparkSession.builder.appName("DataFrameTransformacoesAcoes").getOrCreate()

# Criar DataFrame de exemplo
data = [(1, "Ana", 25), (2, "Carlos", 30), (3, "João", 45), (4, "Mariana", 35)]
columns = ["id", "nome", "idade"]
df = spark.createDataFrame(data, columns)

# Exibir DataFrame inicial
df.show()

# Transformações
print("### Transformações ###")

# Adicionar nova coluna
print("Adicionando coluna 'idade_em_2025':")
df = df.withColumn("idade_em_2025", col("idade") + 2)
df.show()

# Remover coluna
print("Removendo coluna 'idade_em_2025':")
df = df.drop("idade_em_2025")
df.show()

# Selecionar valores únicos
df_distinct = df.distinct()
print("DataFrame com valores únicos:")
df_distinct.show()

# Renomear coluna
print("Renomeando coluna 'nome' para 'nome_completo':")
df = df.withColumnRenamed("nome", "nome_completo")
df.show()

# Ações
print("### Ações ###")

# Contar registros
print("Número de registros no DataFrame:", df.count())

# Coletar dados localmente
print("Coletando dados para uma lista:")
resultados = df.collect()
for linha in resultados:
    print(linha)

# Exibir amostras
print("Exibindo os 2 primeiros registros:")
df.show(2)

print("Pegando os 3 primeiros registros:")
print(df.take(3))

# Ler arquivo CSV
print("### Lendo arquivo CSV ###")
df_csv = spark.read.csv("data/exemplo_transformacoes_acoes.csv", header=True, inferSchema=True)
df_csv.show()
