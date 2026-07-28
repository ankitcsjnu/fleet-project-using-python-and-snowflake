# Google Service Account se login karne ke liye
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import os

# Service Account file name
key_file = "service_account.json"

folder_id = "1JpmFW72IiIbzJwpIbuhSH-H7SlzxUOq5"

# JSON file se authentication create karne ke liye credentials banate hai
auth = service_account.Credentials.from_service_account_file(
    key_file,
    scopes=["https://www.googleapis.com/auth/drive.readonly"]
)

# Google Drive API se connection
drive = build("drive", "v3", credentials=auth)

# Folder ke andar ki saari files ki list
results = drive.files().list(
    q=f"'{folder_id}' in parents",
    fields="files(id, name)"
).execute()

all_files = results.get("files", [])

# downloads naam ka folder bana liya agar pehle se nahi hai toh 
os.makedirs("downloads", exist_ok=True)

# yaha loop ke help se download karenge ek ek file ko
for item in all_files:
    file_id = item["id"]
    file_name = item["name"]

    print("Downloading:", file_name)
    req = drive.files().get_media(fileId=file_id)
    path = os.path.join("downloads", file_name)

    with io.FileIO(path, "wb") as out_file:
        downloader = MediaIoBaseDownload(out_file, req)

        ready = False
        while not ready:
            status, ready = downloader.next_chunk()

    print(file_name, "-> download ho gyi")

print("Saari files 'downloads' folder me aa gayi hai")