import azure.functions as func
import logging
from azure.storage.blob import BlobServiceClient

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="cprcontainer",
                               connection="praveenstrgacct_STORAGE") 
def blob_trigger_func(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    # Read the blob content
    blob_content = myblob.read()
    
    connection_string = ""
    blob_name = "target_test.txt"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    target_container = "cprtargetcontainer"
    blob_client = blob_service_client.get_blob_client(
        container=target_container,
        blob=blob_name
    )
    blob_client.upload_blob(blob_content, overwrite=True)
    logging.info(f"Successfully copied {blob_name} to {target_container}")
