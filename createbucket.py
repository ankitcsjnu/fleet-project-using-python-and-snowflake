
import boto3
from botocore.exceptions import ClientError

def create_bucket_if_not_exists(bucket_name, region="ap-south-1"):
    try:
        # S3 client create karo
        s3 = boto3.client("s3", region_name=region)

        # Check karo bucket exist karta hai ya nahi
        buckets = s3.list_buckets()

        for bucket in buckets["Buckets"]:
            if bucket["Name"] == bucket_name:
                print(f"Bucket '{bucket_name}' already exists.")
                return True

        # Bucket create karo agar exist nahi karta
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": region
            }
        )

        print(f"Bucket '{bucket_name}' created successfully.")
        return True

    except ClientError as e:
        print("Error:", e)
        return False

#function cll
create_bucket_if_not_exists("my-fleet-project-bucket")