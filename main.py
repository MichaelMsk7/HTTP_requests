# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# работа с яндекс диском

import requests
from my_token import TOKEN
from http import HTTPStatus

class YandexDisk:
    URL_FILES_LIST: str = "https://cloud-api.yandex.net/v1/disk/resources/files"
    URL_UPLOAD_LINK: str = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    def __init__(self,token:str):
        self.token = token
    @property
    def header(self):
        return {"Content-Type":"application/json",
                "Authorization":f"OAuth {self.token}"}
    def get_files_list(self):
        response = requests.get(self.URL_FILES_LIST,headers=self.header)
        result =  response.json()
        return result

    def get_upload_link(self,ya_disk_path: str):
        params ={"path": ya_disk_path ,"overwrite": "true"}
        response = requests.get(self.URL_UPLOAD_LINK,headers=self.header, params=params)
        upload_url = response.json().get("href")
        return upload_url

    def upload_file(self, ya_disk_path: str, file_path:str):
        upload_link = self.get_upload_link(ya_disk_path)
        with open(file_path,'rb') as file_obj:
            response = requests.put(url=upload_link, data=file_obj)
            if response.status_code == 201:
                print("Успешно загружено")

        return response.status_code



instance = YandexDisk(TOKEN)
print(instance.upload_file('data.txt',"data.txt"))

#