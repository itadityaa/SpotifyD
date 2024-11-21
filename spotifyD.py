import os
from dotenv import load_dotenv

load_dotenv()

PLAYLIST_URL = os.getenv('PLAYLIST_URL')
DOWNLOAD_PATH = os.getenv('DOWNLOAD_PATH')

def begin_download(PLAYLIST_URL, DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)
    
    command = f"spotdl {PLAYLIST_URL} --output \"{DOWNLOAD_PATH}\""
    
    os.system(command)

begin_download(PLAYLIST_URL, DOWNLOAD_PATH)