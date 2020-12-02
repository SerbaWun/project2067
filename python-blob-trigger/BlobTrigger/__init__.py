import logging

import azure.functions as func


def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

def xmain(inMessage: func.QueueMessage, outMessage: func.Out[func.QueueMessage])
    logging.info(f"Python blob trigger function processed blob {inMessage}\n")
