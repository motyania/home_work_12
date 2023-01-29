import logging
from flask import render_template, Blueprint, request
from classes.work_with_file import FileData

logging.basicConfig(filename="basic.log", level=logging.INFO)

POST_PATH = "posts.json"
main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

# Создаем экземпляр класса
item_data = FileData(POST_PATH)
# Берем данные из json-файла
data = item_data.reading_file()


@main_blueprint.route("/")
def index_page():
    return render_template("index.html")


@main_blueprint.route("/search")
def search_post():
    tag = request.args["s"]
    logging.info(f"Запрошены названия по тегу '{tag}'")
    list_posts = item_data.search_by_tag(data, tag)
    return render_template("post_list.html", tag=tag, items=list_posts)
