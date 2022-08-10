from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
db_password = os.getenv('MY_PASSWORD')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://jbabajohn:{db_password}@localhost:5432/todoapp'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')