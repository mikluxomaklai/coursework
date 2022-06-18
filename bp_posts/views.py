from flask import Blueprint, render_template, current_app
from config import DATA_PATH_POSTS
from bp_posts.dao.post_dao import PostDAO

bp_posts = Blueprint("bp_posts", __name__, template_folder="templates")
post_dao = PostDAO(DATA_PATH_POSTS)

@bp_posts.route("/")
def page_posts_index():
    all_posts = post_dao.get_all()
    return render_template("posts_index.html", posts=all_posts)

@bp_posts.route("/posts/<int:pk>/")
def page_posts_single(pk):
    post = post_dao.get_by_pk(pk)
    return render_template("posts_single.html", post=all_posts)