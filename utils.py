import json
from youtube_upload.client import YoutubeUploader
import os

def load_settings_from_json(file_path='User_Settings.json'):
    try:
        with open(file_path, 'r') as file:
            settings_data = json.load(file)
            folder_path = settings_data.get('folder_path', '')
            token1 = settings_data.get('access_token', '')
            token2 = settings_data.get('refresh_token', '')
            return folder_path, token1, token2
    except FileNotFoundError:
        print(f'Файл {file_path} не найден.')
        return None, None, None
    except json.JSONDecodeError:
        print(f'Ошибка при декодировании JSON в файле {file_path}.')
        return None, None, None

def get_video_list(path: str) -> list:

    if not os.path.exists("User_Settings.json"):
        return "User Settings does not exists!"

    mp4_files = []

    # Проверяем, существует ли указанный путь
    if not os.path.exists(path):
        print(f'Путь {path} не существует.')
        return mp4_files

    # Получаем список всех подпапок в указанном пути
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]

    # Итерируемся по каждой подпапке и находим все файлы с расширением .mp4
    for folder in subfolders:
        for file_name in os.listdir(folder):
            if file_name.endswith('.mp4'):
                mp4_files.append(os.path.join(folder, file_name))
    return mp4_files







