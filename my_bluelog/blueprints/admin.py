# -*- coding: utf-8 -*-

from flask import Blueprint

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    pass