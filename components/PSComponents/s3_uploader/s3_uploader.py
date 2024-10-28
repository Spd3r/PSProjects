import boto3
from botocore.exceptions import NoCredentialsError, ClientError


class S3Uploader:
    """Classe para realizar o upload de arquivos para o Amazon S3."""

    def __init__(self, access):
        self.access = access
        self.s3_client = None

    def connect(self):
        """Estabelece a conexão com o S3."""
        try:
            self.s3_client = boto3.client(
                's3',
                aws_access_key_id=self.access["accessKey"],
                aws_secret_access_key=self.access["secretKey"],
                region_name=self.access["region"]

            )
            print("Conexão com o Amazon S3 estabelecida com sucesso.")
        except NoCredentialsError:
            print("Credenciais S3 não disponíveis.")
            exit(1)
        except Exception as e:
            print(f"Ocorreu um erro ao conectar ao S3: {e}")
            exit(1)

    def upload_file(self, local_file_path, bucket, object_name):
        """Faz o upload do arquivo para o S3."""
        try:
            self.s3_client.upload_file(local_file_path, bucket, object_name)
            print(
                f"Upload do arquivo '{local_file_path}' realizado com sucesso no bucket '{bucket}' como '{object_name}'.")
        except FileNotFoundError:
            print(f"O arquivo '{local_file_path}' não foi encontrado.")
            exit(1)
        except NoCredentialsError:
            print("Credenciais S3 não disponíveis.")
            exit(1)
        except ClientError as e:
            print(f"Erro ao realizar o upload para o S3: {e}")
            exit(1)
        except Exception as e:
            print(f"Ocorreu um erro durante o upload para o S3: {e}")
            exit(1)

    def list_directory(self, bucket, prefix, delimiter):
        try:
            res = self.s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix, Delimiter=delimiter)
            print("Arquivos no S3:")
            for file in res["Contents"]:
                print(file["Key"])

        except Exception as e:
            print(f"Ocorreu um erro ao listar o conteúdo dentro do S3: {e}")
            exit(1)
