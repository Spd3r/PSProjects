import os
import posixpath
from datetime import datetime, timedelta
from flask import jsonify

from components.PSComponents.apiClient import APIClient
from components.PSComponents.csv_generator import CSVGenerator
from components.PSComponents.sftp_uploader import SFTPUploader
from components.PSComponents.s3_uploader import S3Uploader
from components.PSComponents.log_generate import Log


class ReportManager:
    """Classe principal que gerencia todo o processo de coleta, geração e upload de relatórios."""

    def __init__(self, config):
        self.config = config
        self.format_yesterday = self.get_formatted_yesterday_date()

    def get_formatted_yesterday_date(self):
        """Obtém a data de ontem formatada."""
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        return yesterday.strftime('%Y-%m-%d')

    def prepare_payload(self):
        """Prepara o payload com as datas corretas."""
        self.config.api_payload["createdAt"]["begin"] = f"{self.format_yesterday} 00:00:00"
        self.config.api_payload["createdAt"]["end"] = f"{self.format_yesterday} 23:59:59"
        print(f"Payload preparado: {self.config.api_payload}")

    def run(self, mailsender_id, customer_login):
        """Executa todas as etapas do processo."""
        # Garantir que os diretórios necessários existem
        self.config.ensure_directories()

        # Preparar o payload com as datas corretas
        self.prepare_payload()

        # Criar os logs
        self.logs = Log(mailsender_id)

        # Definir caminhos dos arquivos
        local_file_path = os.path.abspath(
            f"reports/{customer_login}-{mailsender_id}/relatorioPushs{self.format_yesterday}.csv")
        remote_filename = f"relatorioPushs{self.format_yesterday}.csv"
        remote_file_path = posixpath.join(
            self.config.remote_dir, remote_filename)

        # Instanciar o cliente da API e coletar dados
        api_client = APIClient(
            url=self.config.api_url,
            headers=self.config.api_headers,
            params=self.config.api_params.copy(),  # Evita modificar o original
            payload=self.config.api_payload,
            mailsender_id=mailsender_id
        )
        client_response = api_client.fetch_data()
        keys = client_response["keys"]
        processed_data = client_response["processed_data"]

        if not api_client.list_result:
            print("Nenhum dado para gerar o CSV. Processo encerrado.")
            exit(1)

        # Instanciar o gerador de CSV e gerar o arquivo
        csv_generator = CSVGenerator(
            local_file_path=local_file_path,
            keys=keys,
            data=api_client.list_result
        )
        csv_generator.generate_csv()

        # Instanciar o uploader SFTP e realizar o upload
        sftp_uploader = SFTPUploader(
            access=self.config.sftp_access,
            remote_dir=self.config.remote_dir,
            mailsender_id=mailsender_id
        )
        sftp_uploader.connect()
        sftp_uploader.verify_remote_directory()
        sftp_uploader.upload_file(local_file_path, remote_file_path)
        sftp_uploader.close()

        # Instanciar o uploader S3 e realizar o upload
        s3_uploader = S3Uploader(access=self.config.s3_access)
        s3_uploader.connect()
        s3_object_name = f"{self.config.s3_access['prefix']}/{customer_login}/{remote_filename}"
        s3_uploader.upload_file(
            local_file_path, self.config.s3_access["bucket"], s3_object_name)
        # Script para validar se o arquivo foi inserido dentro do S3
        # s3_uploader.list_directory(self.config.s3_access["bucket"], self.config.s3_access["prefix"], "/")

        text = f'Total de registros processados: {processed_data}'
        path = f'Arquivo salvo em {remote_file_path}'

        self.logs.post_log(text, "info")

        return jsonify({
            "status": text,
            "path": path,
            "error": False,
        }), 200
