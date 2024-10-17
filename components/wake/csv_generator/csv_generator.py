import csv


class CSVGenerator:
    """Classe para gerar arquivos CSV a partir dos dados coletados."""
    def __init__(self, local_file_path, keys, data):
        self.local_file_path = local_file_path
        self.keys = keys
        self.data = data

    def generate_csv(self):
        """Gera o arquivo CSV com os dados fornecidos."""
        try:
            csv_file = [self.keys]

            for item in self.data:
                csv_file.append([item.get(key, "") for key in self.keys])

            with open(self.local_file_path, mode="w", newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(csv_file)

            print(f"Arquivo CSV '{self.local_file_path}' gerado com sucesso.")
        except Exception as e:
            print(f"Houve um erro ao gerar o arquivo CSV: {e}")
            exit(1)
