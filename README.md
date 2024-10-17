
# Synapse Reports

## Descrição

O projeto **Synapse Reports** tem como objetivo consumir dados da plataforma Synapse, processá-los e gerar relatórios em formatos definidos. A aplicação possui componentes modulares e utiliza a arquitetura **Polylith** para gerenciar e escalar facilmente os módulos e funcionalidades.

## Estrutura do Projeto

```plaintext
synapse_reports/
├── .gitignore
├── .env                        # Configurações de variáveis de ambiente
├── app.py                      # Ponto de entrada da aplicação
├── requirements.txt            # Dependências do projeto
├── pyproject.toml              # Arquivo de configuração do Poetry
├── workspace.toml              # Arquivo de configuração do workspace (Polylith)
├── core/                       # Módulo principal do projeto
│   ├── __init__.py
│   ├── core_module_1.py
│   ├── core_module_2.py
├── components/                 # Componentes independentes
│   ├── __init__.py
│   ├── component_1.py
│   ├── component_2.py
├── projects/                   # Projetos específicos
│   ├── __init__.py
│   ├── project_1.py
├── reports/                    # Diretório para armazenar relatórios gerados
│   ├── __init__.py
│   ├── report_generator.py
├── logs/                       # Diretório de logs, com logs separados por cliente
│   ├── cliente_1.log
│   ├── cliente_2.log
├── tests/                      # Módulo de testes
│   ├── __init__.py
│   ├── test_core.py
│   ├── test_components.py
└── venv/                       # Ambiente virtual do Python
```

## Instalação

### Pré-requisitos

- **Python 3.10+**
- **Poetry** como gerenciador de pacotes.

### Passos para instalação

1. Clone o repositório:

   ```bash
   git clone git clone https://AndersonJSilva@bitbucket.org/andersonjsilva/relatorio-pushs-synapse.git
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
poetry run python app.py
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
