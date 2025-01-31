# Configuração do Ambiente PySpark

Este documento detalha os passos para configurar um ambiente de desenvolvimento PySpark utilizando **Conda**.

## 🔥 Criando o Ambiente Virtual com Conda

1. **Criar um ambiente Conda chamado `pyspark-env`**:
   ```bash
   conda create --name pyspark-env python=3.8
   ```
2. **Ativar o ambiente**:
   ```bash
   conda activate pyspark-env
   ```
3. **Instalar as dependências**:
   ```bash
   conda install -c conda-forge pyspark jupyter findspark
   ```

## 🖥 Configuração no VSCode

1. Abra o **VSCode** e instale as extensões:
   - **Python**
   - **Jupyter**
2. Selecione o ambiente virtual no VSCode:
   - Pressione `Ctrl+Shift+P`
   - Pesquise **Python: Select Interpreter**
   - Escolha `pyspark-env` criado com Conda

## 🚀 Testando a Configuração com Jupyter Notebook

1. **Instalar o Jupyter Notebook no ambiente**:
   ```bash
   pip install jupyter
   ```
2. **Abrir o Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```
3. **Criar um novo notebook e rodar o código abaixo para testar a integração**:
   ```python
   import findspark
   findspark.init()

   from pyspark.sql import SparkSession

   spark = SparkSession.builder.appName("TestePySpark").getOrCreate()
   print(spark.version)
   ```

Se a versão do Spark for exibida sem erros, seu ambiente está pronto! 🎉

