import paramiko

from components.PSComponents.log_generate import Log


class SFTPUploader:
    """Classe para realizar o upload de arquivos via SFTP."""

    def __init__(self, access, remote_dir, mailsender_id):
        self.access = access
        self.remote_dir = remote_dir
        self.ssh_client = None
        self.sftp = None
        self.log = Log(mailsender_id=mailsender_id)

    def connect(self):
        """Estabelece a conexão SFTP."""
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.load_system_host_keys()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            self.ssh_client.connect(
                hostname=self.access["host"],
                port=22,
                username=self.access["userName"],
                password=self.access["pass"]
            )
            self.sftp = self.ssh_client.open_sftp()
            text = "Conexão SFTP estabelecida com sucesso."
            self.log.post_log(text, "info")
            print()
        except paramiko.AuthenticationException:
            text = "Falha na autenticação ao conectar ao servidor SFTP."
            self.log.post_log(text, "error")
            print(text)
            exit(1)
        except paramiko.SSHException as ssh_exception:
            text = f"Erro na conexão SSH: {ssh_exception}"
            self.log.post_log(text, "error")
            print(text)
            exit(1)
        except Exception as e:
            text = f"Ocorreu um erro durante a conexão SFTP: {e}"
            self.log.post_log(text, "error")
            print(text)
            exit(1)

    def verify_remote_directory(self):
        """Verifica se o diretório remoto existe."""
        try:
            self.sftp.chdir(self.remote_dir)
            text = f"Diretório remoto '{self.remote_dir}' acessível."
            self.log.post_log(text, "info")
            print()

        except IOError:
            text = f"Diretório remoto '{self.remote_dir}' não encontrado ou sem permissões."
            self.log.post_log(text, "error")
            print(text)
            self.sftp.mkdir(self.remote_dir)
            text = f"Diretório remoto {self.remote_dir} criado com sucesso!"
            self.log.post_log(text, "info")
            print(text)

    def upload_file(self, local_file_path, remote_file_path):
        """Faz o upload do arquivo para o servidor remoto."""
        try:
            self.sftp.put(local_file_path, remote_file_path)
            text = f"Arquivo '{local_file_path}' enviado com sucesso para '{remote_file_path}'."
            self.log.post_log(text, "info")
            print()
        except FileNotFoundError as fnf_error:
            text = f"Erro: {fnf_error}"
            self.log.post_log(text, "error")
            print()
            self.close()
            exit(1)
        except IOError as io_error:
            text = f"Erro de I/O durante o upload: {io_error}"
            self.log.post_log(text, "error")
            print(text)
            self.close()
            exit(1)
        except Exception as e:
            text = f"Ocorreu um erro durante o upload do arquivo: {e}"
            self.log.post_log(text, "error")
            print(text)
            self.close()
            exit(1)

    def close(self):
        """Fecha as conexões SFTP e SSH."""
        if self.sftp:
            self.sftp.close()
        if self.ssh_client:
            self.ssh_client.close()
        text = "Conexão SFTP fechada."
        self.log.post_log(text, "info")
        print()
