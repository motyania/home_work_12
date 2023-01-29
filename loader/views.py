import logging
from flask import render_template, Blueprint, request
from main.views import item_data, data


UPLOAD_FOLDER = "uploads/images"
ALLOWEDEXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    return render_template("post_form.html")


@loader_blueprint.route("/post/add", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")

    if picture:
        filename = picture.filename
        extention = filename.split(".")[-1]
        if extention in ALLOWEDEXTENSIONS:
            picture.save(f"./{UPLOAD_FOLDER}/{filename}")
        else:
            logging.info(f"Загруженный файл - не картинка")
            return "<h2>Загруженный файл - не картинка</h2>"
    else:
        logging.error("Файл не выбран!")
        return "<h2>Файл не выбран!</h2>"

    content = request.form['content']
    post = {"pic": f"/{UPLOAD_FOLDER}/{filename}", "content": content}
    item_data.load_post_in_json(post, data)
    return render_template("post_uploaded.html", img=f"/{UPLOAD_FOLDER}/{filename}", text=content)
