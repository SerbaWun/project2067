import logging
import requests
import os

import azure.functions as func

def get_bearer_token(resource_uri):
    identity_endpoint = os.environ["IDENTITY_ENDPOINT"]
    identity_header = os.environ["IDENTITY_HEADER"]

    api_version="2019-08-01"
    token_auth_uri = f"{identity_endpoint}?resource={resource_uri}&api-version={api_version}"
    logging.info(f"token_auth_uri {token_auth_uri}")

    headers = {'X-IDENTITY-HEADER':identity_header}

    resp = requests.get(token_auth_uri, headers=headers)
    access_token = resp.json()['access_token']

    return access_token

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    resource_uri="https%3A%2F%2Fvault.azure.net%2F"
    token = get_bearer_token(resource_uri)

    return func.HttpResponse(f"This HTTP triggered function executed successfully. Token = {token}", status_code=200)
