from flask import Blueprint
from flask import render_template,request
from GuMi.GM_ApiServer import send_post
from flask import jsonify

gm = Blueprint('gm', __name__)


@gm.route('/', methods=['GET', 'POST'])
def home():
    return render_template('gumi.html')

@gm.route('/next', methods=['GET', 'POST'])
def next():

    parm_str=request.form['parm_str']
    parm_url = request.form['parm_url']
    data = send_post(parm_url, parm_str)

    print('view返回的结果:%s' %data)
    if isinstance(data,str):
        return data
    else:
        return jsonify(data)