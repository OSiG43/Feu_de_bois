# Fichier qui contient toutes les vues propre à agilog
from flask import Blueprint, render_template

agilog_bp = Blueprint('agilog', __name__, template_folder='../templates/agilog', static_folder='static')

@agilog_bp.route('/test')
def test():
    return render_template('test_agilog.html')

@agilog_bp.route('/suivi_cmd')
def agilogcmd():
    return render_template('agilog_suivi_cmd.html')
