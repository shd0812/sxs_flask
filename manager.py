from flask import Flask,render_template

app = Flask(__name__)
app.secret_key = '123'
from XennHo.XH_View import xnho
app.register_blueprint(xnho,url_prefix='/home')


from GuMi.gumi_View import gm
app.register_blueprint(gm,url_prefix='/gm')

from shd_view import admin
app.register_blueprint(admin,url_prefix='/admin')

from login import login
app.register_blueprint(login,url_prefix='/login')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(host='192.168.110.53',port=1314,debug=True)
