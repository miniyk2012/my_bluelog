# -*- coding: utf-8 -*-

from flask import Blueprint, redirect, flash, url_for, render_template
from flask_login import login_required, current_user

from my_bluelog.forms import SettingForm, PostForm
from my_bluelog.extensions import db
from my_bluelog.models import Post, Category
from my_bluelog.utils import redirect_back

admin_bp = Blueprint('admin', __name__)


@admin_bp.before_request
@login_required
def login_protect():
    """小技巧, 该蓝图下所有路由都需要登录"""
    pass


@admin_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    form = SettingForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.blog_title = form.blog_title.data
        current_user.blog_sub_title = form.blog_sub_title.data
        current_user.about = form.about.data
        # current_user这里就是admin, 因此实际也就是对admin做了更新
        db.session.commit()
        flash('Setting updated.', 'success')
        return redirect(url_for('blog.index'))
    form.name.data = current_user.name
    form.blog_title.data = current_user.blog_title
    form.blog_sub_title.data = current_user.blog_sub_title
    form.about.data = current_user.about
    return render_template('admin/settings.html', form=form)


@admin_bp.route('/post/<slug>/delete', methods=['POST'])
def delete_post(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted.', 'success')
    return redirect_back()


@admin_bp.route('/post/<slug>/edit', methods=['GET', 'POST'])
def edit_post(slug):
    form = PostForm()
    post = Post.query.filter_by(slug=slug).first_or_404()
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        post.category = Category.query.get(form.category.data)
        db.session.commit()
        flash('Post updated.', 'success')
        return redirect(url_for('blog.show_post', slug=post.slug))
    form.title.data = post.title
    form.body.data = post.body
    form.category.data = post.category_id
    return render_template('admin/edit_post.html', form=form)
