FROM python:3.12.1

# Instala o Poetry
RUN pip install poetry

# Copia o código para o contêiner
COPY . /src
WORKDIR /src

# Instala as dependências definidas no pyproject.toml
RUN poetry install

# Expõe a porta 8501 para o Streamlit
EXPOSE 8501

# Comando padrão para iniciar o Streamlit
ENTRYPOINT ["poetry", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Alternativa para rodar um script Python diretamente
# ENTRYPOINT ["poetry", "run", "python", "main.py"]




