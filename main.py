# -*- coding: utf-8
from flask import Flask, render_template, request
from flask import redirect, url_for
from TasksSqliteDB_class import TasksSqliteDB_class

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

TasksSqliteDBFileName = "TasksDB.db"
TasksDB = TasksSqliteDB_class(TasksSqliteDBFileName)

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index_old.html")
	
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

if __name__=="__main__" :
	app.run(debug = True) # app.run()
