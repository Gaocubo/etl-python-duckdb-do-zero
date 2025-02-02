import os
import gdown
import duckdb
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

from duckdb import DuckDBPyRelation
from pandas import DataFrame

from datetime import datetime

url_pasta = 'https://drive.google.com/drive/folders/1I0gkzrUS6Bast_nX95wDB4_qe1Lwwszw'
diretorio_local = './pasta_gdown'

# Função para baixar arquivos do google drive
def baixar_os_arquivos_do_google_drive(url_pasta, diretorio_local):
    os.makedirs(diretorio_local, exist_ok=True)
    gdown.download_folder(url_pasta, output=diretorio_local, quiet=False, use_cookies=False)

# Função para listar arquivos CSV no diretório especificado
def listar_arquivos_csv(diretorio):
    arquivos_csv = []
    todos_os_arquivos = os.listdir(diretorio)
    for arquivo in todos_os_arquivos:
        if arquivo.endswith(".csv"):
            caminho_completo = os.path.join(diretorio, arquivo)
            arquivos_csv.append(caminho_completo)
    #print(arquivos_csv)
    return arquivos_csv

# Função para ler um arquivo CSV e retornar um DataFrame duckdb
def ler_csv(caminho_do_arquivo):
    dataframe_duckdb = duckdb.read_csv(caminho_do_arquivo)
    return dataframe_duckdb

# Função para adicionar uma coluna de total de vendas
def transformar(df: DuckDBPyRelation) -> DataFrame:
    # Executa a consulta SQL que inclui a nova coluna, operando sobre a tabela virtual
    df_transformado = duckdb.sql("SELECT *, quantidade * valor AS total_vendas FROM df").df()

    print(df_transformado)
    # Remove o registro da tabela virtual para limpeza
    return df_transformado

# Transformacao


if __name__ == "__main__":
    url_pasta = 'https://drive.google.com/drive/folders/1I0gkzrUS6Bast_nX95wDB4_qe1Lwwszw'
    diretorio_local = './pasta_gdown'
    #baixar_os_arquivos_do_google_drive(url_pasta,diretorio_local)
    arquivos = listar_arquivos_csv(diretorio_local)
    dataframe_duckdb =  ler_csv(arquivos)
    transformar(dataframe_duckdb)