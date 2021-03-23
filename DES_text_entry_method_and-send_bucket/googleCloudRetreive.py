# The following code will allow USER B 'ALICE' retrieve the stego image
# from to cloud ready to reverse OpenSLL and decode

from google.cloud import storage


def retrieveImage():

    # Setting credentials using the downloaded JSON file
    client = storage.Client.from_service_account_json(json_credentials_path='new.json')
    # Creating bucket object

    bucket_name = 'stegobucket'

    source_blob_name = 'my_stego_encryted_UPLOAD'
    destination_file_name = 'stegoRetreived_Image.png'
    # DOWNLOAD
    #storage_client = storage.Client()
    storage_client = client
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print('Blob {} downloaded to {}.'.format(source_blob_name, destination_file_name))
