import json
import logging
import os
import traceback
from logging.handlers import RotatingFileHandler
from mdc import MDCHandler

import log_config

from flask import Flask, request, jsonify

from config import get_corpus, get_host, get_port
from src.dates_parser_module import parse_datetime

app = Flask(__name__)
app.name = 'dates_extraction'


def initialize_app_logger() -> None:
    """
    Initialize the logger
    """
    os.makedirs('logs', exist_ok=True)

    global app_logger
    app_logger = logging.getLogger()  # 'gunicorn.error'
    app_logger.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
                                  " | %(asctime)s | %(levelname)s")
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10000000, backupCount=50)
    file_handler.setFormatter(formatter)
    app_logger.addHandler(file_handler)
    app_logger.addHandler(MDCHandler())

    log_config.logger = app_logger


@app.route('/date_parser', methods=['GET', 'POST'])
def dates_extraction():
    """
    Triggers the 'demo' environment of table extraction and returns a json object on completion.

    Parameters
    ----------
    self:object

    Returns
    -------
            :JSON

    """
    if request.method == 'GET':
        return 'server running'

    if request.method == 'POST':
        print(
            "\n####################################### STARTING DATES EXTRACTION #######################################\n")
        log_config.logger.info(
            "####################################### STARTING DATES EXTRACTION #######################################")

        meta = {}
        output = {}
        json_data = request.json

        try:
            meta['sentence'] = json_data['sentence']
            log_config.meta_logger = meta
            corpus_info = get_corpus()
            if 'doc_type' in json_data:
                doc_type = json_data['doc_type']
            else:
                doc_type = None
            custom_ner_flag_not_required = json_data.get("custom_ner_flag_not_required")
            date_result = parse_datetime(json_data['sentence'], corpus_info, doc_type, custom_ner_flag_not_required)
            output["date_flag"] = date_result[0]
            output["date_extracted"] = date_result[1]
            output["date_format"] = date_result[2]
            log_config.logger.info(f"Date regex result extracted ::{output}")
            return json.dumps(output)

        except Exception as e:

            print(f"xxxxxxxxxxxxxxxxxxxx ERROR > {traceback.format_exc()} xxxxxxxxxxxxxxxxxxxx")
            log_config.logger.error(f"xxxxxxxxxxxxxxxxxxxx ERROR > {traceback.format_exc()} xxxxxxxxxxxxxxxxxxxx "
                                    f" Date Parsing Failed due to {str(e)}"
                                    f" Error code:{500} *********",
                                    extra={'props': meta})
            return {}

    # print(":::: FINAL AGREEMENT PROCESSING TIME ::::", time.time() - start_processing)

@app.after_request
def add_header(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response


if __name__ == "__main__":
    initialize_app_logger()
    # app.run(host=get_host(), port=get_port(), debug=False)
    app.run(get_host(), get_port(), debug=False)

else:
    initialize_app_logger()
