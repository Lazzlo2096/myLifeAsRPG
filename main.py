# -*- coding: utf-8
from flask import Flask, render_template, request
from flask import redirect, url_for
from TasksSqliteDB_class import TasksSqliteDB_class

# 1.GUI (web)
# SQlite (а может что-то другое?)
# синх в гугл диск (Можно пока просто юзать папку клиента)

TasksSqliteDBFileName = "TasksDB.db"
TasksDB = TasksSqliteDB_class(TasksSqliteDBFileName)

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/tasks_list")
def tasks_list():
	titles = ["name"]
	rows = TasksDB.getTasksList()
	return render_template("tasks_list.html", rows=rows, titles=titles)
	
@app.route("/post_test", methods=["POST","GET"])
def post_test():
	if request.method == "POST":
	
		TasksDB.doneTask(int(request.form['submit']))
		
		return redirect(url_for("doneTasksHistory")) 
		#return render_template("hello.html")

@app.route("/tasks_list_")
def tasks_list_():
	titles = ["task_id", "name", "isEveryday", "reward", "mulct"]
	rows = TasksDB.getTasksList()
	return render_template("list.html", rows=rows, titles=titles)
	
@app.route("/history")
def doneTasksHistory():
	titles = ["task_id", "date"]
	rows = TasksDB.getDoneTasksHistory()
	return render_template("list.html", rows=rows, titles=titles)

if __name__=="__main__" :
	app.run(debug = True) # app.run()
