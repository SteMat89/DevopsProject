from todo_app.flask_config import Config
from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', items=get_items())


@app.route('/items', methods=['POST'])
def post_item():
    add_item(request.form['item-title'])
    return redirect(url_for('index'))