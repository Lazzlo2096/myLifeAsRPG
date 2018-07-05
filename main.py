# -*- coding: utf-8
from flask import Flask, render_template, request
from flask import redirect, url_for
from TasksSqliteDB_class import TasksSqliteDB_class

from flask_sqlalchemy import SQLAlchemy

# 1.GUI (web)
# SQlite (а может что-то другое?)
# синх в гугл диск с API (Можно пока просто юзать папку клиента)

#1. трекер как на гитхабе
#2. (двйные)множественное выполнение в день (и чтоб кнопочка красивая)
#3. тригер для счёта ЕКСПы и наградных алмазов
#4. +таблица наград
#5. кнопка+форма добавления ежндн тасков
#6. напоминания[комп и\или телефон] + автозапуск
#7. красоты

TasksSqliteDBFileName = "test.db"
TasksDB = TasksSqliteDB_class(TasksSqliteDBFileName)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./"+TasksSqliteDBFileName
# app.config['DEBUG'] = True
db = SQLAlchemy(app)

#+=+=+=+=+=+=+=+=+=after merging=+=+=+=+=+=+=+=+=+=

# CREATE TABLE IF NOT EXISTS tasks task_id integer, task_name text, isEveryday integer, reward integer, mulct integer)
class Tasks(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text)
	isEveryday = db.Column(db.Integer)
	reward = db.Column(db.Integer)
	mulct = db.Column(db.Integer)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'), default=1)
	# tasks = db.relationship('Done_tasks_history', backref='Tasks')

# ('''CREATE TABLE IF NOT EXISTS done_tasks_history (task_id integer, date text)''')
class Done_tasks_history(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
	date = db.Column(db.Text)
	
# ++++++

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    tasks = db.relationship('Tasks', backref='category')

# only for local test
@app.before_first_request
def init_db():
    """Insert default categories and demo items.
    """
    db.create_all()
    inbox = Category(name=u'收件箱')
    done = Category(name=u'已完成')
    shopping_list = Category(name=u'购物清单')
    work = Category(name=u'工作')
    item = Tasks(body=u'看一小时《战争与和平》')
    item2 = Tasks(body=u'晒太阳')
    item3 = Tasks(body=u'写作练习30分钟')
    item4 = Tasks(body=u'3瓶牛奶', category=shopping_list)
    item5 = Tasks(body=u'5个苹果', category=shopping_list)
    item6 = Tasks(body=u'12支铅笔', category=shopping_list)
    item7 = Tasks(body=u'浇花', category=done)
    item8 = Tasks(body=u'完成demo', category=work)
    db.session.add_all([inbox, done, item, item2, item3, item4, item5, item6, item7, item8])
    db.session.commit()

#+=+=+=+=+=+=+=+=+=END after merging=+=+=+=+=+=+=+=+=+=



@app.route("/show_table_tasks")
def show_table_tasks():
	titles = ["пока не умею","?"]
	rows = Tasks.query.all() # А КАК ТОГДА?
	# titles, rows = TasksDB.getTable( table_name )
	return render_template("list.html", rows=rows, titles=titles)




# @app.route("/")
# def index():
	# return render_template("index_old.html")
	
@app.route("/tasks_list") #тут можно выполнить задания
def tasks_list():
	titles, rows = TasksDB.getTable("'isEvrdy and not done today'") # НО НУЖНО ЧТОБ ТУТ БЫЛО а ля не так длинно..
	return render_template("tasks_list.html", rows=rows, titles=titles)
	
@app.route("/post_done", methods=["POST","GET"])
def post_done():
	if request.method == "POST":
	
		TasksDB.doneTask( int(request.form['submit']) )
		
		#return render_template("hello.html")
		#return redirect(url_for("show_table", table_name="'isEvrdy and not done today'")) # НО НУЖНО чтобы он редиректил на сам себя tasks_list, то есть прост ообнавлял страничку
		return redirect(url_for("tasks_list")) # НО можно ли чтобы он просто рефрешился? - вроде нет

#===========
#done_tasks_history
#tasks
#'names of done tasks'
#'isEvrdy and not done today'
#isEveryday
@app.route("/show_table/<string:table_name>")
def show_table(table_name):
	titles, rows = TasksDB.getTable( table_name )
	return render_template("list.html", rows=rows, titles=titles)
#===========
	
@app.route("/_history")
def _history():
	titles, rows = TasksDB.getTable("'names of done tasks'")
	return render_template("list.html", rows=rows, titles=titles)
	
#+=+=+=+=+=+=+=+=+=after merging=+=+=+=+=+=+=+=+=+=
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        body = request.form.get('item')
        category_id = request.form.get('category')
        category = Category.query.get_or_404(category_id)
        item = Tasks(body=body, category=category)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('category', id=category_id))
    return redirect(url_for('category', id=1))

@app.route('/category/<int:id>')
def category(id):
    category = Category.query.get_or_404(id)
    categories = Category.query.all()
    tasks = category.tasks
    return render_template('index.html', items=tasks,
                           categories=categories, category_now=category)
						 

						 
						 
						 
						 
						 
						 
						 
						 
						 
						 
						 
						 
@app.route('/new-category', methods=['GET', 'POST'])
def new_category():
    name = request.form.get('name')
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return redirect(url_for('category', id=category.id))


@app.route('/edit-item/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    item = Item.query.get_or_404(id)
    category = item.category
    item.body = request.form.get('body')
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('category', id=category.id))


@app.route('/edit-category/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    category = Category.query.get_or_404(id)
    category.name = request.form.get('name')
    db.session.add(category)
    db.session.commit()
    return redirect(url_for('category', id=category.id))


@app.route('/done/<int:id>', methods=['GET', 'POST'])
def done(id):
    item = Tasks.query.get_or_404(id)
    category = item.category
    done_category = Category.query.get_or_404(2)
    done_item = Tasks(body=item.body, category=done_category)
    db.session.add(done_item)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('category', id=category.id))


@app.route('/delete-item/<int:id>')
def del_item(id):
    item = Tasks.query.get_or_404(id)
    category = item.category
    if item is None:
        return redirect(url_for('category', id=1))
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('category', id=category.id))


@app.route('/delete-category/<int:id>')
def del_category(id):
    category = Category.query.get_or_404(id)
    if category is None or id in [1, 2]:
        return redirect(url_for('category', id=1))
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('category', id=1))
	
#+=+=+=+=+=+=+=+=+=END after merging=+=+=+=+=+=+=+=+=+=

if __name__=="__main__" :
	app.run(debug = True) # app.run()
