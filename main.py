import datetime
import os

FOLDER_PATH = "D:\shadow play"

def get_videos():
    folders = os.listdir(FOLDER_PATH)
    if not folders:
        return "No folders for find"
    video_folders = [folder for folder in folders]
    

get_videos()