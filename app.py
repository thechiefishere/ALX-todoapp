from email.policy import default
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import sys
from flask_migrate import Migrate

load_dotenv()
app = Flask(__name__)
db_password = os.getenv('MY_PASSWORD')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://jbabajohn:{db_password}@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todolist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    
    todos = db.relationship('Todo', backref='todolist')

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    todolist_id = db.Column(db.Integer, db.ForeignKey('todolist.id'), nullable=False)
    

@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))

@app.route('/lists/<list_id>')
def get_list_todos(list_id):
    return render_template('index.html', todos=Todo.query.filter_by(todolist_id=list_id).order_by('id').all(), lists=Todolist.query.all(), active_list=Todolist.query.get(list_id))
    
    
@app.route('/lists/create', methods=['POST'])
def create_list():
    error = False
    response = {}
    try:
        list_name = request.get_json()['new_list']
        new_list_item = Todolist(name=list_name)
        db.session.add(new_list_item)
        db.session.commit()
        response['name'] = new_list_item.name
    except:
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if not error:
        return jsonify(response)

@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        return jsonify(body)
    
@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed(todo_id):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))

@app.route('/todos/<todo_id>/delete-todo', methods=['GET'])
def delete_todo(todo_id):
    try:
        print('am in try')
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')