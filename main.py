# -*- coding: utf-8
from flask import Flask, render_template, request
from flask import redirect, url_for
from TasksSqliteDB_class import TasksSqliteDB_class

# 1.SQlite (а может что-то другое?)
# синх в гугл диск (Можно пока просто юзать папку клиента)
# 2.GUI (web)

TasksSqliteDBFileName = "TasksDB.db"
TasksDB = TasksSqliteDB_class(TasksSqliteDBFileName)

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/list")
def list():
		return render_template("list.html",rows = TasksDB.getTasksList())

if __name__=="__main__" :
	app.run(debug = True) # app.run()
