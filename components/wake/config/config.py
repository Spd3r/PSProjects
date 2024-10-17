import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Classe de configuração para armazenar credenciais e parâmetros."""

    def __init__(self, mailsender_id, customer_login):
        # Dados de acesso SFTP via variáveis de ambiente
        self.sftp_access = {
            "userName": os.getenv("SFTP_USERNAME"),
            "host": os.getenv("SFTP_HOST"),
            "pass": os.getenv("SFTP_PASSWORD")
        }

        # Dados de acesso S3 via variáveis de ambiente
        self.s3_access = {
            "bucket": os.getenv("S3_BUCKET"),
            "accessKey": os.getenv("S3_ACCESS_KEY"),
            "secretKey": os.getenv("S3_SECRET_KEY"),
            "prefix": os.getenv("S3_PREFIX"),
            "region": os.getenv("S3_REGION")
        }

        # URL da API
        self.api_url = "https://synapse-api.allin.com.br/transactional/push/send/sent/scroll"

        # Cabeçalhos da requisição
        self.api_headers = {
            "accept": "application/json",
            "Authorization": f"Basic {os.getenv('SYNAPSE_AUTHORIZATION')}"
        }

        # Parâmetros iniciais da API
        self.api_params = {
            "customerId": mailsender_id,
            "page": 1,
            "limit": "1"
        }

        # Payload inicial da API
        self.api_payload = {
            "createdAt": {}
        }

        # Diretórios locais
        self.local_reports_dir = os.path.abspath(f'./reports/{customer_login}-{mailsender_id}')
        self.local_log_dir = os.path.abspath(f"./logs/{mailsender_id}")

        # Diretório remoto SFTP
        self.remote_dir = f"/home/professional_service/synapse/{customer_login}-{mailsender_id}/"

    def ensure_directories(self):
        """Verifica e cria diretórios locais necessários."""
        reports_dir = os.path.abspath('./reports')
        logs_dir = os.path.abspath("./logs")
        if not os.path.exists(reports_dir):
            os.mkdir(reports_dir)
            text = f"Diretório '{reports_dir}' criado."
            print(text)
        else:
            text = f"Diretório '{reports_dir}' já existe."
            print(text)

        if not os.path.exists(self.local_reports_dir):
            os.mkdir(self.local_reports_dir)
            text = f"Diretório '{self.local_reports_dir}' criado."
            print(text)
        else:
            text = f"Diretório '{self.local_reports_dir}' já existe."
            print(text)
        """Validar diretório de Logs"""
        if not os.path.exists(logs_dir):
            os.mkdir(logs_dir)
            text = f"Diretório '{logs_dir}' criado."
            print(text)
        elif not os.path.exists(self.local_log_dir):
            os.mkdir(self.local_log_dir)

        else:
            text = f"Diretório '{logs_dir}' já existe."
            print(text)
