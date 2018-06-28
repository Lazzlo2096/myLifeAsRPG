import sqlite3 #https://docs.python.org/3/library/sqlite3.html
import datetime #datetime.datetime.now()

class TasksSqliteDB_class:
	def __init__(self, nameSqlDb):
	
		self.conn = sqlite3.connect(nameSqlDb)
		self.cursor = self.conn.cursor()
		
		#====типа иниц ия====
		# Если не существует, то Create table
		self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
             (task_id integer, task_name text, isEveryday integer, reward integer, mulct integer)''')
			 
		self.cursor.execute('''CREATE TABLE IF NOT EXISTS done_tasks_history
             (task_id integer, date text)''')
		#=========
		
		# self.tasks_list = []
		self.last_id = 0
		# self.tasks_done_history = [] # [(task_id, дата-время)]

	def __del__(self):
		self.conn.close()
	
	def addTask(self, name, isEveryday, reward, mulct=0):
		#Предпологаем что в БД уже есть структура
		
		# Insert a row of data
		self.cursor.execute("INSERT INTO tasks VALUES (?,?,?,?,?)", (self.last_id, name, isEveryday, reward, mulct))
		
		# Save (commit) the changes
		self.conn.commit()
		
		self.last_id+=1
		# self.tasks_list.append( Task(self.last_id, name, isEveryday, reward, mulct) )
		
		
		
		#И МОЖНО СОЗДАВАТЬ БУФЕР
		# Larger example that inserts many records at a time
		purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
					 ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
					 ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
					]
		#c.executemany('INSERT INTO tasks VALUES (?,?,?,?,?)', purchases)

	def doneTask(self, task_id):
		# Если эта задача Everyday, то проверять не была ли она уже выполнена сегодня
		#self.tasks_done_history.append( (task_id, datetime.datetime.now()) )

		self.cursor.execute("INSERT INTO done_tasks_history VALUES (?,?)", (task_id, str(datetime.datetime.now())[:-3]))
		self.conn.commit() # Save (commit) the changes

	def testDB(self):
		if len(self.tasks_list) <= self.last_id: print("Test 1 is OK :)")
		else: print("Error Test 1 >:(")

	#def save(self):

	#def load(self):
		#self = pickle.load(file) # А так вообще можно?

	def _show(self): # можно(нужно? !) отправлять (в RAM) в View
		task_id = 0
		t = (task_id,)
		self.cursor.execute('SELECT * FROM tasks')
		
		# Получаем результат сделанного запроса
		#print(self.cursor.fetchone())
		results = self.cursor.fetchall()
		#results2 =  cursor.fetchall() #[]
		if len(results) != 0 :
			print("id, name, isEveryday, reward, mulct")
			print("-----------------------------------")
			for item in results:
				print(item)
		else:
			print("Tasks list is empty!")
			
	def getTasksList(self):
		self.cursor.execute('SELECT * FROM tasks')
		return self.cursor.fetchall()
		
	def getDoneTasksHistory(self):
		self.cursor.execute('SELECT * FROM done_tasks_history')
		return self.cursor.fetchall()
		
def _showListLn(results):
	if len(results) != 0 :
		for item in results:
			print(item)
	else:
		print("This list is empty!")


# TasksSqliteDB = TasksSqliteDB_class('TasksDB.db')
# TasksSqliteDB.addTask("qwer22rr", True, 777)
# TasksSqliteDB.addTask("qwe33r", True, 77544)
# TasksSqliteDB.doneTask(1)

# TasksSqliteDB._show()
# _showListLn(TasksSqliteDB.getTasksList())
# print("====")
# _showListLn(TasksSqliteDB.getDoneTasksHistory())