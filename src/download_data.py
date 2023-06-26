import requests
import click
import zipfile
import os


def download_default_zip():
    folder_path = "../data/raw"
    zip_url = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip"

    # Check if default zip file already downloaded
    if os.path.isfile(f'{folder_path}/kagglecatsanddogs_5340.zip'):
        return

    os.makedirs(folder_path, exist_ok=True)
    response = requests.get(zip_url)
    filename = zip_url.split('/')[-1]
    file_path = os.path.join(folder_path, filename)

    # Write the downloaded content to the file
    with open(file_path, 'wb') as file:
        file.write(response.content)


def unzip_default_zip():
    zip_path = "../data/raw/kagglecatsanddogs_5340.zip"
    extract_path = "../data/raw"

    assert os.path.isfile(zip_path), "File isn't exist"
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

download_default_zip()
unzip_default_zip()