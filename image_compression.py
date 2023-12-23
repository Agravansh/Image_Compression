import os
from PIL import Image
import boto3

def compress_image(input_path, output_path):
    img = Image.open(input_path)
    img.save(output_path, optimize=True) #Compresses an image using Pillow's save method with lossless compression.

def upload_to_s3(file_path, bucket_name, s3_client):
    # Uploads a file to an S3 bucket while retaining the original file structure.
    key = os.path.relpath(file_path)
    s3_client.upload_file(file_path, bucket_name, key)

def process_directory(directory, bucket_name, aws_access_key, aws_secret_key):
    # Traverses through the directory, compresses and uploads images to the specified S3 bucket.
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
                compressed_path = file_path + ".compressed"
                compress_image(file_path, compressed_path)
                upload_to_s3(compressed_path, bucket_name, s3_client)
                os.remove(compressed_path)  # Remove the compressed local file after upload

def main(aws_access_key, aws_secret_key, bucket_name, directory):
    # Main function to execute the image compression and upload process.
    try:
        process_directory(directory, bucket_name, aws_access_key, aws_secret_key)
        print("Image compression and upload completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    aws_access_key = input("Enter AWS Access Key: ")
    aws_secret_key = input("Enter AWS Secret Key: ")
    bucket_name = input("Enter the target S3 bucket name: ")
    directory = input("Enter the directory path to process: ")

    main(aws_access_key, aws_secret_key, bucket_name, directory)
