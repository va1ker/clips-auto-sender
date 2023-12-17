import json
import tkinter as tk
from tkinter import filedialog
# from utils import get_video_list, video_upload, load_settings_from_json
import os
from utils import load_settings_from_json,get_video_list


class FolderPathApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('CAS ver.')
        self.geometry('400x400')
        self.resizable(False, False) 

        self.label_folder = tk.Label(self, text='Выберите путь до папки:')
        self.label_folder.pack(pady=5)

        self.folder_path_input = tk.Entry(self, width=40)
        self.folder_path_input.pack(pady=5)

        self.browse_button = tk.Button(self, text='Обзор', command=self.browse_folder)
        self.browse_button.pack(pady=5)

        self.label_token1 = tk.Label(self, text='Access token:')
        self.label_token1.pack(pady=5)

        self.token1_input = tk.Entry(self, width=40)
        self.token1_input.pack(pady=5)

        self.label_token2 = tk.Label(self, text='Refresh token:')
        self.label_token2.pack(pady=5)

        self.token2_input = tk.Entry(self, width=40)
        self.token2_input.pack(pady=5)

        self.save_button = tk.Button(self, text='Сохранить', command=self.save_to_json)
        self.save_button.pack(pady=10)

        self.scan_button = tk.Button(self, text='Найти видео')
        self.scan_button.pack(pady=10)


        try:
            with open('User_Settings.json', 'r') as file:
                settings_data = json.load(file)
                self.folder_path_input.insert(0, settings_data.get('folder_path', ''))
                self.token1_input.insert(0, settings_data.get('token1', ''))
                self.token2_input.insert(0, settings_data.get('token2', ''))
        except FileNotFoundError:
            pass

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path_input.delete(0, tk.END)
            self.folder_path_input.insert(0, folder_path)

    def open_new_window(self):
        success_window = tk.Toplevel(self)
        success_window.title("Успех")
        label = tk.Label(success_window, text="Данные сохранены в файле User_Settings.json")
        label.pack()
        success_button = tk.Button(success_window, text='Окей', command=self.on_closing)
        success_button.pack(pady=10)

    def save_to_json(self):
        folder_path = self.folder_path_input.get()
        access_token = self.token1_input.get()
        refresh_token = self.token2_input.get()

        if folder_path and access_token and refresh_token:
            data = {'folder_path': folder_path, 'access_token': access_token, 'refresh_token': refresh_token}
            with open('User_Settings.json', 'w') as file:
                json.dump(data, file, indent=4)
                self.open_new_window()

    def on_closing(self):
        self.destroy()


def send_videos():
    if not os.path.exists("User_Settings.json"):
        return "User settings does not exist"
    
    data = load_settings_from_json()
    folder_path = data[0]
    access_token = data[1]
    refresh_token = data[2]
    mp4_routes = get_video_list(folder_path)
    

def run_app():
    app = FolderPathApp()
    app.mainloop()

    



if __name__ == '__main__':
    run_app()
