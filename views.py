from flask_wtf import form
from app import app
from flask import Flask , render_template , request
from mod_users.forms import LoginForm
import pyscreenshot
import flask
from io import BytesIO


@app.route('/')
def index():
    form = LoginForm(request.form)
    return render_template('index.html' , form=form)


@app.route('/screen.png')
def serve_pil_image():
    img_buffer = BytesIO()
    pyscreenshot.grab().save(img_buffer, 'PNG', quality=50)
    img_buffer.seek(0)
    return flask.send_file(img_buffer, mimetype='image/png')


@app.route('/js/<path:path>')
def send_js(path):
    return flask.send_from_directory('js', path)


@app.route('/webinar')
def serve_img():
    return flask.render_template('webinar.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)

