from components.PSComponents.config import Config
from components.PSComponents.report_manager import ReportManager
from flask import Flask, request, jsonify


app = Flask(__name__)


def main(mailsender_id, customer_login):
    """Função principal para executar o gerenciador de relatórios."""
    if not mailsender_id.strip() or not customer_login.strip:
        return jsonify({
            "error": True,
            "status": "Campos de mailsenderId ou Login estão vazios!"
        }), 400
    config = Config(mailsender_id, customer_login)
    report_manager = ReportManager(config)
    return report_manager.run(mailsender_id, customer_login)


@app.route("/generate", methods=["GET"])
def generate():
    body = request.json
    mailsender_id = body["mailsenderId"]
    customer_login = body["customerLogin"]
    return main(mailsender_id, customer_login)


if __name__ == "__main__":
    app.run(host="127.0.0.1")
