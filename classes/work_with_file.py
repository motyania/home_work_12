import logging
import json
from json import JSONDecodeError


class FileData:
    """Класс, которых работает с данными json-файла"""

    def __init__(self, path):
        """Принимает json-файл"""
        self.data = path

    def reading_file(self):
        """Возвращает список постов из json-файла"""
        try:
            with open(self.data, "r", encoding="utf-8") as file:
                data_posts = json.load(file)
        except FileNotFoundError:
            # Будет выполнено, если файл не найден
            logging.exception("Ошибка доступа к файлу")
        except JSONDecodeError:
            # Будет выполнено, если файл найден, но не превращается из JSON
            logging.exception("Файл не удается преобразовать")
        return data_posts

    def search_by_tag(self, data_posts, tag):
        """Находит посты по тегу"""
        list_posts = []
        for post in data_posts:
            if post["content"].lower().find(tag.lower()) != -1:
                list_posts.append(post)

        return list_posts

    def load_post_in_json(self, post, data_posts):
        """Добавить пост в файл.json"""
        data_posts.append(post)
        with open(self.data, "w", encoding="utf-8") as file:
            file.write(json.dumps(data_posts, ensure_ascii=False))

    def __repr__(self):
        return f"{self.data}"
