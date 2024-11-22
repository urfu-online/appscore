import hashlib
import requests
from urllib.parse import urlparse


def calculate_file_hash_by_url(url):
    # Загружаем контент по URL
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        hash_object = hashlib.sha256(content.encode())
        hex_dig = hash_object.hexdigest()

        return hex_dig
    else:
        print(
            f"Ошибка при загрузке контента по URL {url}. Код ответа: {response.status_code}"
        )
        return None


def calculate_filestorage_hash_by_url(url):
    # Загружаем контент по URL
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        # Вычисляем хеш от строки, состоящей из текста и URL
        parsed_url = urlparse(url)

        hash_object = hashlib.sha256(content.encode())
        hex_dig = hash_object.hexdigest()

        hash_filestorage = hashlib.sha256(
            f"{hex_dig}{parsed_url.scheme}://{parsed_url.netloc}/".encode()
        )
        hex_dig_filestorage = hash_filestorage.hexdigest()

        return hex_dig_filestorage
    else:
        print(
            f"Ошибка при загрузке контента по URL {url}. Код ответа: {response.status_code}"
        )
        return None
