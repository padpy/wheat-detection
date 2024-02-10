from googleapiclient.discovery import build
from google.oauth2 import service_account

# Path to your service account credentials JSON file
credentials_file = '/path/to/credentials.json'

# Scopes required for accessing Google Drive
scopes = ['https://www.googleapis.com/auth/drive.readonly']

# Create credentials object from the service account file
credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=scopes)

# Build the Google Drive API client
drive_service = build('drive', 'v3', credentials=credentials)

# ID of the folder containing the files you want to retrieve
folder_id = 'your_folder_id'

# Retrieve the list of files in the folder
results = drive_service.files().list(q=f"'{folder_id}' in parents").execute()
files = results.get('files', [])

# Print the names of the files
for file in files:
    print(file['name'])
