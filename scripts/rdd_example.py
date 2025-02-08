from pyspark.sql import SparkSession

# Criar SparkSession
spark = SparkSession.builder.appName("RDDExample").getOrCreate()
sc = spark.sparkContext  # Criar o SparkContext

# Criando um RDD a partir de uma lista
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Exibir os elementos do RDD
print("Elementos do RDD:", rdd.collect())

# Aplicando uma transformação para dobrar os valores
doubled_rdd = rdd.map(lambda x: x * 2)
print("RDD após transformação:", doubled_rdd.collect())

# Contando o número de elementos no RDD
print("Número de elementos no RDD:", rdd.count())

# Somando todos os valores do RDD
soma = rdd.reduce(lambda x, y: x + y)
print("Soma dos elementos do RDD:", soma)

# Criando um RDD a partir de um arquivo de texto
rdd_from_file = sc.textFile("/home/cezarcarmo/repos/pyspark-guide/data/exemplo.csv")
print("Primeiras linhas do RDD:", rdd_from_file.take(5))

# Definindo número de partições
rdd_particionado = sc.parallelize(data, numSlices=3)
print("Número de partições:", rdd_particionado.getNumPartitions())
