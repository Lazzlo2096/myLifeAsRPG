import pickle
from TasksDB_t import TasksDB_t #import TasksDB_t

# 1.SQlite
# синх в гугл диск (Можно пока просто юзать папку клиента)
# 2.GUI

fileWriteName = "TasksDB"
#commands_list = ["nlat", "exit"]

def showListLn(list):
	if len(list) != 0 :
		for item in list:
			print(item)
	else:
		print("This list is empty!")

class Repl: #view and controller
	def __init__(self):
		self.TasksDB = TasksDB_t()
		#-------типа иниц БД------
		self.TasksDB.addTask("qwee", reward=6, isEveryday=False)
		self.TasksDB.doneTask(1)
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
				#showListLn(self.TasksDB.getTasksList())
				
				if len(self.TasksDB.tasks_list) != 0 :
					print("id, name, isEveryday, reward, mulct")
					print("----------------------------")
					for item in self.TasksDB.tasks_list:
						print(item.id, "'",item.name, "'", item.isEveryday, item.reward, item.mulct)
				else:
					print("Tasks list is empty!")
			
			elif input_command=="hist" :
				if len(self.TasksDB.tasks_done_history) != 0 :
					print("id, time")
					print("--------")
					for item in self.TasksDB.tasks_done_history:
						print(item[0], str(item[1]))
				else:
					print("tasks_done_history is empty!")

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