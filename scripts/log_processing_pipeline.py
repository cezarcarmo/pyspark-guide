from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract, col, count, date_format
import os

# Inicializar SparkSession
spark = SparkSession.builder \
    .appName("Log Processing Pipeline") \
    .getOrCreate()

print("SparkSession iniciada.")

# Criar um exemplo de arquivo de log
log_data = [
    '192.168.0.1 - - [09/Feb/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1043',
    '192.168.0.2 - - [09/Feb/2025:10:05:00 +0000] "POST /submit HTTP/1.1" 200 2326',
    '192.168.0.1 - - [09/Feb/2025:10:10:00 +0000] "GET /about.html HTTP/1.1" 200 5321',
    '192.168.0.3 - - [09/Feb/2025:10:15:00 +0000] "GET /index.html HTTP/1.1" 200 1043',
    '192.168.0.2 - - [09/Feb/2025:10:20:00 +0000] "GET /contact.html HTTP/1.1" 200 789'
]

log_file_path = "/home/cezarcarmo/repos/pyspark-guide/data/logfile.log"
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
with open(log_file_path, 'w') as file:
    for line in log_data:
        file.write(line + '\n')

print(f"Arquivo de log criado em {log_file_path}")

# 1. Leitura dos arquivos de log em formato texto
logs_df = spark.read.text(log_file_path)
print("Leitura dos arquivos de log concluída.")

# 2. Parsing dos logs para extrair campos relevantes (IP, timestamp, URL, etc.)
logs_df = logs_df.withColumn("ip", regexp_extract(col("value"), r'^(\S+)', 1)) \
                 .withColumn("timestamp", regexp_extract(col("value"), r'\[(.*?)\]', 1)) \
                 .withColumn("url", regexp_extract(col("value"), r'\"(GET|POST) (.*?) HTTP', 2))
print("Parsing dos logs concluído.")

# 3. Transformações para agregar dados e calcular métricas
# Contagem de acessos por IP
ip_counts_df = logs_df.groupBy("ip").agg(count("*").alias("access_count"))
print("Contagem de acessos por IP concluída.")

# Páginas mais acessadas
url_counts_df = logs_df.groupBy("url").agg(count("*").alias("access_count"))
print("Contagem de acessos por URL concluída.")

# Horários de pico de acesso
logs_df = logs_df.withColumn("hour", date_format(col("timestamp"), "HH"))
hourly_access_df = logs_df.groupBy("hour").agg(count("*").alias("access_count"))
print("Contagem de acessos por hora concluída.")

# 4. Escrita dos resultados em um formato estruturado (CSV, Parquet, etc.)
output_path = "/home/cezarcarmo/repos/pyspark-guide/data/output"
os.makedirs(output_path, exist_ok=True)
ip_counts_df.write.csv(os.path.join(output_path, "ip_counts.csv"), mode="overwrite", header=True)
url_counts_df.write.csv(os.path.join(output_path, "url_counts.csv"), mode="overwrite", header=True)
hourly_access_df.write.csv(os.path.join(output_path, "hourly_access.csv"), mode="overwrite", header=True)
print(f"Resultados escritos em {output_path}")

# Finalizar SparkSession
spark.stop()
print("SparkSession finalizada.")