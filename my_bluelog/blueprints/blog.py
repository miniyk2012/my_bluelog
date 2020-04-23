# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, current_app, request
from my_bluelog.models import Post

blog_bp = Blueprint('blog', __name__)


# skip it
class current_user:
    is_authenticated = False


@blog_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['BLUELOG_POST_PER_PAGE']
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=per_page)
    posts = pagination.items
    return render_template('blog/index.html', pagination=pagination, posts=posts)

@blog_bp.route('/about')
def about():
    return render_template('blog/about.html')


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    return 'The category page'

@blog_bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    return 'The post page'


@blog_bp.route('/change-theme/<theme_name>')
def change_theme(theme_name):
    return 'The change theme page'