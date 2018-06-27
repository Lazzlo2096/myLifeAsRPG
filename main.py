import pickle
import datetime

class TasksDB_t: #model #экземпляр этого класса будет один на всю программу (если я не захочу одновременно открывать несколько БД)
	def __init__(self):
		self.tasks_list = []
		self.last_id = 0
		
		self.tasks_done_history = [] # [(id, дата-время)]
	
	def addTask(self, name, isEveryday, reward, mulct=0):
		self.last_id+=1
		self.tasks_list.append( Task(self.last_id, name, isEveryday, reward, mulct) )
		
	def doneTask(self, id):
		# Если эта задача Everyday, то проверять не была ли она уже выполнена
		self.tasks_done_history.append( (id, datetime.datetime.now()) )
		
	def testDB(self):
		if len(self.tasks_list) <= self.last_id: print("Test 1 is OK :)")
		else: print("Error Test 1 >:(")
		
	#def save(self):

	#def load(self):
		#self = pickle.load(file) # А так вообще можно?

class Task:
	def __init__(self, id, name, isEveryday, reward, mulct):
		self.id = id
		self.name = name
		self.isEveryday = isEveryday
		self.reward = reward
		self.mulct = mulct #fine - шраф

fileWriteName = "TasksDB"
#commands_list = ["nlat", "exit"]

class Repl: #view and controller
	def __init__(self):
		self.TasksDB = TasksDB_t()
		#-------------
		self.TasksDB.addTask("qwee", reward=6, isEveryday=False)
		#-------------

	def run(self):
		isExit = False
		while not isExit:
			#print('>', end='')
			input_command = input(">")

			if input_command=="nlat" : #nameLastAddTask
				if len(self.TasksDB.tasks_list) != 0:
					print(self.TasksDB.last_id, self.TasksDB.tasks_list[0].name)
				else:
					print("Tasks list is empty!")

			elif input_command=="list" :
				if len(self.TasksDB.tasks_list) != 0 :
					print("id, name, isEveryday, reward, mulct")
					print("----------------------------")
					for item in self.TasksDB.tasks_list:
						print(item.id, "'",item.name, "'", item.isEveryday, item.reward, item.mulct)
				else:
					print("Tasks list is empty!")

			elif input_command=="exit" or input_command=="q":
				isExit = True

			elif input_command=="save":
				with open(fileWriteName, 'wb') as file:
					pickle.dump(self.TasksDB, file)
					file.close()

			elif input_command=="load":
				with open(fileWriteName, 'rb') as file:
					self.TasksDB = pickle.load(file)
					file.close()
					
			elif input_command=="add":
				pass
			elif input_command=="del":
				pass

			else:
				print("Unknown command!")
				#print(commands_list)
	
if __name__ == "__main__":
	Repl().run()