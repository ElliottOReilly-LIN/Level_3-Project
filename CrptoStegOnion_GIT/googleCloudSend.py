# The following code will allow me to send my stego image
# staright to cloud and store in a simple bucket blob

from google.cloud import storage

def sendImage():

    # Setting credentials using the downloaded JSON file
    client = storage.Client.from_service_account_json(json_credentials_path='cmp3747m-oreilly-17666843-d95ac337bb57.json')
    # Creating bucket object

    bucket = client.get_bucket('stegobucket')

    # Name of the object to be stored in the bucket
    object_name_in_gcs_bucket = bucket.blob('my_stego_encryted_UPLOAD')

    # Name of the object in local file system
    object_name_in_gcs_bucket.upload_from_filename('secret-stego_image.png')
