import boto3

def check_s3_connection():
    try:
        
        s3 = boto3.client("s3")

        # Saare buckets ki list lao
        response = s3.list_buckets()

        # Agar buckets mil gaye to True return karega
        if "Buckets" in response:
            print("S3 Connected Successfully!")
            return True

        return False

    except Exception as e:
        print("Error:", e)
        return False


# Function Call
status = check_s3_connection()
print(status)
