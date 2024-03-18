import streamlit as st
import os

from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient, BlobClient

load_dotenv()

BLOB_ADMIN_TOKEN=os.environ.get("BLOB_ADMIN_TOKEN")
BLOB_URL=os.environ.get("BLOB_URL")

st.set_page_config(page_title="Uploading Page", page_icon="📖", layout="wide")

st.header("Upload to Blob Storage")

container_name = st.text_input(
        "Enter the container name"
    )


blob_service_client = BlobServiceClient(BLOB_URL, credential=BLOB_ADMIN_TOKEN)

if container_name:
    container_client = blob_service_client.get_container_client(container=container_name)

try:
    uploaded_files = st.file_uploader("Choose documents", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        blob_client = container_client.upload_blob(name=uploaded_file.name, data=bytes_data, overwrite=True)
except NameError:
    st.header("Please provide a container name where you want to upload to")