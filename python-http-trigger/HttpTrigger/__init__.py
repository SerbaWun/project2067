import logging
import os
import requests

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = "me"

    return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
   
