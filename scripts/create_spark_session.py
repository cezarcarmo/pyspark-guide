from pyspark.sql import SparkSession

def create_spark_session(app_name="pyspark-guide", master="local[*]"):
    """
    Cria uma SparkSession com as configurações especificadas.

    Args:
        app_name (str): Nome do aplicativo Spark.
        master (str): URL do master do Spark (e.g., "local[*]", "spark://master:7077").

    Returns:
        SparkSession: A SparkSession criada.
    """
    spark = SparkSession.builder \
      .appName(app_name) \
      .master(master) \
      .getOrCreate()
    return spark

if __name__ == "__main__":
    spark = create_spark_session()
    print(f"Versão do Spark: {spark.version}")
    spark.stop()

