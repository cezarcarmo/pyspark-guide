from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg
import os
import random

# Inicializar SparkSession
spark = SparkSession.builder \
    .appName("Large Scale Data Processing") \
    .config("spark.sql.shuffle.partitions", "8") \
    .getOrCreate()

print("SparkSession iniciada.")

# Criar um exemplo de arquivo CSV de dados massivos
large_data_file_path = "/home/cezarcarmo/repos/pyspark-guide/data/large_data.csv"
os.makedirs(os.path.dirname(large_data_file_path), exist_ok=True)

num_records = 1000000  # Número de registros a serem gerados
with open(large_data_file_path, 'w') as file:
    file.write("id,value\n")
    for i in range(1, num_records + 1):
        value = random.randint(1, 1000)
        file.write(f"{i},{value}\n")

print(f"Arquivo de dados massivos criado em {large_data_file_path}")

# 1. Configuração de um cluster Spark (local ou em cloud)
# (Para este exemplo, estamos usando um cluster local configurado acima)

# 2. Leitura de dados em diferentes formatos (CSV, Parquet, JSON, etc.)
large_data_df = spark.read.csv(large_data_file_path, header=True, inferSchema=True)
print("Leitura dos dados massivos concluída.")
large_data_df.show(5)

# 3. Aplicação de transformações e ações em DataFrames para processar os dados
# Exemplo de agregação: soma e média dos valores
aggregated_df = large_data_df.groupBy().agg(sum("value").alias("total_value"), avg("value").alias("average_value"))
print("Agregação dos dados concluída.")
aggregated_df.show()

# 4. Otimização do desempenho utilizando técnicas como particionamento, cache e broadcast joins
# Particionamento
large_data_df = large_data_df.repartition(4)
print("Reparticionamento dos dados concluído.")

# Cache
large_data_df.cache()
print("Cache dos dados concluído.")

# 5. Escrita dos resultados em um formato otimizado para consultas rápidas (Parquet, ORC, etc.)
output_path = "/home/cezarcarmo/repos/pyspark-guide/data/output"
os.makedirs(output_path, exist_ok=True)
aggregated_df.write.parquet(os.path.join(output_path, "aggregated_data.parquet"), mode="overwrite")
print(f"Resultados escritos em {output_path}")

# Verificar se os arquivos foram escritos
print("Verificando arquivos de saída...")
for file_name in ["aggregated_data.parquet"]:
    file_path = os.path.join(output_path, file_name)
    if os.path.exists(file_path):
        print(f"Arquivo {file_name} criado com sucesso.")
    else:
        print(f"Erro: Arquivo {file_name} não encontrado.")

# Finalizar SparkSession
spark.stop()
print("SparkSession finalizada.")