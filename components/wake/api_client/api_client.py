import requests
import json


from tqdm import tqdm
from components.wake.log_generate import Log


class APIClient:
    """Classe para interagir com a API e coletar dados."""

    def __init__(self, url, headers, params, payload, mailsender_id):
        self.url = url
        self.headers = headers
        self.params = params
        self.payload = payload
        self.list_result = []
        self.log = Log(mailsender_id=mailsender_id)

    def fetch_data(self):
        """Realiza a requisição à API e coleta os dados com paginação."""
        try:
            # Requisição inicial para obter totalPages e chaves dos dados
            response = requests.post(
                self.url,
                params=self.params,
                headers=self.headers,
                data=json.dumps(self.payload)
            )
            response.raise_for_status()
            response_data = response.json()

            total_pages = response_data.get("totalPages", 0)
            result = response_data.get("result", [])

            if not result:
                text = "Nenhum dado retornado pela API na requisição inicial."
                self.log.post_log(text, "error")
                print(text)
                return None

            # Extrai as chaves do primeiro item para uso no CSV
            keys = list(result[0].keys())

            # Ajusta totalPages e limit se necessário
            if total_pages % 1000 > 0:
                total_pages = int(total_pages / 1000) + 1
                self.params["limit"] = "1000"

            # Coleta dados de todas as páginas com barra de progresso
            for page in tqdm(range(1, total_pages + 1), desc="Progresso"):
                text = f"{page}/{total_pages} de páginas Processadas"
                self.log.post_log(text, "info")
                response = requests.post(
                    self.url,
                    params=self.params,
                    headers=self.headers,
                    data=json.dumps(self.payload)
                )
                response.raise_for_status()
                response_data = response.json()
                result = response_data.get("result", [])
                self.params["searchId"] = response_data.get("searchId", "")

                self.list_result.extend(result)

            if not self.list_result:
                text = "Nenhum dado retornado pela API após todas as requisições. FINALIZADO!"
                self.log.post_log(text, "info")
                print(text)
                return None

            return {"keys": keys, "processed_data": len(self.list_result)}

        except requests.exceptions.RequestException as e:
            text = f"Erro ao fazer a requisição: {e}"
            self.log.post_log(text, "critical")
            print(text)
            exit(1)
        except Exception as e:
            text = f"Houve um erro ao coletar dados da API: {e}"
            self.log.post_log(text, "critical")
            print(text)
            exit(1)
