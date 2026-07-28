import boto3
import os

# S3 Client
s3 = boto3.client("s3", region_name="ap-south-1")

# Bucket Name
bucket_name = "my-fleet-project-bucket"

folder_path = r"C:\Users\ankit\OneDrive\Desktop\fleet project\downloads"


for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    # CSV files ko CSV folder me upload karo
    if file.endswith(".csv"):
        s3_key = f"CSV/{file}"

    # JSON files ko JSON folder me upload karo
    elif file.endswith(".json.gz"):
        s3_key = f"JSON/{file}"

    else:
        continue

    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"{file} uploaded successfully.")

    except Exception as e:
        print(f"Error uploading {file}: {e}")