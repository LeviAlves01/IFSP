from flask import Flask

from controllers.auth_controller import auth_bp
from controllers.admin_controller import admin_bp
from controllers.recep_controller import recep_bp
from controllers.maid_controller import maid_bp
from controllers.guest_controller import guest_bp
from controllers.main_controller import main_bp

app = Flask(__name__)
app.secret_key = 'dev_secret_change'

# registre tudo AQUI e somente aqui
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(recep_bp, url_prefix='/recep')
app.register_blueprint(maid_bp, url_prefix='/camareira')
app.register_blueprint(guest_bp, url_prefix='/hospede')
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
