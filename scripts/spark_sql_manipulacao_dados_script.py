from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, upper
from pyspark.sql.types import StringType

# Criar SparkSession
spark = SparkSession.builder.appName("SparkSQLExample").getOrCreate()

# Criar DataFrame de exemplo
data = [(1, "Ana", 25), (2, "Carlos", 30), (3, "João", 45)]
columns = ["id", "nome", "idade"]
df = spark.createDataFrame(data, columns)

# Registrar DataFrame como tabela temporária
df.createOrReplaceTempView("pessoas")

# Consultar os dados com SQL
print("Consulta SQL - Todos os registros")
spark.sql("SELECT * FROM pessoas").show()

# Filtrar pessoas com idade maior que 30
print("Consulta SQL - Filtrar pessoas com idade > 30")
spark.sql("SELECT * FROM pessoas WHERE idade > 30").show()

# Criar um segundo DataFrame para Join
df_salarios = spark.createDataFrame([(1, 3000), (2, 4000), (3, 5000)], ["id", "salario"])
df_salarios.createOrReplaceTempView("salarios")

# Executar um INNER JOIN
print("Consulta SQL - Inner Join entre pessoas e salários")
spark.sql("""
    SELECT p.id, p.nome, p.idade, s.salario
    FROM pessoas p
    INNER JOIN salarios s
    ON p.id = s.id
""").show()

# Agregações com SQL
print("Consulta SQL - Média de idade")
spark.sql("SELECT AVG(idade) AS idade_media FROM pessoas").show()

print("Consulta SQL - Contagem de registros")
spark.sql("SELECT COUNT(*) AS total_pessoas FROM pessoas").show()

# Funções SQL embutidas
print("Consulta SQL - Converter nomes para maiúsculas")
spark.sql("SELECT id, UPPER(nome) AS nome_maiusculo FROM pessoas").show()

# Criar e registrar uma UDF
def prefixar_nome(nome):
    return f"Sr(a). {nome}"

prefixar_udf = udf(prefixar_nome, StringType())
spark.udf.register("prefixar_nome", prefixar_udf)

# Aplicar UDF na consulta SQL
print("Consulta SQL - Aplicar UDF para prefixar nomes")
spark.sql("SELECT id, prefixar_nome(nome) AS nome_formatado FROM pessoas").show()
