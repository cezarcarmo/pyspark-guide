from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when
import os

# Inicializar SparkSession
spark = SparkSession.builder \
    .appName("E-commerce Data Analysis") \
    .getOrCreate()

print("SparkSession iniciada.")

# Criar um exemplo de arquivo CSV de transações
transaction_data = """customer_id,transaction_id,product_id,quantity,price,timestamp
1,1001,2001,2,50.0,2025-02-09 10:00:00
2,1002,2002,1,30.0,2025-02-09 10:05:00
1,1003,2003,1,20.0,2025-02-09 10:10:00
3,1004,2001,3,50.0,2025-02-09 10:15:00
2,1005,2004,2,15.0,2025-02-09 10:20:00
"""

transaction_file_path = "/home/cezarcarmo/repos/pyspark-guide/data/transactions.csv"
os.makedirs(os.path.dirname(transaction_file_path), exist_ok=True)
with open(transaction_file_path, 'w') as file:
    file.write(transaction_data)

print(f"Arquivo de transações criado em {transaction_file_path}")

# 1. Leitura dos dados de transações em formato CSV
transactions_df = spark.read.csv(transaction_file_path, header=True, inferSchema=True)
print("Leitura dos dados de transações concluída.")
transactions_df.show()

# 2. Limpeza e transformação dos dados (remoção de duplicatas, tratamento de valores nulos, etc.)
transactions_df = transactions_df.dropDuplicates()
transactions_df = transactions_df.na.fill({'quantity': 0, 'price': 0.0})
print("Limpeza e transformação dos dados concluída.")
transactions_df.show()

# 3. Análise exploratória dos dados para identificar padrões e tendências
# Contagem de transações por cliente
customer_transactions_df = transactions_df.groupBy("customer_id").agg(count("*").alias("transaction_count"))
print("Contagem de transações por cliente concluída.")
customer_transactions_df.show()

# Produtos mais vendidos
product_sales_df = transactions_df.groupBy("product_id").agg(count("*").alias("sales_count"))
print("Contagem de produtos mais vendidos concluída.")
product_sales_df.show()

# 4. Aplicação de algoritmos de machine learning para segmentação de clientes e previsão de churn
# (Exemplo simplificado: contagem de clientes com mais de uma transação)
churn_df = customer_transactions_df.withColumn("churn_risk", when(col("transaction_count") > 1, 0).otherwise(1))
print("Análise de churn concluída.")
churn_df.show()

# Escrita dos resultados em um formato estruturado (CSV, Parquet, etc.)
output_path = "/home/cezarcarmo/repos/pyspark-guide/data/output"
os.makedirs(output_path, exist_ok=True)
customer_transactions_df.write.csv(os.path.join(output_path, "customer_transactions.csv"), mode="overwrite", header=True)
product_sales_df.write.csv(os.path.join(output_path, "product_sales.csv"), mode="overwrite", header=True)
churn_df.write.csv(os.path.join(output_path, "churn_analysis.csv"), mode="overwrite", header=True)
print(f"Resultados escritos em {output_path}")

# Verificar se os arquivos foram escritos
print("Verificando arquivos de saída...")
for file_name in ["customer_transactions.csv", "product_sales.csv", "churn_analysis.csv"]:
    file_path = os.path.join(output_path, file_name)
    if os.path.exists(file_path):
        print(f"Arquivo {file_name} criado com sucesso.")
    else:
        print(f"Erro: Arquivo {file_name} não encontrado.")

# Finalizar SparkSession
spark.stop()
print("SparkSession finalizada.")