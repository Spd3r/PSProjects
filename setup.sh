#!/bin/bash

# Verifica se o Poetry está instalado
if ! command -v poetry &> /dev/null
then
    echo "Poetry não está instalado. Instale o Poetry antes de continuar."
    exit 1
fi

# Caminho do diretório do projeto (ajuste conforme necessário)
PROJECT_DIR="$(pwd)"

# Navega até o diretório do projeto
cd "$PROJECT_DIR"

# Instala as dependências do projeto usando o Poetry
echo "Instalando dependências do projeto..."
poetry install

# Verifica se a instalação foi bem-sucedida
if [ $? -ne 0 ]; then
    echo "Erro na instalação das dependências."
    exit 1
fi

# Ativa o ambiente virtual do Poetry
echo "Ativando ambiente virtual do Poetry..."
poetry shell

echo "Instalação concluída com sucesso!"
