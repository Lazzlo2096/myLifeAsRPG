import pickle
#from TasksDB_t import TasksDB_t #import TasksDB_t
from TasksSqliteDB_class import TasksSqliteDB_class

# 1.SQlite (а может что-то другое?)
# синх в гугл диск (Можно пока просто юзать папку клиента)
# 2.GUI

fileWriteName = "TasksDB"
TasksSqliteDBFileName = "TasksDB.db"
commands_list = ["tasks_list", "history", "save", "load", "add", "del", "exit"]

def showListLn(list):
	if len(list) != 0 :
		for item in list:
			print(item)
	else:
		print("This list is empty!")

class Repl: #view and controller
	def __init__(self):
		self.TasksDB = TasksSqliteDB_class(TasksSqliteDBFileName)
		#-------типа иниц БД------
		# self.TasksDB.addTask("qwer22rr", True, 2)
		# self.TasksDB.addTask("Just do it!", True, 777)
		# self.TasksDB.addTask("Something1", False, 5)
		# self.TasksDB.addTask("qwee", reward=6, isEveryday=False)
		# self.TasksDB.doneTask(0)
		
		# showListLn(self.TasksDB.getTasksList())
		# print("====")
		# showListLn(self.TasksDB.getDoneTasksHistory())
		#-------------

	def run(self):
		isExit = False
		while not isExit:
			#print('>', end='')
			input_command = input(">")

			if input_command=="tasks_list" :
				print("task_id, name, isEveryday, reward, mulct")
				print("----------------------------")
				showListLn(self.TasksDB.getTasksList())
			
			elif input_command=="history" :
				print("task_id, time")
				print("-------------")
				showListLn(self.TasksDB.getDoneTasksHistory())

			elif input_command=="exit" or input_command=="q":
				isExit = True

			elif input_command=="save":
				# with open(fileWriteName, 'wb') as file:
					# pickle.dump(self.TasksDB, file)
					# file.close()
				pass

			elif input_command=="load":
				# with open(fileWriteName, 'rb') as file:
					# self.TasksDB = pickle.load(file)
					# file.close()
				pass
					
			elif input_command=="add":
				#Вот тут опастность ввода некоректных данных!
				print("Add new task:")
				name = input("name=")
				isEveryday = input("isEveryday(0/1)=") # как sqlite допускает ввод текста в Integer???
				reward = input("reward=")
				mulct = input("mulct=")
				
				self.TasksDB.addTask(name, isEveryday, reward, mulct)
				
			elif input_command=="del":
				pass

			else:
				print("Unknown command!")
				print(commands_list)
	
if __name__ == "__main__":
	Repl().run()