
# PSProjects

## Estrutura do Projeto

```plaintext
PSProjects/
├── .gitignore
├── LICENSE
├── pyproject.toml              # Arquivo de configuração do Poetry
├── workspace.toml              # Arquivo de configuração do workspace (Polylith)
├── README.md
├── poetry.lock
├── requirements.txt            # Dependências do projeto
├── .flake8
├── setup.sh
├── start.sh
├── bases/                      # Diretório base
│   ├── .keep
├── components/                 # Componentes independentes
│   ├── api_client/
│   │   ├── __init__.py
│   │   ├── api_client.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── csv_generator/
│   │   ├── __init__.py
│   │   ├── csv_generator.py
│   ├── s3_uploader/
│   │   ├── __init__.py
│   │   ├── s3_uploader.py
│   ├── sftp_uploader/
│   │   ├── __init__.py
│   │   ├── sftp_uploader.py
│   ├── report_manager/
│   │   ├── __init__.py
│   │   ├── report_manager.py
│   ├── log_generate/
│   │   ├── __init__.py
│   │   ├── logs.py
├── projects/                   # Projetos específicos
│   ├── synapse_report_api/
│   │   ├── app.py              # Ponto de entrada da aplicação
│   │   ├── pyproject.toml
│   │   ├── ___init__.py
├── development/                # Diretório de desenvolvimento
│   ├── .keep
└─── test/                       # Módulo de testes
    ├── __init__.py

```

## Instalação

### Pré-requisitos

- **Python 3.10+**
- **Poetry** como gerenciador de pacotes.

### Passos para instalação

1. Clone o repositório:

   ```bash
   git clone https://AndersonJSilva@bitbucket.org/smengineering/psprojects.git
   cd synapse_reports
   ```

2. Instale as dependências usando o Poetry:

   ```bash
   poetry install
   ```

3. Crie um arquivo `.env` na raiz do projeto, com as variáveis de ambiente necessárias.

4. (Opcional) Ative o ambiente virtual gerenciado pelo Poetry:

   ```bash
   poetry shell
   ```

## Como Executar

Para rodar o projeto, use os seguintes comandos:

Dev:

```bash
poetry run python app.py --debug
```

Prod:

```bash
poetry run gunicorn --workers 3 app:app
```

## Estrutura Modular

O projeto utiliza a arquitetura **Polylith**, o que significa que está organizado em **componentes** e **projetos** reutilizáveis e independentes.

- **Core**: Contém a lógica central.
- **Components**: Componentes reutilizáveis.
- **Projects**: Projetos que integram os componentes para criar a funcionalidade final.

## Testes

Para rodar os testes, utilize:

```bash
poetry run pytest
```

Os testes estão localizados no diretório `tests/` e cobrem tanto os módulos centrais quanto os componentes.

## Logs

Os logs da aplicação são centralizados no diretório `logs/` e estão organizados por cliente. Cada cliente terá seu próprio arquivo de log, por exemplo:

```plaintext
logs/
├── cliente_1.log
├── cliente_2.log
```

Isso facilita a auditoria e o acompanhamento de eventos específicos para cada cliente.

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça o commit das suas alterações:
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Envie a sua branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
