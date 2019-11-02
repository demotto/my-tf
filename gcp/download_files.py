from google.cloud import storage

storage_client = storage.Client()
storage_client.download_blob_to_file()

from google.cloud import storage
client = storage.Client()

with open('downloaded_file') as file_obj:
    client.download_blob_to_file('gs://bucket_name/path/to/blob', file_obj)


