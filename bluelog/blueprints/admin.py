from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    return render_template('admin/settings.html')